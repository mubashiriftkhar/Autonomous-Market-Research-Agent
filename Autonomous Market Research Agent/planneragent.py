from state import State
from client import llm
from pydantic import BaseModel
from typing import List
import json
class TaskList(BaseModel):
    tasks:List[str]

def taskPlannerNode(state:State)-> dict:
    print("Planner Agent Started")
    userQuery = state["query"]
    prompt= f"""
    query:{userQuery}
You are an expert Autonomous Market Research Planner Agent.
Your role is to deeply analyze the given query and construct a well-structured, diverse research plan.
We have to give these queries to Web Search agent to work on.
Think step-by-step:
1. First, carefully read the query and understand the user's real research need.
2. Look for time interval and country where user want to search and which time interval user wants
3. Identify the core topic and related subtopics.
4. Extract the following fields from the query:
   - intent (choose exactly one from: trend_analysis, competitor_comparison, pricing, sentiment_analysis)
   - brands (list of strings)
   - products (list of strings)
   - dates (tuple of start year and end year in "year-year" format) If Date is not in Query then add relevent date by yourself but if available then use given date.
   - locations (list of strings)
   - keywords (important words such as product names and country/place names)
5. Generate Atleast 5 to 7 Sub Queries.


Finally:

- Respond ONLY with a valid Python List.
- Do not include your reasoning or intermediate steps in the final output.
- The List should be directly usable as Python code.

"""
    structuredLLm=llm.with_structured_output(schema=TaskList)
    response=structuredLLm.invoke(prompt)

    
    state["tasks"] = response.tasks
    with open("hydrogenVehicals.json", "w", encoding="utf-8") as f:
               json.dump(state, f, indent=4, ensure_ascii=False)
    print("Planner Agent Ended")

    return state
 
   
# test_state = {
#         "messages": [
#             {"role": "user", "content": "What is the AI in healthcare market size in the United States from 2020–2025?"}
#         ],
#         "tasks": []
#     }
# result=taskPlannerNode(test_state)
# print(result)
