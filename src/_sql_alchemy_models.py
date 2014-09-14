from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.types import LargeBinary
from _sql_alchemy_helpers import get_sql_session

Base = declarative_base()

class SimpleRecord(Base):
  __tablename__ = 'simple_donce_record'

  id = Column(Integer, primary_key=True)
  name = Column(String(255, convert_unicode=True))
  key = Column(String(255, convert_unicode=True))


class BloomRecord(Base):
  __tablename__ = 'bloom_donce_record'

  id = Column(Integer, primary_key=True)
  name = Column(String(255))
  bitarray = Column(LargeBinary(255))

session, engine = get_sql_session(echo=True)
Base.metadata.create_all(engine)
