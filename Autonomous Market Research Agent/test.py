from planneragent import taskPlannerNode
from webSearchAgent import Web_Search
from summaryAgent import summarizeResult
# from htmlAgent import htmlConverterAgent
import json
# from pprint import pprint
# Sample input for planner node
import time
start_time = time.time()
initial_state = {
        "messages": [{"role": "user", "content": "AI tools SEO 2025"}],
        "tasks": ["Electric Vehicle Market Size USA",
"Electric Vehicle Market Size USA",
"Electric Vehicle Sales USA 2021 trends and growth analysis",
"Electric Vehicle Brands USA top competitors comparison",
]  ,
 'originalQuery':"What is the market size of Electric Vehical in USA?"
    }

    # 1. Test Planner Node
# planner_output = taskPlannerNode(initial_state)
# print(planner_output)

    # 2. Prepare state for Web Search Node
web_search_state = {
        "messages": initial_state["messages"],
        "tasks": initial_state.get("tasks", []),
        "searchResults": {},
        "originalQuery":initial_state.get("originalQuery","")
    }

    # 3. Test Web Search Node
web_search_output = Web_Search(web_search_state)
summarized_result=summarizeResult(web_search_output)
# htmlResponse=htmlConverterAgent(summarized_result)
# pprint(web_search_output)
end_time = time.time()

elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.2f} seconds")

file_path = "answer.json"
with open(file_path, "w") as json_file:
     json.dump(web_search_output, json_file, indent=4)
