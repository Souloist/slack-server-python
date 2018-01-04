from sqlalchemy import (
    Column,
    Integer,
    Text,
)
from server.models.meta import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(Text, nullable=False)
    email = Column(Text, nullable=False)
    password = Column(Text, nullable=False)

    def __repr__(self):
        return "<User {}>".format(self.username)
