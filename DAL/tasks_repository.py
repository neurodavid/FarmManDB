# DAL/tasks_repository.py
from .database import Database

class TasksRepository:
    def __init__(self, db: Database):
        self.db = db

    def create_task(self, field_id, employee_id, machinery_id, task_type, start_time, end_time):
        query = """
        INSERT INTO Tasks (FieldID, EmployeeID, MachineryID, TaskType, StartTime, EndTime)
        VALUES (?, ?, ?, ?, ?, ?)
        """
        self.db.execute_query(query, (field_id, employee_id, machinery_id, task_type, start_time, end_time))

    def get_task(self, task_id):
        query = "SELECT * FROM Tasks WHERE TaskID = ?"
        return self.db.fetch_one(query, (task_id,))

    def get_tasks_for_field(self, field_id):
        query = "SELECT * FROM Tasks WHERE FieldID = ?"
        return self.db.fetch_all(query, (field_id,))

    def delete_task(self, task_id):
        query = "DELETE FROM Tasks WHERE TaskID = ?"
        self.db.execute_query(query, (task_id,))