from fastapi import APIRouter, Depends
from app.privileges.schemas import SPrivilegeAdd, SPrivilegeUpd
from app.privileges.dao import PrivilegeDAO
from app.users.models import User
from app.users.dependecies import get_current_admin_user

router = APIRouter(prefix="/privilege", tags=["Privileges"])


@router.get("/all_privileges/")
async def get_all_privileges(user_data: User = Depends(get_current_admin_user)):
    check = await PrivilegeDAO.find_all()
    if check:
        return check
    else:
        return {"message": "No privileges"}


@router.post("/add/")
async def add_privilege(privilege: SPrivilegeAdd, user_data: User = Depends(get_current_admin_user)):
    check = await PrivilegeDAO.add(**privilege.dict())
    if check:
        return {"message": "Privilege added successfully", "privilege": privilege}
    else:
        return {"message" "Error during adding privilege"}


@router.delete("/delete/{privilege_name}")
async def delete_privilege(privilege_name: str, user_data: User = Depends(get_current_admin_user)):
    check = await PrivilegeDAO.delete(privilege_name=privilege_name)
    if check:
        return {"message": "Privilege deleted successfully"}
    else:
        return {"message" "Error during deleting privilege"}


@router.put("/edit/{privilege_name}")
async def edit_privilege(privilege_name: str, privilege_data: SPrivilegeUpd,
                         user_data: User = Depends(get_current_admin_user)):
    check = await PrivilegeDAO.update(filter_by={"privilege_name": privilege_name},
                                      **privilege_data.dict())
    if check:
        return {"message": "Privilege edited successfully", "privilege": privilege_name}
    else:
        return {"message" "Error during editing privilege"}
