# DimBuildingType

## Description

Defines the category of each commercial building.

---

## Primary Key

BuildingTypeID

---

## Columns

| Column | Data Type | Description |
|---------|-----------|-------------|
| BuildingTypeID | INT | Unique identifier |
| BuildingType | VARCHAR(50) | Office, Hospital, Warehouse, etc. |
| Description | VARCHAR(250) | Category description |
| ExpectedOccupancy | INT | Average occupancy |
| TypicalEnergyUsage | VARCHAR(50) | Low, Medium, High |
| CreatedDate | DATE | Record creation |

---

## Business Rules

Allowed values:

- Office
- Hospital
- Retail
- Warehouse
- Hotel
- University
- Airport
- Government
- Shopping Mall
- Mixed Use
