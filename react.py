from dotenv import load_dotenv
from langchain_core.tools import tool   # this will help us to create a tool for the agent
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

load_dotenv()

@tool
def triple(num:float) -> float:
    """
    param num: a number to be tripled
    returns: the triple of the input number
    """
    return num * 3

tools = [TavilySearch(max_results=1), triple] #tavily search has already has the description of the tool so we don't need to add it here

