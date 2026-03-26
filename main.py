"""

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
