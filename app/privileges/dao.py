from app.dao.base import BaseDAO
from app.privileges.models import Privilege


class PrivilegeDAO(BaseDAO):
    model = Privilege
