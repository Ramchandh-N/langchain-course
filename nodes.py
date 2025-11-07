from dotenv import load_dotenv
from langgraph.graph import \
    MessagesState  # this will help us to store the messages in the graph, list of messages will be stored in the state
from langgraph.prebuilt import \
    ToolNode  # This is a node to execute the tools, its going to check the last message between agent and human and if the last meessage is an ai message that has a value tool call its going to exexute the tooll call assuming that the tool call is initated by the tool node.
from react import llm, reasoning_agent, tools

load_dotenv()

SYSTEM_MESSAGE = """
You are a helpful assistant that can use the following tools to answer questions and help the user.
"""

def run_agent_reasoning(state: MessagesState) -> MessagesState: #its a dictionary of messages
    """
    This function is used to run the reasoning agent.
    """
    response = reasoning_agent.invoke([{"role": "system", "content": SYSTEM_MESSAGE}, *state["messages"]])
    return {"messages": [response]}

tool_node = ToolNode(tools)