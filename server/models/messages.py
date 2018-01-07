from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    Text,
)
from server.models.meta import Base


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True)
    text = Column(Text, nullable=False)
    user_id = Column(
        Integer,
        ForeignKey("users.id", ondelete="cascade"),
        nullable=False,
    )

    channel_id = Column(
        Integer,
        ForeignKey("channels.id", ondelete="cascade"),
        nullable=False,
    )

    def __repr__(self):
        return "<Message {}>".format(self.id)
