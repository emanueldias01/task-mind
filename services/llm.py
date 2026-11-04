from datetime import date
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

    current_date = date.today()
    print("\nDescreva sua tarefa:")
    description = input("-> ")

    task = output_structured.invoke(
        f"""
        Extraia as informações da seguinte tarefa:

        Data atual: {current_date}

        {description}

        Interprete datas relativas considerando a data atual.
        Por exemplo:
        - amanhã: dia seguinte à data atual;
        - depois de amanhã: dois dias após a data atual;
        - próxima sexta-feira: a próxima sexta-feira no calendário.


        Se não houver uma data explícita, retorne null.
        Não invente informações.
        """
    )

    save_tarefa(task)

    print(f"\nTarefa salva com sucesso!")
    print(task)
