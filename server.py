from multicast import MultiCast
from uuid import uuid4
from constants.routes_config import RoutesConfig

import Pyro4 as pyro


def _get_last_replica(key_list):
    return list(key_list.keys())[-1]


def get_replica():
    ns = pyro.locateNS(host=RoutesConfig.HOST, port=RoutesConfig.PORT)
    servers = ns.list('custom-route-')
    if servers:
        server_name = _get_last_replica(servers)
        return pyro.Proxy(servers[server_name])


if __name__ == "__main__":
    route = "custom-route-{}".format(uuid4())

    server_copy = get_replica()
    server = MultiCast()

    if server_copy:
        server.overwrite_messages(server_copy.get_messages)

    with pyro.Daemon() as daemon:
        ns = pyro.locateNS(host=RoutesConfig.HOST, port=RoutesConfig.PORT)
        uri = daemon.register(server)
        ns.register(route, uri)
        print("Server running...")
        daemon.requestLoop()
