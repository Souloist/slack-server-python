from sqlalchemy import Column, Integer, Text, Boolean
from server.models.meta import Base


class Channel(Base):
    __tablename__ = "channels"

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    is_private = Column(Boolean, nullable=False)

    def __repr__(self):
        return "<Channel {}>".format(self.name)
