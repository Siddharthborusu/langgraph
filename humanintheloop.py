from dotenv import load_dotenv
from langchain_groq import ChatGroq
from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain_core.tools import tool
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.checkpoint.memory import MemorySaver
from langgraph.types import interrupt, Command
load_dotenv()


# this is the human in the loop example for langgraph. It demonstrates how to use the interrupt function to pause the execution of the graph and wait for user input before resuming. The example uses a simple chatbot that can get stock prices and buy stocks based on user input. The chatbot will ask for user approval before buying stocks, and the user can approve or decline the purchase.
#  The state of the graph is saved in memory, allowing for a seamless interaction between the chatbot and the user.
# we involve human approval for a function to execute and this is an example for interacting where an approval is needed before executing a function.
# The chatbot will ask for the current price of a stock and then ask the user if they want to buy the stock at that price. The user can approve or decline the purchase, and the chatbot will respond accordingly.
#  This example demonstrates how to use the interrupt function to pause the execution of the graph and wait for user input before resuming.


class State(TypedDict):
    messages: Annotated[list, add_messages]


@tool
def get_stock_price(symbol: str) -> float:
    """Return the current price of a stock given the stock symbol"""
    return {"MSFT": 200.3, "AAPL": 100.4, "AMZN": 150.0, "RIL": 87.6}.get(symbol, 0.0)


@tool
def buy_stocks(symbol: str, quantity: int, total_price: float) -> str:
    """Buy stocks given the stock symbol and quantity"""
    decision = interrupt(
        f"Approve buying {quantity} {symbol} stocks for ${total_price:.2f}?"
    )

    if decision == "yes":
        return f"You bought {quantity} shares of {symbol} for a total price of {total_price}"
    else:
        return "Buying declined."


tools = [get_stock_price, buy_stocks]

llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0)
llm_with_tools = llm.bind_tools(tools)


def chatbot_node(state: State):
    msg = llm_with_tools.invoke(state["messages"])
    return {"messages": [msg]}


memory = MemorySaver()
builder = StateGraph(State)
builder.add_node("chatbot", chatbot_node)
builder.add_node("tools", ToolNode(tools))
builder.add_edge(START, "chatbot")
builder.add_conditional_edges("chatbot", tools_condition)
builder.add_edge("tools", "chatbot")
builder.add_edge("chatbot", END)
graph = builder.compile(checkpointer=memory)

config = {"configurable": {"thread_id": "buy_thread"}}

# Step 1: user asks price
state = graph.invoke(
    {
        "messages": [
            {"role": "user", "content": "What is the current price of 10 MSFT stocks?"}
        ]
    },
    config=config,
)
print(state["messages"][-1].content)

# Step 2: user asks to buy
state = graph.invoke(
    {"messages": [{"role": "user", "content": "Buy 10 MSFT stocks at current price."}]},
    config=config,
)
print(state.get("__interrupt__"))

decision = input("Approve (yes/no): ")
state = graph.invoke(Command(resume=decision), config=config)
print(state["messages"][-1].content)

