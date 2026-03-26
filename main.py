"""
UNDERSTANDING LANG-GRAPH
First: What LangGraph actually is

LangGraph (by LangChain) is a framework for building stateful, multi-step LLM workflows.

Think of it like this:

Concept	Mental Model
Function calls	One-off execution
Chains (LangChain)	Linear pipeline
LangGraph	State machine with memory + branching

Lang graph = Nodes + States + Edges

State → shared memory (dictionary)
Nodes → functions that modify state
Edges → control flow (who runs next)


"""

from typing import TypedDict
from langgraph.graph import StateGraph


# Define state -> shared memory
class State(TypedDict):
    input: str
    output: str


# define node -> function that updates state


def process_input(state: State):
    print(f"Processing input : {state['input']}")
    return {"output": state["input"].upper()}


# build graph
def build_graph():
    builder = StateGraph(State)
    builder.add_node("process", process_input)

    builder.set_entry_point("process")
    builder.set_finish_point("process")

    return builder.compile()

# RUN

def main():
    graph = build_graph()
    result = graph.invoke({'input':'hello langgraph'})
    print("Final Result", result)


if __name__ =="__main__":
    main()
