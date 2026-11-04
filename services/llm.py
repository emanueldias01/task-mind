from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os

load_dotenv()

MODEL = os.getenv("MODEL")
PROVIDER = os.getenv("PROVIDER")


model = init_chat_model(
    model=MODEL,
    model_provider=PROVIDER,
)