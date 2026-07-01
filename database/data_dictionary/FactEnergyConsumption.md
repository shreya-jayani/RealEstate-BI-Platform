# FactEnergyConsumption

## Description

Stores monthly utility consumption.

---

## Primary Key

EnergyID

---

## Foreign Keys

BuildingID
DateID

---

## Columns

| Column | Data Type | Description |
|---------|-----------|-------------|
| EnergyID | BIGINT | Primary Key |
| BuildingID | INT | Building reference |
| DateID | INT | Date reference |
| ElectricitykWh | DECIMAL(14,2) | Electricity usage |
| GaskWh | DECIMAL(14,2) | Gas usage |
| HeatingkWh | DECIMAL(14,2) | Heating usage |
| CoolingkWh | DECIMAL(14,2) | Cooling usage |
| WaterConsumption | DECIMAL(14,2) | Water usage |
| SolarGeneration | DECIMAL(14,2) | Solar production |
| CO2Emission | DECIMAL(12,2) | CO₂ emissions |

---

## Business Rules

- One record per Building per Month.
- CO₂ values calculated using emission factors.
