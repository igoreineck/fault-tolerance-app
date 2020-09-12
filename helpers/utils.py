from uuid import uuid4

import Pyro4 as pyro

from constants.routes_config import RoutesConfig


def get_last_replica(servers):
    return list(servers.keys())[-1]


def generate_route():
    return 'custom-route-{}'.format(uuid4())


def get_replica():
    ns = pyro.locateNS(host=RoutesConfig.HOST, port=RoutesConfig.PORT)
    servers = ns.list('custom-route-')
    if servers:
        server_name = get_last_replica(servers)
        return pyro.Proxy(servers[server_name])
