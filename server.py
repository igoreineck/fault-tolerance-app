from multicast import MultiCast
import Pyro4


if __name__ == "__main__":

    exposed_class = Pyro4.expose(MultiCast)
    route = "myroute"
    FILENAME = "route.txt"

    with open(FILENAME, "w") as file:
        file.write(route)

    with Pyro4.Daemon() as daemon:
        daemon.serveSimple(
            {
                exposed_class: route
            },
            ns=False,
            host="0.0.0.0",
            port=9090
        )

        ns = Pyro4.locateNS(host='localhost', port=9090)
        print(ns)
