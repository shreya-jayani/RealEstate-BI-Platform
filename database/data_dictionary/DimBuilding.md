# DimBuilding

## Business Rules

- Building names must be unique within a customer portfolio.
- ConstructionYear must be between 1950 and the current year.
- GrossAreaSqm must be greater than NetAreaSqm.
- EnergyRating must be one of: A+, A, B, C, D, E, F, G.
- Active buildings must have a valid LocationID and CustomerID.

## Description

Stores static information about every commercial building.

---

## Primary Key

BuildingID

---

## Columns

| Column | Data Type | Description |
|---------|-----------|-------------|
| BuildingID | INT | Unique building identifier |
| BuildingCode | VARCHAR(20) | Internal building code |
| BuildingName | VARCHAR(150) | Building name |
| CustomerID | INT | Building owner |
| BuildingTypeID | INT | Office, Hospital, etc. |
| LocationID | INT | City reference |
| ConstructionYear | SMALLINT | Year built |
| GrossAreaSqm | DECIMAL(10,2) | Gross floor area |
| NetAreaSqm | DECIMAL(10,2) | Usable area |
| Floors | INT | Number of floors |
| ParkingSpaces | INT | Parking capacity |
| OccupancyCapacity | INT | Maximum occupancy |
| EnergyRating | CHAR(2) | A+ to G |
| HVACType | VARCHAR(50) | HVAC system |
| SolarPanels | BIT | Solar installation |
| EVCharging | BIT | EV charging available |
| Latitude | DECIMAL(9,6) | GPS latitude |
| Longitude | DECIMAL(9,6) | GPS longitude |
| Status | VARCHAR(20) | Active / Inactive |
| CreatedDate | DATE | Record creation |
