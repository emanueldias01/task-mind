from datetime import date
from pydantic import BaseModel

class Tarefa(BaseModel):
    materia: str
    descricao: str
    data: date | None = None
