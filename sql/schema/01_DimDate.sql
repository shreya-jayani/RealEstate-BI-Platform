/*
============================================================
Table: DimDate
Description:
Stores calendar information for time-based analysis.
============================================================
*/

USE RealEstateBI;
GO

CREATE TABLE dbo.DimDate
(
    DateID              INT             NOT NULL PRIMARY KEY,
    FullDate            DATE            NOT NULL,
    DayNumber           TINYINT         NOT NULL,
    DayName             VARCHAR(20)     NOT NULL,
    DayOfWeek           TINYINT         NOT NULL,
    WeekNumber          TINYINT         NOT NULL,
    MonthNumber         TINYINT         NOT NULL,
    MonthName           VARCHAR(20)     NOT NULL,
    QuarterNumber       TINYINT         NOT NULL,
    QuarterName         VARCHAR(5)      NOT NULL,
    YearNumber          SMALLINT        NOT NULL,
    FiscalYear          SMALLINT        NOT NULL,
    FiscalQuarter       VARCHAR(5)      NOT NULL,
    IsWeekend           BIT             NOT NULL,
    IsHoliday           BIT             NOT NULL,
    Season              VARCHAR(20)     NOT NULL,
    MonthStart          BIT             NOT NULL,
    MonthEnd            BIT             NOT NULL,
    YearStart           BIT             NOT NULL,
    YearEnd             BIT             NOT NULL,
    CreatedDate         DATETIME2       DEFAULT GETDATE()
);
GO
