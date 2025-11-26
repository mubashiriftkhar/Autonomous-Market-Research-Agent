from state import State
from client import llm
import json




def summarizeResult(state:State)->dict:

    print("Summary Agent Started")
    
    search_results=state["searchResults"]
    query=state["query"]
    prompt=f"""
    "You are an expert Autonomous Market Research Agent.\n"
    "Your task is to summarize the context and extract usefull insights from it and create proper human readable report in raw html.\n"
    "If there are insights available then create proper charts and report of it in inline html.\n"
    "You must use ONLY the provided context to answer the user query.\n"
    "If the answer is not present in the context, respond with:\n"
    "'The provided context does not contain any relevant information.'\n\n"
    
    "Think step-by-step using the following reasoning process:\n"
    "1. Carefully read the user query.\n"
    "2. Analyze the context to find relevant sections that may contain the answer.\n"
    "3. If relevant information is found, extract and summarize the key insights.\n"
    "4. Present the final answer in a well-structured, inline html format.\n"
    "5. Include helpful resource links (from the provided list) that support your answer.\n"
    "6. If the answer is not found in the context, clearly say it is not available.\n"
    "7. Use Proper inline HTML Tags but do not use any kind of style or css or javascript.\n"
    "8. Do not start with ```html and end with ``` just generate required response
  

This is the context. Use this and follow the above reasoning process to answer the user query:
--- START OF CONTEXT ---
{search_results}
--- END OF CONTEXT ---
User Query:
{query}
Now provide the structured HTML output (no explanation, just inline HTML):
"""

    response=llm.invoke(prompt)

    state["summarizeResult"]=response.content
    print(state["summarizeResult"])
    with open("hydrogenVehicals.json", "w", encoding="utf-8") as f:
               json.dump(state, f, indent=4, ensure_ascii=False)
    print("Summary Agent Ended")

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
#       "timeInterval":'2020-2025',                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
#     }    
# with open("hydrogenVehicals.json","r") as file:
#     test_state=json.load(file)
# print(test_state)    
# results=summarizeResult(test_state)
# print(results)
# print(results["summarizedResult"])
    
# with open("answer.json","w") as file:
#     json.dump(results, file, indent=4, ensure_ascii=False)
