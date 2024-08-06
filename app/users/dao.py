from sqlalchemy import select
from sqlalchemy.orm import joinedload

from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.users.models import User


class UsersDAO(BaseDAO):
    model = User

    @classmethod
    async def find_full_data(cls, user_id: int):
        async with async_session_maker() as session:
            query = select(cls.model).options(joinedload(cls.model.privilege)).filter_by(id=user_id)
            result = await session.execute(query)
            user_info = result.scalar_one_or_none()

            if not user_info:
                return None

            return user_info
