# main.py
import tkinter as tk
from DAL import Database, FieldsRepository, TasksRepository
from GUI.fields_gui import FieldsGUI
from GUI.tasks_gui import TasksGUI

def show_frame(frame):
    frame.tkraise()  # Lyfter fram vald modul

def main():
    # Initiera databasen och repositories
    db = Database("farm_management.db")
    fields_repo = FieldsRepository(db)
    tasks_repo = TasksRepository(db)

    # Skapa huvudfönster
    root = tk.Tk()
    root.title("Gårdsdatabas - Administrationsverktyg")

    # Skapa huvudlayout med sidomeny och huvudområde
    sidebar = tk.Frame(root, width=200, bg="#333", padx=5, pady=5)
    sidebar.pack(side="left", fill="y")

    main_area = tk.Frame(root)
    main_area.pack(side="right", expand=True, fill="both")

    # Skapa och lägg till GUI-ramar för varje modul
    fields_frame = tk.Frame(main_area)
    FieldsGUI(fields_frame, fields_repo)
    fields_frame.grid(row=0, column=0, sticky="nsew")

    tasks_frame = tk.Frame(main_area)
    TasksGUI(tasks_frame, tasks_repo)
    tasks_frame.grid(row=0, column=0, sticky="nsew")

    # Knapp för att växla mellan moduler
    tk.Button(sidebar, text="Fält", command=lambda: show_frame(fields_frame)).pack(fill="x")
    tk.Button(sidebar, text="Arbetsuppgifter", command=lambda: show_frame(tasks_frame)).pack(fill="x")

    # Starta med att visa Fields Frame
    show_frame(fields_frame)

    # Kör huvudloopen för GUI:t
    root.mainloop()

if __name__ == "__main__":
    main()