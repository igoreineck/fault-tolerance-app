import sys

from helpers.utils import get_replica, get_servers
from Pyro4 import Proxy


class ClientHandler:

    def echo(self, message):
        servers = get_servers()

        if servers:
            for server in list(servers.keys()):
                conn = Proxy(servers[server])
                conn.echo(message)
        else:
            print('Não há nenhum servidor ativo')
            sys.exit(0)

    def get_messages(self):
        try:
            conn = get_replica()
            return conn.get_messages
        except AttributeError:
            print('Não há nenhum servidor ativo')
            sys.exit(0)
