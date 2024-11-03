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

    def get_all_fields(self):
        query = "SELECT * FROM Fields"
        return self.db.fetch_all(query)


    def get_field(self, field_id):
        query = "SELECT * FROM Fields WHERE FieldID = ?"
        return self.db.fetch_one(query, (field_id,))

    def update_field(self, field_id, field_name, area,   location):
        query = """
        UPDATE Fields SET FieldName =?, Area =?, PolygonData =?, Location =? 
        WHERE FieldID =?
        """
        self.db.execute_query(query, (field_id, field_name, area, polygon_data, location))
        
    def delete_field(self, field_id):
        query = "DELETE FROM Fields WHERE FieldID = ?"
        self.db.execute_query(query, (field_id,))