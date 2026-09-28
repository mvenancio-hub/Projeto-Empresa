from departamento import *

def menu_departamento():
    while True:
        print("\n=====================")
        print("Departamento")
        print("=====================")
        print("1 - INSERIR")
        print("2 - CONSULTAR DEPARTAMENTO")
        print("0 - VOLTAR")

        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            inserir_departamento() 
        elif opcao == "2":
            listar_departamento()  
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_departamento()