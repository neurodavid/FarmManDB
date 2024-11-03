# main.py
from DAL import Database, FieldsRepository, TasksRepository

# Initiera databasen och repositories
db = Database("farm_management.db")
fields_repo = FieldsRepository(db)
tasks_repo = TasksRepository(db)

# Använd exempel: Skapa ett fält
fields_repo.create_field("Field B", 20.0, "POLYGON((...))", "North side")

# Använd exempel: Hämta ett fält
field = fields_repo.get_field(1)
print("Field details:", field)