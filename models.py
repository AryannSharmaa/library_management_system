from typing import Optional
from pydantic import BaseModel
from pydantic.types import conint, constr


class address(BaseModel):
    city: constr(min_length=1)
    country: constr(min_length=1)


class Student(BaseModel):
    name: constr(min_length=1)
    age: conint(gt=0)
    address: address


class addressUpdate(BaseModel):
    city: Optional[str]
    country: Optional[str]


class StudentUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    address: Optional[addressUpdate] = None
