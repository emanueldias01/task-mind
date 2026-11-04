
from models.tarefa import Tarefa
from pathlib import Path

def save_tarefa(tarefa: Tarefa):
    file = Path("tarefas.txt")

    with file.open("a", encoding="utf-8") as f:
        f.write(tarefa.model_dump_json() + "\n")