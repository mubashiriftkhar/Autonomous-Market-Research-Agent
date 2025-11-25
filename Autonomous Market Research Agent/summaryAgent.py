from state import State
from client import client
import json




def summarizeResult(state:State)->dict:

    snippets= []
    urls = []
    search_results=state["searchResults"]
# Assuming only one key in searchResults, get its list of results
    for results in search_results.values():
        for item in results:
            snippet = item.get("snippet", "")
            url = item.get("url", "")
            if snippet:
                snippets.append(snippet)
            if url:
                urls.append(url)
    completion = client.chat.completions.create(
    extra_body={},
    model="mistralai/mistral-7b-instruct:free",
    messages=[
       {
  "role": "system",
  "content": (
    "You are an expert Autonomous Market Research Agent.\n"
    "Your task is to summarize the context and extract usefull insights from it and create proper human readable report in raw html.\n"
    "If there are insights available then create proper charts and report of it in raw html.\n"
    "You must use ONLY the provided context to answer the user query.\n"
    "If the answer is not present in the context, respond with:\n"
    "'The provided context does not contain any relevant information.'\n\n"
    
    "Think step-by-step using the following reasoning process:\n"
    "1. Carefully read the user query.\n"
    "2. Analyze the context to find relevant sections that may contain the answer.\n"
    "3. If relevant information is found, extract and summarize the key insights.\n"
    "4. Present the final answer in a well-structured, readable paragraph format (not bullet points or one-liners).\n"
    "5. Include helpful resource links (from the provided list) that support your answer.\n"
    "6. If the answer is not found in the context, clearly say it is not available.\n"
  )
},
{
  "role": "system",
  "content": f"""
This is the context. Use this and follow the above reasoning process to answer the user query:
--- START OF CONTEXT ---
{snippets}
--- END OF CONTEXT ---

User Query:
{state['originalQuery']}

These are the links to use if they support your answer:
{urls}

Now provide the structured HTML output (no explanation, just raw HTML):
"""
}
    ]
    )

    summary=completion.choices[0].message.content
    return {
        "summarizedResult": summary
    }
    



# with open("answer.json","r") as file:
#     test_state=json.load(file)
# # print(test_state)    
# print(summarizeResult(test_state))
    
