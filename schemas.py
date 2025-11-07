from dataclasses import field
from typing import List
from pydantic import BaseModel, Field #BaseModel is the core pydantic calass that we're going to ingerit from in order to create our own data models and data objects.
                                      #when we create the class that is going to ingerit from the BaseModel we get automatic validations, serilization and deserialization, jsom and auto completion of the data.
                                      # field is functino that lets us add extra validations metadata to our model attributes. we can set constraints like minimum length, maximum length, regex, description, default value, etc.
from pydantic_core import Url

class source(BaseModel):
    """schema for a source used by a agent"""
    Url: str = Field(description="The url of the source")

class AgentResponse(BaseModel):
    """schema for a response from a agent"""
    answer: str = Field(description="The agent answer to the question")
    sources: List[source] = Field(
        default_factory=list, description="List of sources useed to generate the answer"
    )