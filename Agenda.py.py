# Lista para armazenar os contatos
agenda = []

# Função para incluir um contato
def incluir_contato():
    nome = input("Digite o nome: ")
    telefone = input("Digite o telefone: ")
    agenda.append([nome, telefone])
    print('-'*60)
    print("Contato adicionado!")
    print('-'*60)

# Função para pesquisar um contato
def pesquisar_contato():
    nome = input("Digite o nome para pesquisar: ")
    for contato in agenda:
        if contato[0] == nome:
            print(f"Nome: {contato[0]}, Telefone: {contato[1]}")
            return
    print('-'*60)
    print("Contato não encontrado.")
    print('-'*60)

# Função para atualizar um contato
def atualizar_contato():
    nome = input("Digite o nome para atualizar: ")
    for contato in agenda:
        if contato[0] == nome:
            telefone = input("Digite o novo telefone: ")
            contato[1] = telefone
            print("Contato atualizado!")
            return
    print('-'*60) 
    print("Contato não encontrado.")
    print('-'*60)

# Função para excluir um contato
def excluir_contato():
    nome = input("Digite o nome para excluir: ")
    for contato in agenda:
        if contato[0] == nome:
            agenda.remove(contato)
            print("Contato excluído!")
            return
    print('-'*60)
    print("Contato não encontrado.")
    print('-'*60)

# Função para ordenar os contatos
def ordenar_contatos():
    agenda.sort()
    print('-'*60) 
    print("Contatos ordenados!")
    print('-'*60)

# Menu principal
while True:
    print("1. Incluir contato")
    print("2. Pesquisar contato")
    print("3. Atualizar contato")
    print("4. Excluir contato")
    print("5. Ordenar contatos")
    print("6. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == '1':
        incluir_contato()
    elif opcao == '2':
        pesquisar_contato()
    elif opcao == '3':
        atualizar_contato()
    elif opcao == '4':
        excluir_contato()
    elif opcao == '5':
        ordenar_contatos()
    elif opcao == '6':
        print("Saindo...")
        break
    else:
        print("Opção inválida, tente novamente!")
