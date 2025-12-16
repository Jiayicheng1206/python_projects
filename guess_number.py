import random

print("Welcome to number guess!")

while True:
    secret = random.randint(1, 100)
    print("I have a number in 1~100, please guess!")
    print('(If you want to cheat pls input "c", \nif you want to quit pls input "q" )')
    attempts = 0
    quit_flag = False
    while True:

        guess_str = input("Please input:")

        if guess_str.lower() == "q":
            quit_flag = True
            break
        elif guess_str.lower() == "c":
            print("The answer is:", secret)
            continue
        try:
            guess = int(guess_str)
            attempts += 1
        except ValueError:
            print("Please enter a valid input!")
            continue
        
        if guess < secret:
            print("too small!")
        elif guess > secret:
            print("too big!")
        else:
            print("you are right!!!")
            print("you guessed", attempts, "times!")
            break
    
    if quit_flag:
        break

    play_again = input("Do you want to play again? pls enter (y/n): ")
    if play_again.lower() == "n":
        break
    elif play_again.lower() == "y":
        print("Start a new game:")
        continue

print("You quit, see you next time!")
