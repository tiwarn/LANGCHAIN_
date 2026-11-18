from pathlib import Path

from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

text_file = Path(__file__).with_name("cricket.txt")
loader = TextLoader(str(text_file), encoding="utf-8")

docs = loader.load()

print(docs[0].page_content)

model = ChatOpenAI(model='gpt-4o-mini', temperature=0.7)

prompt = PromptTemplate(
    template="Summarize the following text:-\n {poem}",
    input_variables=["poem"],
)

parser = StrOutputParser()

chain = prompt | model | parser

print(chain.invoke({"poem": docs[0].page_content}))



