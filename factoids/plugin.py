import re

from slackbucket.baseplugin import BasePlugin
from slackbucket.db import config as db

from .models import Factoid

# Used to match an idle chatter command given to learn a factoid
re_cmd = "(.*?)\s+(?P<action>\<[^ <>]+\>(.*)"


class CRUDFactoidEvent(object):

    def __init__(self):
        self.session = db.config.session

    def process(self, trigger, action, tidbit):
        """ Override this method to create, read, update, or delete a factoid
        inside of a sqlalchemy session. Any uncaught exceptions will trigger a
        session.rollback() before returning"""

    def __call__(self, *args, **kwargs):
        self.session()
        try:
            result = self.process(*args, **kwargs)
            self.session.commit()
            return result
        except:
            self.session.rollback()
        finally:
            self.session.close()


class CreateOrUpdateFactoid(CRUDFactoidEvent):

    def process(self, fact, action, tidbit):
        self.session.query(Factoid).filter_by(fact=fact)


class Factoids(BasePlugin):
    name = 'factoids'
    version = '0.0.1'

    def __init__(self):
        self.last_factoid = None
        self.last_factoid_time = None
        print("Factoids initialized.")
        Factoid()

    def recv_cmd(self, msg):
        """ Accepts a command from a user, generally to learn a new factoid

        Learning new factoids can look like this:
        "@bucket, say a thing <reply> thing!"
        "@bucket, do a thing <action> does a thing"

        Generally there's a metafactoid here, which is that bucket must know about <reply>
        and <action>. These will end up being different responses from the bot itself; additionally
        behavior may differ between communication mediums (irc, slack, discord, etc..)
        """

        split_msg = re.split(re_cmd, msg)
        if len(split_msg) > 3:
            _, fact, action, tidbit = split_msg
        elif len(split_msg) > 1:
            fact, action, tidbit = split_msg

        print("Factoids receiving cmd!")
        print(msg)

    def match(self, msg):
        print("Factoids receiving msg!")
        print(msg)
        return True, "Shutup!"