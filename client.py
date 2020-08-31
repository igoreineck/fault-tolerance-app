from time import sleep

import Pyro4 as pyro


if __name__ == "__main__":

    FILENAME = "route.txt"
    SERVERNAME = 'localhost'
    PORT = 9090

    with open(FILENAME, "r") as file:
        route = file.read()

        connection = pyro.Proxy(
            "PYRO:{route}@{server}:{port}".format(
                route=route,
                server=SERVERNAME,
                port=PORT
            )
        )

        while True:
            print(connection.method())
            sleep(2)
