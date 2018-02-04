import os
import importlib

class PluginNotFoundError(Exception):
    """ Raised when plugins can't be found for some reason"""


class PluginManager(object):
    """ Provides a registration point for plugins; loads plugins at runtime; handles other plugin-related meta tasking

    Plugins can declare a priority so that they get
    """

    def __init__(self, active, plugins=None):
        if plugins:
            self.plugins = plugins
        else:
            self.plugins = {}

        self.active = active
        self.load()

        for name, p in self.plugins.items():
            if name in self.active:
                self.use(name)

        self.in_use = []

    def load(self):
        """ Dynamically load all potential python modules in the plugins directory, and register them
        """
        for f in os.listdir('slackbucket/plugins'):
            if f.endswith('.py'):
                # Take care to notice that when given a package plugins must use dot-prefixed names
                mod = importlib.import_module(f'.{f.split(".py")[0]}', package='slackbucket.plugins')
                plugin = mod.Plugin()
                self.register(plugin)

    def unregister(self, name):
        del self.plugins[name]

    def register(self, plugin):
        self.plugins[plugin.name] = plugin

    def use(self, name):
        p = self.plugins.get(name)
        if not p:
            raise PluginNotFoundError(f"Plugin {name} not found in PluginManager.")

        self.in_use.append(self.plugins[name])


class BasePlugin(object):
    """ The most basic plugin consists of 2 functions, a name, and a version"""

    name = ''
    # Should be a tuple
    version = None

    def recv_cmd(self, msg):
        pass

    def match(self, msg):
        pass


mgr = PluginManager()
