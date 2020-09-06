from datetime import datetime

from rmihandler import RmiHandler

import Pyro4 as pyro


if __name__ == "__main__":

    OPTION_ECHO = '1'
    OPTION_LIST = '2'
    OPTION_EXIT = '0'

    # while True:

    # connection = RmiHandler().get_connection()
    ns = pyro.locateNS(host='localhost', port=9090)
    servers = ns.list('custom-route-')
    for server in servers.keys():
        conn = pyro.Proxy(servers[server])
        conn.echo('Mensagem enviada as {}'.format(datetime.now()))
        print(conn.get_messages())
        break

        # print('\n#############\n')
        # print('Opções...')
        # print('{}) Enviar mensagem '.format(OPTION_ECHO))
        # print('{}) Listar mensagens '.format(OPTION_LIST))
        # print('{}) Sair '.format(OPTION_EXIT))
        # print('\n')
        # option = input('Escolha uma opção: ')

        # if option == OPTION_ECHO:
        #     print('enviando mensagem')
        #     message = input('Escreva sua mensagem: ')
        #     connection.echo(message)
        #     continue

        # if option == OPTION_LIST:
        #     print('listando mensagens')
        #     messages = connection.get_messages()
        #     print(messages)
        #     continue

        # if option == OPTION_EXIT:
        #     print('saindo')
        #     break
