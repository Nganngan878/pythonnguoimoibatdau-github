try:
    age=int(input("Enter age:"))
    if age <0:
        raise ValueError("Age cannot be negative")
except ValueError as e:
    print("error:",e)
else:
    if age >=18:
        print("You are an adult")
    else:
        print("You are a minor")
finally:
    print("Program ended")