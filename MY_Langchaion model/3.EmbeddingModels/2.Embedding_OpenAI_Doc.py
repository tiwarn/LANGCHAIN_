from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

embeddings = OpenAIEmbeddings(model = 'text-embedding-3-large', dimensions = 32)

documents = ['Hello world', 'This is a test document.', 'LangChain is awesome!']


result = embeddings.embed_documents(documents)

print(str(result))