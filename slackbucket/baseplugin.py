
class BasePlugin(object):
    """ The most basic plugin consists of 2 functions, a name, and a version

    A Plugin is expected to implement all methods and attributes of BasePlugin.
    """

    name = ''
    # Should be a tuple
    version = None

    def recv_cmd(self, msg):
        """ When the bot is addressed directly this method is invoked with the succeeding message

        :param str msg: Message sent from another user, directed at the bot
        :returns (bool, str): True/False whether command succeeded; string of reply if any
        """
        return False, ""

    def match(self, msg):
        """ When any text is said on the chat that _is not_ directly addressing the bot, but a possible trigger, this
        method is invoked with the message

        :param str msg:
        :returns (bool, str): Same return value as recv_cmd
        """
        return False, ""
