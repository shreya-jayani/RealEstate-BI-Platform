# DimEnergySource

## Description

Stores energy source information.

---

## Primary Key

EnergySourceID

---

## Columns

| Column | Data Type | Description |
|---------|-----------|-------------|
| EnergySourceID | INT | Unique identifier |
| EnergySource | VARCHAR(50) | Electricity, Gas, Solar |
| Renewable | BIT | Renewable source |
| CO2Factor | DECIMAL(8,4) | CO₂ emission factor |
| Unit | VARCHAR(20) | kWh |
| CreatedDate | DATE | Record creation |

---

## Business Rules

Allowed sources:

- Electricity
- Natural Gas
- District Heating
- Solar
- Wind
- Water
