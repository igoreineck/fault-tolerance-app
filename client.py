from constants.input_options import InputOptions
from client_handler import ClientHandler
import os


if __name__ == "__main__":

    option = -1
    client = ClientHandler()

    while option != InputOptions.OPTION_EXIT:
        print('\n#############\n')
        print('Opções...')
        print('{}) Enviar mensagem '.format(InputOptions.OPTION_ECHO))
        print('{}) Listar mensagens '.format(InputOptions.OPTION_LIST))
        print('{}) Sair '.format(InputOptions.OPTION_EXIT))
        print('\n')

        try:
            option = int(input('Escolha uma opção: '))

            if option == InputOptions.OPTION_ECHO:
                os.system('clear')
                message = input('Escreva sua mensagem: ')
                client.echo(message)

            elif option == InputOptions.OPTION_LIST:
                os.system('clear')
                messages = client.get_messages()
                print('Listando Mensagens: {}'.format(messages))

            elif option == InputOptions.OPTION_EXIT:
                os.system('clear')
                print('Saindo')

            else:
                print('Selecione uma opção válida')

        except ValueError:
            print('Selecione uma opção válida')
