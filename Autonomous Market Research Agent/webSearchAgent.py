# agents/web_research_agent_node.py
from state import State
from client import tavily_client
import json



def Web_Search(state:State)-> dict:
        print("Web Agent Started")
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
        state["searchResults"]=searchResult
        with open("hydrogenVehicals.json", "w", encoding="utf-8") as f:
               json.dump(state, f, indent=4, ensure_ascii=False)
        print("Web Agent Started")
        return state       
        

# test_state = {
#         "messages": [
#             {"role": "user", "content": "What is the market size of Electric Vehical in USA?"}
#         ],
#         "tasks": [
#       "Identify the current market size and growth rate of the global electric vehicle (EV) market from 2020 to 2025, focusing on key regions such as North America, Europe, and Asia-Pacific.",
#       "Analyze the market share of leading electric vehicle manufacturers (e.g., Tesla, BYD, Volkswagen, Nissan, and BMW) in the specified regions for the years 2020-2023.",
#       "Investigate the adoption trends of electric vehicles in major countries (e.g., U.S., China, Germany, Norway, and Japan) and highlight factors driving or hindering growth in these markets.",
#       "Examine the impact of government policies, subsidies, and regulations on the electric vehicle market in the U.S., China, and the European Union during 2020-2023.",
#       "Compare the pricing strategies of top electric vehicle models (e.g., Tesla Model 3, BYD Han, Volkswagen ID.4, Nissan Leaf) across different regions and analyze consumer price sensitivity.",
#       "Explore consumer sentiment and preferences toward electric vehicles in 2023, including concerns about charging infrastructure, battery life, and environmental benefits.",
#       "Assess the role of technological advancements (e.g., battery technology, autonomous driving) in shaping the future of the electric vehicle market and their projected impact by 2025."
#       ],
#       "timeInterval":'2020-2025'
#     }    
# results=Web_Search(state=test_state)
# print(results)


    
