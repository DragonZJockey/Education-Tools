import time
import gameproject

def start_game_history():
    print("Welcome to Historical Quest!")
    time.sleep(1)
    print("Your goal is to navigate through different historical periods and make the right choices to succeed.")
    time.sleep(1)
    first_choice()

def first_choice():
    print("\nYou find yourself in ancient Egypt. You see the construction of a pyramid in progress.")
    time.sleep(1)
    print("1. Help with the construction.")
    print("2. Explore the nearby village.")
    choice = input("Enter 1 or 2: ")
    
    if choice == '1':
        pyramid_construction()
    elif choice == '2':
        explore_village()
    else:
        print("Invalid choice. Please try again.")
        first_choice()

def pyramid_construction():
    print("\nYou start helping with the pyramid construction.")
    print("A worker asks you a question to see if you're knowledgeable enough to help.")
    print("What is the name of the Pharaoh who built the Great Pyramid of Giza?")
    answer = input("Your answer: ")
    
    if answer.lower() == "khufu":
        print("Correct! You gain the trust of the workers and learn about the construction techniques.")
        second_choice()
    else:
        print("Incorrect. The correct answer is Khufu. You are not allowed to help further.")
        first_choice()

def explore_village():
    print("\nYou explore the nearby village and meet a merchant.")
    print("The merchant offers you a riddle to solve for a reward.")
    print("Riddle: I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?")
    answer = input("Your answer: ")
    
    if answer.lower() == "echo":
        print("Correct! The merchant gives you a map to a hidden treasure.")
        second_choice()
    else:
        print("Incorrect. The correct answer is Echo. The merchant walks away.")
        first_choice()

def second_choice():
    print("\nYou now have a choice to make:")
    print("1. Travel to ancient Greece.")
    print("2. Travel to medieval Europe.")
    
    choice = input("Enter 1 or 2: ")
    
    if choice == '1':
        ancient_greece()
    elif choice == '2':
        medieval_europe()
    else:
        print("Invalid choice. Please try again.")
        second_choice()

def ancient_greece():
    print("\nYou arrive in ancient Greece during the time of the first Olympic Games.")
    print("You are asked to participate in a philosophical debate. Who is considered the father of Western philosophy?")
    answer = input("Your answer: ")
    
    if answer.lower() == "socrates":
        print("Correct! You impress the Greeks with your knowledge and gain their respect.")
        end_game()
    else:
        print("Incorrect. The correct answer is Socrates. You are not allowed to participate in the debate.")
        second_choice()

def medieval_europe():
    print("\nYou arrive in medieval Europe during the time of the Black Death.")
    print("You need to find a way to protect yourself. What common medieval remedy was believed to prevent the plague?")
    answer = input("Your answer: ")
    
    if answer.lower() == "garlic":
        print("Correct! You use garlic to protect yourself and survive the plague.")
        end_game()
    else:
        print("Incorrect. The correct answer is garlic. You fall ill to the plague.")
        second_choice()

def end_game():
    print("\nCongratulations! You have successfully navigated through different historical periods and made the right choices.")
    print("You have expanded your knowledge of math! Go try other subjects")
    gameproject.start_game()
    time.sleep(1)

if __name__ == "__main__":
    start_game_history()