from datetime import datetime
from Pyro4 import expose


@expose
class MultiCast:
    def __init__(self):
        self._messages = []

    def echo(self, message):
        self._messages.append(message)
        return "Message received: {}".format(message)

    @property
    def get_messages(self):
        return self._messages

    def overwrite_messages(self, messages):
        self._messages = messages
