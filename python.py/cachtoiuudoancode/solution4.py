# thiết kế và tối ưu hóa code
guess=1
while True:
    num=input("Please enter a number(between 1 and 100): ")
    try:
        num=int(num)
    except:
        print("Invalid number,please guess again.")
        continue
    if num <45:
        print("Your guess was under")
    elif num >45:
        print("Your guess was over")
    else:
        break
    guess+=1
print(f"Congratulations! You guessed the number in {guess} tries.")