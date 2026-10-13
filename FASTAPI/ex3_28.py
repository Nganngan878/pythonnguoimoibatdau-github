from fastapi import FastAPI
app = FastAPI()
@app.get("/happy",status_code=204)
def happy():
     return ":)"