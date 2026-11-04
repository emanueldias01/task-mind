from services.llm import create_task
from services.files import show_tasks

def main():
    while True:
        print("\n--- TASKMIND ---")
        print("1 - Cadastrar tarefa")
        print("2 - Listar tarefas")
        print("3 - Sair")

        option = input("\nEscolha uma opção: ")

        if option == "1":
            create_task()

        elif option == "2":
            show_tasks()

        elif option == "3":
            print("\nEncerrando TaskMind...")
            break

        else:
            print("\nOpção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
