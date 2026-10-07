#!/usr/bin/env python3
"""Генератор Excel-модели метрик брокерского бизнеса (этап 1 дорожной карты).

Собирает broker_roadmap_model.xlsx: легенда, сводка, дерево метрик, вводные,
чувствительность, расчётная модель со сценариями и паспорта метрик.

Файл модели — источник правды для данных: если вы уже внесли в него свои
значения, генератор не перезапишет файл без флага --force.

Запуск:  python3 tools/build_model.py [--out PATH] [--force]
После сборки откройте файл в Excel или пересчитайте через LibreOffice,
чтобы формулы получили значения.
"""

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path

from openpyxl import Workbook
from openpyxl.formatting.rule import DataBarRule
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

DEFAULT_OUT = Path(__file__).resolve().parent.parent / "broker_roadmap_model.xlsx"

# --- Оформление --------------------------------------------------------------
FONT_NAME = "Arial"
BLUE, GREEN, BLACK, WHITE, GREY = "FF0000FF", "FF008000", "FF000000", "FFFFFFFF", "FF808080"


def _fill(rgb):
    return PatternFill("solid", start_color=rgb, end_color=rgb)


FILL_INPUT = _fill("FFFFFF00")
FILL_HEAD = _fill("FF1F3864")
FILL_SECTION = _fill("FFD9E1F2")
FILL_RESULT = _fill("FFE2EFDA")
THIN = Side(style="thin", color="FFBFBFBF")
BOX = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)
WRAP = Alignment(wrap_text=True, vertical="top")

NUM = {
    "чел.": '#,##0;(#,##0);"-"',
    "шт.": '#,##0;(#,##0);"-"',
    "шт./клиент": '#,##0.0;(#,##0.0);"-"',
    "у.е.": '#,##0;(#,##0);"-"',
    "%": '0.0##%;(0.0##%);"-"',
    "б.п.": '#,##0.0;(#,##0.0);"-"',
    "мес.": '#,##0.0;(#,##0.0);"-"',
    "x": '0.0"x";(0.0"x");"-"',
    "коэф.": '0.00;(0.00);"-"',
    "режим": '0',
}
NUM_CALC = dict(NUM, **{"%": '0.0%;(0.0%);"-"'})
DIR_FMT = '"↑ больше — лучше";"↓ меньше — лучше";"—"'


def font(color=BLACK, bold=False, italic=False, size=10):
    return Font(name=FONT_NAME, size=size, bold=bold, italic=italic, color=color)


# --- Сегменты и вводные ------------------------------------------------------
SEGMENTS = [("MR", "Масс-розница"), ("AF", "Состоятельные"), ("IC", "Институционалы и корп.")]
SEG_SHORT = {"MR": "МР", "AF": "СК", "IC": "ИК"}
ILLUSTRATIVE = "Иллюстративно"


@dataclass
class Inp:
    code: str
    name: str
    unit: str
    values: tuple            # МР, СК, ИК
    direction: int           # +1 — больше лучше, -1 — меньше лучше
    control: str             # Управляемый / Частично / Внешний / Состояние
    lever: str               # Объёмный / Ценовой / Затратный / Внешний / База
    affects: str
    source: str = ILLUSTRATIVE
    comment: str = ""
    step: float = None       # практический шаг для драйверов в %
    step_label: str = ""
    shock: bool = True       # участвует в анализе чувствительности
    total: bool = False      # суммируется в «Итого»


PP, BP, BP10, PP01 = (0.01, "1 п.п."), (0.0001, "1 б.п."), (0.001, "10 б.п."), (0.001, "0,1 п.п.")


def inp(code, name, unit, values, direction, control, lever, affects, step=None, **kw):
    if step:
        kw["step"], kw["step_label"] = step
    return Inp(code, name, unit, values, direction, control, lever, affects, **kw)


INPUT_SECTIONS = [
    ("Клиентская база и воронка", [
        inp("N0", "Фондированные клиенты на начало периода", "чел.", (500_000, 15_000, 400), 1,
            "Состояние", "База", "Все ветки", shock=False, total=True,
            comment="Фондированный клиент — активы на счёте выше порога (порог зафиксировать)."),
        inp("LEADS", "Заявки на открытие счёта за период (ИК — потенциальные клиенты в воронке продаж)", "шт.",
            (300_000, 2_000, 120), 1, "Управляемый", "Объёмный", "NEW, C2", total=True),
        inp("CR_OPEN", "Конверсия: заявка → открытый счёт (KYC пройден; ИК — договор подписан)", "%",
            (0.45, 0.70, 0.40), 1, "Управляемый", "Объёмный", "NEW", PP),
        inp("CR_FUND", "Конверсия: открытый счёт → фондированный (первое пополнение)", "%",
            (0.55, 0.80, 0.75), 1, "Управляемый", "Объёмный", "NEW", PP),
        inp("CHURN", "Годовой отток фондированных клиентов (вывели активы ниже порога или закрыли счёт)", "%",
            (0.12, 0.06, 0.08), -1, "Управляемый", "Объёмный", "CHURNED → N_AVG, LTV", PP),
        inp("ACT", "Доля активных: среднемесячная доля фондированных клиентов с ≥1 сделкой", "%",
            (0.25, 0.45, 0.70), 1, "Управляемый", "Объёмный", "ACTIVE → TURN → R1", PP),
    ]),
    ("Торговая активность и комиссии", [
        inp("TPA", "Сделок в месяц на активного клиента", "шт.", (8, 4, 150), 1,
            "Частично", "Объёмный", "TURN → R1", comment="Зависит от волатильности рынка."),
        inp("TICKET", "Средний объём сделки", "у.е.", (800, 15_000, 100_000), 1,
            "Частично", "Объёмный", "TURN → R1"),
        inp("TAKE", "Комиссия брокера, % от оборота (эффективная, с учётом тарифов и скидок)", "%",
            (0.0015, 0.0010, 0.0002), 1, "Управляемый", "Ценовой", "R1", BP,
            comment="Ценовой рычаг: эффект показан при неизменном обороте; учитывать эластичность."),
        inp("EXEC", "Затраты на исполнение (биржевые, клиринговые, депозитарные сборы, вышестоящий брокер), % от оборота",
            "%", (0.0003, 0.0002, 0.00008), -1, "Частично", "Затратный", "R1", BP),
    ]),
    ("Активы клиентов и свободные остатки", [
        inp("AUC_PC", "Средние активы на фондированного клиента", "у.е.", (8_000, 200_000, 25_000_000), 1,
            "Частично", "Объёмный", "AUC → R3, R6, R7",
            comment="Управляемая часть — чистый приток (NNA); переоценка — рыночный эффект."),
        inp("CASH", "Доля свободных денежных средств в активах клиентов", "%", (0.12, 0.08, 0.05), 1,
            "Частично", "Объёмный", "CASHBAL → R3", PP,
            comment="Рост доли кэша повышает R3, но может снижать оборот и продажи продуктов."),
        inp("FLOAT_Y", "Доходность размещения свободных остатков клиентов", "%", (0.05, 0.05, 0.05), 1,
            "Внешний", "Внешний", "R3", PP,
            comment="Определяется ставками денежного рынка и правилами размещения клиентских средств."),
        inp("FLOAT_P", "Ставка, выплачиваемая клиентам на свободные остатки", "%", (0.02, 0.025, 0.035), -1,
            "Управляемый", "Ценовой", "R3", PP,
            comment="Ценовой рычаг: снижение ставки может вызвать отток остатков."),
    ]),
    ("Маржинальное кредитование", [
        inp("MRG_PEN", "Проникновение маржинальной торговли: доля фондированных клиентов с задолженностью", "%",
            (0.05, 0.10, 0.20), 1, "Управляемый", "Объёмный", "MPORT → R2, C5", PP),
        inp("MRG_DEBT", "Средняя задолженность маржинального клиента", "у.е.", (8_000, 150_000, 5_000_000), 1,
            "Частично", "Объёмный", "MPORT → R2, C5"),
        inp("MRG_RATE", "Ставка для клиента по маржинальному кредиту (деньги и ценные бумаги)", "%",
            (0.12, 0.10, 0.08), 1, "Управляемый", "Ценовой", "R2", PP,
            comment="Ценовой рычаг: учитывать эластичность спроса на плечо."),
        inp("FUND_RATE", "Стоимость фондирования маржинального портфеля", "%", (0.07, 0.07, 0.065), -1,
            "Внешний", "Внешний", "R2", PP),
        inp("CL", "Кредитные потери по маржинальному портфелю, % в год", "%", (0.005, 0.002, 0.001), -1,
            "Частично", "Затратный", "C5", PP01),
    ]),
    ("Валютообменные операции", [
        inp("FX_PEN", "Доля фондированных клиентов, совершающих конвертации", "%", (0.30, 0.50, 0.40), 1,
            "Управляемый", "Объёмный", "FXVOLUME → R4", PP),
        inp("FX_VOL", "Объём конвертаций на конвертирующего клиента в год", "у.е.", (5_000, 100_000, 10_000_000), 1,
            "Частично", "Объёмный", "FXVOLUME → R4"),
        inp("FX_SPREAD", "Комиссия и спред за конвертацию, % от объёма", "%", (0.005, 0.003, 0.0005), 1,
            "Управляемый", "Ценовой", "R4", BP),
    ]),
    ("Размещения и продукты", [
        inp("PRD_PEN", "Доля фондированных клиентов, купивших размещения или продукты за год "
            "(ИК — доля клиентов-эмитентов, проведших размещение)", "%", (0.08, 0.35, 0.05), 1,
            "Управляемый", "Объёмный", "PRDVOLUME → R5", PP),
        inp("PRD_VOL", "Средний объём покупок продуктов на клиента в год (ИК — средний объём размещения)", "у.е.",
            (3_000, 80_000, 50_000_000), 1, "Частично", "Объёмный", "PRDVOLUME → R5"),
        inp("PRD_FEE", "Средняя комиссия или маржа по продуктам и размещениям, % от объёма", "%",
            (0.01, 0.012, 0.01), 1, "Управляемый", "Ценовой", "R5", BP10),
    ]),
    ("ДУ и консультирование", [
        inp("AM_SHARE", "Доля активов клиентов в ДУ, модельных портфелях и на консультировании", "%",
            (0.02, 0.20, 0.05), 1, "Управляемый", "Объёмный", "AUM → R6", PP),
        inp("AM_FEE", "Комиссия за управление и консультирование, % годовых (вкл. success fee)", "%",
            (0.01, 0.010, 0.003), 1, "Управляемый", "Ценовой", "R6", BP10),
    ]),
    ("Подписки и сервисные комиссии", [
        inp("SUB_PEN", "Доля фондированных клиентов с платной подпиской или премиальным тарифом", "%",
            (0.08, 0.15, 0.0), 1, "Управляемый", "Объёмный", "SUBS → R7", PP),
        inp("SUB_PRICE", "Стоимость подписки или премиального обслуживания в год", "у.е.", (60, 1_000, 0), 1,
            "Управляемый", "Ценовой", "R7"),
        inp("CUST_FEE", "Депозитарная и кастодиальная комиссия, % от активов в год", "%",
            (0.0002, 0.0005, 0.0003), 1, "Управляемый", "Ценовой", "R7", BP),
    ]),
    ("Затраты на обслуживание", [
        inp("SUP_RATE", "Обращений в поддержку на фондированного клиента в год", "шт./клиент", (1.0, 3.0, 12.0), -1,
            "Управляемый", "Затратный", "C1"),
        inp("SUP_COST", "Стоимость обработки одного обращения", "у.е.", (5, 15, 30), -1,
            "Управляемый", "Затратный", "C1"),
        inp("KYC_UNIT", "Стоимость автоматической проверки заявки (KYC/AML-сервисы, документы)", "у.е.",
            (1.5, 3, 50), -1, "Управляемый", "Затратный", "C2"),
        inp("KYC_MAN", "Доля заявок, требующих ручной проверки", "%", (0.30, 0.60, 1.0), -1,
            "Управляемый", "Затратный", "C2", PP,
            comment="Ручная проверка также удлиняет онбординг и снижает CR_OPEN."),
        inp("KYC_MAN_COST", "Стоимость ручной проверки заявки", "у.е.", (8, 40, 1_500), -1,
            "Управляемый", "Затратный", "C2"),
        inp("OPS_PC", "Операций бэк-офиса на фондированного клиента в год "
            "(вводы/выводы, переводы ЦБ, корп. действия, заявления)", "шт./клиент", (6, 15, 200), -1,
            "Частично", "Затратный", "C3"),
        inp("OPS_MAN", "Доля операций с ручной обработкой (не STP)", "%", (0.10, 0.25, 0.30), -1,
            "Управляемый", "Затратный", "C3", PP),
        inp("OPS_COST", "Стоимость ручной обработки одной операции", "у.е.", (3, 10, 25), -1,
            "Управляемый", "Затратный", "C3"),
        inp("RM_LOAD", "Клиентов на одного персонального менеджера / сотрудника покрытия (0 — модели нет)", "чел.",
            (0, 150, 15), 1, "Управляемый", "Затратный", "C4",
            comment="Затраты обратно пропорциональны нагрузке — эффект почти, но не строго линеен."),
        inp("RM_COST", "Полная годовая стоимость менеджера (ФОТ, налоги, бонусы, рабочее место)", "у.е.",
            (0, 60_000, 150_000), -1, "Частично", "Затратный", "C4"),
    ]),
    ("Привлечение и потери", [
        inp("CAC", "Затраты на привлечение одного фондированного клиента (маркетинг, агентские, бонусы)", "у.е.",
            (80, 1_500, 15_000), -1, "Управляемый", "Затратный", "ACQ"),
        inp("OPLOSS", "Операционные потери за период: ошибки, компенсации клиентам, штрафы", "у.е.",
            (300_000, 100_000, 200_000), -1, "Управляемый", "Затратный", "C6", total=True),
    ]),
]
INPUTS = {i.code: i for _, items in INPUT_SECTIONS for i in items}

# Ориентиры для вводных — из отчёта reports/Бенчмарки метрик публичных брокеров.md.
# Цифры получены из поисковых выдержек первоисточников; перед внешним использованием сверить с отчётами компаний.
BENCHMARKS = {
    "N0": "Масштаб условный.",
    "LEADS": "Масштаб условный.",
    "CR_OPEN": "Futu 2025: пользователь приложения → брокерский счёт 20,4%. Цифровой KYC завершают 60–90% "
               "начавших (вендорные данные).",
    "CR_FUND": "Futu 2025: счёт → фондированный 56,6%. Регистрация → фондированный: eToro ≈9%, Webull 19–23%.",
    "CHURN": "Удержание клиентов в год: Webull и Futu ≈88–92%, Wealthfront 95%, AJ Bell 94,2%, "
             "Hargreaves Lansdown 91–92% (2023–2025).",
    "ACT": "Мосбиржа 2025: в среднем месяце торгуют 8,7% всех счетов при ≈37% непустых → ≈24% от непустых "
           "[расчёт]. Robinhood: MAU ÷ фондированные ≈47% (2023; заходы, не сделки).",
    "TPA": "Сделок на клиента в год: flatexDEGIRO 23–26, Nordnet ≈25–30 (в модели МР: ACT × TPA × 12 = 24); "
           "счёт Schwab ≈75; IBKR ≈160 (2025–2026).",
    "TICKET": "Условно.",
    "TAKE": "Тарифы: Россия 0,3% без абонплаты и 0,018–0,06% на активных тарифах; Казахстан: Freedom 0,085%, "
            "Halyk 0,03%. Эффективная ставка зависит от микса тарифов.",
    "EXEC": "IBKR 2025: затраты на исполнение и клиринг ≈21% от комиссий.",
    "AUC_PC": "Robinhood ≈ $10 тыс. на фондированного [расчёт: ARPU $171 ÷ 173 б.п.]; T-Investments ≈219 тыс. ₽ "
              "на клиента (2026); РФ: 2,3 млн ₽ на клиента с активами > 10 тыс. ₽ (ЦБ РФ, Q2 2026).",
    "CASH": "Свободные остатки к активам: Robinhood 8,1% (08.2026), Schwab 8,8–9,7%, IBKR 19–21% (2026).",
    "FLOAT_Y": "Внешний фактор: ставки денежного рынка; значение условное.",
    "FLOAT_P": "Условно: зависит от тарифной политики и конкурентов.",
    "MRG_PEN": "Маржинальный портфель к активам: Robinhood 5,6% (08.2026), IBKR 10,9–11,7%, Schwab ≈1–1,3%. "
               "Доля клиентов с маржой публично не раскрывается.",
    "MRG_DEBT": "Через портфель к активам (см. MRG_PEN).",
    "MRG_RATE": "Freedom (РК): базовая ставка НБРК + 4 п.п., не ниже 15%; T-Investments Premium ≈14–26% годовых "
                "[расчёт].",
    "FUND_RATE": "Внешний фактор; значение условное.",
    "CL": "Условно; ориентир — данные риск-менеджмента.",
    "FX_PEN": "Условно: доля конвертирующих клиентов в открытых источниках не найдена.",
    "FX_VOL": "Условно.",
    "FX_SPREAD": "Условно; у Swissquote валютные операции ≈13% выручки (2025).",
    "PRD_PEN": "Условно; российские брокеры: комиссии за размещения выросли в 1,5 раза в 1П 2026.",
    "PRD_VOL": "Условно.",
    "PRD_FEE": "Условно; диапазоны комиссий андеррайтинга не подтверждены источниками.",
    "AM_SHARE": "UBS GWM: доля мандатов ≈38% (2024); активы с комиссией ≈44% инвестированных [расчёт].",
    "AM_FEE": "Частные банки: валовая маржа на активы 82–91 б.п. (Julius Baer, EFG, 2025–2026).",
    "SUB_PEN": "Robinhood Gold: 4,8 млн подписчиков ≈17% фондированных; ≈40% новых клиентов оформляют "
               "подписку (2026).",
    "SUB_PRICE": "Robinhood Gold ≈ $5 в месяц; T «Трейдер» 290–390 ₽ в месяц.",
    "CUST_FEE": "Условно: кастодиальные ставки не подтверждены источниками.",
    "SUP_RATE": "Условно: нагрузку на поддержку брокеры не раскрывают.",
    "SUP_COST": "Gartner (2019): $8,01 за живой контакт против $0,10 за самообслуживание.",
    "KYC_UNIT": "Прайс-листы KYC-провайдеров (Sumsub, Veriff): $0,80–1,85 за проверку.",
    "KYC_MAN": "Условно.",
    "KYC_MAN_COST": "Условно.",
    "OPS_PC": "Условно.",
    "OPS_MAN": "Условно; DTCC: подтверждение сделки в день сделки ≈94,5–94,8% после перехода США на T+1 "
               "(институциональный ориентир STP).",
    "OPS_COST": "Условно.",
    "RM_LOAD": "Julius Baer: ≈ CHF 438 млн активов на менеджера (частный банк, верхняя граница).",
    "RM_COST": "Условно.",
    "CAC": "Robinhood: $15–53 на нового фондированного (2019–2021), ≈ $222 верхняя граница (2025); Wealthfront "
           "$85–131; Futu ≈ $295; Tiger $150–400; eToro ≈ $575 (верхняя граница). Маркетинг: 8,9% выручки "
           "Robinhood, 20% net contribution eToro.",
    "OPLOSS": "Условно.",
}
assert set(BENCHMARKS) == set(INPUTS), set(INPUTS) ^ set(BENCHMARKS)
for _code, _text in BENCHMARKS.items():
    INPUTS[_code].source = _text
SHOCK_DRIVERS = [i.code for _, items in INPUT_SECTIONS for i in items if i.shock]

# --- Расчётная модель ---------------------------------------------------------
# ("section", заголовок) | ("input", код) |
# ("calc", код, название, ед., формула-текст, шаблон Excel, режим «Итого»: sum | same)
HORIZON_REF = "'Вводные'!$D$6"
SHOCK_REF = "'Вводные'!$D$5"
MODEL_FIRST_ROW = 8
HORIZONS = [(1, "год 1"), (3, "долгосрочно")]

MODEL = [
    ("section", "Клиентская база"),
    ("input", "N0"), ("input", "LEADS"), ("input", "CR_OPEN"), ("input", "CR_FUND"),
    ("calc", "NEW", "Новые фондированные клиенты", "чел.", "LEADS × CR_OPEN × CR_FUND",
     "{LEADS}*{CR_OPEN}*{CR_FUND}", "sum"),
    ("input", "CHURN"),
    ("calc", "CHURNED", "Ушедшие фондированные клиенты", "чел.", "N0 × CHURN", "{N0}*{CHURN}", "sum"),
    ("calc", "N_AVG", "Фондированные клиенты, среднее за период", "чел.",
     "Горизонт 1: N0 + ½(NEW − CHURNED); 2: N0 + NEW − CHURNED; 3: NEW ÷ CHURN",
     "IF({@H}=3,IF({CHURN}>0,{NEW}/{CHURN},{N0}),{N0}+IF({@H}=1,0.5,1)*({NEW}-{CHURNED}))", "sum"),
    ("input", "ACT"),
    ("calc", "ACTIVE", "Активные клиенты (среднемесячно)", "чел.", "N_AVG × ACT", "{N_AVG}*{ACT}", "sum"),
    ("calc", "AUC", "Активы клиентов, среднее за период", "у.е.", "N_AVG × AUC_PC", "{N_AVG}*{AUC_PC}", "sum"),

    ("section", "R1. Торговые комиссии"),
    ("input", "TPA"), ("input", "TICKET"),
    ("calc", "TURN", "Оборот клиентов за период", "у.е.", "ACTIVE × TPA × 12 × TICKET",
     "{ACTIVE}*{TPA}*12*{TICKET}", "sum"),
    ("input", "TAKE"), ("input", "EXEC"),
    ("calc", "R1", "Торговые комиссии (нетто)", "у.е.", "TURN × (TAKE − EXEC)", "{TURN}*({TAKE}-{EXEC})", "sum"),

    ("section", "R2. Маржинальное кредитование"),
    ("input", "MRG_PEN"), ("input", "MRG_DEBT"),
    ("calc", "MPORT", "Маржинальный портфель, среднее за период", "у.е.", "N_AVG × MRG_PEN × MRG_DEBT",
     "{N_AVG}*{MRG_PEN}*{MRG_DEBT}", "sum"),
    ("input", "MRG_RATE"), ("input", "FUND_RATE"),
    ("calc", "R2", "Маржинальное кредитование (нетто)", "у.е.", "MPORT × (MRG_RATE − FUND_RATE)",
     "{MPORT}*({MRG_RATE}-{FUND_RATE})", "sum"),

    ("section", "R3. Доход на свободные остатки"),
    ("input", "AUC_PC"), ("input", "CASH"),
    ("calc", "CASHBAL", "Свободные денежные остатки клиентов", "у.е.", "AUC × CASH", "{AUC}*{CASH}", "sum"),
    ("input", "FLOAT_Y"), ("input", "FLOAT_P"),
    ("calc", "R3", "Доход на свободные остатки (нетто)", "у.е.", "CASHBAL × (FLOAT_Y − FLOAT_P)",
     "{CASHBAL}*({FLOAT_Y}-{FLOAT_P})", "sum"),

    ("section", "R4. Конвертация валют"),
    ("input", "FX_PEN"), ("input", "FX_VOL"),
    ("calc", "FXVOLUME", "Объём конвертаций за период", "у.е.", "N_AVG × FX_PEN × FX_VOL",
     "{N_AVG}*{FX_PEN}*{FX_VOL}", "sum"),
    ("input", "FX_SPREAD"),
    ("calc", "R4", "Конвертация валют", "у.е.", "FXVOLUME × FX_SPREAD", "{FXVOLUME}*{FX_SPREAD}", "sum"),

    ("section", "R5. Размещения и продукты"),
    ("input", "PRD_PEN"), ("input", "PRD_VOL"),
    ("calc", "PRDVOLUME", "Объём продаж продуктов и размещений", "у.е.", "N_AVG × PRD_PEN × PRD_VOL",
     "{N_AVG}*{PRD_PEN}*{PRD_VOL}", "sum"),
    ("input", "PRD_FEE"),
    ("calc", "R5", "Размещения и продукты", "у.е.", "PRDVOLUME × PRD_FEE", "{PRDVOLUME}*{PRD_FEE}", "sum"),

    ("section", "R6. ДУ и консультирование"),
    ("input", "AM_SHARE"),
    ("calc", "AUM", "Активы в ДУ и на консультировании", "у.е.", "AUC × AM_SHARE", "{AUC}*{AM_SHARE}", "sum"),
    ("input", "AM_FEE"),
    ("calc", "R6", "ДУ и консультирование", "у.е.", "AUM × AM_FEE", "{AUM}*{AM_FEE}", "sum"),

    ("section", "R7. Подписки и сервисные комиссии"),
    ("input", "SUB_PEN"),
    ("calc", "SUBS", "Платные подписчики", "чел.", "N_AVG × SUB_PEN", "{N_AVG}*{SUB_PEN}", "sum"),
    ("input", "SUB_PRICE"), ("input", "CUST_FEE"),
    ("calc", "R7", "Подписки и сервисные комиссии", "у.е.", "SUBS × SUB_PRICE + AUC × CUST_FEE",
     "{SUBS}*{SUB_PRICE}+{AUC}*{CUST_FEE}", "sum"),

    ("section", "Чистая выручка"),
    ("calc", "NR", "ЧВ — чистая выручка", "у.е.", "R1 + R2 + R3 + R4 + R5 + R6 + R7",
     "{R1}+{R2}+{R3}+{R4}+{R5}+{R6}+{R7}", "sum"),

    ("section", "Затраты на обслуживание"),
    ("input", "SUP_RATE"), ("input", "SUP_COST"),
    ("calc", "C1", "Поддержка клиентов", "у.е.", "N_AVG × SUP_RATE × SUP_COST", "{N_AVG}*{SUP_RATE}*{SUP_COST}", "sum"),
    ("input", "KYC_UNIT"), ("input", "KYC_MAN"), ("input", "KYC_MAN_COST"),
    ("calc", "C2", "Онбординг и KYC", "у.е.", "LEADS × (KYC_UNIT + KYC_MAN × KYC_MAN_COST)",
     "{LEADS}*({KYC_UNIT}+{KYC_MAN}*{KYC_MAN_COST})", "sum"),
    ("input", "OPS_PC"), ("input", "OPS_MAN"), ("input", "OPS_COST"),
    ("calc", "C3", "Бэк-офис: ручные операции", "у.е.", "N_AVG × OPS_PC × OPS_MAN × OPS_COST",
     "{N_AVG}*{OPS_PC}*{OPS_MAN}*{OPS_COST}", "sum"),
    ("input", "RM_LOAD"), ("input", "RM_COST"),
    ("calc", "C4", "Персональные менеджеры и покрытие", "у.е.", "N_AVG ÷ RM_LOAD × RM_COST",
     "IF({RM_LOAD}>0,{N_AVG}/{RM_LOAD}*{RM_COST},0)", "sum"),
    ("calc", "CTS", "ЗО — затраты на обслуживание", "у.е.", "C1 + C2 + C3 + C4", "{C1}+{C2}+{C3}+{C4}", "sum"),

    ("section", "Привлечение и потери"),
    ("input", "CAC"),
    ("calc", "ACQ", "ЗП — затраты на привлечение", "у.е.", "NEW × CAC", "{NEW}*{CAC}", "sum"),
    ("input", "CL"),
    ("calc", "C5", "Кредитные потери", "у.е.", "MPORT × CL", "{MPORT}*{CL}", "sum"),
    ("input", "OPLOSS"),
    ("calc", "C6", "Операционные потери", "у.е.", "OPLOSS", "{OPLOSS}", "sum"),
    ("calc", "LOSS", "ПТ — потери", "у.е.", "C5 + C6", "{C5}+{C6}", "sum"),

    ("section", "Маржинальный доход"),
    ("calc", "CM", "МД — маржинальный доход", "у.е.", "ЧВ − ЗО − ЗП − ПТ", "{NR}-{CTS}-{ACQ}-{LOSS}", "sum"),

    ("section", "Производные KPI"),
    ("calc", "ARPU", "Чистая выручка на фондированного клиента", "у.е.", "NR ÷ N_AVG",
     "IF({N_AVG}>0,{NR}/{N_AVG},0)", "same"),
    ("calc", "YIELD", "Доходность активов клиентов", "б.п.", "NR ÷ AUC × 10 000",
     "IF({AUC}>0,{NR}/{AUC}*10000,0)", "same"),
    ("calc", "CM_MARGIN", "Маржинальность (МД ÷ ЧВ)", "%", "CM ÷ NR", "IF({NR}>0,{CM}/{NR},0)", "same"),
    ("calc", "CM_PC", "МД на фондированного клиента", "у.е.", "CM ÷ N_AVG", "IF({N_AVG}>0,{CM}/{N_AVG},0)", "same"),
    ("calc", "CONTRIB_PC", "Вклад клиента до затрат на привлечение, в год", "у.е.", "(NR − CTS − LOSS) ÷ N_AVG",
     "IF({N_AVG}>0,({NR}-{CTS}-{LOSS})/{N_AVG},0)", "same"),
    ("calc", "LTV", "LTV — вклад клиента за срок жизни", "у.е.", "CONTRIB_PC ÷ (CHURNED ÷ N0)",
     "IF({CHURNED}>0,{CONTRIB_PC}*{N0}/{CHURNED},0)", "same"),
    ("calc", "LTV_CAC", "LTV ÷ CAC", "x", "LTV ÷ (ACQ ÷ NEW)", "IF({ACQ}>0,{LTV}*{NEW}/{ACQ},0)", "same"),
    ("calc", "PAYBACK", "Срок окупаемости привлечения", "мес.", "(ACQ ÷ NEW) ÷ (CONTRIB_PC ÷ 12)",
     "IF(AND({NEW}>0,{CONTRIB_PC}>0),{ACQ}/{NEW}/({CONTRIB_PC}/12),0)", "same"),
    ("calc", "RATE_SHARE", "Доля ЧВ, зависящая от процентных ставок", "%", "(R2 + R3) ÷ NR",
     "IF({NR}>0,({R2}+{R3})/{NR},0)", "same"),
]
CALC = {r[1]: r for r in MODEL if r[0] == "calc"}


def meta(code):
    """Название, единица и формула-текст метрики модели."""
    if code in INPUTS:
        i = INPUTS[code]
        return i.name, i.unit, "Вводная"
    _, _, name, unit, ftext, _, _ = CALC[code]
    return name, unit, ftext


# --- Листы --------------------------------------------------------------------
def header_row(ws, row, labels, height=30):
    for col, label in enumerate(labels, start=1):
        c = ws.cell(row=row, column=col, value=label)
        c.font = font(WHITE, bold=True)
        c.fill = FILL_HEAD
        c.alignment = Alignment(wrap_text=True, vertical="center")
        c.border = BOX
    ws.row_dimensions[row].height = height


def title(ws, text, subtitle=None):
    ws["A1"] = text
    ws["A1"].font = font(bold=True, size=14)
    if subtitle:
        ws["A2"] = subtitle
        ws["A2"].font = font(GREY, italic=True)


def widths(ws, mapping):
    for col, w in mapping.items():
        ws.column_dimensions[col].width = w


def section_row(ws, row, text, ncols):
    for col in range(1, ncols + 1):
        ws.cell(row=row, column=col).fill = FILL_SECTION
    ws.cell(row=row, column=1, value=text).font = font(bold=True)


def build_inputs(wb):
    ws = wb.create_sheet("Вводные")
    title(ws, "Вводные модели по сегментам",
          "Синий шрифт на жёлтом фоне — вводные. Значения иллюстративные: замените их фактическими данными. "
          "Все суммы — в условных единицах (у.е.) за период (год).")
    section_row(ws, 4, "Глобальные параметры", 12)
    for row, code, name, unit, value, note in [
        (5, "SHOCK", "Шаг анализа чувствительности (улучшение драйвера, относительное)", "%", 0.01,
         "1% — стандарт; модель линейна по каждому драйверу, поэтому эффект +5% = 5 × эффект +1%."),
        (6, "HORIZON", "Горизонт оценки для листов «Сводка», «Дерево» и колонок E–H «Модели»", "режим", 1,
         "1 — год 1: P&L плана, новые и ушедшие клиенты учитываются за полгода; 2 — run-rate на конец года; "
         "3 — долгосрочно: база сходится к NEW ÷ CHURN. Чувствительность всегда считается в режимах 1 и 3."),
    ]:
        ws.cell(row=row, column=1, value=code).font = font(bold=True)
        ws.cell(row=row, column=2, value=name).font = font()
        ws.cell(row=row, column=3, value=unit).font = font()
        c = ws.cell(row=row, column=4, value=value)
        c.font, c.fill, c.number_format, c.border = font(BLUE), FILL_INPUT, NUM[unit], BOX
        ws.cell(row=row, column=12, value=note).font = font(GREY, italic=True)
    dv = DataValidation(type="list", formula1='"1,2,3"', allow_blank=False)
    ws.add_data_validation(dv)
    dv.add("D6")

    for col, (seg, _) in enumerate(SEGMENTS, start=4):
        ws.cell(row=8, column=col, value=seg).font = font(GREY, size=8)
    ws.cell(row=8, column=1, value="коды сегментов →").font = font(GREY, size=8)
    header_row(ws, 9, ["Код", "Параметр", "Ед."] + [s[1] for s in SEGMENTS] +
               ["Направление", "Управляемость", "Тип рычага", "Влияет на", "Источник / ориентир", "Комментарий"])
    row = 10
    for section, items in INPUT_SECTIONS:
        section_row(ws, row, section, 12)
        row += 1
        for i in items:
            ws.cell(row=row, column=1, value=i.code).font = font(bold=True)
            ws.cell(row=row, column=2, value=i.name).font = font()
            ws.cell(row=row, column=3, value=i.unit).font = font()
            for col, v in enumerate(i.values, start=4):
                c = ws.cell(row=row, column=col, value=v)
                c.font, c.fill, c.number_format, c.border = font(BLUE), FILL_INPUT, NUM[i.unit], BOX
            d = ws.cell(row=row, column=7, value=i.direction)
            d.font, d.number_format = font(), DIR_FMT
            for col, v in enumerate([i.control, i.lever, i.affects, i.source, i.comment], start=8):
                ws.cell(row=row, column=col, value=v).font = font(GREY if col >= 11 else BLACK)
            for col in range(1, 13):
                ws.cell(row=row, column=col).alignment = WRAP
            row += 1
    widths(ws, {"A": 13, "B": 52, "C": 9, "D": 14, "E": 14, "F": 16, "G": 17, "H": 14, "I": 12,
                "J": 20, "K": 42, "L": 48})
    ws.freeze_panes = "D10"
    return ws, 10, row - 1


def build_model(wb, in_first, in_last):
    ws = wb.create_sheet("Модель")
    title(ws, "Расчётная модель маржинального дохода",
          "Колонки E–H — расчёт в режиме HORIZON с листа «Вводные». Справа (сгруппированы, раскрываются "
          "кнопкой «+») — технические сценарии чувствительности: база и по одному улучшенному драйверу на "
          "сегмент, в горизонтах «год 1» и «долгосрочно».")
    col_of = {}  # (сегмент, драйвер, горизонт) -> колонка; горизонт "G" — режим HORIZON
    for idx, (seg, _) in enumerate(SEGMENTS):
        col_of[(seg, "BASE", "G")] = 5 + idx
    first_scen_col = col = 10  # J
    for h, _ in HORIZONS:
        for seg, _ in SEGMENTS:
            for drv in ["BASE"] + SHOCK_DRIVERS:
                col_of[(seg, drv, h)] = col
                col += 1
    last_col = col - 1

    for label, r in [("Сегмент", 3), ("Шок драйвера", 4), ("Горизонт", 5), ("Ключ сценария", 6)]:
        ws.cell(row=r, column=1, value=label).font = font(GREY, size=8)
    labels = ["Код", "Метрика", "Ед.", "Формула"] + [s[1] for s in SEGMENTS] + ["Итого", ""]
    for (seg, drv, h), c in col_of.items():
        L = get_column_letter(c)
        ws.cell(row=3, column=c, value=seg).font = font(GREY, size=8)
        ws.cell(row=4, column=c, value=drv).font = font(GREY, size=8)
        if h == "G":
            ws.cell(row=5, column=c, value=f"={HORIZON_REF}").font = font(GREEN, size=8)
            ws.cell(row=6, column=c, value=f"{seg}|ПОКАЗ").font = font(GREY, size=8)
        else:
            ws.cell(row=5, column=c, value=h).font = font(GREY, size=8)
            ws.cell(row=6, column=c, value=f'={L}3&"|"&{L}4&"|"&{L}5').font = font(GREY, size=8)
            hname = dict(HORIZONS)[h]
            labels.append(f"{SEG_SHORT[seg]}, {hname}: {'база' if drv == 'BASE' else drv}")
    header_row(ws, 7, labels, height=42)

    rows, r, row_of = [], MODEL_FIRST_ROW, {}
    for item in MODEL:
        rows.append((r, item))
        if item[0] != "section":
            row_of[item[1]] = r
        r += 1
    last_row = r - 1

    in_vals = f"'Вводные'!$D${in_first}:$F${in_last}"
    in_codes = f"'Вводные'!$A${in_first}:$A${in_last}"
    in_dirs = f"'Вводные'!$G${in_first}:$G${in_last}"
    in_segs = "'Вводные'!$D$8:$F$8"

    def expand(template, L):
        def repl(m):
            key = m.group(1)
            return f"{L}$5" if key == "@H" else f"{L}{row_of[key]}"
        return "=" + re.sub(r"\{(@?\w+)\}", repl, template)

    data_cols = sorted(col_of.values())
    for r, item in rows:
        if item[0] == "section":
            section_row(ws, r, item[1], 8)
            continue
        code = item[1]
        name, unit, ftext = meta(code)
        ws.cell(row=r, column=1, value=code).font = font(bold=item[0] == "calc")
        ws.cell(row=r, column=2, value=name).font = font(bold=code in ("NR", "CTS", "ACQ", "LOSS", "CM"))
        ws.cell(row=r, column=3, value=unit).font = font()
        ws.cell(row=r, column=4, value=ftext).font = font(GREY)
        for col in data_cols:
            L = get_column_letter(col)
            if item[0] == "input":
                f = (f"=INDEX({in_vals},MATCH($A{r},{in_codes},0),MATCH({L}$3,{in_segs},0))"
                     f"*(1+IF({L}$4=$A{r},{SHOCK_REF}*INDEX({in_dirs},MATCH($A{r},{in_codes},0)),0))")
                color = GREEN
            else:
                f = expand(item[5], L)
                color = BLACK
            c = ws.cell(row=r, column=col, value=f)
            c.font = font(color, bold=code == "CM")
            c.number_format = NUM[unit] if item[0] == "input" else NUM_CALC[unit]
        H = ws.cell(row=r, column=8)
        if item[0] == "input":
            H.value = f"=SUM(E{r}:G{r})" if INPUTS[code].total else None
        elif item[6] == "sum":
            H.value = f"=SUM(E{r}:G{r})"
        else:
            H.value = expand(item[5], "H")
        H.font = font(bold=code == "CM")
        H.number_format = NUM[unit] if item[0] == "input" else NUM_CALC[unit]
        if code in ("NR", "CTS", "ACQ", "LOSS", "CM"):
            for col in range(1, 9):
                ws.cell(row=r, column=col).fill = FILL_RESULT

    widths(ws, {"A": 12, "B": 44, "C": 7, "D": 34, "E": 15, "F": 15, "G": 17, "H": 16, "I": 3})
    for col in range(first_scen_col, last_col + 1):
        ws.column_dimensions[get_column_letter(col)].width = 14
    ws.column_dimensions.group(get_column_letter(first_scen_col), get_column_letter(last_col),
                               hidden=True, outline_level=1)
    ws.freeze_panes = f"E{MODEL_FIRST_ROW}"
    return ws, row_of, first_scen_col, last_col, last_row


ACQ_DRIVERS = {"LEADS", "CR_OPEN", "CR_FUND"}


def build_sensitivity(wb, row_of, in_first, in_last, first_scen_col, last_col):
    ws = wb.create_sheet("Чувствительность")
    title(ws, "Чувствительность маржинального дохода к драйверам",
          "Сколько у.е. МД в год даёт улучшение драйвера на 1% (относительно текущего значения) или на "
          "практический шаг, при прочих равных — в двух горизонтах: «год 1» (P&L плана) и «долгосрочно» "
          "(база сходится к NEW ÷ CHURN). Чувствительность — не приоритет: приоритет = ценность × достижимый "
          "сдвиг × вероятность ÷ трудозатраты.")
    cm = row_of["CM"]
    F, L = get_column_letter(first_scen_col), get_column_letter(last_col)
    keys = f"'Модель'!${F}$6:${L}$6"
    cm_scen = f"'Модель'!${F}${cm}:${L}${cm}"

    def cm_of(seg, drv_expr, h):
        return f'INDEX({cm_scen},MATCH("{seg}|"&{drv_expr}&"|{h}",{keys},0))'

    for label_cell, label, val_cell, h in [("J3", "Базовый МД, год 1:", "M3", 1),
                                           ("N3", "Базовый МД, долгосрочно:", "Q3", 3)]:
        ws[label_cell] = label
        ws[label_cell].font = font(GREY)
        ws[val_cell] = "=" + "+".join(cm_of(seg, '"BASE"', h) for seg, _ in SEGMENTS)
        ws[val_cell].font, ws[val_cell].number_format = font(GREEN, bold=True), NUM["у.е."]
    header_row(ws, 4, ["Код", "Драйвер", "Ед.", "Направление", "Управляемость", "Тип рычага",
                       "Значение: МР", "Значение: СК", "Значение: ИК",
                       "ΔМД +1%, год 1: МР", "ΔМД +1%, год 1: СК", "ΔМД +1%, год 1: ИК", "ΔМД +1%, год 1: итого",
                       "ΔМД +1%, долгосрочно: МР", "ΔМД +1%, долгосрочно: СК", "ΔМД +1%, долгосрочно: ИК",
                       "ΔМД +1%, долгосрочно: итого", "Доля от МД (долгосрочно)", "Ранг в группе (долгосрочно)",
                       "Практический шаг", "ΔМД за шаг, год 1: итого", "ΔМД за шаг, долгосрочно: итого",
                       "Комментарий", "ключ: объёмные и затратные", "ключ: ценовые"], height=56)
    in_codes = f"'Вводные'!$A${in_first}:$A${in_last}"
    first = r = 5
    last = first + len(SHOCK_DRIVERS) - 1
    for code in SHOCK_DRIVERS:
        i = INPUTS[code]
        ws.cell(row=r, column=1, value=code).font = font(bold=True)
        ws.cell(row=r, column=2, value=i.name).font = font()
        ws.cell(row=r, column=3, value=i.unit).font = font()
        d = ws.cell(row=r, column=4, value=i.direction)
        d.number_format, d.font = DIR_FMT, font()
        ws.cell(row=r, column=5, value=i.control).font = font()
        ws.cell(row=r, column=6, value=i.lever).font = font()
        for k, (seg, base_col) in enumerate([("MR", "D"), ("AF", "E"), ("IC", "F")]):
            v = ws.cell(row=r, column=7 + k,
                        value=f"=INDEX('Вводные'!${base_col}${in_first}:${base_col}${in_last},MATCH($A{r},{in_codes},0))")
            v.font, v.number_format = font(GREEN), NUM[i.unit]
            for start_col, h in [(10, 1), (14, 3)]:
                dcell = ws.cell(row=r, column=start_col + k,
                                value=f"={cm_of(seg, f'$A{r}', h)}-{cm_of(seg, chr(34) + 'BASE' + chr(34), h)}")
                dcell.font, dcell.number_format = font(GREEN), NUM["у.е."]
        for col, rng in [(13, "J{r}:L{r}"), (17, "N{r}:P{r}")]:
            t = ws.cell(row=r, column=col, value="=SUM(" + rng.format(r=r) + ")")
            t.number_format, t.font = NUM["у.е."], font(bold=True)
        sh = ws.cell(row=r, column=18, value=f"=IF($Q$3<>0,Q{r}/$Q$3,0)")
        sh.number_format, sh.font = '0.00%;(0.00%);"-"', font()
        ws.cell(row=r, column=19,
                value=(f'=IF($E{r}="Внешний","",IF($F{r}="Ценовой",RANK(Y{r},$Y${first}:$Y${last}),'
                       f'RANK(X{r},$X${first}:$X${last})))')).font = font()
        ws.cell(row=r, column=20, value=i.step_label or "").font = font()
        if i.step:
            for col, (a, b, c) in [(21, ("J", "K", "L")), (22, ("N", "O", "P"))]:
                parts = [f"IF({v}{r}<>0,{dl}{r}*{i.step}/({v}{r}*{SHOCK_REF}),0)"
                         for v, dl in zip(("G", "H", "I"), (a, b, c))]
                t = ws.cell(row=r, column=col, value="=" + "+".join(parts))
                t.number_format, t.font = NUM["у.е."], font(bold=col == 22)
        note = []
        if code in ACQ_DRIVERS:
            note.append("В горизонте «год 1» рост привлечения снижает МД: CAC платится сразу, доход приходит позже.")
        if code == "CHURN":
            note.append("Долгосрочный эффект нелинеен (база = NEW ÷ CHURN): шаг в 1 п.п. оценён приблизительно.")
        if i.lever == "Ценовой":
            note.append("Ценовой рычаг: эффект при неизменных объёмах — учитывать эластичность.")
        if i.control == "Внешний":
            note.append("Внешний фактор: гипотезы на него не претендуют, используется для сценариев.")
        if code == "RM_LOAD":
            note.append("Эффект обратно пропорционален нагрузке — линейность приблизительная.")
        ws.cell(row=r, column=23, value=" ".join(note)).font = font(GREY, italic=True)
        for col, cond in [(24, f'OR($E{r}="Внешний",$F{r}="Ценовой")'), (25, f'$F{r}<>"Ценовой"')]:
            key = ws.cell(row=r, column=col, value=f"=IF({cond},-1E+15,Q{r})+ROW()/1000000000")
            key.font, key.number_format = font(GREY, size=8), NUM["у.е."]
        for col in range(1, 24):
            ws.cell(row=r, column=col).alignment = WRAP
        r += 1
    for rng in (f"M{first}:M{last}", f"Q{first}:Q{last}"):
        ws.conditional_formatting.add(rng, DataBarRule(start_type="num", start_value=0, end_type="max",
                                                       color="FF5B9BD5"))
    widths(ws, {"A": 12, "B": 44, "C": 9, "D": 17, "E": 13, "F": 12, "G": 12, "H": 12, "I": 13,
                "J": 13, "K": 13, "L": 13, "M": 14, "N": 13, "O": 13, "P": 13, "Q": 14, "R": 11, "S": 10,
                "T": 10, "U": 14, "V": 14, "W": 46, "X": 4, "Y": 4})
    ws.column_dimensions["X"].hidden = True
    ws.column_dimensions["Y"].hidden = True
    ws.freeze_panes = "C5"
    return ws, first, last, keys, F, L


TREE = [
    (0, "CM"), (1, "NR"),
    (2, "R1"), (3, "TURN"), (4, "ACTIVE"), (4, "TPA"), (4, "TICKET"), (3, "TAKE"), (3, "EXEC"),
    (2, "R2"), (3, "MPORT"), (4, "MRG_PEN"), (4, "MRG_DEBT"), (3, "MRG_RATE"), (3, "FUND_RATE"),
    (2, "R3"), (3, "CASHBAL"), (4, "AUC"), (5, "AUC_PC"), (4, "CASH"), (3, "FLOAT_Y"), (3, "FLOAT_P"),
    (2, "R4"), (3, "FXVOLUME"), (4, "FX_PEN"), (4, "FX_VOL"), (3, "FX_SPREAD"),
    (2, "R5"), (3, "PRDVOLUME"), (4, "PRD_PEN"), (4, "PRD_VOL"), (3, "PRD_FEE"),
    (2, "R6"), (3, "AUM"), (4, "AM_SHARE"), (3, "AM_FEE"),
    (2, "R7"), (3, "SUBS"), (4, "SUB_PEN"), (3, "SUB_PRICE"), (3, "CUST_FEE"),
    (1, "CTS"),
    (2, "C1"), (3, "SUP_RATE"), (3, "SUP_COST"),
    (2, "C2"), (3, "LEADS"), (3, "KYC_UNIT"), (3, "KYC_MAN"), (3, "KYC_MAN_COST"),
    (2, "C3"), (3, "OPS_PC"), (3, "OPS_MAN"), (3, "OPS_COST"),
    (2, "C4"), (3, "RM_LOAD"), (3, "RM_COST"),
    (1, "ACQ"), (2, "NEW"), (2, "CAC"),
    (1, "LOSS"), (2, "C5"), (3, "CL"), (2, "C6"), (3, "OPLOSS"),
    ("section", "Клиентская база — общий драйвер веток R1–R7 и затрат"),
    (1, "N_AVG"), (2, "N0"), (2, "NEW"), (3, "LEADS"), (3, "CR_OPEN"), (3, "CR_FUND"),
    (2, "CHURNED"), (3, "CHURN"),
    (1, "ACTIVE"), (2, "ACT"),
    ("section", "Производные KPI"),
    (1, "ARPU"), (1, "YIELD"), (1, "CM_MARGIN"), (1, "CM_PC"), (1, "CONTRIB_PC"), (1, "LTV"),
    (1, "LTV_CAC"), (1, "PAYBACK"), (1, "RATE_SHARE"),
]


def build_tree(wb, model_last_row):
    ws = wb.create_sheet("Дерево")
    title(ws, "Дерево метрик: от маржинального дохода к драйверам",
          "Каждый узел — формула от дочерних. Значения — базовый расчёт с листа «Модель».")
    header_row(ws, 4, ["Уровень", "Код", "Метрика", "Формула", "Ед.", "Масс-розница", "Состоятельные",
                       "Институционалы и корп.", "Итого", "Тип"])
    rng = f"'Модель'!$A${MODEL_FIRST_ROW}:$A${model_last_row}"
    r = 5
    for item in TREE:
        if item[0] == "section":
            section_row(ws, r, item[1], 10)
            r += 1
            continue
        level, code = item
        name, unit, ftext = meta(code)
        kind = ("Вводная: " + INPUTS[code].lever.lower()) if code in INPUTS else "Расчёт"
        ws.cell(row=r, column=1, value=level).font = font(GREY)
        ws.cell(row=r, column=2, value=code).font = font(bold=level <= 1)
        c = ws.cell(row=r, column=3, value=name)
        c.font, c.alignment = font(bold=level <= 1), Alignment(indent=level * 2, vertical="top")
        ws.cell(row=r, column=4, value=ftext).font = font(GREY)
        ws.cell(row=r, column=5, value=unit).font = font()
        for k, col in enumerate(["E", "F", "G", "H"]):
            if col == "H" and code in INPUTS and not INPUTS[code].total:
                continue
            v = ws.cell(row=r, column=6 + k,
                        value=f"=INDEX('Модель'!${col}${MODEL_FIRST_ROW}:${col}${model_last_row},MATCH($B{r},{rng},0))")
            v.font = font(GREEN, bold=level <= 1)
            v.number_format = NUM[unit] if code in INPUTS else NUM_CALC[unit]
        ws.cell(row=r, column=10, value=kind).font = font(GREY)
        if level <= 1:
            for col in range(1, 11):
                ws.cell(row=r, column=col).fill = FILL_RESULT
        r += 1
    widths(ws, {"A": 8, "B": 12, "C": 52, "D": 36, "E": 7, "F": 15, "G": 15, "H": 17, "I": 16, "J": 20})
    ws.freeze_panes = "D5"


def build_summary(wb, row_of, model_last_row, sens_first, sens_last, keys, F, L):
    ws = wb.create_sheet("Сводка")
    title(ws, "Сводка: экономика брокерского бизнеса по сегментам",
          "Значения иллюстративные до замены вводных фактическими данными. P&L и KPI — в режиме HORIZON "
          "(лист «Вводные»).")
    ws["F3"] = "Режим HORIZON:"
    ws["F3"].font = font(GREY)
    ws["G3"] = f"={HORIZON_REF}"
    ws["G3"].font = font(GREEN, bold=True)
    rng = f"'Модель'!$A${MODEL_FIRST_ROW}:$A${model_last_row}"

    def link(r, col_model, code_cell, unit):
        c = ws.cell(row=r, column=col_model[0],
                    value=f"=INDEX('Модель'!${col_model[1]}${MODEL_FIRST_ROW}:${col_model[1]}${model_last_row},"
                          f"MATCH({code_cell},{rng},0))")
        c.font, c.number_format = font(GREEN), NUM_CALC[unit]
        return c

    header_row(ws, 4, ["Код", "P&L, у.е. за период", "Масс-розница", "Состоятельные", "Институционалы и корп.",
                       "Итого", "Доля в ЧВ"])
    pl = ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "NR", "C1", "C2", "C3", "C4", "CTS", "ACQ", "C5", "C6",
          "LOSS", "CM"]
    r = 5
    nr_row = None
    for code in pl:
        name, unit, _ = meta(code)
        ws.cell(row=r, column=1, value=code).font = font(bold=True)
        ws.cell(row=r, column=2, value=name).font = font(bold=code in ("NR", "CTS", "ACQ", "LOSS", "CM"))
        for k, col in enumerate(["E", "F", "G", "H"]):
            link(r, (3 + k, col), f"$A{r}", unit)
        if code == "NR":
            nr_row = r
        r += 1
    for rr in range(5, r):
        s = ws.cell(row=rr, column=7, value=f"=IF($F${nr_row}<>0,F{rr}/$F${nr_row},0)")
        s.number_format, s.font = '0.0%;(0.0%);"-"', font()
        if ws.cell(row=rr, column=1).value in ("NR", "CTS", "ACQ", "LOSS", "CM"):
            for col in range(1, 8):
                ws.cell(row=rr, column=col).fill = FILL_RESULT

    r += 1
    header_row(ws, r, ["Код", "Ключевые показатели", "Масс-розница", "Состоятельные", "Институционалы и корп.",
                       "Итого", ""])
    r += 1
    for code in ["N_AVG", "NEW", "ACTIVE", "AUC", "TURN", "MPORT", "ARPU", "YIELD", "CM_MARGIN", "CM_PC",
                 "LTV", "LTV_CAC", "PAYBACK", "RATE_SHARE"]:
        name, unit, _ = meta(code)
        ws.cell(row=r, column=1, value=code).font = font(bold=True)
        ws.cell(row=r, column=2, value=name).font = font()
        for k, col in enumerate(["E", "F", "G", "H"]):
            link(r, (3 + k, col), f"$A{r}", unit)
        r += 1

    # долгосрочный ориентир: базовые сценарии горизонта 3
    r += 1
    header_row(ws, r, ["Код", "Долгосрочный ориентир (горизонт 3: база = NEW ÷ CHURN)", "Масс-розница",
                       "Состоятельные", "Институционалы и корп.", "Итого", ""])
    r += 1
    for code in ["N_AVG", "NR", "CM"]:
        name, unit, _ = meta(code)
        ws.cell(row=r, column=1, value=code).font = font(bold=True)
        ws.cell(row=r, column=2, value=name).font = font()
        for k, (seg, _) in enumerate(SEGMENTS):
            c = ws.cell(row=r, column=3 + k,
                        value=f"=INDEX('Модель'!${F}${row_of[code]}:${L}${row_of[code]},"
                              f'MATCH("{seg}|BASE|3",{keys},0))')
            c.font, c.number_format = font(GREEN), NUM_CALC[unit]
        t = ws.cell(row=r, column=6, value=f"=SUM(C{r}:E{r})")
        t.font, t.number_format = font(bold=True), NUM_CALC[unit]
        r += 1

    s_rng = lambda col: f"'Чувствительность'!${col}${sens_first}:${col}${sens_last}"
    n_price = sum(1 for c in SHOCK_DRIVERS if INPUTS[c].lever == "Ценовой")
    for heading, key_col, n in [("Топ-10 объёмных и затратных драйверов: ценность улучшения на 1%", "X", 10),
                                ("Ценовые рычаги: ценность +1% при неизменных объёмах (без эластичности)", "Y",
                                 n_price)]:
        r += 1
        header_row(ws, r, ["Ранг", heading, "Код", "ΔМД в год, долгосрочно", "ΔМД, год 1", "Тип рычага",
                           "Управляемость"], height=30)
        r += 1
        for k in range(1, n + 1):
            ws.cell(row=r, column=1, value=k).font = font()
            pos = f"MATCH(LARGE({s_rng(key_col)},{k}),{s_rng(key_col)},0)"
            for col, src, fmt in [(3, "A", None), (2, "B", None), (4, "Q", NUM["у.е."]), (5, "M", NUM["у.е."]),
                                  (6, "F", None), (7, "E", None)]:
                c = ws.cell(row=r, column=col, value=f"=INDEX({s_rng(src)},{pos})")
                c.font = font(GREEN)
                if fmt:
                    c.number_format = fmt
            r += 1
    for text in ["Рейтинг — по долгосрочному эффекту. Внешние факторы (ставки рынка) исключены; ценовые рычаги — "
                 "отдельный тип решений, их эффект показан без реакции клиентов.",
                 "Отрицательный эффект года 1 у драйверов привлечения — не ошибка: CAC платится сразу, доход "
                 "приходит позже. На иллюстративных данных рейтинг показывает механику, а не приоритеты."]:
        r += 1
        ws.cell(row=r, column=1, value=text).font = font(GREY, italic=True)
    widths(ws, {"A": 13, "B": 66, "C": 15, "D": 15, "E": 17, "F": 16, "G": 14})
    ws.freeze_panes = "C5"


LEGEND = [
    ("Документ", "Модель метрик брокерского бизнеса — этап 1 дорожной карты проектов"),
    ("Версия", "v0.1 — черновик для обсуждения"),
    ("Назначение", "Единая система метрик, связывающая управляемые драйверы с маржинальным доходом (МД). "
                   "На этапе 2 каждая гипотеза ссылается на код драйвера, а её эффект переводится в деньги "
                   "через лист «Чувствительность»."),
    ("Статус данных", "Значения вводных иллюстративные: условный брокер среднего размера, ориентиры — публичные "
                      "брокеры (см. колонку «Источник / ориентир» на листе «Вводные» и отчёт с бенчмарками "
                      "в репозитории). Перед выводами замените жёлтые ячейки фактом."),
    ("Надёжность ориентиров", "Цифры бенчмарков получены из поисковых выдержек первоисточников: прямой доступ к "
                              "отчётам компаний был закрыт. Перед внешним использованием сверить с документами."),
    ("Единицы", "у.е. — условные денежные единицы; все суммы — за период (год)."),
    (None, None),
    ("Этапы", ""),
    ("1. Метрики", "Этот файл: дерево, паспорта, модель, чувствительность — черновик готов"),
    ("2. Гипотезы", "Шаблон карты гипотез, привязка к драйверам — следующий шаг"),
    ("3. Трудозатраты", "Оценка гипотез — после этапа 2"),
    ("4. Дорожная карта", "Приоритизация и раскладка по времени — после этапа 3"),
    (None, None),
    ("Листы", ""),
    ("Сводка", "P&L по сегментам, ключевые KPI, топ-10 драйверов по ценности улучшения"),
    ("Дерево", "Иерархия метрик от МД до драйверов с текущими значениями"),
    ("Вводные", "Все допущения модели по сегментам — редактировать здесь"),
    ("Чувствительность", "Ценность улучшения каждого драйвера на 1% и на практический шаг (1 п.п., 1 б.п.) — "
                         "в горизонтах «год 1» и «долгосрочно»"),
    ("Модель", "Расчёт по сегментам; справа сгруппированы технические сценарии для чувствительности"),
    ("Паспорта", "Определения, формулы, источники данных, владельцы; опережающие индикаторы, "
                 "ограничители, внешние факторы"),
    (None, None),
    ("Цвета", ""),
    ("Вводная", "Синий шрифт на жёлтом фоне — допущения, которые нужно заменить фактом"),
    ("Формула", "Чёрный шрифт — расчёт"),
    ("Ссылка", "Зелёный шрифт — значение с другого листа"),
    (None, None),
    ("Принятые решения", ""),
    ("Рынок", "Универсальная модель без привязки к юрисдикции; бенчмарки — публичные брокеры"),
    ("Сегменты", "Масс-розница, состоятельные, институционалы и корпоративные; B2B вне периметра"),
    ("Верх дерева", "Маржинальный доход; регуляторные задачи — отдельный обязательный трек без денежной оценки"),
    ("Формат", "Excel-модель + описание в markdown в репозитории"),
    (None, None),
    ("Как пользоваться", ""),
    ("Шаг 1", "Замените значения на листе «Вводные» фактическими данными по сегментам"),
    ("Шаг 2", "Сверьте «Сводку» с управленческой отчётностью: ЧВ и МД по сегментам должны совпасть (±5%)"),
    ("Шаг 3", "На листе «Чувствительность» — сколько МД даёт улучшение каждого драйвера"),
    ("Шаг 4", "HORIZON на листе «Вводные» переключает «Сводку» и «Дерево»: 1 — год 1 (P&L плана), "
              "2 — run-rate на конец года, 3 — долгосрочно (база = NEW ÷ CHURN). «Чувствительность» всегда "
              "показывает горизонты 1 и 3 рядом"),
    (None, None),
    ("Ограничения", ""),
    ("Сегменты", "Независимы: переход клиентов между сегментами (апгрейд) пока не моделируется"),
    ("Эластичность", "Не учитывается: ценовые рычаги показаны при неизменных объёмах"),
    ("Линейность", "Модель линейна по каждому драйверу (кроме нагрузки на менеджера): эффект +5% = 5 × эффект "
                   "+1%; совместные изменения дают небольшой перекрёстный эффект"),
    ("Периметр", "Постоянные расходы (ИТ-платформа, центральные функции, аренда) в МД не входят"),
    ("Горизонт", "Долгосрочный режим — упрощение: без дисконтирования и при неизменных драйверах; это ориентир "
                 "для сравнения гипотез, а не прогноз"),
]


def build_legend(wb):
    ws = wb.active
    ws.title = "Легенда"
    title(ws, "Дорожная карта брокерского бизнеса — модель метрик (этап 1)")
    r = 3
    for key, val in LEGEND:
        if key is None:
            r += 1
            continue
        k = ws.cell(row=r, column=1, value=key)
        v = ws.cell(row=r, column=2, value=val)
        if val == "":
            section_row(ws, r, key, 2)
        else:
            k.font, v.font = font(bold=True), font()
            v.alignment = WRAP
        if key == "Вводная" and r > 20:
            v.font, v.fill = font(BLUE), FILL_INPUT
        elif key == "Ссылка":
            v.font = font(GREEN)
        r += 1
    widths(ws, {"A": 22, "B": 110})


# --- Паспорта метрик -------------------------------------------------------------
PASSPORT_COLS = ["Код", "Метрика", "Уровень", "Тип", "Группа", "Определение", "Формула / расчёт", "Ед.",
                 "Сегменты", "Направление", "Управляемость", "Опережающая / запаздывающая", "Влияет на",
                 "Источник данных", "Частота", "Владелец (роль)", "Риски интерпретации"]

# код: (уровень, тип, группа, определение, источник, частота, владелец, опер./запазд., риски)
P = {
    "CM": ("L0", "Результат", "Финансы",
           "Чистая выручка за вычетом затрат на обслуживание, привлечение и потерь, прямо относимых на клиентов и "
           "операции. Постоянные расходы (ИТ-платформа, центральные функции, аренда) не вычитаются.",
           "Управленческий P&L по сегментам", "Месяц", "Финансовый директор", "Запаздывающая",
           "Значимая часть колебаний — рынок (ставки, волатильность): оценивать с поправкой на внешние факторы."),
    "NR": ("L1", "Результат", "Доходы",
           "Сумма доходов по семи источникам, каждый за вычетом прямых затрат, неотделимых от операции: биржевые "
           "и клиринговые сборы, стоимость фондирования, проценты клиентам на остатки.",
           "Главная книга, биллинг, бэк-офис", "Месяц", "Финансовый директор", "Запаздывающая",
           "Сравнивать с конкурентами только в нетто-выражении: валовые комиссии завышают долю торговли."),
    "CTS": ("L1", "Результат", "Затраты",
            "Затраты, растущие с числом клиентов и операций: поддержка, онбординг и KYC, ручные операции "
            "бэк-офиса, персональные менеджеры и покрытие.",
            "Учёт затрат по процессам (activity-based costing)", "Квартал", "Операционный директор", "Запаздывающая",
            "Экономия от автоматизации реальна, только если высвобожденные ресурсы сокращены или поглощают рост "
            "без найма."),
    "ACQ": ("L1", "Результат", "Затраты",
            "Затраты на привлечение новых фондированных клиентов: маркетинг, агентские и реферальные вознаграждения, "
            "бонусы и акции.", "Маркетинговая аналитика, бюджет", "Месяц", "Директор по маркетингу",
            "Запаздывающая",
            "Акции «без комиссии» — недополученная выручка, а не затраты: отражать их в TAKE, а не в CAC."),
    "LOSS": ("L1", "Результат", "Риск",
             "Кредитные потери по маржинальным позициям и операционные потери: ошибки исполнения, компенсации, "
             "штрафы.", "Риск-менеджмент, бухгалтерия", "Месяц", "Директор по рискам", "Запаздывающая",
             "Редкие крупные события искажают годовую картину — смотреть скользящее среднее за 2–3 года."),
    "R1": ("L2", "Компонент дохода", "Доходы",
           "Комиссии за исполнение поручений клиентов за вычетом биржевых, клиринговых, депозитарных сборов "
           "и комиссий вышестоящих брокеров.", "Бэк-офис (сделки), биллинг", "День / месяц",
           "Директора сегментов", "Запаздывающая",
           "Сильно зависит от волатильности: нормировать на рыночный оборот (доля рынка)."),
    "R2": ("L2", "Компонент дохода", "Доходы",
           "Процентный доход по займам клиентам деньгами и ценными бумагами (включая плату за шорт) за вычетом "
           "стоимости фондирования. Кредитные потери — отдельно (C5).", "Бэк-офис, казначейство", "День / месяц",
           "Казначейство и продукт", "Запаздывающая",
           "Рост портфеля повышает риск и потребность в капитале — смотреть вместе с G_CREDIT и G_PRUD."),
    "R3": ("L2", "Компонент дохода", "Доходы",
           "Доход от размещения свободных денежных средств клиентов (в пределах, разрешённых регулятором) "
           "за вычетом процентов, выплаченных клиентам.", "Казначейство, бэк-офис", "Месяц", "Казначейство",
           "Запаздывающая",
           "Главный «рыночный» источник: при снижении ставок падает без действий брокера — планировать по "
           "сценариям ставки."),
    "R4": ("L2", "Компонент дохода", "Доходы", "Комиссии и спред по конвертациям валют клиентов.",
           "Бэк-офис, казначейство", "Месяц", "Директор по продукту", "Запаздывающая",
           "Зависит от курса и валютного регулирования."),
    "R5": ("L2", "Компонент дохода", "Доходы",
           "Комиссии за участие клиентов в размещениях (IPO/SPO, облигации), маржа по структурным продуктам "
           "и внебиржевым бумагам, комиссии за дистрибуцию фондов; для ИК — андеррайтинг и организация.",
           "Бэк-офис, CRM, инвестбанкинг", "Месяц", "Директора сегментов", "Запаздывающая",
           "Зависит от календаря размещений; продажи сложных продуктов — под ограничителем G_SUIT."),
    "R6": ("L2", "Компонент дохода", "Доходы",
           "Комиссии за доверительное управление, модельные портфели, робо-эдвайзинг и инвестиционное "
           "консультирование, включая success fee.", "Учёт ДУ, биллинг", "Месяц", "Директор по управлению активами",
           "Запаздывающая", "Success fee волатилен — планировать по базовой комиссии."),
    "R7": ("L2", "Компонент дохода", "Доходы",
           "Платные тарифы и подписки, плата за премиальное обслуживание, депозитарные и кастодиальные комиссии, "
           "прочие сервисные комиссии.", "Биллинг, депозитарий", "Месяц", "Директор по продукту", "Запаздывающая",
           "Платные подписки могут повышать отток неплатящих — отслеживать вместе с CHURN."),
    "C1": ("L2", "Компонент затрат", "Затраты", "Обработка обращений клиентов: колл-центр, чат, почта.",
           "Хелпдеск, учёт затрат", "Месяц", "Руководитель клиентского сервиса", "Запаздывающая", ""),
    "C2": ("L2", "Компонент затрат", "Затраты",
           "Проверка и оформление заявок: внешние KYC/AML-сервисы и ручная проверка.", "KYC-платформа, учёт затрат",
           "Месяц", "Руководитель онбординга", "Запаздывающая", ""),
    "C3": ("L2", "Компонент затрат", "Затраты",
           "Ручная обработка операций бэк-офиса: вводы и выводы, переводы ЦБ, корпоративные действия, сверки, "
           "заявления.", "Бэк-офис, учёт затрат", "Месяц", "Операционный директор", "Запаздывающая", ""),
    "C4": ("L2", "Компонент затрат", "Затраты",
           "Персональные менеджеры (СК) и сотрудники покрытия (ИК).", "HR, учёт затрат", "Квартал",
           "Директора сегментов", "Запаздывающая", "Полупеременные затраты: меняются ступенчато."),
    "C5": ("L2", "Компонент затрат", "Риск",
           "Непокрытые убытки по маржинальным позициям после принудительного закрытия.", "Риск-менеджмент",
           "Месяц", "Директор по рискам", "Запаздывающая", ""),
    "C6": ("L2", "Компонент затрат", "Риск", "Ошибки исполнения, компенсации клиентам, штрафы регулятора.",
           "База событий операционного риска", "Месяц", "Директор по рискам", "Запаздывающая", ""),
    "NEW": ("L3", "Драйвер (расчётный)", "Клиентская база", "Клиенты, впервые пополнившие счёт за период.",
            "CRM, бэк-офис", "Неделя", "Директор по маркетингу", "Опережающая", ""),
    "CHURNED": ("L3", "Драйвер (расчётный)", "Клиентская база",
                "Фондированные клиенты, которые вывели активы ниже порога или закрыли счёт.", "Бэк-офис, CRM",
                "Месяц", "Директор по продукту", "Запаздывающая", ""),
    "N_AVG": ("L3", "Драйвер (расчётный)", "Клиентская база",
              "Среднее за период число фондированных клиентов (активы выше порога).", "Бэк-офис", "Месяц",
              "Директора сегментов", "Запаздывающая",
              "Порог «фондированности» нужно зафиксировать; без порога база раздувается пустыми счетами."),
    "ACTIVE": ("L3", "Драйвер (расчётный)", "Клиентская база",
               "Среднемесячное число фондированных клиентов, совершивших хотя бы одну сделку.", "Бэк-офис", "Месяц",
               "Директор по продукту", "Опережающая", ""),
    "AUC": ("L3", "Драйвер (расчётный)", "Активы",
            "Средние за период активы клиентов на счетах брокера: ценные бумаги по рыночной стоимости и деньги.",
            "Бэк-офис, депозитарий", "День / месяц", "Директора сегментов", "Запаздывающая",
            "Рост может быть переоценкой — разделять на чистый приток (L4_NNA) и рыночный эффект."),
    "TURN": ("L3", "Драйвер (расчётный)", "Торговля", "Суммарный объём сделок клиентов за период.", "Бэк-офис",
             "День", "Директора сегментов", "Запаздывающая", ""),
    "MPORT": ("L3", "Драйвер (расчётный)", "Маржинальное кредитование",
              "Средняя задолженность клиентов по маржинальным займам деньгами и ценными бумагами.",
              "Бэк-офис, риск-менеджмент", "День", "Казначейство", "Запаздывающая", ""),
    "CASHBAL": ("L3", "Драйвер (расчётный)", "Активы", "Средние свободные денежные остатки клиентов.", "Бэк-офис",
                "День", "Казначейство", "Запаздывающая", ""),
    "FXVOLUME": ("L3", "Драйвер (расчётный)", "Валюта", "Объём конвертаций валют клиентов за период.", "Бэк-офис",
                 "День", "Директор по продукту", "Запаздывающая", ""),
    "PRDVOLUME": ("L3", "Драйвер (расчётный)", "Продукты",
                  "Объём покупок клиентами продуктов и размещений (ИК — объём организованных размещений).",
                  "Бэк-офис, CRM", "Месяц", "Директора сегментов", "Запаздывающая", ""),
    "AUM": ("L3", "Драйвер (расчётный)", "Управление активами",
            "Активы клиентов в ДУ, модельных портфелях и на консультировании.", "Учёт ДУ", "Месяц",
            "Директор по управлению активами", "Запаздывающая", ""),
    "SUBS": ("L3", "Драйвер (расчётный)", "Подписки", "Клиенты с платной подпиской или премиальным тарифом.",
             "Биллинг", "Месяц", "Директор по продукту", "Запаздывающая", ""),
    "ARPU": ("KPI", "Производный KPI", "Эффективность", "Чистая выручка на среднего фондированного клиента.",
             "Расчёт из модели", "Месяц", "Финансовый директор", "Запаздывающая",
             "Растёт и при «чистке» базы от пустых счетов — смотреть вместе с N_AVG."),
    "YIELD": ("KPI", "Производный KPI", "Эффективность",
              "Чистая выручка на единицу активов клиентов, б.п. в год — сопоставимая с публичными брокерами метрика.",
              "Расчёт из модели", "Квартал", "Финансовый директор", "Запаздывающая",
              "Падает при росте активов «пассивных» клиентов — это не всегда плохо."),
    "CM_MARGIN": ("KPI", "Производный KPI", "Эффективность", "Доля маржинального дохода в чистой выручке.",
                  "Расчёт из модели", "Квартал", "Финансовый директор", "Запаздывающая", ""),
    "CM_PC": ("KPI", "Производный KPI", "Эффективность", "Маржинальный доход на фондированного клиента.",
              "Расчёт из модели", "Квартал", "Финансовый директор", "Запаздывающая", ""),
    "CONTRIB_PC": ("KPI", "Производный KPI", "Юнит-экономика",
                   "Годовой вклад клиента до затрат на привлечение: (ЧВ − ЗО − ПТ) на клиента.", "Расчёт из модели",
                   "Квартал", "Финансовый директор", "Запаздывающая", ""),
    "LTV": ("KPI", "Производный KPI", "Юнит-экономика",
            "Вклад клиента за срок жизни: годовой вклад × средний срок жизни (1 ÷ годовой отток).",
            "Расчёт из модели", "Квартал", "Финансовый директор", "Запаздывающая",
            "Без дисконтирования и роста дохода клиента: для сравнения сегментов и каналов, не для оценки бизнеса."),
    "LTV_CAC": ("KPI", "Производный KPI", "Юнит-экономика", "Отношение LTV к затратам на привлечение клиента.",
                "Расчёт из модели", "Квартал", "Директор по маркетингу", "Запаздывающая",
                "Ориентир здоровой экономики — 3x и выше; считать по каналам."),
    "PAYBACK": ("KPI", "Производный KPI", "Юнит-экономика",
                "Через сколько месяцев вклад клиента окупает затраты на его привлечение.", "Расчёт из модели",
                "Квартал", "Директор по маркетингу", "Запаздывающая", ""),
    "RATE_SHARE": ("KPI", "Производный KPI", "Риск бизнес-модели",
                   "Доля чистой выручки, зависящая от процентных ставок: (R2 + R3) ÷ ЧВ.", "Расчёт из модели",
                   "Квартал", "Финансовый директор", "Запаздывающая",
                   "Высокая доля — уязвимость к снижению ставок; учитывать при выборе гипотез."),
}

# Паспорта вводных: код -> (источник, частота, владелец, опер./запазд., риски)
P_INPUT = {
    "N0": ("Бэк-офис", "Месяц", "Директора сегментов", "Запаздывающая", ""),
    "LEADS": ("Продуктовая и маркетинговая аналитика, CRM", "День", "Директор по маркетингу", "Опережающая",
              "Считать заявки, а не регистрации без начала анкеты."),
    "CR_OPEN": ("KYC-платформа, продуктовая аналитика", "Неделя", "Продакт онбординга", "Опережающая", ""),
    "CR_FUND": ("Бэк-офис, продуктовая аналитика", "Неделя", "Продакт онбординга", "Опережающая",
                "Считать по когорте открытых счетов с окном (например, 30 дней), а не по календарному месяцу."),
    "CHURN": ("Бэк-офис, CRM", "Месяц", "Директора сегментов", "Запаздывающая",
              "Определять по активам (вывод ниже порога), а не только по закрытию счёта: клиенты чаще «засыпают»."),
    "ACT": ("Бэк-офис (сделки)", "Месяц", "Директор по продукту", "Опережающая", ""),
    "TPA": ("Бэк-офис", "Месяц", "Директор по продукту", "Опережающая",
            "Сравнивать с рыночной активностью. Не путать с TPA = Total Platform Assets в отчётности Robinhood. "
            "Сделок на фондированного клиента в год = ACT × TPA × 12."),
    "TICKET": ("Бэк-офис", "Месяц", "Директор по продукту", "Запаздывающая", ""),
    "TAKE": ("Биллинг, бэк-офис", "Месяц", "Директор по продукту", "Запаздывающая",
             "Ценовой рычаг: рост ставки снижает оборот и повышает отток — оценивать с эластичностью."),
    "EXEC": ("Бэк-офис, договоры с биржами и брокерами", "Месяц", "Операционный директор", "Запаздывающая", ""),
    "AUC_PC": ("Бэк-офис, депозитарий", "Месяц", "Директора сегментов", "Запаздывающая",
               "Разделять чистый приток и переоценку."),
    "CASH": ("Бэк-офис", "Месяц", "Казначейство", "Запаздывающая", ""),
    "FLOAT_Y": ("Казначейство", "Месяц", "Казначейство", "Запаздывающая", "Внешний фактор."),
    "FLOAT_P": ("Тарифы", "Месяц", "Директор по продукту", "Запаздывающая", "Ценовой рычаг."),
    "MRG_PEN": ("Бэк-офис, риск-менеджмент", "Месяц", "Директор по продукту", "Опережающая", ""),
    "MRG_DEBT": ("Бэк-офис", "Месяц", "Директор по продукту", "Запаздывающая", ""),
    "MRG_RATE": ("Тарифы", "Месяц", "Директор по продукту", "Запаздывающая", "Ценовой рычаг."),
    "FUND_RATE": ("Казначейство", "Месяц", "Казначейство", "Запаздывающая", "Внешний фактор."),
    "CL": ("Риск-менеджмент", "Месяц", "Директор по рискам", "Запаздывающая", ""),
    "FX_PEN": ("Бэк-офис", "Месяц", "Директор по продукту", "Опережающая", ""),
    "FX_VOL": ("Бэк-офис", "Месяц", "Директор по продукту", "Запаздывающая", ""),
    "FX_SPREAD": ("Тарифы, казначейство", "Месяц", "Директор по продукту", "Запаздывающая", "Ценовой рычаг."),
    "PRD_PEN": ("Бэк-офис, CRM", "Месяц", "Директора сегментов", "Опережающая", ""),
    "PRD_VOL": ("Бэк-офис, CRM", "Месяц", "Директора сегментов", "Запаздывающая", ""),
    "PRD_FEE": ("Бэк-офис", "Месяц", "Директора сегментов", "Запаздывающая", "Ценовой рычаг; под G_SUIT."),
    "AM_SHARE": ("Учёт ДУ", "Месяц", "Директор по управлению активами", "Опережающая", ""),
    "AM_FEE": ("Тарифы ДУ", "Квартал", "Директор по управлению активами", "Запаздывающая", "Ценовой рычаг."),
    "SUB_PEN": ("Биллинг", "Месяц", "Директор по продукту", "Опережающая", ""),
    "SUB_PRICE": ("Тарифы", "Квартал", "Директор по продукту", "Запаздывающая", "Ценовой рычаг."),
    "CUST_FEE": ("Тарифы, депозитарий", "Квартал", "Директор по продукту", "Запаздывающая", "Ценовой рычаг."),
    "SUP_RATE": ("Хелпдеск", "Неделя", "Руководитель клиентского сервиса", "Опережающая", ""),
    "SUP_COST": ("Хелпдеск, учёт затрат", "Квартал", "Руководитель клиентского сервиса", "Запаздывающая", ""),
    "KYC_UNIT": ("KYC-платформа, договоры с провайдерами", "Квартал", "Руководитель онбординга", "Запаздывающая",
                 ""),
    "KYC_MAN": ("KYC-платформа", "Неделя", "Руководитель онбординга", "Опережающая", ""),
    "KYC_MAN_COST": ("Учёт затрат", "Квартал", "Руководитель онбординга", "Запаздывающая", ""),
    "OPS_PC": ("Бэк-офис", "Месяц", "Операционный директор", "Запаздывающая", ""),
    "OPS_MAN": ("Бэк-офис", "Неделя", "Операционный директор", "Опережающая", ""),
    "OPS_COST": ("Учёт затрат", "Квартал", "Операционный директор", "Запаздывающая", ""),
    "RM_LOAD": ("CRM, HR", "Квартал", "Директора сегментов", "Запаздывающая", ""),
    "RM_COST": ("HR, учёт затрат", "Год", "Директора сегментов", "Запаздывающая", ""),
    "CAC": ("Маркетинговая аналитика (атрибуция)", "Месяц", "Директор по маркетингу", "Запаздывающая",
            "Считать на фондированного, а не зарегистрированного клиента; включать бонусы и реферальные выплаты."),
    "OPLOSS": ("База событий операционного риска", "Месяц", "Директор по рискам", "Запаздывающая", ""),
}

# Опережающие индикаторы, ограничители, внешние факторы:
# (код, метрика, уровень, тип, группа, определение, формула, ед., сегменты, направление, управляемость,
#  опер./запазд., влияет на, источник, частота, владелец, риски)
EXTRA = [
    # --- опережающие индикаторы
    ("L4_REG", "Конверсия визит/установка → заявка", "Привлечение",
     "Доля посетителей и установивших приложение, начавших заявку", "Заявки ÷ установки (визиты)", "%",
     "МР, СК", "↑", "LEADS", "Продуктовая и маркетинговая аналитика", "День", "Директор по маркетингу"),
    ("L4_CPL", "Стоимость заявки по каналам", "Привлечение", "Затраты канала на одну заявку",
     "Затраты канала ÷ заявки из канала", "у.е.", "МР, СК", "↓", "CAC", "Маркетинговая аналитика", "Неделя",
     "Директор по маркетингу"),
    ("L4_REF", "Доля привлечения по рекомендациям", "Привлечение",
     "Доля новых фондированных клиентов, пришедших по реферальной программе",
     "Новые фондированные по рефералам ÷ все новые фондированные", "%", "МР, СК", "↑", "CAC, LEADS",
     "Маркетинговая аналитика", "Месяц", "Директор по маркетингу"),
    ("L4_KYC_PASS", "Доля успешно прошедших KYC", "Онбординг", "Доля начатых заявок, прошедших проверку",
     "Одобренные ÷ начатые заявки", "%", "Все", "↑", "CR_OPEN", "KYC-платформа", "День", "Продакт онбординга"),
    ("L4_KYC_TIME", "Время прохождения KYC (медиана)", "Онбординг", "Время от начала заявки до открытия счёта",
     "Медиана (открытие − начало заявки)", "мин / ч", "Все", "↓", "CR_OPEN", "KYC-платформа", "День",
     "Продакт онбординга"),
    ("L4_KYC_AUTO", "Доля автоматического одобрения заявок", "Онбординг",
     "Доля заявок, одобренных без участия сотрудника", "Автоодобренные ÷ все одобренные", "%", "Все", "↑",
     "KYC_MAN, CR_OPEN", "KYC-платформа", "Неделя", "Продакт онбординга"),
    ("L4_TTF", "Время до первого пополнения", "Онбординг", "Сколько дней проходит от открытия счёта до пополнения",
     "Медиана (первое пополнение − открытие)", "дни", "МР, СК", "↓", "CR_FUND", "Бэк-офис", "Неделя",
     "Продакт онбординга"),
    ("L4_FUND30", "Доля счетов, пополненных за 30 дней", "Онбординг",
     "Доля открытых счетов, пополненных в течение 30 дней", "Пополненные за 30 дней ÷ открытые (когорта)", "%",
     "МР, СК", "↑", "CR_FUND", "Бэк-офис", "Неделя", "Продакт онбординга"),
    ("L4_FIRSTDEP", "Средний первый депозит", "Онбординг", "Средняя сумма первого пополнения",
     "Сумма первых пополнений ÷ их число", "у.е.", "МР, СК", "↑", "AUC_PC", "Бэк-офис", "Неделя",
     "Продакт онбординга"),
    ("L4_PIPE", "Воронка продаж ИК: объём, win rate, цикл сделки", "Привлечение",
     "Число и потенциальный доход клиентов в воронке, доля выигранных, медианный цикл сделки",
     "CRM-воронка", "шт. / % / дни", "ИК", "↑", "LEADS, CR_OPEN", "CRM", "Неделя",
     "Директор по институциональному бизнесу"),
    ("L4_UPGRADE", "Переход клиентов из массового сегмента в состоятельный", "Привлечение",
     "Доля клиентов МР с активами выше порога СК, перешедших на персональное обслуживание",
     "Перешедшие ÷ клиенты МР выше порога", "%", "МР → СК", "↑", "LEADS (СК)", "CRM", "Месяц",
     "Директор состоятельного сегмента"),
    ("L4_ACT30", "Активация: первая сделка за 30 дней", "Активация",
     "Доля новых фондированных клиентов, совершивших первую сделку в течение 30 дней",
     "С первой сделкой за 30 дней ÷ новые фондированные (когорта)", "%", "МР, СК", "↑", "ACT, CHURN",
     "Бэк-офис, продуктовая аналитика", "Неделя", "Директор по продукту"),
    ("L4_MAU", "Доля фондированных, заходивших за месяц", "Вовлечённость",
     "Доля фондированных клиентов, открывавших приложение или терминал за месяц", "MAU ÷ фондированные", "%",
     "МР, СК", "↑", "ACT, TPA, CHURN", "Продуктовая аналитика", "Месяц", "Директор по продукту"),
    ("L4_AUTOINV", "Регулярные пополнения и автоинвестирование", "Вовлечённость",
     "Доля клиентов с регулярными пополнениями или активным планом автоинвестирования",
     "Клиенты с ≥3 пополнениями за 3 мес. или планом ÷ фондированные", "%", "МР, СК", "↑", "AUC_PC, CHURN",
     "Бэк-офис", "Месяц", "Директор по продукту"),
    ("L4_XSELL", "Продуктов на клиента", "Вовлечённость",
     "Среднее число используемых продуктов: торговля, маржа, валюта, подписка, ДУ, продукты",
     "Σ используемых продуктов ÷ фондированные", "шт.", "Все", "↑", "CHURN, проникновения", "CRM, бэк-офис",
     "Месяц", "Директор по продукту"),
    ("L4_FEATURE", "Использование ключевых функций", "Вовлечённость",
     "Доля активных клиентов, использующих аналитику, скринеры, алерты", "Пользователи функции ÷ активные", "%",
     "МР, СК", "↑", "TPA", "Продуктовая аналитика", "Месяц", "Директор по продукту"),
    ("L4_COMMS", "Конверсия коммуникаций в целевое действие", "Вовлечённость",
     "Доля доставленных коммуникаций, после которых клиент совершил целевое действие",
     "Целевые действия ÷ доставленные коммуникации", "%", "Все", "↑", "TPA, PRD_PEN, AUC_PC", "CRM-маркетинг",
     "Неделя", "Директор по маркетингу"),
    ("L4_COHORT", "Когортное удержание M1 / M3 / M6 / M12", "Удержание",
     "Доля когорты новых фондированных, остающихся фондированными (и активными) через N месяцев",
     "Фондированные в месяце N ÷ размер когорты", "%", "Все", "↑", "CHURN", "Бэк-офис, продуктовая аналитика",
     "Месяц", "Директор по продукту"),
    ("L4_DORMANT", "Доля «спящих» счетов", "Удержание",
     "Доля фондированных счетов без операций и входов 6+ месяцев", "Спящие ÷ фондированные", "%", "Все", "↓",
     "ACT, CHURN", "Бэк-офис, продуктовая аналитика", "Месяц", "Директор по продукту"),
    ("L4_OUTFLOW", "Отток активов", "Удержание", "Выводы и исходящие переводы ЦБ к средним активам",
     "(Выводы + исходящие переводы ЦБ) ÷ средние активы, % в год", "%", "Все", "↓", "AUC_PC, CHURN", "Бэк-офис",
     "Месяц", "Директора сегментов"),
    ("L4_NNA", "Чистый приток активов (NNA)", "Удержание",
     "Чистый приток денег и бумаг без учёта переоценки к активам на начало периода",
     "(Вводы + входящие переводы − выводы − исходящие) ÷ активы на начало", "%", "Все", "↑", "AUC_PC", "Бэк-офис",
     "Месяц", "Директора сегментов"),
    ("L4_NPS", "NPS / CSAT", "Удержание", "Готовность рекомендовать; удовлетворённость после обращений",
     "Опросы", "индекс", "Все", "↑", "CHURN, LEADS", "Опросы клиентов", "Квартал", "Директор по клиентскому опыту"),
    ("L4_TARIFF", "Эффективная комиссия и микс тарифов", "Монетизация",
     "Фактическая комиссия на единицу оборота; распределение клиентов по тарифам", "Комиссии ÷ оборот × 10 000",
     "б.п.", "Все", "↑", "TAKE", "Биллинг, бэк-офис", "Месяц", "Директор по продукту"),
    ("L4_MRG_ELIG", "Доступ к маржинальной торговле", "Монетизация",
     "Доля клиентов с подключённой маржинальной торговлей (прошли тестирование / квалификацию)",
     "Клиенты с доступом ÷ фондированные", "%", "Все", "↑", "MRG_PEN", "Бэк-офис", "Месяц", "Директор по продукту"),
    ("L4_PRD_CONV", "Конверсия предложений продуктов в покупку", "Монетизация",
     "Доля показов предложения, завершившихся покупкой", "Покупки ÷ показы", "%", "Все", "↑", "PRD_PEN",
     "Продуктовая аналитика, CRM", "Неделя", "Директора сегментов"),
    ("L4_SUB_CONV", "Конверсия в подписку и её продление", "Монетизация",
     "Доля активных клиентов, оформивших подписку; доля продлений", "Новые подписки ÷ активные; продления ÷ к продлению",
     "%", "МР, СК", "↑", "SUB_PEN", "Биллинг", "Месяц", "Директор по продукту"),
    ("L4_RECUR", "Доля активов с регулярной комиссией", "Монетизация",
     "Доля активов клиентов СК в ДУ, консультировании и фондах", "Активы с регулярной комиссией ÷ активы", "%",
     "СК", "↑", "AM_SHARE", "Учёт ДУ, бэк-офис", "Месяц", "Директор состоятельного сегмента"),
    ("L4_SOW", "Доля кошелька клиента", "Монетизация",
     "Доля оборота институционального клиента, проходящая через брокера", "Оборот через брокера ÷ оборот клиента",
     "%", "ИК", "↑", "TPA, TICKET", "CRM, данные биржи", "Квартал", "Директор по институциональному бизнесу"),
    ("L4_CONTACTS", "Обращений на 1 000 активных клиентов", "Обслуживание", "Нагрузка на поддержку",
     "Обращения ÷ активные × 1 000", "шт.", "Все", "↓", "SUP_RATE", "Хелпдеск", "Неделя",
     "Руководитель клиентского сервиса"),
    ("L4_SELFSERV", "Доля решений через самообслуживание", "Обслуживание",
     "Доля вопросов, решённых без оператора (бот, справка)", "Решённые без оператора ÷ все вопросы", "%", "Все",
     "↑", "SUP_COST, SUP_RATE", "Хелпдеск, чат-бот", "Неделя", "Руководитель клиентского сервиса"),
    ("L4_FCR", "Решение с первого обращения (FCR)", "Обслуживание",
     "Доля обращений, закрытых без повторного контакта", "Закрытые с первого раза ÷ все", "%", "Все", "↑",
     "SUP_RATE", "Хелпдеск", "Неделя", "Руководитель клиентского сервиса"),
    ("L4_STP", "Сквозная обработка операций (STP)", "Операции",
     "Доля операций бэк-офиса, обработанных без ручного вмешательства", "Операции без ручного шага ÷ все", "%",
     "Все", "↑", "OPS_MAN", "Бэк-офис", "Неделя", "Операционный директор"),
    ("L4_WD_TIME", "Время исполнения вывода средств", "Операции",
     "Сколько часов проходит от заявки на вывод до зачисления", "Медиана (зачисление − заявка)", "ч", "Все", "↓",
     "CHURN, SUP_RATE", "Бэк-офис", "Неделя", "Операционный директор"),
    ("L4_RM_PROD", "Доход и чистый приток на менеджера", "Обслуживание",
     "Чистая выручка и NNA клиентов, закреплённых за менеджером", "Σ по клиентам менеджера", "у.е.", "СК, ИК", "↑",
     "RM_LOAD, AUC_PC", "CRM", "Квартал", "Директора сегментов"),
]
for e in EXTRA:
    assert len(e) == 12, e[0]

GUARDRAILS = [
    ("G_UPTIME", "Доступность торговой системы в торговую сессию", "Доля времени торговой сессии без отказа "
     "ключевых сервисов (вход, поручения, котировки)", "Время доступности ÷ время сессии", "%", "↑",
     "OPLOSS, CHURN", "Мониторинг ИТ", "День", "Технический директор"),
    ("G_EXEC", "Качество исполнения поручений", "Время исполнения и доля отклонённых поручений",
     "Медиана задержки; отклонённые ÷ все поручения", "мс / %", "↓", "TPA, CHURN", "Торговая система", "День",
     "Руководитель торговых операций"),
    ("G_INC", "Инциденты P1 / P2", "Число критичных и высоких инцидентов", "Счёт инцидентов", "шт.", "↓",
     "OPLOSS, CHURN", "ITSM", "Неделя", "Технический директор"),
    ("G_CREDIT", "Кредитный риск маржинального портфеля",
     "Кредитные потери к портфелю, доля клиентов под маржин-коллом, принудительные закрытия",
     "Потери ÷ портфель; клиенты под маржин-коллом ÷ маржинальные", "%", "↓", "CL, MRG_PEN", "Риск-менеджмент",
     "День", "Директор по рискам"),
    ("G_PRUD", "Запас по пруденциальным нормативам", "Запас до лимитов по достаточности капитала и ликвидности",
     "(Норматив − лимит) ÷ лимит", "%", "↑", "MPORT, рост бизнеса", "Риск-менеджмент, финансы", "День",
     "Директор по рискам"),
    ("G_COMPL", "Жалобы клиентов", "Жалобы на 10 000 активных клиентов, в том числе направленные регулятору",
     "Жалобы ÷ активные × 10 000", "шт.", "↓", "CHURN, OPLOSS", "Хелпдеск, комплаенс", "Месяц",
     "Директор по клиентскому опыту"),
    ("G_SUIT", "Соответствие продаж профилю клиента",
     "Доля продаж сложных продуктов без тестирования или с нарушением инвестиционного профиля; возвраты и жалобы",
     "Продажи с нарушением ÷ все продажи сложных продуктов", "%", "↓", "PRD_PEN, AM_SHARE", "Комплаенс", "Месяц",
     "Комплаенс"),
    ("G_AML", "ПОД/ФТ и KYC", "Просроченные обновления анкет, нарушения требований ПОД/ФТ",
     "Просроченные ÷ все анкеты; число нарушений", "% / шт.", "↓", "KYC_MAN, CR_OPEN", "Комплаенс", "Месяц",
     "Комплаенс"),
    ("G_CONC", "Концентрация доходов", "Доля крупнейшего контрагента (маркет-мейкера, вышестоящего брокера, "
     "клиента) и крупнейшей продуктовой линии в чистой выручке. Пример риска: у Freedom 71% комиссий — от одного "
     "маркет-мейкера (FY2026)", "Доход от крупнейшего контрагента ÷ ЧВ; то же по продуктовой линии", "%", "↓",
     "R1, R5, все источники", "Финансы, бэк-офис", "Квартал", "Финансовый директор"),
    ("G_PRICE", "Реакция на изменение тарифов", "Отток клиентов и активов в когорте, затронутой изменением тарифа",
     "Отток в затронутой когорте − отток в контрольной", "п.п.", "↓", "TAKE, MRG_RATE, FX_SPREAD, SUB_PRICE",
     "Бэк-офис, CRM", "Неделя после изменения", "Директор по продукту"),
]

EXTERNAL = [
    ("X_RATE", "Ключевая ставка и ставки денежного рынка", "Ставки, определяющие доходность размещения и фондирования",
     "%", "FLOAT_Y, FUND_RATE, MRG_RATE, CASH", "Центральный банк, рынок", "День", "Казначейство"),
    ("X_VOL", "Волатильность рынка", "Индекс волатильности основного рынка", "индекс", "TPA, TICKET, MRG_PEN",
     "Биржа", "День", "Аналитика"),
    ("X_MKT", "Динамика фондового индекса", "Изменение основного фондового индекса за период", "%",
     "AUC_PC (переоценка), LEADS", "Биржа", "День", "Аналитика"),
    ("X_FX", "Курс национальной валюты и валютное регулирование", "Курс и ограничения на конвертацию", "курс",
     "FX_VOL, FX_PEN", "Центральный банк", "День", "Казначейство"),
    ("X_IPO", "Календарь размещений на рынке", "Число и объём IPO, SPO и выпусков облигаций", "шт. / у.е.",
     "PRD_PEN, PRD_VOL", "Биржа, ДКМ", "Месяц", "Инвестбанкинг"),
    ("X_REG", "Регуляторные изменения", "Лимиты плеча, доступ к иностранным бумагам, налоговые льготы, правила "
     "размещения клиентских средств", "—", "Многие драйверы", "Регулятор", "По событию", "Комплаенс"),
    ("X_COMP", "Тарифы и предложения конкурентов", "Мониторинг тарифов и акций конкурентов", "—",
     "TAKE, CHURN, CAC", "Мониторинг рынка", "Месяц", "Директор по продукту"),
    ("X_SHARE", "Доля рынка брокера", "Доля в рыночном обороте, активных клиентах и активах — нормирует "
     "результаты на рынок и отделяет эффект брокера от эффекта рынка", "%", "Оценка всех гипотез",
     "Биржа, регулятор, отчёты рынка", "Месяц", "Аналитика"),
]


def build_passports(wb):
    ws = wb.create_sheet("Паспорта")
    title(ws, "Паспорта метрик",
          "Уровни: L0 — результат, L1 — составляющие МД, L2 — источники дохода и статьи затрат, "
          "L3 — драйверы модели, L4 — опережающие индикаторы, которые гипотезы двигают напрямую.")
    header_row(ws, 4, PASSPORT_COLS, height=36)
    r = 5

    def put(values, bold_first=True):
        nonlocal r
        for col, v in enumerate(values, start=1):
            c = ws.cell(row=r, column=col, value=v)
            c.font = font(bold=(col <= 2 and bold_first))
            c.alignment = WRAP
        r += 1

    parent = {"NR": "CM", "CTS": "CM", "ACQ": "CM", "LOSS": "CM",
              **{f"R{k}": "NR" for k in range(1, 8)}, **{f"C{k}": "CTS" for k in range(1, 5)},
              "C5": "LOSS", "C6": "LOSS", "NEW": "N_AVG, ACQ", "CHURNED": "N_AVG, LTV", "N_AVG": "Все ветки",
              "ACTIVE": "TURN", "AUC": "CASHBAL, AUM, R7", "TURN": "R1", "MPORT": "R2, C5", "CASHBAL": "R3",
              "FXVOLUME": "R4", "PRDVOLUME": "R5", "AUM": "R6", "SUBS": "R7"}

    def model_rows(codes):
        for code in codes:
            name, unit, ftext = meta(code)
            lvl, typ, grp, definition, src, freq, owner, ll, risk = P[code]
            put([code, name, lvl, typ, grp, definition, ftext, unit, "Все", "↑" if code not in
                 ("CTS", "ACQ", "LOSS", "C1", "C2", "C3", "C4", "C5", "C6", "CHURNED", "PAYBACK") else "↓",
                 "Частично", ll, parent.get(code, "Мониторинг"), src, freq, owner, risk])

    section_row(ws, r, "Результат и составляющие (L0–L2)", len(PASSPORT_COLS)); r += 1
    model_rows(["CM", "NR", "CTS", "ACQ", "LOSS", "R1", "R2", "R3", "R4", "R5", "R6", "R7",
                "C1", "C2", "C3", "C4", "C5", "C6"])
    section_row(ws, r, "Драйверы модели: расчётные (L3)", len(PASSPORT_COLS)); r += 1
    model_rows(["N_AVG", "NEW", "CHURNED", "ACTIVE", "AUC", "TURN", "MPORT", "CASHBAL", "FXVOLUME", "PRDVOLUME",
                "AUM", "SUBS"])
    section_row(ws, r, "Драйверы модели: вводные (L3) — на них ссылаются гипотезы", len(PASSPORT_COLS)); r += 1
    for _, items in INPUT_SECTIONS:
        for i in items:
            src, freq, owner, ll, risk = P_INPUT[i.code]
            put([i.code, i.name, "L3", "Драйвер (вводная)", i.lever, i.comment or i.name, "Вводная", i.unit, "Все",
                 "↑" if i.direction > 0 else "↓", i.control, ll, i.affects, src, freq, owner, risk])
    section_row(ws, r, "Опережающие индикаторы (L4) — то, что гипотезы двигают напрямую", len(PASSPORT_COLS)); r += 1
    for code, name, grp, definition, formula, unit, segs, d, link, src, freq, owner in EXTRA:
        put([code, name, "L4", "Опережающий индикатор", grp, definition, formula, unit, segs, d, "Управляемый",
             "Опережающая", link, src, freq, owner, ""])
    section_row(ws, r, "Ограничители — не должны ухудшаться при реализации гипотез", len(PASSPORT_COLS)); r += 1
    for code, name, definition, formula, unit, d, link, src, freq, owner in GUARDRAILS:
        put([code, name, "G", "Ограничитель", "Риск и качество", definition, formula, unit, "Все", d, "Управляемый",
             "Опережающая", link, src, freq, owner, "Гипотеза принимается, только если ограничители в норме."])
    section_row(ws, r, "Внешние факторы — для сценариев и нормирования, гипотезы на них не претендуют",
                len(PASSPORT_COLS)); r += 1
    for code, name, definition, unit, link, src, freq, owner in EXTERNAL:
        put([code, name, "X", "Внешний фактор", "Рынок", definition, "—", unit, "Все", "—", "Внешний",
             "—", link, src, freq, owner, ""])
    section_row(ws, r, "Производные KPI", len(PASSPORT_COLS)); r += 1
    model_rows(["ARPU", "YIELD", "CM_MARGIN", "CM_PC", "CONTRIB_PC", "LTV", "LTV_CAC", "PAYBACK", "RATE_SHARE"])
    widths(ws, {"A": 13, "B": 34, "C": 7, "D": 18, "E": 16, "F": 48, "G": 32, "H": 9, "I": 10, "J": 10, "K": 13,
                "L": 13, "M": 22, "N": 26, "O": 11, "P": 24, "Q": 40})
    ws.freeze_panes = "C5"
    ws.auto_filter.ref = f"A4:Q{r - 1}"


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--out", type=Path, default=DEFAULT_OUT)
    ap.add_argument("--force", action="store_true", help="перезаписать существующий файл")
    args = ap.parse_args()
    if args.out.exists() and not args.force:
        sys.exit(f"{args.out} уже существует — в нём могут быть ваши данные. Используйте --force.")

    wb = Workbook()
    build_legend(wb)
    _, in_first, in_last = build_inputs(wb)
    _, row_of, first_scen_col, last_col, model_last_row = build_model(wb, in_first, in_last)
    _, sens_first, sens_last, keys, F, L = build_sensitivity(wb, row_of, in_first, in_last, first_scen_col,
                                                             last_col)
    build_tree(wb, model_last_row)
    build_summary(wb, row_of, model_last_row, sens_first, sens_last, keys, F, L)
    build_passports(wb)
    for idx, name in enumerate(["Легенда", "Сводка", "Дерево", "Вводные", "Чувствительность", "Модель", "Паспорта"]):
        wb.move_sheet(name, offset=idx - wb.sheetnames.index(name))
    for ws in wb.worksheets:
        ws.page_setup.orientation = "landscape"
        ws.page_setup.fitToWidth = 1
        ws.page_setup.fitToHeight = 0
        ws.sheet_properties.pageSetUpPr.fitToPage = True
    wb.save(args.out)
    print(f"Сохранено: {args.out}")


if __name__ == "__main__":
    main()
