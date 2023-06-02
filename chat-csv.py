import os
from langchain.document_loaders import CSVLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI



os.environ[ "OPENAI_API_KEY"] = "**************I"
# Load the documents
loader = CSVLoader(file_path='Pokemon_full.csv')
# Create an index using the loaded documents
index_creator = VectorstoreIndexCreator()
docsearch = index_creator.from_loaders([loader])
# Create a question-answering chain using the index
chain = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="stuff", 
        retriever=docsearch.vectorstore.as_retriever(), input_key="question")
# Pass a query to the chain
query = "how many shipments in Shanghai?"
response = chain({"question": query})
print(response)
query = "how many shipments are using the Mode: Air?"
response = chain ({"question": query})
print(response)
## RESPONSE:
#{'question': 'what is charizard stats', 'result': Charizard has a Pokedex ID of 6, a height of 17, weight of 905, a type of Fire and a secundary type of Flying. Its HP is 78, attack is 84, defense is 78, Sp Atk is 109, Sp Def is 85 and speed is 100. '}
#{'question': 'what is magikarp health', 'result': ' Magikarp has 20 HP. ')