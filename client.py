from constants.routes_config import RoutesConfig

import Pyro4 as pyro


def _get_last_replica(key_list):
    return list(key_list.keys())[-1]


def check_replica():
    ns = pyro.locateNS(host=RoutesConfig.HOST, port=RoutesConfig.PORT)
    servers = ns.list('custom-route-')
    server_name = _get_last_replica(servers)
    return pyro.Proxy(servers[server_name])


if __name__ == "__main__":

    OPTION_ECHO = 1
    OPTION_LIST = 2
    OPTION_EXIT = 0

    option = -1

    conn = check_replica()

    while option != OPTION_EXIT:
        print('\n#############\n')
        print('Opções...')
        print('{}) Enviar mensagem '.format(OPTION_ECHO))
        print('{}) Listar mensagens '.format(OPTION_LIST))
        print('{}) Sair '.format(OPTION_EXIT))
        print('\n')

        option = int(input('Escolha uma opção: '))

        if option == OPTION_ECHO:
            print('enviando mensagem')
            message = input('Escreva sua mensagem: ')
            try:
                conn.echo(message)
            except pyro.errors.ConnectionClosedError:
                conn = check_replica()
                conn.echo(message)

        elif option == OPTION_LIST:
            print('listando mensagens')
            try:
                messages = conn.get_messages
            except pyro.errors.ConnectionClosedError:
                conn = check_replica()
                messages = conn.get_messages
            finally:
                print(messages)

        elif option == OPTION_EXIT:
            print('saindo')
