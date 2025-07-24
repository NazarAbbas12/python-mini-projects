import random

while True:
    user_answer = input("Do you want to guess?(Y/N)").strip()

    if user_answer.lower() == 'y':

        user_choise = input("Guess the number\nFrom 0 to 9").strip()

        if user_choise.isdigit():

            user_choise = int(user_choise)
            computer_choise = random.randint(0, 9)

            if 0 <= user_choise <= 9:
                if user_choise == computer_choise:
                    print(
                        f"Congratulations!!\nYou guessed correctly:{user_choise}")
                else:
                    print(
                        f"You guessed:{user_choise}\nComputer guessed:{computer_choise}")
            else:
                print("Guess number from 0 to 9")
                continue
        else:
            print("Enter any digit from 0 to 9")
            print(f"You typed: {user_choise} ❌ Not a digit.")
            continue

    elif user_answer.lower() == 'n':
        print("Thanks for playing")
        break
    else:
        print("Wrong selection!")
        continue
