# FactInspection

## Description

Stores building inspection records.

---

## Primary Key

InspectionID

---

## Foreign Keys

BuildingID
InspectionTypeID
DateID

---

## Columns

| Column | Data Type | Description |
|---------|-----------|-------------|
| InspectionID | BIGINT | Primary Key |
| BuildingID | INT | Building reference |
| InspectionTypeID | INT | Inspection type |
| DateID | INT | Inspection date |
| ComplianceScore | DECIMAL(5,2) | Score |
| IssuesFound | INT | Number of issues |
| Passed | BIT | Pass/Fail |
| InspectorName | VARCHAR(100) | Inspector |
| DurationHours | DECIMAL(6,2) | Inspection duration |

---

## Business Rules

- Compliance score between 0 and 100.
