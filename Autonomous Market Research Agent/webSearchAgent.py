# agents/web_research_agent_node.py
from langgraph.graph.message import add_messages
from state import State
from client import tavily_client




def Web_Search(state:State)-> dict:
        subTasks=state["tasks"]
        searchResult={}
        for query in subTasks:
            response = tavily_client.search(query=query,search_depth='advanced',max_results=3,include_raw_content=True,time_range="year")
            rawResult=response.get('results',[])
            result=[]
            for item in rawResult:
                result.append({
                    "title": item.get("title", ""),    
                    "url": item.get("url", ""),
                    "snippet": item.get("content", "")
    })

            searchResult[query]=result    
        return {
            "messages": [{"role": "system", "content": f"Completed web search for {len(subTasks)} subtasks."}],
            "searchResults": searchResult,
        }
     



    