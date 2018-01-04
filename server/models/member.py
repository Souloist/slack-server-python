from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    Text,
)
from server.models.meta import Base


class Member(Base):
    __tablename__ = "members"

    id = Column(Integer, primary_key=True)
    team_id = Column(
        Text,
        ForeignKey("teams.id", ondelete="cascade"),
        nullable=False,
    )
    user_id = Column(
        Text,
        ForeignKey("users.id", ondelete="cascade"),
        nullable=False,
    )

    def __repr__(self):
        return "<Member {}>".format(self.id)
