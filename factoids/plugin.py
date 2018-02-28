from slackbucket.baseplugin import BasePlugin
from slackbucket.db import config as db

from .models import Factoid


class Factoids(BasePlugin):
    name = 'factoids'
    version = '0.0.1'

    def __init__(self):
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

        if '<reply>' in msg:
            self._learn_reply(msg)
        print("Factoids receiving cmd!")
        print(msg)

    def match(self, msg):
        print("Factoids receiving msg!")
        print(msg)
        return True, "Shutup!"