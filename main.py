from fastapi import FastAPI, HTTPException
from models import Student, StudentUpdate
from database import collection

app = FastAPI()


@app.post("/students", status_code=201)
async def create_stuents(student: Student):
    try:
        student.address = dict(student.address)
        id = collection.insert_one(dict(student))
        return {"id": str(id.inserted_id)}
    except:
        raise HTTPException(status_code=503, detail="error connecting to database")
