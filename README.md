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



