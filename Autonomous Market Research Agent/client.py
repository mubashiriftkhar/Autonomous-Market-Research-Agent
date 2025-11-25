from openai import OpenAI
from tavily import TavilyClient
import os
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=os.getenv('deepseekKey'),
)


tavily_client = TavilyClient(api_key=os.getenv("tavilyKey"))