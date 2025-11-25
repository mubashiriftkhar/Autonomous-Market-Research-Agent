# from langgraph.graph.message import add_messages
import ast
from state import State
from client import client


def taskPlannerNode(state:State)-> dict:
    userQuery = state['messages'][-1]['content']
    completion = client.chat.completions.create(
    extra_body={},
    model="mistralai/mistral-7b-instruct:free",
    messages=[
       {
  "role": "system",
  "content": (
   """
You are an expert Autonomous Market Research Planner Agent.
Your role is to deeply analyze the given query and construct a well-structured, diverse research plan.
We have three agents to work on user Query Finance Agent, Social Agent, Web Agent You have to assign task to these three agent that what these should do.
Think step-by-step:
1. First, carefully read the query and understand the user's real research need.
2. Look for time interval and country where user want to search and which time interval user wants
3. Identify the core topic and related subtopics.
4. Extract the following fields from the query:
   - intent (choose exactly one from: trend_analysis, competitor_comparison, pricing, sentiment_analysis)
   - brands (list of strings)
   - products (list of strings)
   - dates (tuple of start year and end year in "year-year" format)
   - locations (list of strings)
   - keywords (important words such as product names and country/place names)
5. Based on these extracted details, decide where to get the information like social media platform or other and wirte name of that platform and Write it in a Python dictionary, write atleast 5 platform


Finally:
- Respond ONLY with a valid Python dictionary.
- Do not include your reasoning or intermediate steps in the final output.
- The dict should be directly usable as Python code.

"""
  )
},
{
  "role": "user",
  "content": f"Query: {userQuery}"
}
    ]
    )
    reply = completion.choices[0].message.content
    
    try:
        subTasks = ast.literal_eval(reply)
    except Exception:
        subTasks = [reply]
    state['tasks']=subTasks
    return state
 
   
test_state = {
        "messages": [
            {"role": "user", "content": "What is the market size of Electric Vehical in USA?"}
        ],
        "tasks": []
    }
result=taskPlannerNode(test_state)
print(result)