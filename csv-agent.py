from langchain.agents import create_csv_agent
from langchain.llms import OpenAI
import os

os.environ[ "OPENAI_API_KEY"] = "*************"

agent = create_csv_agent(OpenAI(temperature=0), 'export.csv', verbose=True)

agent.run("how many rows are there?")