""" Simple Implementation of Donce """

from _sql_alchemy_helpers import get_sql_session
from _sql_alchemy_models import SimpleRecord

class SimpleDonce(object):
  def __init__(self, name):
    self.name = name
    self.session, _ = get_sql_session()
    self.keys = set([x[0] for x in self.session.query(SimpleRecord.key).filter_by(name=name).all()])

  def copy(self):
    pass

  def __contains__(self, key):
    return key in self.keys

  def add(self, key, skip_check=False):
    """ Adds key.  If key is already there, returns True, otherwise False. """
    # SQLAlchemy will coerce into string.
    # This fixes a loading bug where int keys are loaded from the DB as strings and not matched
    key = str(key)

    if not skip_check and key in self:
      return True

    # add record
    new_record = SimpleRecord(name=self.name, key=key)
    self.session.add(new_record)
    self.session.commit()

    # add to cached set
    self.keys.add(key)

    return False;

  def _delete(self):
    """ Clears the records for this name """
    records = self.session.query(SimpleRecord).filter_by(name=self.name).all()
    for record in records:
      self.session.delete(record)
    self.session.commit()
