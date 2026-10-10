#Return the User-Agent header 
from fastapi import FastAPI, Header
app = FastAPI()
@app.get("/agent")
def greet(user_agent:str=Header()):
    return f"Hello {user_agent}?"