# GUI/fields_gui.py
import tkinter as tk
from tkinter import messagebox
from DAL import FieldsRepository

class FieldsGUI:
    def __init__(self, root, fields_repo: FieldsRepository):
        self.fields_repo = fields_repo

        # Huvudram för Fältsektionen
        self.frame = tk.Frame(root)
        self.frame.pack(fill="both", expand=True)

        tk.Label(self.frame, text="Fältnamn").grid(row=0, column=0)
        self.field_name_entry = tk.Entry(self.frame)
        self.field_name_entry.grid(row=0, column=1)

        tk.Label(self.frame, text="Area (ha)").grid(row=1, column=0)
        self.area_entry = tk.Entry(self.frame)
        self.area_entry.grid(row=1, column=1)

        tk.Label(self.frame, text="Plats").grid(row=2, column=0)
        self.location_entry = tk.Entry(self.frame)
        self.location_entry.grid(row=2, column=1)

        tk.Button(self.frame, text="Skapa Fält", command=self.create_field).grid(row=3, column=0, columnspan=2)

        self.fields_listbox = tk.Listbox(self.frame, width=50, height=10)
        self.fields_listbox.grid(row=4, column=0, columnspan=2)
        self.load_fields()

    def create_field(self):
        field_name = self.field_name_entry.get()
        area = self.area_entry.get()
        location = self.location_entry.get()
        if not field_name or not area or not location:
            messagebox.showwarning("Input Error", "Alla fält måste fyllas i!")
            return
        self.fields_repo.create_field(field_name, float(area), "POLYGON((...))", location)
        messagebox.showinfo("Success", f"Fält '{field_name}' skapades!")
        self.load_fields()

    def load_fields(self):
        self.fields_listbox.delete(0, tk.END)
        fields = self.fields_repo.get_all_fields()
        for field in fields:
            self.fields_listbox.insert(tk.END, f"{field[0]} - {field[1]} ({field[2]} ha)")