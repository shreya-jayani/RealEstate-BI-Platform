# FactLeaseRevenue

## Description

Stores rental income information.

---

## Primary Key

LeaseRevenueID

---

## Foreign Keys

BuildingID
DateID

---

## Columns

| Column | Data Type | Description |
|---------|-----------|-------------|
| LeaseRevenueID | BIGINT | Primary Key |
| BuildingID | INT | Building reference |
| DateID | INT | Date |
| RentalIncome | DECIMAL(14,2) | Monthly rent |
| ParkingIncome | DECIMAL(12,2) | Parking revenue |
| ServiceCharges | DECIMAL(12,2) | Service charges |
| TotalRevenue | DECIMAL(14,2) | Total revenue |

---

## Business Rules

- TotalRevenue is the sum of all revenue components.
