from datetime import date
from typing import Any, Callable

from langchain.chat_models import init_chat_model

from config import AppConfig, load_config
from models.tarefa import Tarefa
from services.errors import (
    CommunicationError,
    CredentialError,
    InputError,
    ResponseError,
    ServiceUnavailableError,
)
from services.files import save_tarefa

def prepare_prompt(description: str, current_date: date | None = None) -> str:
    current_date = current_date or date.today()
    return f"""
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


def build_model(config: AppConfig):
    try:
        return init_chat_model(model=config.model, model_provider=config.provider)
    except Exception as error:
        raise _classify_llm_error(error) from error


def request_task(description: str, config: AppConfig, model_factory: Callable = build_model) -> Tarefa:
    """Prepara a solicitação, chama o LLM e valida sua resposta."""
    if not description.strip():
        raise InputError("A descrição da tarefa não pode ficar vazia.")
    try:
        model = model_factory(config).with_structured_output(Tarefa)
        response = model.invoke(prepare_prompt(description))
    except Exception as error:
        if isinstance(error, (CredentialError, ServiceUnavailableError, CommunicationError)):
            raise
        raise _classify_llm_error(error) from error

    if isinstance(response, Tarefa):
        return response
    if isinstance(response, dict):
        try:
            return Tarefa.model_validate(response)
        except Exception as error:
            raise ResponseError(
                "O serviço respondeu, mas os dados da tarefa vieram em formato inválido."
            ) from error
    raise ResponseError("O serviço respondeu sem uma tarefa válida.")


def create_task(description: str, config: AppConfig | None = None, model_factory: Callable = build_model) -> Tarefa:
    if not description.strip():
        raise InputError("A descrição da tarefa não pode ficar vazia.")
    config = config or load_config()
    task = request_task(description, config, model_factory)

    save_tarefa(task)
    return task


def _classify_llm_error(error: Exception) -> Exception:
    """Converte detalhes técnicos do provedor em mensagens úteis e sem segredos."""
    message = str(error).lower()
    error_name = type(error).__name__.lower()

    if "api key" in message or "credential" in message or "authentication" in message or "unauthorized" in message or "permission" in message or "auth" in error_name:
        return CredentialError("A credencial foi recusada pelo serviço. Verifique a chave configurada e tente novamente.")
    if "timeout" in message or "deadline" in message:
        return CommunicationError("O serviço demorou demais para responder. Tente novamente em instantes.")
    if any(term in message for term in ("unavailable", "overloaded", "503", "404")):
        return ServiceUnavailableError("O modelo escolhido está indisponível no momento. Tente novamente mais tarde.")
    return CommunicationError("Não foi possível comunicar com o serviço de IA. Verifique sua conexão e tente novamente.")
