from fastapi import APIRouter
from app.majors.dao import MajorDAO
from app.majors.schemas import SMajorsAdd
from app.majors.schemas import SMajorUpdDesc

router = APIRouter(prefix='/majors', tags=['Work with majors'])


@router.post("/add/")
async def register_user(major: SMajorsAdd) -> dict:
    check = await MajorDAO.add(**major.dict())
    if check:
        return {"message": "Факультет успешно добавлен!", "major": major}
    else:
        return {"message": "Ошибка при добавлении факультета!"}


@router.put("/update_description/")
async def update_major_description(major: SMajorUpdDesc) -> dict:
    check = await MajorDAO.update(filter_by={'major_name': major.major_name},
                                  major_description=major.major_description)
    if check:
        return {"message": "Описание факультета успешно обновлено!", "major": major}
    else:
        return {"message": "Ошибка при обновлении описания факультета!"}


@router.delete("/delete/{major_id}")
async def delete_major(major_id: int) -> dict:
    check = await MajorDAO.delete(id=major_id)
    if check:
        return {"message": f"Факультет с ID {major_id} удален!"}
    else:
        return {"message": "Ошибка при удалении факультета!"}
