import base64
import os
import yaml

from slackclient import SlackClient
from .db import config as dbconfig


class PluginLoader(object):
    pass


class MetaConfig:
    def __init__(self, path='config.yaml'):
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

        if 'password' in cfg['database'] or 'username' in cfg['database']:
            raise RuntimeWarning("Please put secrets in environment variables instead of files.")

        db_password = os.getenv('DB_PASSWORD')
        db_username = os.getenv('DB_USERNAME')

        if 'database' in cfg:
            self.db = {
                'host': cfg['database']['host'],
                'port': cfg['database']['port'],
                'name': cfg['database']['name'],
                'vendor': cfg['database']['vendor'],
                'username': db_username,
                'password': db_password
            }
        else:
            self.db = {
                'host': '',
                'password': '',
                'port': '',
                'vendor': 'sqlite'
            }

        dbconfig.create(self.db)

    @property
    def token(self):
        """ Lazily read the token file and cache the value for the session """
        if not self._token:
            try:
                with open(self.tokenfile, 'r') as f:
                    self._token = f.read().strip()
            except FileNotFoundError:
                self._token = os.getenv('SLACK_TOKEN').strip()
                if not self._token:
                    raise RuntimeWarning("Unable to load slack token from either a file or an environment variable.")

        return self._token

    @property
    def slack(self):
        """ Lazily start the slack client and cache the object """
        if not self._slack:
            self._slack = SlackClient(self.token)
        return self._slack



