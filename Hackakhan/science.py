import time
import gameproject

def start_game_science():
    print("Welcome to the Scientific Adventure")
    time.sleep(1)
    print("Your goal is to navigate through different scientific topics and answer correctly to succeed.")
    time.sleep(1)
    physics_challenge()

def physics_challenge():
    print("\nYou encounter a physics puzzle:")
    time.sleep(1)
    print("What is the acceleration due to gravity on Earth?")
    answer = input("Your answer (in m/s^2): ")
    if answer == '9.8' or answer == '9.81':
        print("\nCongratulations! You've solved the physics challenge.")
        time.sleep(1)
        print("You gain valuable physics knowledge and advance to the next stage.")
        chemistry_challenge()
    else:
        print("\nIncorrect. Try again to solve the physics challenge.")
        physics_challenge()

def chemistry_challenge():
    print("\nYou face a chemistry inquiry:")
    time.sleep(1)
    print("What is the chemical formula for table salt?")
    answer = input("Your answer: ")
    if answer.lower() == 'nacl':
        print("\nWell done! You've answered the chemistry challenge correctly.")
        time.sleep(1)
        print("You acquire chemical knowledge and progress further in your quest.")
        biology_challenge()
    else:
        print("\nThat's not correct. Keep trying to answer the chemistry challenge.")
        chemistry_challenge()

def biology_challenge():
    print("\nYou encounter a biology puzzle:")
    time.sleep(1)
    print("What is the powerhouse of the cell?")
    answer = input("Your answer: ")
    if answer.lower() == 'mitochondria':
        print("\nExcellent! You've successfully solved the biology challenge.")
        time.sleep(1)
        print("You learn about cellular biology and move forward in your adventure.")
        astronomy_challenge()
    else:
        print("\nIncorrect. Keep exploring to find the answer to the biology challenge.")
        biology_challenge()

def astronomy_challenge():
    print("\nYou face an astronomy question:")
    time.sleep(1)
    print("Which planet is known as the Red Planet?")
    answer = input("Your answer: ")
    if answer.lower() == 'mars':
        print("\nCorrect! You've answered the astronomy challenge.")
        time.sleep(1)
        print("You have expanded your knowledge of math! Go try other subjects")
        gameproject.start_game()
        time.sleep(1)
    else:
        print("\nIncorrect. Keep trying to answer the astronomy challenge.")
        astronomy_challenge()

def main():
    start_game_science_()
    physics_challenge()
    chemistry_challenge()
    biology_challenge()
    astronomy_challenge()
    print("\nCongratulations! You have completed the Scientific Adventure!")
    time.sleep(1)
    print("You have acquired knowledge across various scientific topics. Well done!")

if __name__ == "__main__":
    main()