# DimCustomer

## Description

Stores information about organizations that own or manage one or more commercial buildings.

---

## Primary Key

CustomerID

---

## Columns

| Column | Data Type | Description |
|---------|-----------|-------------|
| CustomerID | INT | Unique customer identifier |
| CustomerCode | VARCHAR(20) | Internal customer code |
| CompanyName | VARCHAR(150) | Customer name |
| Industry | VARCHAR(100) | Industry sector |
| PortfolioSize | INT | Number of managed buildings |
| HeadquartersCity | VARCHAR(100) | Headquarters city |
| HeadquartersState | VARCHAR(100) | Headquarters state |
| Country | VARCHAR(100) | Country |
| ContactPerson | VARCHAR(100) | Primary contact |
| ContactEmail | VARCHAR(150) | Business email |
| ContactPhone | VARCHAR(30) | Contact number |
| CustomerSince | DATE | Customer onboarding date |
| AnnualRevenue | DECIMAL(18,2) | Annual company revenue |
| ESGRating | CHAR(2) | ESG performance rating |
| ActiveStatus | BIT | Active customer |
| CreatedDate | DATE | Record creation date |
