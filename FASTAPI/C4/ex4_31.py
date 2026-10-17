import time


def q():
  print("Why can't programmers tell jokes?")
  time.sleep(3)  # Dùng time.sleep chuẩn của Python, làm nghẽn toàn bộ luồng


def a():
  print("Timing!")


def main():
  q()
  a()


if __name__ == "__main__":
  main()