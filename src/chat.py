import os

from langchain import hub

from GoogleAI.chat_google import ChatGoogleGenAI

chat = ChatGoogleGenAI()

llm = chat.createModel(
    model_name=os.getenv("GENAI_MODEL_NAME")
)

prompt = hub.pull(owner_repo_commit=os.getenv("PROMPT_NAME"))

chain = prompt | llm