# DimLocation

## Description

Stores geographical information for every building location. This table supports regional analysis, benchmarking, mapping, and climate-based comparisons.

---

## Primary Key

LocationID

---

## Columns

| Column | Data Type | Description |
|---------|-----------|-------------|
| LocationID | INT | Unique location identifier |
| City | VARCHAR(100) | City name |
| State | VARCHAR(100) | German federal state |
| PostalCode | VARCHAR(10) | Postal code |
| Country | VARCHAR(50) | Country |
| Latitude | DECIMAL(9,6) | Latitude |
| Longitude | DECIMAL(9,6) | Longitude |
| ClimateZone | VARCHAR(50) | Climate region |
| Population | INT | City population |
| Region | VARCHAR(50) | North, South, East or West Germany |
| AverageTemperature | DECIMAL(4,1) | Annual average temperature |
| AverageRainfall | DECIMAL(6,2) | Annual rainfall (mm) |
| CreatedDate | DATE | Record creation date |

---

## Business Rules

- Every building must belong to one location.
- PostalCode must be valid.
- Latitude and Longitude must be within Germany.
- Country will always be Germany.
