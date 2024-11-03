# DAL/fields_repository.py
from .database import Database

class FieldsRepository:
    def __init__(self, db: Database):
        self.db = db

    def create_field(self, field_name, area, polygon_data, location):
        query = """
        INSERT INTO Fields (FieldName, Area, PolygonData, Location)
        VALUES (?, ?, ?, ?)
        """
        self.db.execute_query(query, (field_name, area, polygon_data, location))

    def get_field(self, field_id):
        query = "SELECT * FROM Fields WHERE FieldID = ?"
        return self.db.fetch_one(query, (field_id,))

    def update_field(self, field_id, field_name=None, area=None, polygon_data=None, location=None):
        updates = []
        params = []
        
        if field_name:
            updates.append("FieldName = ?")
            params.append(field_name)
        if area:
            updates.append("Area = ?")
            params.append(area)
        if polygon_data:
            updates.append("PolygonData = ?")
            params.append(polygon_data)
        if location:
            updates.append("Location = ?")
            params.append(location)
        
        params.append(field_id)
        query = f"UPDATE Fields SET {', '.join(updates)} WHERE FieldID = ?"
        self.db.execute_query(query, params)

    def delete_field(self, field_id):
        query = "DELETE FROM Fields WHERE FieldID = ?"
        self.db.execute_query(query, (field_id,))