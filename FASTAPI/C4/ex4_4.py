import asyncio


async def q():
  print("Why can't programmers tell jokes?")
  await asyncio.sleep(10)  # Nhường quyền, không chặn luồng trong lúc chờ


async def a():
  print("Timing!")


async def main():
  # Chạy đồng thời cả q() và a() thông qua asyncio.gather
  await asyncio.gather(q(), a())


if __name__ == "__main__":
  # Khởi chạy vòng lặp sự kiện asyncio
  asyncio.run(main())