from app.database import Base, str_uniq, int_pk, str_null_true
from sqlalchemy.orm import relationship, Mapped
from app.users.models import User


class Privilege(Base):
    id: Mapped[int_pk]
    privilege_name: Mapped[str_uniq]
    privilege_description: Mapped[str_null_true]

    users: Mapped[list["User"]] = relationship("User", back_populates="privilege")

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, privilege_name={self.privilege_name!r})"

    def __repr__(self):
        return str(self)
