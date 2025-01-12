from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from langserve import add_routes

from .chat import chain

app = FastAPI(
    title="A helpful chatbot",
    version="1.0",
    description="A chatbot that tries to answer user queries to the best of its knowledge."
)

add_routes(
    app=app,
    runnable=chain,
    path="/chat"
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)