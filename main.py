from unittest import result
from dotenv import load_dotenv
from langchain import hub
from langchain.agents import AgentExecutor, agent, create_react_agent
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch


load_dotenv()


tools = [TavilySearch()]
llm = ChatOpenAI(model="gpt-4")
react_prompt = hub.pull("hwchase17/react")
agent = create_react_agent(llm, tools, prompt=react_prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
chain = agent_executor


def main():
    result = chain.invoke(
        input={
            "input": "Search for 2 job postings for an AI engineer using langchain openai, ollama on linkedin in india and list their details"
        }
    )
    print(result)

if __name__ == "__main__":
    main()
