import os
lista = []
backup_tarefas = []


def listar(lista):
    if not lista:
        print("Lista vaiza!")
    else:
        print("TAREFAS:")
        for tarefa in lista:
            print(tarefa.rjust(15, "."))
    

def desfazer(lista):
    try:
        lista.pop()
    except:
        print("Nada na lista!")


def refazer(lista):
    try:
        if not lista:
            lista.append(backup_tarefas[0])
        else:
            lista.append(backup_tarefas[len(lista)])
    except IndexError:
        print()


while True:
    print("Comandos: listar, desfazer, revazer, sair")
    comando = input("Digite uma tarefa ou comando: ")
    
    match comando.lower():
        case "listar":
            listar(lista)
        
        case "desfazer":
            desfazer(lista)
        
        case "refazer":
            refazer(lista)

        case "clear":
            os.system('cls')
        
        case "sair":
            break

        case _:
            lista.append(comando)
            backup_tarefas.append(comando)
    
    print()
