from constants.routes_config import RoutesConfig
from Pyro4.errors import (
    ConnectionClosedError,
    CommunicationError
)
from helpers.utils import get_last_replica, get_replica
import Pyro4 as pyro
import sys


class ClientHandler:

    def echo(self, message):
        try:
            conn = get_replica()
            conn.echo(message)
        except CommunicationError:
            print('Não há nenhum servidor ativo')
            sys.exit(0)

    def get_messages(self):
        try:
            conn = get_replica()
            return conn.get_messages
        except CommunicationError:
            print('Não há nenhum servidor ativo')
            sys.exit(0)
