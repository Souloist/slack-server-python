from sqlalchemy import (
    Boolean,
    Column,
    Integer,
    ForeignKey,
    Text,
)
from server.models.meta import Base


class Channel(Base):
    __tablename__ = "channels"

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    team_id = Column(
        Integer,
        ForeignKey("teams.id", ondelete="cascade"),
        nullable=False,
    )
    is_private = Column(Boolean, nullable=False, server_default="f", default=False)

    def __repr__(self):
        return "<Channel {}>".format(self.name)
