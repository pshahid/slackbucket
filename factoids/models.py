from sqlalchemy import Column, Integer, String, Boolean

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



