from sqlalchemy import text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base, str_uniq, int_pk


class User(Base):
    id: Mapped[int_pk]
    phone_number: Mapped[str_uniq]
    first_name: Mapped[str]
    last_name: Mapped[str]
    email: Mapped[str_uniq]
    password: Mapped[str]
    privilege_id: Mapped[int] = mapped_column(ForeignKey('privileges.id'), server_default=text('1'))
    privilege: Mapped["Privilege"] = relationship("Privilege", back_populates="users")

    extend_existing = True

    def __repr__(self):
        return f"{self.__class__.__name__}(id={self.id})"

    def to_dict(self):
        return {
            "id": self.id,
            "phone_number": self.phone_number,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "privilege_id": self.privilege_id,
            "privilege": self.privilege.privilege_name,
        }
