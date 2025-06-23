import random
def guessing_the_number():
    guessed_number=random.randint(1,100)
    attempts=0
    print("welcome to number guessing game... :)")
    while True:
        try:
            guess=int(input("guess the number"))
            attempts+=1
            if guess<1 or guess>100:
                print("please enter the numbers of range 1 and 100")
            elif guess<guessed_number:
                print("increase your guess to reach the number")
            elif guess>guessed_number:
                print("decrease the guess to reach the number")
            else:
                print(f"congratulations!!!! you won the game. your guess is correct. you guessed the number in {attempts} attempts..")
                break
        except ValueError:
            print("!!! please enter a valid number")
guessing_the_number()
    
