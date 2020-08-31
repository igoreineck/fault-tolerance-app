from Pyro4 import expose, Daemon
from classtest import Testing


if __name__ == "__main__":

    exposed_class = expose(Testing)
    route = "myroute"
    FILENAME = "route.txt"

    with open(FILENAME, "w") as file:
        file.write(route)

    with Daemon() as daemon:
        daemon.serveSimple(
            {
                exposed_class: route
            },
            ns=False,
            host="localhost",
            port=9090
        )
