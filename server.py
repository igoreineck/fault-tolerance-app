from multicast import MultiCast
# from rmihandler i
from uuid import uuid4
import Pyro4 as pyro


if __name__ == "__main__":

    HOST = 'localhost'
    PORT = 9090

    route = "custom-route-{}".format(uuid4())

    with pyro.Daemon() as daemon:
        # ns = RmiHandler().get_named_servers()
        ns = pyro.locateNS(host='localhost', port=9090)
        # server = MultiCast()
        uri = daemon.register(MultiCast)
        ns.register(route, uri)
        print("Server running...")
        daemon.requestLoop()
        # while True:
        #     mensagens = server.get_messages()
