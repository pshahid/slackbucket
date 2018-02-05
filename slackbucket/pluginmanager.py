import os
import importlib


class PluginNotFoundError(Exception):
    """ Raised when plugins can't be found for some reason"""


class PluginRegistry(object):
    """ Provides a registration point for plugins; loads plugins at runtime; handles other plugin-related meta tasking
    """

    def __init__(self, plugins=()):
        self.ready = False
        self.loaded = []
        if plugins:
            self.load(plugins)

    def load(self, plugins):
        """ Loads all python modules declared in the config, and registers them here. Once registered Bucket should
        use the module/plugin references to pass commands/text to each plugin.

        We expect that each plugin is a directory with at least one file: plugin.py, containing an attribute which is
        an instance of BasePlugin. For now, we just look in a package of this repo (.plugins) but maybe in the future
        it would make sense to allow them to be pip-installable or something.
        """

        if self.ready:
            return

        for p in plugins:
            mod = importlib.import_module(f".{p}.plugin", package=".plugins")
            self.loaded.append(mod)
        self.ready = True

plugins = PluginRegistry()
