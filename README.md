# TaskMind

O TaskMind é uma aplicação de linha de comando desenvolvida em Python que utiliza um Large Language Model (LLM) para transformar descrições informais de atividades acadêmicas em tarefas estruturadas.

O objetivo é facilitar a organização de atividades acadêmicas, extraindo informações como matéria, descrição e data de entrega a partir de textos escritos livremente pelo usuário.

## Funcionalidades

- Cadastro de tarefas por meio de descrições textuais.
- Extração estruturada de informações utilizando um LLM.
- Interpretação de datas relativas, como "amanhã" e "próxima sexta-feira".
- Listagem das tarefas cadastradas.
- Persistência local das tarefas em arquivo TXT.

## Tecnologias utilizadas

- **Python:** linguagem principal do projeto.
- **LangChain:** integração com o modelo de linguagem.
- **Pydantic:** definição e validação da estrutura das tarefas.
- **Google Gemini:** modelo de linguagem utilizado.
- **python-dotenv:** gerenciamento de variáveis de ambiente.

## Estrutura de uma tarefa

Cada tarefa é representada pelos seguintes campos:

| Campo | Descrição |
|---|---|
| `materia` | Disciplina relacionada à atividade. |
| `descricao` | Descrição da tarefa acadêmica. |
| `data` | Data de entrega, quando informada ou identificável. |

## Organização e tratamento de erros

O fluxo foi dividido em responsabilidades independentes: `main.py` captura a entrada e apresenta o resultado; `config.py` carrega e valida a configuração; `services/llm.py` prepara o prompt, chama o modelo e valida a resposta; `services/files.py` cuida da persistência; e `services/errors.py` define erros esperados.

Entradas vazias são rejeitadas antes da chamada ao modelo. Configuração ou credencial ausente, credencial inválida, indisponibilidade, falha de comunicação, timeout e resposta inesperada são convertidos em mensagens compreensíveis, sem exibir detalhes técnicos ou segredos.

## Como executar

### 1. Clonar o repositório

```bash
git clone <URL_DO_REPOSITORIO>
cd taskmind
```

### 2. Instalar as dependências

```bash
uv sync
```

O comando cria o ambiente virtual e instala as dependências declaradas no `pyproject.toml` e registradas no `uv.lock`.

### 3. Configurar as variáveis de ambiente

Copie o exemplo e configure o arquivo `.env` na raiz:

```env
cp .env.example .env
```

Edite o `.env`:

```env
MODEL=gemini-2.0-flash
PROVIDER=google_genai
GOOGLE_API_KEY=sua_chave_de_api
```

Substitua `sua_chave_de_api` por uma chave válida da API do Google Gemini.

### 4. Executar a aplicação

```bash
uv run main.py
```

## Utilização

Ao executar a aplicação, será apresentado um menu com as seguintes opções:

1. Cadastrar tarefa.
2. Listar tarefas cadastradas.
3. Sair.

Para cadastrar uma tarefa, basta descrever a atividade em linguagem natural. O modelo de linguagem interpretará o texto e retornará as informações no formato definido pela aplicação.

## Persistência dos dados

As tarefas são armazenadas localmente no arquivo `tarefas.txt`, utilizando o formato JSON Lines. Cada linha representa uma tarefa independente, permitindo adicionar novos registros sem sobrescrever os anteriores.


## OBS
- Deixarei 3 testes que fiz da ferramenta em `tarefas.txt`, os prompts mandados foram:

 1. tarefa de machine learning pra quinta valendo nota
 2. trabalho de k8s em sistemas distribuidos pra próxima semana
 3. tarefa de IHC pra entregar nesse domingo

