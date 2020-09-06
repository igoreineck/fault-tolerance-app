from time import sleep

import Pyro4 as pyro


if __name__ == "__main__":

    FILENAME = "route.txt"
    SERVERNAME = 'localhost'
    PORT = 9090

    OPTION_ECHO = '1'
    OPTION_LIST = '2'
    OPTION_EXIT = '0'

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
            print('\n#############\n')
            print('Opções...')
            print('{}) Enviar mensagem '.format(OPTION_ECHO))
            print(OPTION_LIST+') Listar mensagens ')
            print(OPTION_EXIT+') Sair ')
            print('\n')
            option = input('Escolha uma opção: ')

            if option == OPTION_ECHO:
                print('enviando mensagem')
                message = input('Escreva sua mensagem: ')
                connection.echo(message)
                continue

            if option == OPTION_LIST:
                print('listando mensagens')
                messages = connection.get_messages()
                print(messages)
                continue

            if option == OPTION_EXIT:
                print('saindo')
                break
