import pandas as pd

from app.config.settings import GENERATED_DIR, START_DATE, END_DATE
from app.utils.file_utils import ensure_directory

def get_season(month: int) -> str:
    if month in (12, 1, 2):
        return "Winter"
    elif month in (3, 4, 5):
        return "Spring"
    elif month in (6, 7, 8):
        return "Summer"
    return "Autumn"


def generate_date():

    dates = pd.date_range(
        start=START_DATE,
        end=END_DATE,
        freq="D"
    )

    df = pd.DataFrame({
        "DateID": dates.strftime("%Y%m%d").astype(int),
        "FullDate": dates,
        "Day": dates.day,
        "DayName": dates.day_name(),
        "Week": dates.isocalendar().week.astype(int),
        "Month": dates.month,
        "MonthName": dates.month_name(),
        "Quarter": "Q" + dates.quarter.astype(str),
        "Year": dates.year,
        "FiscalYear": dates.year,
        "IsWeekend": dates.dayofweek >= 5,
        "IsHoliday": False,
        "Season": dates.month.map(get_season)
    })

    ensure_directory(GENERATED_DIR)

    output = GENERATED_DIR / "DimDate.csv"

    df.to_csv(output, index=False)

    print(f"✓ DimDate generated ({len(df):,} rows)")
