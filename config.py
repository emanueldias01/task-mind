import os
from dataclasses import dataclass
from dotenv import load_dotenv
from services.errors import ConfigurationError, CredentialError

SUPPORTED_PROVIDERS = {"google_genai": "GOOGLE_API_KEY"}


@dataclass(frozen=True)
class AppConfig:
    model: str
    provider: str
    credential_name: str


def load_config() -> AppConfig:
    """Carrega e valida a configuração sem exibir valores sensíveis."""
    load_dotenv()

    model = os.getenv("MODEL", "").strip()
    provider = os.getenv("PROVIDER", "").strip()
    credential_name = _credential_name(provider)

    if not model or not provider:
        raise ConfigurationError(
            "A configuração do modelo está incompleta. Confira MODEL e PROVIDER no arquivo .env."
        )

    if provider not in SUPPORTED_PROVIDERS:
        raise ConfigurationError(
            f"O provedor '{provider}' não é suportado. Use google_genai conforme o .env.example."
        )

    if not os.getenv(credential_name, "").strip():
        raise CredentialError(
            f"A credencial de acesso ({credential_name}) não foi configurada. "
            "Preencha o .env e tente novamente."
        )

    return AppConfig(model=model, provider=provider, credential_name=credential_name)


def _credential_name(provider: str) -> str:
    return SUPPORTED_PROVIDERS.get(provider, "API_KEY")
