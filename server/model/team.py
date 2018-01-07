from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    Text,
)
from server.model.meta import Base


class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    owner = Column(
        Integer,
        ForeignKey("users.id", ondelete="cascade"),
        nullable=False,
    )

    def __repr__(self):
        return "<Team {}>".format(self.name)
