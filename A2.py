# 1) user input => low and bound *
# 2) random => [a, b] *
# 3) loop => condition=> guess_count=5 => feedback *
import random

try:
    low = int(input("Enter lower bound: \n"))
    high = int(input("Enter high bound: \n"))
except:
    print("please enter a valid number")


r = random.randint(low, high)

guess_count = 5

while guess_count > 0:

    try:
        new_guess_str = input(f"remained guess: {guess_count} => Enter your next guess: \n")
        new_guess = int(new_guess_str)
        if r == new_guess:
            print("great! yuor guess is correct!")
            break
        elif r > new_guess:
            print("your guess is lower than the number")
        else:
            print("your guess is higher than the number")

        guess_count -= 1
    except:
        print("please enter a valid number")
        
   