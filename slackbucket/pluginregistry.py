import os
import importlib


from baseplugin import BasePlugin


class PluginNotFoundError(Exception):
    """ Raised when plugins can't be found for some reason"""


class PluginConfigurationError(Exception):
    """ Raised when something has gone wrong when attempting to configure a plugin """


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

        This is heavily inspired by Django's AppConfig code. Some code was borrowed.
        """

        if self.ready:
            return

        for p in plugins:
            print(f"Attempting to load {p}")
            module_path, _, cls_name = p.rpartition('.')
            if not module_path:
                raise Exception(f"Path for plugin {p} must be absolute path to plugin module.")

            mod = importlib.import_module(module_path)

            try:
                cls = getattr(mod, cls_name)
            except AttributeError as ae:
                raise Exception(f"Class name specified in configuration not found in module {p}") from ae

            if not issubclass(cls, BasePlugin):
                raise PluginConfigurationError(f"Class {cls} is not a subclass of BasePlugin")

            try:
                plugin_package_name = cls.name
            except AttributeError:
                raise PluginConfigurationError(f"Plugin config class {cls_name} does not have attribute 'name'")

            try:
                plugin_package = importlib.import_module(plugin_package_name)
            except ImportError as e:
                raise PluginConfigurationError(f"Plugin package not found for {p}") from e

            self.loaded.append(plugin_package)
        self.ready = True

plugins = PluginRegistry()
