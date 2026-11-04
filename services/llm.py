from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os
from models.tarefa import Tarefa
from services.files import save_tarefa

load_dotenv()

MODEL = os.getenv("MODEL")
PROVIDER = os.getenv("PROVIDER")


model = init_chat_model(
    model=MODEL,
    model_provider=PROVIDER,
)


def create_task():
    output_structured = model.with_structured_output(Tarefa)

    print("\nDescreva sua tarefa acadêmica:")
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

    print(f"\nTarefa salva com sucesso!")
    print(task)
