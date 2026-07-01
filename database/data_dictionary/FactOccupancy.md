# FactOccupancy

## Description

Stores monthly occupancy information.

---

## Primary Key

OccupancyID

---

## Foreign Keys

BuildingID
DateID

---

## Columns

| Column | Data Type | Description |
|---------|-----------|-------------|
| OccupancyID | BIGINT | Primary Key |
| BuildingID | INT | Building reference |
| DateID | INT | Date |
| OccupiedArea | DECIMAL(12,2) | Occupied area |
| VacantArea | DECIMAL(12,2) | Vacant area |
| OccupancyRate | DECIMAL(5,2) | Occupancy percentage |
| TenantCount | INT | Active tenants |

---

## Business Rules

- OccupancyRate between 0 and 100.
