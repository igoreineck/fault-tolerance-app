from constants.routes_config import RoutesConfig
from helpers.utils import generate_route, get_replica
from multicast import MultiCast
from Pyro4 import locateNS, Daemon
from Pyro4.errors import CommunicationError


if __name__ == "__main__":
    route = generate_route()
    server = MultiCast()

    try:
        server_copy = get_replica()
        if server_copy:
            server.overwrite_messages(server_copy.get_messages)
    except CommunicationError:
        pass

    with Daemon() as daemon:
        ns = locateNS(host=RoutesConfig.HOST, port=RoutesConfig.PORT)
        uri = daemon.register(server)
        servers = ns.list('custom-route-')
        ns.register(route, uri)
        print("Server running...")
        daemon.requestLoop()
        ns.remove(route, uri)
