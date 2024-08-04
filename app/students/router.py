from fastapi import APIRouter, Depends
from app.students.dao import StudentDAO
from app.students.rb import RBStudent
from app.students.schemas import SStudent, SStudentAdd
from typing import List

router = APIRouter(prefix='/students', tags=['Work with students'])


@router.get("/", summary="Get all students", response_model=List[SStudent])
async def get_all_students(request_body: RBStudent = Depends()) -> List[SStudent]:
    return await StudentDAO.find_all(**request_body.to_dict())


@router.get("/by_filter", summary="Get one student by filter")
async def get_student_by_filter(request_body: RBStudent = Depends()) -> SStudent | dict:
    rez = await StudentDAO.find_one_or_none(**request_body.to_dict())
    if rez is None:
        return {'message': f'Студент с указанными вами параметрами не найден!'}
    return rez


@router.get("/{id}", summary="Get one student by id")
async def get_student_by_id(student_id: int) -> SStudent | dict:
    student = await StudentDAO.find_full_data(student_id)
    if student is None:
        return {'message': f'Student with id {student_id} not found'}
    return student


@router.post("/add/")
async def add_student(student: SStudentAdd) -> dict:
    check = await StudentDAO.add_student(**student.dict())
    if check:
        return {"message": "Студент успешно добавлен!", "student": student}
    else:
        return {"message": "Ошибка при добавлении студента!"}


@router.delete("/dell/{student_id}")
async def dell_student_by_id(student_id: int) -> dict:
    check = await StudentDAO.delete_student_by_id(student_id=student_id)
    if check:
        return {"message": f"Студент с ID {student_id} удален!"}
    else:
        return {"message": "Ошибка при удалении студента!"}
