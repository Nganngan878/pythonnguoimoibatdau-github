from fastapi import FastAPI, Response

app = FastAPI()


@app.get("/happy", status_code=204)
def happy(response: Response):
  return