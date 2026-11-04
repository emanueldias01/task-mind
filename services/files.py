from models.tarefa import Tarefa
from pathlib import Path
import json
from services.errors import ResponseError, CommunicationError

FILE = Path("tarefas.txt")


def save_tarefa(tarefa: Tarefa):
    try:
        with FILE.open("a", encoding="utf-8") as f:
            f.write(tarefa.model_dump_json() + "\n")
    except OSError as error:
        raise CommunicationError(
            "Não foi possível salvar a tarefa no arquivo local."
        ) from error


def _list_tarefas() -> list[Tarefa]:
    if not FILE.exists():
        return []

    try:
        with FILE.open("r", encoding="utf-8") as file:
            return [
                Tarefa.model_validate(json.loads(line)) for line in file if line.strip()
            ]
    except (OSError, json.JSONDecodeError, ValueError) as error:
        raise ResponseError(
            "O arquivo de tarefas está indisponível ou contém dados inválidos."
        ) from error


def show_tasks():
    tasks = _list_tarefas()

    if not tasks:
        print("\nNenhuma tarefa cadastrada.")
        return

    print("\n--- TAREFAS CADASTRADAS ---")

    for index, task in enumerate(tasks, start=1):
        print(f"\nTarefa {index}")
        print(f"Matéria: {task.materia}")
        print(f"Descrição: {task.descricao}")
        print(f"Data: {task.data or 'Não informada'}")
