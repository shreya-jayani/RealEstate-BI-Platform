# FactBenchmark

## Description

Stores benchmark values used to compare building performance.

---

## Primary Key

BenchmarkID

---

## Foreign Keys

BuildingID
DateID

---

## Columns

| Column | Data Type | Description |
|---------|-----------|-------------|
| BenchmarkID | BIGINT | Primary Key |
| BuildingID | INT | Building reference |
| DateID | INT | Date |
| IndustryAverageCost | DECIMAL(12,2) | Average cost |
| IndustryAverageEnergy | DECIMAL(12,2) | Average energy |
| BenchmarkScore | DECIMAL(6,2) | Overall score |
| CostVariance | DECIMAL(8,2) | Cost difference |
| EnergyVariance | DECIMAL(8,2) | Energy difference |
| Rank | INT | Building ranking |

---

## Business Rules

- Benchmark score between 0 and 100.
