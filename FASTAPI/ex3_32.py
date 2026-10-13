import datetime
import json

import pytest
from fastapi import FastAPI, Response
from fastapi.encoders import jsonable_encoder


@pytest.fixture
def data():
    return datetime.datetime.now()


def test_json_dump(data):
    with pytest.raises(Exception):
        _ = json.dumps(data)


def test_encoder(data):
    out = jsonable_encoder(data)
import datetime
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app = FastAPI()


# Khởi tạo một Pydantic model có chứa trường thời gian (datetime)
class Article(BaseModel):
  title: str
  published_at: datetime.datetime


@app.get("/article")
def get_article():
  # Tạo dữ liệu mẫu với thời gian hiện tại
  my_article = Article(
      title="Học FastAPI cùng Ngân", published_at=datetime.datetime.now()
  )

  # Dùng jsonable_encoder để chuyển đổi đối tượng phức tạp thành cấu trúc tương thích với JSON
  safe_data = jsonable_encoder(my_article)

  return {
      "status": "success",
      "message": "Đã chuyển đổi datetime thành công nhờ jsonable_encoder!",
      "data": safe_data,
  }