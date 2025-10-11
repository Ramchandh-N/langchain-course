from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
load_dotenv()


def main():
    print("Hello from langchain-course!")
    information = """Workday is a cloud-based software vendor that provides enterprise cloud applications for financial management and human resources, helping organizations manage finances, HR, planning, and analytics. Founded in 2005 by former PeopleSoft executives, Workday uses artificial intelligence and machine learning to help companies automate tasks, gain real-time insights, and adapt to change. The company's applications are designed to unify business processes, with services including talent management, payroll, and procurement. Cloud-based platform: Workday delivers its applications over the internet, which allows for quick implementation and continuous updates. 
Core applications: It offers a unified suite of cloud-based applications for financial management and human capital management (HCM), which includes services like payroll, recruiting, and talent management. 
AI and machine learning: The platform is built with AI and machine learning at its core to help automate tasks, provide predictive insights, and improve efficiency. 
Real-time data: By combining transactional and analytical data in a single system, Workday provides businesses with real-time insights for better decision-making. 
Founded in 2005: The company was founded by Dave Duffield and Aneel Bhusri, who previously founded the ERP company PeopleSoft. """

    summary_template = """ 
   given the following information: {information} about a company, i want you to create:
   1. a summary of the company
   2. Two key facts about the company
   """
    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)


    llm = ChatOpenAI(temperature=0,model="gpt-4o")
    # llm = ChatOllama(temperature=0,model="gemma3:270m")
    chain = summary_prompt_template | llm

    response = chain.invoke({"information": information})
    print(response.content)


if __name__ == "__main__":
    main()
