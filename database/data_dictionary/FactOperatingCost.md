# FactOperatingCost

## Description

Stores monthly operating costs for each building.

---

## Primary Key

OperatingCostID

---

## Foreign Keys

BuildingID
DateID

---

## Columns

| Column | Data Type | Description |
|---------|-----------|-------------|
| OperatingCostID | BIGINT | Primary Key |
| BuildingID | INT | Building reference |
| DateID | INT | Date reference |
| ElectricityCost | DECIMAL(12,2) | Electricity expenses |
| HeatingCost | DECIMAL(12,2) | Heating expenses |
| CoolingCost | DECIMAL(12,2) | Cooling expenses |
| WaterCost | DECIMAL(12,2) | Water expenses |
| CleaningCost | DECIMAL(12,2) | Cleaning expenses |
| SecurityCost | DECIMAL(12,2) | Security expenses |
| InsuranceCost | DECIMAL(12,2) | Insurance expenses |
| WasteCost | DECIMAL(12,2) | Waste disposal |
| FacilityManagementCost | DECIMAL(12,2) | FM expenses |
| PropertyTax | DECIMAL(12,2) | Property taxes |
| TotalOperatingCost | DECIMAL(14,2) | Total monthly operating cost |

---

## Business Rules

- One record per Building per Month.
- TotalOperatingCost equals the sum of all cost components.
