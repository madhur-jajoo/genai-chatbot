# This file is used to create a Google AI chatbot using the Google AI API.
from langchain_google_genai import ChatGoogleGenerativeAI

class ChatGoogleGenAI():
    def __init__(self):
        self.model = "gemini-1.5-flash"
        self.temperature = 1
        self.max_tokens = 8192
        self.top_p = 0.95
        self.top_k = 40
        self.response_mime_type = "text/plain"

    def createModel(self, model_name):
        llm = ChatGoogleGenerativeAI(
            model=model_name or self.model
        )

        return llm


if __name__=="__main__":
    chat = ChatGoogleGenAI()
    llm = chat.createModel("gemini-1.5-flash")

    messages = [
        (
            "system",
            "You are a helpful and obidient assistant.",
        ),
        (
            "human",
            "What is the capital of France?",
        )
    ]

    ai_message = llm.invoke(messages)
    print(ai_message.content)

