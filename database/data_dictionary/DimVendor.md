# DimVendor

## Description

Stores contractor and service provider information.

---

## Primary Key

VendorID

---

## Columns

| Column | Data Type | Description |
|---------|-----------|-------------|
| VendorID | INT | Unique identifier |
| VendorName | VARCHAR(150) | Company name |
| ServiceType | VARCHAR(100) | HVAC, Cleaning, Security |
| City | VARCHAR(100) | Vendor location |
| State | VARCHAR(100) | State |
| Rating | DECIMAL(3,2) | Vendor rating |
| Active | BIT | Active vendor |
| CreatedDate | DATE | Record creation |

---

## Business Rules

Service types include:

- HVAC
- Cleaning
- Plumbing
- Electrical
- Security
- Landscaping
- Elevator
