# FactWorkOrders

## Description

Stores work orders raised for maintenance and repairs.

---

## Primary Key

WorkOrderID

---

## Foreign Keys

BuildingID
VendorID
DateID

---

## Columns

| Column | Data Type | Description |
|---------|-----------|-------------|
| WorkOrderID | BIGINT | Primary Key |
| BuildingID | INT | Building reference |
| VendorID | INT | Vendor |
| DateID | INT | Date |
| WorkOrderType | VARCHAR(100) | Work category |
| Priority | VARCHAR(20) | Priority |
| Status | VARCHAR(30) | Open, Closed |
| EstimatedCost | DECIMAL(12,2) | Estimated cost |
| ActualCost | DECIMAL(12,2) | Actual cost |
| ResolutionTimeHours | DECIMAL(8,2) | Resolution time |

---

## Business Rules

- ActualCost cannot be negative.
- ResolutionTimeHours must be greater than zero.
