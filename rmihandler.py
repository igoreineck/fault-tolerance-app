import Pyro4 as pyro


class RmiHandler:

    def __init__(self):
        self.hostname = 'localhost'
        self.port = 9090

    def get_connection(self):
        ns = pyro.locateNS(host=self.hostname, port=self.port)
        for key in list(server_names.keys()):
            if key == 'Pyro.NameServer':
                continue
            try:
                connection = pyro.Proxy(server_names[key])
                connection.get_messages()
                return connection
            except Exception:
                pass

    def register_named_server(self, uri, uuid):
        ns = pyro.locateNS(host=self.hostname, port=self.port)
        ns.register(uuid, uri)

    def get_named_servers(self):
        ns = pyro.locateNS(host=self.hostname, port=self.port)
        return ns.list()

    def get_server(self, instance):
        return pyro.Proxy("{}".format(instance))
