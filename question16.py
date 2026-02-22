import random

def question16():
    best_score = None  # Track minimum attempts

    while True:
        number = random.randint(1, 100)
        attempts = 7
        print("\nI have selected a number between 1 and 100. You have 7 attempts!")

        for attempt in range(1, attempts + 1):
            guess = int(input(f"Attempt {attempt}: Enter your guess: "))

            if guess == number:
                print(f"Congratulations! You guessed it in {attempt} attempts.")
                if best_score is None or attempt < best_score:
                    best_score = attempt
                    print(f"New best score: {best_score} attempts!")
                break
            elif guess < number:
                print("Too low!", end='')
            else:
                print("Too high!", end='')

                #Hint if close (within 5)
            if abs(guess - number) <= 5 and guess != number:
                print(" You're very close!", end='')
            print(f"Attempts remaining: {attempts - attempt}")
        else:
            print(f"You failed! The number was {number}.")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            if best_score:
                print(f"Your best score was {best_score} attempts.")
            break
# Run the game

question16()
        

        
            

        