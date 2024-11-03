import sqlite3

def create_database(db_name="farm_management.db"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    # Skapa tabeller med alla relationer
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Fields (
        FieldID INTEGER PRIMARY KEY AUTOINCREMENT,
        FieldName TEXT NOT NULL,
        Area REAL,
        PolygonData TEXT,
        Location TEXT
    );
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Land (
        LandID INTEGER PRIMARY KEY AUTOINCREMENT,
        FieldID INTEGER,
        TaxValue REAL,
        SaleMultiplier REAL DEFAULT 2.1,
        CalculatedSaleValue REAL,
        InsuranceValue REAL,
        InsuranceCost REAL,
        InsuranceProvider TEXT,
        FOREIGN KEY(FieldID) REFERENCES Fields(FieldID)
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Buildings (
        BuildingID INTEGER PRIMARY KEY AUTOINCREMENT,
        BuildingType TEXT,
        PurchaseValue REAL,
        DepreciationPeriod INTEGER,
        CurrentValue REAL,
        Location TEXT,
        Capacity INTEGER,
        InsuranceValue REAL,
        InsuranceCost REAL,
        InsuranceProvider TEXT
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Machinery (
        MachineryID INTEGER PRIMARY KEY AUTOINCREMENT,
        Type TEXT,
        PurchaseValue REAL,
        DepreciationRate REAL,
        ResidualValue REAL,
        UsageHours INTEGER,
        NextMaintenance INTEGER,
        InsuranceValue REAL,
        InsuranceCost REAL,
        InsuranceProvider TEXT
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS MaintenanceRecords (
        RecordID INTEGER PRIMARY KEY AUTOINCREMENT,
        MachineryID INTEGER,
        ServiceDate TEXT,
        ServiceType TEXT,
        ServiceCost REAL,
        Notes TEXT,
        FOREIGN KEY(MachineryID) REFERENCES Machinery(MachineryID)
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Tasks (
        TaskID INTEGER PRIMARY KEY AUTOINCREMENT,
        FieldID INTEGER,
        EmployeeID INTEGER,
        MachineryID INTEGER,
        TaskType TEXT,
        StartTime TEXT,
        EndTime TEXT,
        FOREIGN KEY(FieldID) REFERENCES Fields(FieldID),
        FOREIGN KEY(EmployeeID) REFERENCES Employees(EmployeeID),
        FOREIGN KEY(MachineryID) REFERENCES Machinery(MachineryID)
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Resources (
        ResourceID INTEGER PRIMARY KEY AUTOINCREMENT,
        TaskID INTEGER,
        ResourceType TEXT,
        Quantity REAL,
        CostPerUnit REAL,
        PropertyType TEXT,
        FOREIGN KEY(TaskID) REFERENCES Tasks(TaskID)
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS EconomicMetrics (
        MetricID INTEGER PRIMARY KEY AUTOINCREMENT,
        MetricType TEXT,
        Value REAL,
        Timestamp TEXT
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Animals (
        AnimalID INTEGER PRIMARY KEY AUTOINCREMENT,
        Age INTEGER,
        Breed TEXT,
        Sex TEXT,
        Status TEXT
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS FeedingPlans (
        FeedingPlanID INTEGER PRIMARY KEY AUTOINCREMENT,
        AgeGroup TEXT,
        FeedType TEXT,
        QuantityPerDay REAL,
        CostPerUnit REAL
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS AnimalTasks (
        TaskID INTEGER PRIMARY KEY AUTOINCREMENT,
        AnimalID INTEGER,
        EmployeeID INTEGER,
        TaskType TEXT,
        StartTime TEXT,
        EndTime TEXT,
        FOREIGN KEY(AnimalID) REFERENCES Animals(AnimalID),
        FOREIGN KEY(EmployeeID) REFERENCES Employees(EmployeeID)
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Pastures (
        PastureID INTEGER PRIMARY KEY AUTOINCREMENT,
        FieldID INTEGER,
        AnimalID INTEGER,
        Season TEXT,
        FOREIGN KEY(FieldID) REFERENCES Fields(FieldID),
        FOREIGN KEY(AnimalID) REFERENCES Animals(AnimalID)
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS AnimalBuildings (
        BuildingID INTEGER PRIMARY KEY AUTOINCREMENT,
        BuildingType TEXT,
        Capacity INTEGER,
        AnimalID INTEGER,
        FOREIGN KEY(AnimalID) REFERENCES Animals(AnimalID)
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS SoilAnalysis (
        AnalysisID INTEGER PRIMARY KEY AUTOINCREMENT,
        FieldID INTEGER,
        pH REAL,
        SoilType TEXT,
        NutrientLevels TEXT,
        OrganicMatter REAL,
        FOREIGN KEY(FieldID) REFERENCES Fields(FieldID)
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Income (
        IncomeID INTEGER PRIMARY KEY AUTOINCREMENT,
        SourceType TEXT,
        SourceID INTEGER,
        Amount REAL,
        Date TEXT
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS WeatherData (
        WeatherID INTEGER PRIMARY KEY AUTOINCREMENT,
        FieldID INTEGER,
        Date TEXT,
        Rainfall REAL,
        Temperature REAL,
        FOREIGN KEY(FieldID) REFERENCES Fields(FieldID)
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS MaintenanceSchedule (
        ScheduleID INTEGER PRIMARY KEY AUTOINCREMENT,
        MachineryID INTEGER,
        ScheduledHours INTEGER,
        ServiceType TEXT,
        EstimatedCost REAL,
        FOREIGN KEY(MachineryID) REFERENCES Machinery(MachineryID)
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Employees (
        EmployeeID INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT,
        Role TEXT,
        HourlyRate REAL,
        Schedule TEXT
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS CropRotation (
        RotationID INTEGER PRIMARY KEY AUTOINCREMENT,
        FieldID INTEGER,
        Crop TEXT,
        Season TEXT,
        Yield REAL,
        FOREIGN KEY(FieldID) REFERENCES Fields(FieldID)
    );
    """)

    # Spara och stäng anslutningen
    conn.commit()
    conn.close()
    print("Databasen och tabeller har skapats.")

# Kör skriptet för att skapa databasen och tabeller
if __name__ == "__main__":
    create_database()