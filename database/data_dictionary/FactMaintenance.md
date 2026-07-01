# FactMaintenance

## Description

Stores all maintenance activities.

---

## Primary Key

MaintenanceID

---

## Foreign Keys

BuildingID
VendorID
DateID

---

## Columns

| Column | Data Type | Description |
|---------|-----------|-------------|
| MaintenanceID | BIGINT | Primary Key |
| BuildingID | INT | Building reference |
| VendorID | INT | Contractor |
| DateID | INT | Date |
| MaintenanceType | VARCHAR(100) | Repair category |
| Priority | VARCHAR(20) | Low, Medium, High |
| Status | VARCHAR(30) | Completed, Pending |
| DurationHours | DECIMAL(6,2) | Work duration |
| Cost | DECIMAL(12,2) | Maintenance cost |
| Preventive | BIT | Preventive maintenance |

---

## Business Rules

- Costs cannot be negative.
