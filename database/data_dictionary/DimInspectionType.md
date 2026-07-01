# DimInspectionType

## Description

Stores inspection categories.

---

## Primary Key

InspectionTypeID

---

## Columns

| Column | Data Type | Description |
|---------|-----------|-------------|
| InspectionTypeID | INT | Unique identifier |
| InspectionType | VARCHAR(100) | Inspection name |
| FrequencyMonths | INT | Inspection interval |
| Regulatory | BIT | Mandatory inspection |
| Description | VARCHAR(250) | Description |
| CreatedDate | DATE | Record creation |

---

## Business Rules

Inspection types include:

- Fire Safety
- HVAC
- Electrical
- Elevator
- Roof
- Structural
- Emergency Exit
- Water Quality
