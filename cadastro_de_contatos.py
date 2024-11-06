print("Bem-vindos à lista de contatos de Victor Gabriel da Silva Monteiro")
print('-'*56)
print('-'*20,'MENU PRINCIPAL','-'*20)

# Lista para armazenar contatos e variável global de id
lista_contatos = []
id_global = 4996692

def cadastrar_contato(id):
    """
    C: Função para cadastrar um contato
    a: Pergunta o nome, atividade e telefone
    b: Armazena o id, nome, atividade e telefone em um dicionário
    c: Adiciona o dicionário à lista de contatos
    """
    print('-'*20,'MENU CADASTRAR CONTATO','-'*20)
    print(f"ID do contato: {id}")  # Exibe o ID do contato
    nome = input('Digite o nome do contato: ')
    atividade = input('Digite a atividade do contato: ')
    telefone = input('Digite o número de telefone do contato: ')

    contato = {
        'id': id,
        'nome': nome,  # Mudei 'Nome' para 'nome' para ser consistente
        'atividade': atividade,
        'telefone': telefone  # Mudei 'Telefone' para 'telefone' para ser consistente
    }

    # c: Copia o dicionário para a lista de contatos
    lista_contatos.append(contato.copy())
    print('Contato cadastrado com sucesso!')

# D: Função para consultar contatos
def consultar_contatos():
    while True:
        print('-'*20,'MENU CONSULTAR CONTATO','-'*20)
        print("Escolha uma opção:")
        print("1. Consultar Todos")
        print("2. Consultar por Id")
        print("3. Consultar por Atividade")
        print("4. Retornar ao menu")
        print('-' * 30)

        opcao = input("Digite sua escolha (1-4): ")

        if opcao == '1':
            # i: Apresentar todos os contatos
            if lista_contatos:  # Verifica se a lista não está vazia
                for contato in lista_contatos:
                    print('-' * 30)  # Linha separadora
                    print(f'ID: {contato["id"]}')  # Correção aqui: uso de aspas duplas
                    print(f'Nome: {contato["nome"]}')  # Correção aqui: uso de aspas duplas
                    print(f'Atividade: {contato["atividade"]}')  # Correção aqui: uso de aspas duplas
                    print(f'Telefone: {contato["telefone"]}')  # Correção aqui: uso de aspas duplas
            else:
                print("Nenhum contato cadastrado.")
        elif opcao == '2':
            # ii: Consultar por Id
            id_consulta = input("Digite o id do contato: ")
            contato_encontrado = next((c for c in lista_contatos if c['id'] == int(id_consulta)), None)
            if contato_encontrado:
                print('-' * 30)
                print(f'ID: {contato_encontrado["id"]}')  # Correção aqui: uso de aspas duplas
                print(f'Nome: {contato_encontrado["nome"]}')  # Correção aqui: uso de aspas duplas
                print(f'Atividade: {contato_encontrado["atividade"]}')  # Correção aqui: uso de aspas duplas
                print(f'Telefone: {contato_encontrado["telefone"]}')  # Correção aqui: uso de aspas duplas
                print('-' * 30)
            else:
                print("Contato não encontrado.")
        elif opcao == '3':
            # iii: Consultar por Atividade
            atividade = input("Digite a atividade: ")
            contatos_encontrados = [c for c in lista_contatos if c['atividade'].lower() == atividade.lower()]
            if contatos_encontrados:
                for c in contatos_encontrados:
                    print('-' * 30)
                    print(f'ID: {c["id"]}')  # Correção aqui: uso de aspas duplas
                    print(f'Nome: {c["nome"]}')  # Correção aqui: uso de aspas duplas
                    print(f'Atividade: {c["atividade"]}')  # Correção aqui: uso de aspas duplas
                    print(f'Telefone: {c["telefone"]}')  # Correção aqui: uso de aspas duplas
                print('-' * 30)
            else:
                print("Nenhum contato encontrado para esta atividade.")
        elif opcao == '4':
            return  # iv: Retornar ao menu principal
        else:
            print("Opção inválida. Por favor, tente novamente.")  # v


def remover_contato():
    """
    E: Função para remover um contato
    a: Pergunta pelo id do contato a ser removido
    b: Remove o contato da lista de contatos
    """
    while True:
        print('-' * 20, 'MENU REMOVER CONTATO', '-' * 20)
        id_remocao = input("Digite o id do contato a ser removido: ")
        contato_remover = next((c for c in lista_contatos if c['id'] == int(id_remocao)), None)

        if contato_remover:
            lista_contatos.remove(contato_remover)  # b
            print("Contato removido com sucesso!")
            return  # Sair da função após a remoção
        else:
            print("Id inválido. Por favor, tente novamente.")  # c


# F: Estrutura do menu principal
while True:
    print('-' * 20)
    print("Escolha uma opção:")
    print("1. Cadastrar Contato")
    print("2. Consultar Contato")
    print("3. Remover Contato")
    print("4. Encerrar Programa")
    print('-' * 20)

    escolha = input("Digite sua escolha (1-4): ")

    if escolha == '1':
        id_global += 1  # i: Incrementar o id global
        cadastrar_contato(id_global)  # ii: Chamar a função de cadastro
    elif escolha == '2':
        consultar_contatos()  # iii: Chamar a função de consulta
    elif escolha == '3':
        remover_contato()  # iv: Chamar a função de remoção
    elif escolha == '4':
        print("Encerrando o programa.")
        break  # v: Sair do programa
    else:
        print("Opção inválida. Por favor, tente novamente.")  # vi