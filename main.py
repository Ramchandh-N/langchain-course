from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.agents.structured_output import ProviderStrategy
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

# importing schemas from the schemas.py file
from schemas import AgentResponse

load_dotenv()


# Define tools - TavilySearch allows the agent to search the web
tools = [TavilySearch()]

# Create the LLM model
model = ChatOpenAI(model="gpt-4")

# System prompt for the agent - defines how the agent should behave
system_prompt = """Answer the following questions as best you can. You have access to search tools.

Use the following approach:
1. Think about what information you need
2. Use the available tools to gather information
3. Synthesize the information into a comprehensive answer
4. Include relevant sources in your response

Be thorough and provide detailed answers with proper source attribution."""

# Create the agent using the new create_agent interface
# - Uses ProviderStrategy for structured output (OpenAI's native structured output)
# - Automatically handles the ReAct loop (Reasoning + Acting)
# - No need for separate AgentExecutor or manual chaining
agent = create_agent(
    model=model,
    tools=tools,
    system_prompt=system_prompt,
    response_format=ProviderStrategy(AgentResponse)
)


def main():
    print("Hello from main function")
    
    # Invoke the agent with a message
    # The new interface uses a messages-based format
    result = agent.invoke({
        "messages": [{
            "role": "user",
            "content": "Search for 3 job postings for an AI engineer using langchain in India on LinkedIn and list their details"
        }]
    })
    
    # The structured response (AgentResponse) is in result["structured_response"]
    structured_response = result.get("structured_response")
    
    if structured_response:
        print("\n=== Agent Response ===")
        print(f"Answer: {structured_response.answer}")
        print(f"\nSources ({len(structured_response.sources)}):")
        for i, source in enumerate(structured_response.sources, 1):
            print(f"  {i}. {source.Url}")
    else:
        print("\n=== Full Result ===")
        print(result)


if __name__ == "__main__":
    main()
