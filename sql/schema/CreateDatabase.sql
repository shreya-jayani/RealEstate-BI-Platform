/*
===========================================================
Project : Real Estate Business Intelligence Platform
Author  : Shreya Jayani
Database: RealEstateBI
===========================================================
*/

IF DB_ID('RealEstateBI') IS NOT NULL
BEGIN
    ALTER DATABASE RealEstateBI SET SINGLE_USER WITH ROLLBACK IMMEDIATE;
    DROP DATABASE RealEstateBI;
END
GO

CREATE DATABASE RealEstateBI;
GO

USE RealEstateBI;
GO
