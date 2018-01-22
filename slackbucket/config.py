import base64
import os
import yaml

from slackclient import SlackClient


class PluginLoader(object):
    pass


class MetaConfig:
    def __init__(self, path='/usr/src/app/config.yaml'):
        self.path = path
        self.cfgs = {}
        for team, cfg in self._new_config_from_file().items():
            self.cfgs[team] = Configurator(team, cfg)

    def _new_config_from_file(self):
        with open(self.path, 'r') as f:
            all_cfgs = yaml.load(f)

        return all_cfgs


class Configurator(object):
    def __init__(self, name, cfg):
        self._raw = cfg
        self._token = None
        self._slack = None
        self.name = name
        self.tokenfile = cfg['token']
        self.plugins = cfg['plugins']
        self.channels = cfg['channels']

    @property
    def token(self):
        """ Lazily read the token file and cache the value for the session """
        if not self._token:
            try:
                with open(self.tokenfile, 'r') as f:
                    self._token = f.read().strip()
            except FileNotFoundError:
                # HACK: workaround for k8s auto-base64-encoding secrets. Determine how we can not make this assumption
                self._token = base64.b64decode(os.getenv('SLACK_TOKEN')).strip()
                if not self._token:
                    raise RuntimeWarning("Unable to load slack token from either a file or an environment variable.")

        return self._token

    @property
    def slack(self):
        """ Lazily start the slack slack and cache the object """
        if not self._slack:
            self._slack = SlackClient(self.token)
        return self._slack



