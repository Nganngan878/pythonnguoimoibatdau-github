try:
    file=open("data.txt","r")
    content=file.read()
except FileNotFoundError:
    print("error:Không tìm thấy file")
else:
    print("Nội dung file:",content)
    print(content)
finally:
    print("Chương trình kết thúc")
