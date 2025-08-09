from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# HumanMessage -> msg sent by us
# AiMessage -> msg sent by AI
# SystemMessage -> start of conversation

messages = [
    SystemMessage(content='You are a helpful assistant'),
    HumanMessage(content='tell me about langchain')
]

result = model.invoke(messages)
messages.append(AIMessage(content = result.content))

print(messages)