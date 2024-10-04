import random

def main():
    game()

def game():
    number_of_guesses = 0
    random_num = random.randrange(0, 101)
    print("Python Number Guessing Game")
    print("Select a number between 1 and 100")
    while True:
        try: 
            num_prediction = int(input("Enter your guess: "))
            number_of_guesses += 1
        except ValueError:
            print("Enter a valid number")
            break
        if num_prediction > 100 or num_prediction < 0:
            print("Enter a number in range of 0-100")
        elif num_prediction > random_num:
            print("Too high. Try again")
        elif num_prediction < random_num:
            print("Too low. Try again.")
        else:
            print(f"CORRECT! The answer was {random_num}")
            print(f"Number of guesses: {number_of_guesses} ")
            break
        
if __name__ == "__main__":
    main()