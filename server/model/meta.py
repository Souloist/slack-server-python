from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from server.settings import SQLALCHEMY_DATABASE_URI

engine = create_engine(SQLALCHEMY_DATABASE_URI, convert_unicode=True)

Session = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)
session = scoped_session(Session)

Base = declarative_base()
Base.query = session.query_property()
