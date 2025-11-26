from langchain_openai import ChatOpenAI
from tavily import TavilyClient
import os
from dotenv import load_dotenv
load_dotenv()

llm = ChatOpenAI(
  base_url="https://openrouter.ai/api/v1",
  model="openrouter/bert-nebulon-alpha",
  api_key=os.getenv('OpenRouterKey'),
)

tavily_client = TavilyClient(api_key=os.getenv("tavilyKey"))
