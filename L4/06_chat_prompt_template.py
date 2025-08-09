# we use this when we are working with list of messages and dyanamic messages

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

chat_template = ChatPromptTemplate([
    ('system', 'you are a helpful {domain} expert'),
    ('human', 'explain in simple words, what is {topic}')
])

prompt = chat_template.invoke({'domain': 'cricket', 'topic':'wicket'})

print(prompt)