
class BasePlugin(object):
    """ The most basic plugin consists of 2 functions, a name, and a version"""

    name = ''
    # Should be a tuple
    version = None

    def recv_cmd(self, msg):
        pass

    def match(self, msg):
        pass