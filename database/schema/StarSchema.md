# Star Schema

                    DimDate
                       │
                       │
DimCustomer ─ FactOperatingCost ─ DimBuilding
                       │
                       │
                DimBuildingType
                       │
                       │
                 DimLocation

Additional Fact Tables

FactEnergy

FactMaintenance

FactInspection

FactBenchmark

FactOccupancy
