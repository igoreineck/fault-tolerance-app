import os

from client_handler import ClientHandler
from constants.input_options import InputOptions


if __name__ == "__main__":
    client = ClientHandler()
    option = -1

    while option != InputOptions.EXIT:
        print("---------------------------")
        print("Opções\n")
        print("{}) Enviar mensagem".format(InputOptions.ECHO))
        print("{}) Listar mensagens".format(InputOptions.LIST))
        print("{}) Sair".format(InputOptions.EXIT))
        print("---------------------------")

        try:
            option = int(input('Escolha uma opção: '))

            if option == InputOptions.ECHO:
                os.system('clear')
                message = input('Escreva sua mensagem: ')
                client.echo(message)

            elif option == InputOptions.LIST:
                os.system('clear')
                messages = client.get_messages()
                print('Listando Mensagens: {}'.format(messages))

            elif option == InputOptions.EXIT:
                os.system('clear')
                print('Finalizando...')

            else:
                print('Selecione uma opção válida')

        except ValueError:
            print('Selecione uma opção válida')
