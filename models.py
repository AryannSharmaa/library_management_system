from typing import Optional
from pydantic import BaseModel


class address(BaseModel):
    city: str
    country: str


class Student(BaseModel):
    name: str
    age: int
    address: address


class addressUpdate(BaseModel):
    city: Optional[str]
    country: Optional[str]


class StudentUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    address: Optional[addressUpdate] = None
