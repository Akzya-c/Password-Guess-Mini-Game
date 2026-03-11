import random

def password_puzzle():
    words = ["code", "data", "loop", "hash", "byte", "node"]
    password = random.choice(words)
    attempts = 5

    print("Password Cracking Puzzle (Educational)")
    print("Hints:", len(password), "-letter lowercase word")
    print("You have", attempts, "attempts")

    while attempts > 0:
        guess = input("Enter password guess: ").lower()

        if guess == password:
            print("Access granted. Password cracked.")
            return
        else:
            correct = 0
            for i in range(min(len(password), len(guess))):
                if guess[i] == password[i]:
                    correct += 1

            print("Incorrect password")
            print("Correct letters in correct positions:", correct)

        attempts -= 1
        print("Attempts left:", attempts)

    print("Access denied. The password was:", password)

password_puzzle()
