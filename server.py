import Pyro4 as pyro
from Pyro4.errors import CommunicationError

from constants.routes_config import RoutesConfig
from helpers.utils import generate_route, get_last_replica, get_replica
from multicast import MultiCast

if __name__ == "__main__":
    route = generate_route()
    server = MultiCast()

    try:
        server_copy = get_replica()
        if server_copy:
            server.overwrite_messages(server_copy.get_messages)
    except CommunicationError:
        pass

    with pyro.Daemon() as daemon:
        ns = pyro.locateNS(host=RoutesConfig.HOST, port=RoutesConfig.PORT)
        uri = daemon.register(server)
        servers = ns.list('custom-route-')
        ns.register(route, uri)
        print("Server running...")
        daemon.requestLoop()
        # remove server on stop to get only active servers on ns.list
        ns.remove(route, uri)
