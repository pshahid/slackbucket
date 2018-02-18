from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from slackbucket.db import config


class Factoid(config.base):
    __tablename__ = 'bucket_facts'

    id = Column(Integer, primary_key=True)
    fact = Column(String)
    tidbit = Column(String)
    verb = Column(String)
    RE = Column(Boolean)
    protected = Column(Boolean)
    mood = Column(String)
    chance = Column(Integer)


class Items(config.base):
    __tablename__ = 'bucket_items'

    id = Column(Integer, primary_key=True)
    channel = Column(String)
    what = Column(String)
    user = Column(String)


class Vars(config.base):
    __tablename__ = 'bucket_vars'

    id = Column(Integer, primary_key=True)
    values = relationship("VarsValues")
    name = Column(String)
    perms = Column(String)
    type = Column(String)


class VarsValues(config.base):
    __tablename__ = 'bucket_values'

    id = Column(Integer, primary_key=True)
    var_id = Column(Integer, ForeignKey('bucket_vars.id'))
    value = Column(String)



