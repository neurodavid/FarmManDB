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

        # Knappar för att hantera arbetsuppgifter
        tk.Button(self.frame, text="Lägg till Fält", command=self.create_field).grid(row=3, column=0)
        tk.Button(self.frame, text="Redigera Fält", command=self.update_fields).grid(row=3, column=1)
        tk.Button(self.frame, text="Ta bort Fält", command=self.delete_fields).grid(row=3, column=2)

        #tk.Button(self.frame, text="Skapa Fält", command=self.create_field).grid(row=3, column=0, columnspan=2)

        self.fields_listbox = tk.Listbox(self.frame, width=50, height=10)
        self.fields_listbox.grid(row=4, column=0, columnspan=2)
        self.fields_listbox.bind("<<ListBoxSelect>>", self.load_fields_details)
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

    def load_fields_details(self, event):
        selection = self.fields_listbox.curselection()
        if selection:
            field_id = self.fields_listbox.get(selection[0]).split("-")[0]
            field = self.fields_repo.get_field((field_id))

            if field:
                self.field_name_entry.delete(0, tk.END)
                self.field_name_entry.insert(0, field[1])
                self.area_entry.delete(0, tk.END)
                self.area_entry.insert(0, field[2])
                self.location_entry.delete(0, tk.END)
                self.location_entry.insert(0, field[3])

            self.frame.update()
            

    def update_fields(self):
        selection = self.fields_listbox.curselection()
        if not selection:
            messagebox.showwarning("Selection Error", "Välj ett fält att redigera!")
            return

        field_id = self.fields_listbox.get(selection[0]).split("-")[0]
        field_name = self.field_name_entry.get()
        area = self.area_entry.get()
        location = self.location_entry.get()
       
        self.fields_repo.update_field(
            field_id=field_id,
            field_name=(field_name),
            area=(area),
            location=(location)
            
        )
        messagebox.showinfo("Success", "Uppgiften har uppdaterats!")
        self.load_fields()

    def delete_fields(self):
        selection = self.fields_listbox.curselection()
        if not selection:
            messagebox.showwarning("Selection Error", "Välj en uppgift att ta bort!")
            return

        field_id = self.fields_listbox.get(selection[0]).split(" - ")[0]
        self.fields_repo.delete_field(field_id)
        messagebox.showinfo("Success", "Uppgiften har tagits bort!")
        self.load_fields()
    # Fler funktioner för att redigera och ta bort uppgifter kan läggas till här