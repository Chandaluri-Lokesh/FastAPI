from fastapi import APIRouter
from models.student import Student
from config.db import conn
from schemas.student import serializeDict,serializeList
student = APIRouter()

@student.get('/')
def home():
    return "Hello World"

@student.get('/get-all-list/')
async def get_all_students():
    return serializeList(conn.Sample_db.Sample_collection.find())
    
@student.get("/get-student-by-name/{student_name}")
async def get_by_name(student_name:str):
    return serializeList(conn.Sample_db.Sample_collection.find({"name":student_name}))

@student.post("/create-student/")
async def create_student(student: Student):
    conn.Sample_db.Sample_collection.insert_one(dict(student))
    return serializeList(conn.Sample_db.Sample_collection.find())

@student.put("/update-student/{student_name}")
def update_student(student_name:str, student:Student):
    conn.Sample_db.Sample_collection.find_one_and_update({"name":student_name},{"$set":dict(student)})
    return serializeList(conn.Sample_db.Sample_collection.find({"name":student_name}))

@student.delete("/delete-student/{student_name}")
def delete_student(student_name: str):
    conn.Sample_db.Sample_collection.find_one_and_delete({"name":student_name})
    return serializeList(conn.Sample_db.Sample_collection.find())