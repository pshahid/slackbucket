import time

from pluginregistry import PluginRegistry

class Bucket(object):
    """ Single-threaded blocking version of Bucket which listens with the real-time api. """

    def __init__(self, slack, cfg):
        self.cfg = cfg
        self.slack = slack
        self.listening = False
        self._pre_start_hooks = []
        self._post_start_hooks = []
        self.user_id = ''
        self.username = ''
        self.team_id = ''
        self.team = ''
        self.plugin_manager = PluginRegistry(plugins=cfg.plugins)

    def _whoami(self):
        resp = self.slack.api_call('auth.test')
        self.user_id = resp['user_id']
        self.team_id = resp['team_id']
        self.username = resp['user']
        self.team = resp['team']
        print(f"I am {self.username}, identified by {self.user_id}, on the {self.team} team!")

    def _pre_start(self):
        for hook in self._pre_start_hooks:
            hook(self)

    def _post_start(self):
        for hook in self._post_start_hooks:
            hook(self)

    def _cmd(self, event, msg):
        """ Internal call to delegate command behavior to plugins, returns response from plugin in slack """
        for plugin in self.plugin_manager.loaded:
            response = plugin.recv_cmd(msg)
            if response:
                self.say(response, event['channel'])
                break

    def _match(self, event, msg):
        """ Another very similar internal call to _cmd, delegates match behavior to plugins; basically first match wins
        here"""
        for plugin in self.plugin_manager.loaded:
            response = plugin.match(msg)
            if response:
                self.say(response, event['channel'])
                break

    def say(self, something, channel):
        self.slack.api_call('chat.postMessage', channel=channel, text=something)

    def listen(self):
        """ Handles the three most core pieces of functionality:
        1) Read from slack feeds
        2) Determine if something is a command or not
        3) If command, delegate to correct module; if not command attempt to trigger, passing along data either way"""

        events = self.slack.rtm_read()
        if not events:
            return

        for event in events:
            if event['type'] == 'message':
                msg = event['text']
                if msg.startswith(f"<@{self.user_id}>,"):
                    self._cmd(event, msg)
                else:
                    self._match(event, msg)

    def start(self):
        # Need to figure out what our user-id is so we can know when we're being talked at
        self._post_start_hooks.append(Bucket._whoami)
        self._pre_start()
        if self.slack.rtm_connect(with_team_state=False):
            self.listening = True
            self._post_start()
            while self.listening:
                self.listen()
                time.sleep(1)
        else:
            self.listening = False
            print("Connection failed.")

    def stop(self):
        self.listening = False
        print("Stopping.")
