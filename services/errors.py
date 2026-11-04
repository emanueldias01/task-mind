class TaskMindError(Exception):
    """Erro esperado, seguro para ser apresentado ao usuário."""


class ConfigurationError(TaskMindError):
    pass


class InputError(TaskMindError):
    pass


class CredentialError(TaskMindError):
    pass


class ServiceUnavailableError(TaskMindError):
    pass


class CommunicationError(TaskMindError):
    pass


class ResponseError(TaskMindError):
    pass
