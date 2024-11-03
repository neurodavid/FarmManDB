# GUI/tasks_gui.py
import tkinter as tk
from tkinter import messagebox
from DAL import TasksRepository

class TasksGUI:
    def __init__(self, root, tasks_repo: TasksRepository):
        self.tasks_repo = tasks_repo

        # Huvudram för arbetsuppgifter
        self.frame = tk.Frame(root)
        self.frame.pack(fill="both", expand=True)

        # Inmatningsfält för arbetsuppgifter
        tk.Label(self.frame, text="Fält-ID").grid(row=0, column=0)
        self.field_id_entry = tk.Entry(self.frame)
        self.field_id_entry.grid(row=0, column=1)

        tk.Label(self.frame, text="Anställd-ID").grid(row=1, column=0)
        self.employee_id_entry = tk.Entry(self.frame)
        self.employee_id_entry.grid(row=1, column=1)

        tk.Label(self.frame, text="Maskin-ID").grid(row=2, column=0)
        self.machinery_id_entry = tk.Entry(self.frame)
        self.machinery_id_entry.grid(row=2, column=1)

        tk.Label(self.frame, text="Uppgiftstyp").grid(row=3, column=0)
        self.task_type_entry = tk.Entry(self.frame)
        self.task_type_entry.grid(row=3, column=1)

        tk.Label(self.frame, text="Starttid").grid(row=4, column=0)
        self.start_time_entry = tk.Entry(self.frame)
        self.start_time_entry.grid(row=4, column=1)

        tk.Label(self.frame, text="Sluttid").grid(row=5, column=0)
        self.end_time_entry = tk.Entry(self.frame)
        self.end_time_entry.grid(row=5, column=1)

        # Knappar för att hantera arbetsuppgifter
        tk.Button(self.frame, text="Lägg till Uppgift", command=self.create_task).grid(row=6, column=0)
        tk.Button(self.frame, text="Redigera Uppgift", command=self.update_task).grid(row=6, column=1)
        tk.Button(self.frame, text="Ta bort Uppgift", command=self.delete_task).grid(row=6, column=2)

        # Lista över arbetsuppgifter
        self.tasks_listbox = tk.Listbox(self.frame, width=80, height=10)
        self.tasks_listbox.grid(row=7, column=0, columnspan=3)
        self.tasks_listbox.bind("<<ListboxSelect>>", self.load_task_details)
        self.load_tasks()

    def create_task(self):
        field_id = self.field_id_entry.get()
        employee_id = self.employee_id_entry.get()
        machinery_id = self.machinery_id_entry.get()
        task_type = self.task_type_entry.get()
        start_time = self.start_time_entry.get()
        end_time = self.end_time_entry.get()

        if not (field_id and employee_id and machinery_id and task_type and start_time and end_time):
            messagebox.showwarning("Input Error", "Alla fält måste fyllas i!")
            return

        self.tasks_repo.create_task(
            field_id=int(field_id), 
            employee_id=int(employee_id), 
            machinery_id=int(machinery_id), 
            task_type=task_type, 
            start_time=start_time, 
            end_time=end_time
        )
        messagebox.showinfo("Success", "Uppgiften har skapats!")
        self.load_tasks()

    def load_tasks(self):
        self.tasks_listbox.delete(0, tk.END)
        tasks = self.tasks_repo.get_all_tasks()
        for task in tasks:
            self.tasks_listbox.insert(tk.END, f"{task[0]} - Field: {task[1]}, Employee: {task[2]}, Machinery: {task[3]}, Type: {task[4]}")

    def load_task_details(self, event):
        selection = self.tasks_listbox.curselection()
        if selection:
            task_id = self.tasks_listbox.get(selection[0]).split(" ")[0]
            task = self.tasks_repo.get_task(int(task_id))

            if task:
                self.field_id_entry.delete(0, tk.END)
                self.field_id_entry.insert(0, task[1])
                self.employee_id_entry.delete(0, tk.END)
                self.employee_id_entry.insert(0, task[2])
                self.machinery_id_entry.delete(0, tk.END)
                self.machinery_id_entry.insert(0, task[3])
                self.task_type_entry.delete(0, tk.END)
                self.task_type_entry.insert(0, task[4])
                self.start_time_entry.delete(0, tk.END)
                self.start_time_entry.insert(0, task[5])
                self.end_time_entry.delete(0, tk.END)
                self.end_time_entry.insert(0, task[6])

    def update_task(self):
        selection = self.tasks_listbox.curselection()
        if not selection:
            messagebox.showwarning("Selection Error", "Välj en uppgift att redigera!")
            return

        task_id = int(self.tasks_listbox.get(selection[0]).split(" ")[0])
        field_id = self.field_id_entry.get()
        employee_id = self.employee_id_entry.get()
        machinery_id = self.machinery_id_entry.get()
        task_type = self.task_type_entry.get()
        start_time = self.start_time_entry.get()
        end_time = self.end_time_entry.get()

        self.tasks_repo.update_task(
            task_id=task_id,
            field_id=int(field_id),
            employee_id=int(employee_id),
            machinery_id=int(machinery_id),
            task_type=task_type,
            start_time=start_time,
            end_time=end_time
        )
        messagebox.showinfo("Success", "Uppgiften har uppdaterats!")
        self.load_tasks()

    def delete_task(self):
        selection = self.tasks_listbox.curselection()
        if not selection:
            messagebox.showwarning("Selection Error", "Välj en uppgift att ta bort!")
            return

        task_id = int(self.tasks_listbox.get(selection[0]).split(" ")[0])
        self.tasks_repo.delete_task(task_id)
        messagebox.showinfo("Success", "Uppgiften har tagits bort!")
        self.load_tasks()
    # Fler funktioner för att redigera och ta bort uppgifter kan läggas till här