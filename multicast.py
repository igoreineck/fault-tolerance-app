import Pyro4 as pyro

from datetime import datetime


@pyro.expose
class MultiCast:
    def __init__(self):
        self.messages = []

    def echo(self, message):
        # self.messages.append(message)
        self.dispatch()
        return "Message received: {}".format(message)

    def get_messages(self):
        return self.messages

    def add_messages(self, messages):
        self.messages = messages

    def dispatch(self):
        ns = pyro.locateNS(host='localhost', port=9090)
        servers = ns.list('custom-route-')
        for server in servers.keys():
            try:
                conn = pyro.Proxy(servers[server])
                msg = conn.add_messages(self.get_messages())
                print(msg)
            except Exception:
                import traceback
                traceback.print_exc()
                print('deu ruim')
