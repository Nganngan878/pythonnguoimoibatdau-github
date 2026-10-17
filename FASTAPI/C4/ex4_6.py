from fastapi import FastAPI
import asyncio
import uvicorn 
app=FastAPI()
@app.get("/hi")
async def greet():  
    await asyncio.sleep(5)
    return "HEllo?Wor"
if __name__=="__main__":
    uvicorn.run("ex4_6:app")