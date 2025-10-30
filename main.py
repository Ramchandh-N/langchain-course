from unittest import result

from dotenv import load_dotenv
from langchain import hub #designed for sharing and exploring prompts,chains,agents,created by the community.
from langchain.agents import agent, create_react_agent, AgentExecutor# is going to be the runtime of the agent, its generally a for loop.
# from langchain_classics.agents import AgentExecutor
from langchain_core import output_parsers
from langchain_openai import ChatOpenAI
# from langchain_ollama import Ollama
from langchain_tavily import TavilySearch
# from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda #this is a part of langchain expression language that allows us to compose and chain together different components of langchain.

#importing schemas and prompts from the schemas.py and prompt.py files.
from schemas import AgentResponse
from prompt import REACT_PROMPT_WITH_FORMAT_INSTRUCTIONS
load_dotenv()


tools = [TavilySearch()]   #lc toola is component that allows the llm's to interact with the external utilities.
llm = ChatOpenAI(model="gpt-4")
structured_llm = llm.with_structured_output(AgentResponse)
# llm = Ollama(model="llama3.2")
# react_prompt = hub.pull("hwchase17/react")

# output_parsers = PydanticOutputParser(pydantic_object=AgentResponse) #this is a part of langchain expression language that allows us to parse the output of the agent into a pydantic object.

react_prompt_with_format_instructions = PromptTemplate(
     template= REACT_PROMPT_WITH_FORMAT_INSTRUCTIONS,
     input_variables=["input", "agent_scratchpad", "tool_names"]
      ).partial(format_instructions="")

agent = create_react_agent(llm=llm, tools=tools, prompt=react_prompt_with_format_instructions, ) #create a reasoning agent that can use the tools to answer the question. reasoning chain.
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True) #runtime of the agent, its generally a for loop.
extract_output = RunnableLambda(lambda x: x.get("output"))
# parse_output = RunnableLambda(lambda x: output_parsers.parse(x))
chain = agent_executor | extract_output | structured_llm #structured_llm is a part of langchain expression language that allows us to parse the output of the agent into a pydantic object.


def main():
    print("hello from main function")
    result = chain.invoke(
        input={
            "input": "Search of 3 job postings for an ai engineer using langchain in the india on linkedin and list their details"
        }
    )
    print(result) #this is dictionary contains answer and sources that we specified in the schema.py file.


if __name__ == "__main__":
    main()
