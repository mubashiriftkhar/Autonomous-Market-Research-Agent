from langgraph.graph import StateGraph
from planneragent import taskPlannerNode
from webSearchAgent import Web_Search
from summaryAgent import summarizeResult
from htmlAgent import htmlConverterAgent
from state import State
import time
start_time = time.time()
graphBuilder=StateGraph(State)    


graphBuilder.add_node("PlannerNode",taskPlannerNode)
graphBuilder.add_node("WebSearchNode",Web_Search)
graphBuilder.add_node("SummarizerNode",summarizeResult)
# graphBuilder.add_node("HTMLNode",htmlConverterAgent)

graphBuilder.set_entry_point("PlannerNode")
graphBuilder.add_edge("PlannerNode","WebSearchNode")
graphBuilder.add_edge("WebSearchNode","SummarizerNode")
# graphBuilder.add_edge("SummarizerNode","HTMLNode")
graphBuilder.set_finish_point("SummarizerNode")


graph=graphBuilder.compile()
input_state = {
    "messages": [
        {"role": "user", "content": "What is the market size of Electric Vehical in USA?"}
    ],
    "tasks": [],
    "searchResults": {},
    "originalQuery": "",
    "summarizedResult": "",
}

answer=graph.invoke(input=input_state)
print(answer['summarizedResult'])
end_time = time.time()

elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.2f} seconds")
# with open("graph2.png", "wb") as f:
#     f.write(graph.get_graph().draw_mermaid_png())