import pickle

# Função para carregar os contatos do arquivo
def load_contacts():
    try:
        with open("contacts.pkl", "rb") as f:
            contacts = pickle.load(f)
    except FileNotFoundError:
        contacts = {}
    return contacts

# Função para salvar os contatos no arquivo
def save_contacts(contacts):
    with open("contacts.pkl", "wb") as f:
        pickle.dump(contacts, f)

# Função para adicionar um contato
def add_contact(contacts):
    name = input("Nome: ")
    number = input("Número: ")
    contacts[name] = number
    save_contacts(contacts)
    print("Contato adicionado com sucesso!")

# Função para visualizar todos os contatos
def view_contacts(contacts):
    if contacts:
        print("Lista de Contatos:")
        for name, number in contacts.items():
            print(f"Nome: {name}, Número: {number}")
    else:
        print("Nenhum contato na agenda.")

# Função para buscar um contato por nome
def search_contact(contacts):
    name = input("Digite o nome do contato: ")
    if name in contacts:
        print(f"Nome: {name}, Número: {contacts[name]}")
    else:
        print("Contato não encontrado.")

# Função para excluir um contato
def delete_contact(contacts):
    name = input("Digite o nome do contato que deseja excluir: ")
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print("Contato excluído com sucesso!")
    else:
        print("Contato não encontrado.")

# Função principal
def main():
    contacts = load_contacts()
    while True:
        print("\n== Agenda de Contatos ==")
        print("1. Adicionar Contato")
        print("2. Visualizar Contatos")
        print("3. Buscar Contato")
        print("4. Excluir Contato")
        print("5. Sair")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
