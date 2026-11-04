from services.llm import model
from models.tarefa import Tarefa
from services.files import save_tarefa

def main():
    output_structured = model.with_structured_output(Tarefa)

    print("---TASKMIND---")
    print("Descreva sua tarefa:")

    description = input("-> ")

    task = output_structured.invoke(
    f"""
        Extraia as informações da seguinte tarefa acadêmica:
        {description}

        Se não houver uma data explícita, retorne null.
        Não invente informações.
        """
    )

    save_tarefa(task)

    print(f"Tarefa salva: {task}")

if __name__ == "__main__":
    main()
