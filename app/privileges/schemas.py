from pydantic import BaseModel, Field


class SPrivilegeAdd(BaseModel):
    privilege_name: str = Field(..., description="Название роли")
    privilege_description: str = Field(None, description="Описание роли")


class SPrivilegeUpd(BaseModel):
    privilege_name: str = Field(None, description="Новое название роли")
    privilege_description: str = Field(None, description="Новое описание роли")
