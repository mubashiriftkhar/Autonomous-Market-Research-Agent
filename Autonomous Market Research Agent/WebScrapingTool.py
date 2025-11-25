import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
from langchain.tools import Tool
load_dotenv(dotenv_path='./.env')
tavilyApi=os.getenv("tavilyKey")


def search_web(query: str, num_results: int = 3) -> str:
    response = requests.post("https://api.tavily.com/search", json={
        "api_key": tavilyApi,
        "query": query,
        "search_depth": "basic",
        "include_answer": False,
        "max_results": num_results
    })

    results = response.json().get("results", [])
    docs = []

    for result in results:
        url = result.get("url", "")
        try:
            page = requests.get(url, timeout=5)
            soup = BeautifulSoup(page.text, "html.parser")
            text = "\n".join(p.get_text() for p in soup.find_all("p"))
            docs.append(f"URL: {url}\n{text[:1000]}")
        except Exception as e:
            continue

    return "\n\n".join(docs[:3])

# LangChain Tool wrapper
WebSearchTool = Tool(
    name="WebSearch",
    func=search_web,
    description="Use this to search the web and retrieve content about a topic."
)