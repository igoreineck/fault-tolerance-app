import sys

import Pyro4 as pyro
from Pyro4.errors import CommunicationError, ConnectionClosedError

from constants.routes_config import RoutesConfig
from helpers.utils import get_last_replica, get_replica, get_servers


class ClientHandler:

    def echo(self, message):
        servers = get_servers()
        if servers:
            for server in list(servers.keys()):
                conn = pyro.Proxy(servers[server])
                conn.echo(message)
        else:
            print('Não há nenhum servidor ativo')
            sys.exit(0)

    def get_messages(self):
        try:
            conn = get_replica()
            return conn.get_messages
        except:
            print('Não há nenhum servidor ativo')
            sys.exit(0)
