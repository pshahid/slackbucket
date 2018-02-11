from slackbucket.baseplugin import BasePlugin

from .models import Factoid


class Factoids(BasePlugin):
    name = 'factoids'
    version = '0.0.1'

    def __init__(self):
        print("Factoids initialized.")
        Factoid()

    def recv_cmd(self, msg):
        print("Factoids receiving cmd!")
        print(msg)

    def match(self, msg):
        print("Factoids receiving msg!")
        print(msg)