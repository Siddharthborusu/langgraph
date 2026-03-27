LangGraph 
LangGraph (by LangChain) is a framework for building stateful, multi-step LLM workflows.

--> is used for designing the shape and evolution of the state
--> is a statemachine that evolves memory through steps
--> system that moves through states


Think of it like this:

Concept	Mental Model
Function calls	One-off execution
Chains (LangChain)	Linear pipeline
LangGraph	State machine with memory + branching

Lang graph = Nodes + States + Edges

State → shared memory (dictionary)
Nodes → functions that modify state
Edges → control flow (who runs next)


** refer the images attached in the images folder regarding the the fundamentals and the mapping of the visuals

the  fundamentals are practiced in the jup notebooks to first build an intuition and understanding of the working of Langgraph
referred and followed this youtube tutorial to build an understanding of langgraph 
[video](https://www.youtube.com/watch?v=CnXdddeZ4tQ) 

state -> shared memory -> dictionary of input, output and variables
      -> holds facts and memory


node -> tasks to execute 
     -> each node is a transition
     -> each nodes changes/modifies the state

edge -> connection and the flow and order of tasks/nodes to execute
|
|__> defines the flow of execution


Langsmith -> A platform to debug, monitor, evaluate, and improve LLM applications
With Langsmith - AI becomes debuggable system ✅
A platform to debug, monitor, evaluate, and improve LLM applications


# Setup 
set up .env with the following parameters
GROQ_API_KEY = # your api key
LANGSMITH_API_KEY = # your api key
LANGSMITH_TRACING=true
LANGSMITH_ENDPOINT=https://api.smith.langchain.com
LANGSMITH_PROJECT= #project name 

one can also use the command uv sync to install all the necessary dependencies 
# Usage
To use LangGraph, you can follow the examples provided in the Jupyter notebooks. These examples demonstrate how to create nodes, define states, and connect them with edges to build complex workflows. You can also refer to the documentation for more detailed information on the available functions and features.   

# Human in the loop example
This example demonstrates how to use the interrupt function to pause the execution of the graph and wait for user input before resuming. The example uses a simple chatbot that can get stock prices and buy stocks based on user input. The chatbot will ask for user approval before buying stocks, and the user can approve or decline the purchase. The state of the graph is saved in memory, allowing for a seamless interaction between the chatbot and the user.

Refer to the humanintheloop.py file for the complete code of the example.