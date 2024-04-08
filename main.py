from fastapi import FastAPI, HTTPException
from models import Student, StudentUpdate
from database import collection
from schemas import list_serial, individual_serial
from bson.objectid import ObjectId

app = FastAPI()


@app.post("/students", status_code=201)
async def create_stuents(student: Student):
    try:
        student.address = dict(student.address)
        id = collection.insert_one(dict(student))
        return {"id": str(id.inserted_id)}
    except:
        raise HTTPException(status_code=503, detail="error connecting to database")


@app.get("/students")
async def get_students(country: str | None = None, age: int | None = None):
    students = list_serial(collection.find())
    if country and age:
        filtered = filter(
            lambda x: x["address"]["country"] == country and x["age"] >= age, students
        )
        return {"students": list(filtered)}
    if country:
        filtered = filter(lambda x: x["address"]["country"] == country, students)
        return {"students": list(filtered)}
    if age:
        filtered = filter(lambda x: x["age"] >= age, students)
        return {"students": list(filtered)}
    return {"students": (students)}


@app.get("/students/{students_id}")
async def get_student(student_id: str):
    try:
        student = individual_serial(collection.find_one({"_id": ObjectId(student_id)}))
        print(student)
        return {"student": dict(student)}
    except:
        raise HTTPException(status_code=404, detail="No student found")
