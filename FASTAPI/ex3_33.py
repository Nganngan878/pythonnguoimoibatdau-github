from datetime import datetime
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class TagIn(BaseModel):
  tag: str


class Tag(BaseModel):
  tag: str
  created: datetime
  secret: str


class TagOut(BaseModel):
  tag: str
  created: datetime
@app.get("/tag", response_model=TagOut)
def get_tag():
  return Tag(
      tag="fastapi-tutorial",
      created=datetime.now(),
      secret="TOP_SECRET_12345",
  )