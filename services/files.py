
from models.tarefa import Tarefa
from pathlib import Path
import json

FILE = Path("tarefas.txt")

def save_tarefa(tarefa: Tarefa):
    with FILE.open("a", encoding="utf-8") as f:
        f.write(tarefa.model_dump_json() + "\n")


def _list_tarefas() -> list[Tarefa]:
    if not FILE.exists():
        return []

    with FILE.open("r", encoding="utf-8") as file:
        return [
            Tarefa.model_validate(json.loads(line))
            for line in file
            if line.strip()
        ]


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
