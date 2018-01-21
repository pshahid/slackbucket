import time


class Bucket(object):
    """ Single-threaded blocking version of Bucket which listens with the real-time api. """

    def __init__(self, slack, cfg):
        self.cfg = cfg
        self.slack = slack
        self.listening = False
        self._pre_start_hooks = []

    def _pre_start(self):
        pass

    def _post_start(self):
        for channel in self.cfg.channels:
            if not channel.startswith('#'):
                c = f"#{channel}"
            print(self.slack.api_call('channels.join', channel=c))

    def listen(self):
        event = self.slack.rtm_read()
        print(f"[x] Event: {event}")

    def start(self):
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