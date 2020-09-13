from constants.routes_config import RoutesConfig
from Pyro4 import locateNS, Proxy
from uuid import uuid4


def get_first_replica(servers):
    return list(servers.keys())[0]


def generate_route():
    return 'custom-route-{}'.format(uuid4())


def get_servers():
    ns = locateNS(host=RoutesConfig.HOST, port=RoutesConfig.PORT)
    return ns.list('custom-route-')


def get_replica():
    servers = get_servers()
    if servers:
        server_name = get_first_replica(servers)
        return Proxy(servers[server_name])
