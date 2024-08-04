from app.dao.base import BaseDAO
from app.majors.models import Major


class MajorDAO(BaseDAO):
    model = Major
