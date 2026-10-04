class GuessNumber:
    def __init__(self,number ,min=0,max=100):
        self.number=number
        self.guess=0
        self.min=min
        self.max=max
    def get_guess(self):
        guess=input(f"Please enter a number(between {self.min} - {self.max}): ")
        if self.valid_number(guess):
            return int(guess)
        else:
            print("Plea enter a valid number.")
            return self.get_guess()
    def valid_number(self,str_number):
        try:
            number=int(str_number)
        except:
            return False
        return self.min<=number<=self.max
    def play(self):
        while True:
            self.guess +=1
            guess= self.get_guess()
            if guess<self.number:
                print("Your guess was under")
            elif guess>self.number:
                print("Your guess was over")
            else:
                print(f"Congratulations! You guessed the number in {self.guess} guesses.")
                break
        print(f"Congratulations! You guessed the number in {self.guess} guesses.")
game=GuessNumber(45,min=1,max=100)
game.play()
game=GuessNumber(45,23,67)
game.play()