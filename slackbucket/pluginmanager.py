

class PluginManager(object):
    """ Provides a registration point for plugins; loads plugins at runtime; handles other plugin-related meta tasking
    """

    def __init__(self, dir='', plugins=None):
        if plugins:
            self.plugins = plugins
        else:
            self.plugins = []

        self.loaded = []
        self.dir = dir

    def load(self):
        pass


class Plugin(object):
    """ The most basic plugin consists of 2 functions, a name, and a version"""

    name = ''
    # Should be a tuple
    version = None

    def recv_cmd(self, msg):
        pass

    def match(self, msg):
        pass
