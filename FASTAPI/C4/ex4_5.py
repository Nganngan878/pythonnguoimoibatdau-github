from fastapi import FastAPI
import asyncio
app=FastAPI()
@app.get("/hi")
async def greet():  
    await asyncio.sleep(2)
    return "HEllo?World"