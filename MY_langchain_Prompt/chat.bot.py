from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini", temperature=0.7, max_tokens=100)

chat_history = [
    SystemMessage(content="You are a helpful assistant.")]

while True:
    user_input = input("You: ")

    if user_input == "exit":
        break

    chat_history.append(HumanMessage(content=user_input))
    result= model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print(f"AI: {result.content}")

print("Exiting the chat. Goodbye!")