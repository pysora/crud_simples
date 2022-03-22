lista = []

def menu():
    opvalidas = ['c', 'r', 'u', 'd', 'e', 'C', 'R', 'U', 'D', 'E']
    print('[c] - Create')
    print('[r] - Read')
    print('[u] - Update')
    print('[d] - Delete')
    print('[e] - Exit')

    while True:

        opcao = input('Opção: ')
        if opcao in opvalidas:
            break
        else:
            print("Opção invalida, tente novamente")

    return opcao

def create():
    nome = input('Nome: ')
    lista.append(nome)

def read():
    if lista == []:
        print("A lista está vazia.")

        for indice, v in enumerate(lista):
            print(indice, ' - ', v)
    else:
        print(lista)

def update():

    listaNaoVazia()

    try:
        p = int(input("Qual posição: "))
        novo_nome = input("Novo nome: ")
        lista[p] = novo_nome

    except IndexError:
        print("Posição não existe")


def delete():

    listaNaoVazia()

    nome = input("Qual nome: ")

    if nome in lista:
        lista.remove(nome)
    else:
        print(f"O {nome} não esta na lista")

def listaNaoVazia():

    if lista != []:
        read()

    else:
        print("A lista esta vazia")

if __name__ == '__main__':

    while True:
        op = menu()
        if op in 'cC':
            create()
        elif op in 'rR':
            read()
        elif op in 'uU':
            update()
        elif op in 'dD':
            delete()
        else:
            break
