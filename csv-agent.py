from langchain.agents import create_csv_agent
from langchain.llms import OpenAI
import os

os.environ[ "OPENAI_API_KEY"] = "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"

agent = create_csv_agent(OpenAI(temperature=0), 'export.csv', verbose=True)

agent.run("how many rows are there?")