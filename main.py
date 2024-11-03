# main.py
import tkinter as tk
from DAL import Database, FieldsRepository, TasksRepository
from GUI.fields_gui import FieldsGUI

def main():
    # Initiera databasen och repositories
    db = Database("farm_management.db")
    fields_repo = FieldsRepository(db)
    tasks_repo = TasksRepository(db)

    # Initiera huvudfönstret för GUI
    root = tk.Tk()
    root.title("Gårdsdatabas - Administrationsverktyg")

    # Instansiera och visa Fields GUI
    fields_gui = FieldsGUI(root, fields_repo)

    # Kör GUI
    root.mainloop()

if __name__ == "__main__":
    main()