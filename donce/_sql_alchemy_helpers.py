import getpass
import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import logging

DONCE_USER = 'donce_user'
DONCE_DB = 'donce_db'

def get_sql_session(user=DONCE_USER, db=DONCE_DB, echo=False):
  try:
    with open(os.path.expanduser("~/.mysql_%s_pw" % user)) as fh:
      passwd = fh.read().strip()
  except:
    passwd = getpass.getpass("MySQL Password: ")

  # start and connect to mysql
  engine = create_engine('mysql://%s:%s@localhost/%s' % (user, passwd, db), echo=echo)
  Session = sessionmaker(bind=engine)
  session = Session()
  base = declarative_base()
  base.metadata.create_all(engine)
  return session, engine


