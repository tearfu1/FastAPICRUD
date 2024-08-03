from enum import Enum
from pydantic import BaseModel, EmailStr, Field, field_validator, ValidationError
from datetime import date, datetime
from typing import Optional, List
from fastapi import FastAPI, Depends
from utils import json_to_dict_list, dict_list_to_json
import os
import re

app = FastAPI()

script_dir = os.path.dirname(os.path.abspath(__file__))

parent_dir = os.path.dirname(script_dir)

path_to_json = os.path.join(parent_dir, 'students.json')


class SStudent(BaseModel):
    class Major(str, Enum):
        informatics = "Информатика"
        economics = "Экономика"
        law = "Право"
        medicine = "Медицина"
        engineering = "Инженерия"
        languages = "Языки"
        psychology = "Психология"
        biology = "Биология"
        maths = "Математика"
        ecology = "Экология"
        history = "История"

    student_id: int
    phone_number: str = Field(default=..., description="Номер телефона в международном формате, начинающийся с '+'")
    first_name: str = Field(default=..., min_length=1, max_length=50, description="Имя студента, от 1 до 50 символов")
    last_name: str = Field(default=..., min_length=1, max_length=50,
                           description="Фамилия студента, от 1 до 50 символов")
    date_of_birth: date = Field(default=..., description="Дата рождения студента в формате ГГГГ-ММ-ДД")
    email: EmailStr = Field(default=..., description="Электронная почта студента")
    address: str = Field(default=..., min_length=10, max_length=200,
                         description="Адрес студента, не более 200 символов")
    enrollment_year: int = Field(default=..., ge=2002, description="Год поступления должен быть не меньше 2002")
    major: Major = Field(default=..., description="Специальность студента")
    course: int = Field(default=..., ge=1, le=5, description="Курс должен быть в диапазоне от 1 до 5")
    special_notes: Optional[str] = Field(default=None, max_length=500,
                                         description="Дополнительные заметки, не более 500 символов")

    @field_validator("phone_number")
    @classmethod
    def validate_phone_number(cls, values: str) -> str:
        if not re.match(r'^\+\d{1,15}$', values):
            raise ValueError('Номер телефона должен начинаться с "+" и содержать от 1 до 15 цифр')
        return values

    @field_validator("date_of_birth")
    @classmethod
    def validate_date_of_birth(cls, values: date):
        if values and values >= datetime.now().date():
            raise ValueError('Дата рождения должна быть в прошлом')
        return values


class RBStudent:
    def __init__(self, course: int, major: Optional[str] = None, enrollment_year: Optional[int] = None):
        self.course: int = course
        self.major: Optional[str] = major
        self.enrollment_year: Optional[int] = enrollment_year


@app.get("/student", response_model=SStudent)
def get_student_from_param_id(student_id: int):
    students = json_to_dict_list(path_to_json)
    for student in students:
        if student["student_id"] == student_id:
            return student


@app.get("/students/{course}")
def get_all_students_course(request_body: RBStudent = Depends()) -> List[SStudent]:
    students = json_to_dict_list(path_to_json)
    filtered_students = []
    course = request_body.course
    major = request_body.major
    enrollment_year = request_body.enrollment_year
    for student in students:
        if student["course"] == course:
            filtered_students.append(student)

    if major:
        filtered_students = [student for student in filtered_students if student['major'].lower() == major.lower()]

    if enrollment_year:
        filtered_students = [student for student in filtered_students if student['enrollment_year'] == enrollment_year]
    return filtered_students
