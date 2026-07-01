# DimDate

## Description

Calendar dimension used for all time-based analysis.

---

## Primary Key

DateID

---

## Columns

| Column | Data Type | Description |
|---------|-----------|-------------|
| DateID | INT | YYYYMMDD |
| FullDate | DATE | Calendar date |
| Day | INT | Day number |
| DayName | VARCHAR(20) | Monday |
| Week | INT | Week number |
| Month | INT | Month number |
| MonthName | VARCHAR(20) | January |
| Quarter | INT | Quarter |
| Year | INT | Calendar year |
| FiscalYear | INT | Fiscal year |
| IsWeekend | BIT | Weekend indicator |
| IsHoliday | BIT | Public holiday |
| Season | VARCHAR(20) | Winter, Spring, Summer, Autumn |

---

## Business Rules

- No duplicate dates.
- Continuous calendar.
- Covers 2017–2026.
