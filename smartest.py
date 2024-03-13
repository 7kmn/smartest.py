import random

def main():
    # Generate a random number between 1 and 10
    random_number = random.randint(1, 10)
    
    # Print the prompt
    print("Think of a number between 1 and 10.")
    
    # Print the randomly generated number
    print("The randomly generated number is:", random_number)
    
    # Ask the user to input their guessed number
    guessed_number = input("Enter your guessed number: ")
    print("You guessed:", guessed_number)

if __name__ == "__main__":
    main()
