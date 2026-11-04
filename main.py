from services.llm import create_task
from services.files import show_tasks
from services.errors import TaskMindError

def main():
    while True:
        print("\n--- TASKMIND ---")
        print("1 - Cadastrar tarefa")
        print("2 - Listar tarefas")
        print("3 - Sair")

        option = input("\nEscolha uma opção: ").strip()

        if option == "1":
            print("\nDescreva sua tarefa:")
            description = input("-> ").strip()
            if not description:
                print("\nA descrição não pode ficar vazia.")
                continue
            try:
                task = create_task(description)
                print("\nTarefa salva com sucesso!")
                print(task)
            except TaskMindError as error:
                print(f"\nNão foi possível cadastrar a tarefa: {error}")
            except Exception:
                print("\nOcorreu um erro inesperado. Tente novamente ou procure o responsável pelo sistema.")

        elif option == "2":
            try:
                show_tasks()
            except TaskMindError as error:
                print(f"\nNão foi possível listar as tarefas: {error}")
            except Exception:
                print("\nNão foi possível ler as tarefas salvas.")

        elif option == "3":
            print("\nEncerrando TaskMind...")
            break

        else:
            print("\nOpção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
