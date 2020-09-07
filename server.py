from multicast import MultiCast
from constants.routes_config import RoutesConfig
from helpers.utils import (
    get_last_replica,
    generate_route,
    get_replica,
)
import Pyro4 as pyro
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

    with pyro.Daemon() as daemon:
        ns = pyro.locateNS(host=RoutesConfig.HOST, port=RoutesConfig.PORT)
        uri = daemon.register(server)
        ns.register(route, uri)
        print("Server running...")
        daemon.requestLoop()
