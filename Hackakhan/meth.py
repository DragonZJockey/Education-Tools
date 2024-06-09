import time
import gameproject

def start_game_meth():
    print("Welcome to the Math Quests!")
    time.sleep(1)
    print("Your goal is to navigate through different mathematic topics and answer correctly to succeed.")
    time.sleep(1)
    arithmetic_challenge()

def arithmetic_challenge():
    print("\nYou encounter an arithmetic puzzle:")
    time.sleep(1)
    print("What is the result of 12 + 8?")
    answer = input("Your answer: ")
    if answer == '20':
        print("\nCongratulations! You've solved the arithmetic challenge.")
        time.sleep(1)
        print("You gain valuable arithmetic knowledge and advance to the next stage.")
        algebra_challenge()
    else:
        print("\nIncorrect. Try again to solve the arithmetic challenge.")
        arithmetic_challenge()

def algebra_challenge():
    print("\nYou face an algebra inquiry:")
    time.sleep(1)
    print("Solve for x: 2x + 3 = 7")
    answer = input("Your answer: ")
    if answer == '2':
        print("\nWell done! You've answered the algebra challenge correctly.")
        time.sleep(1)
        print("You acquire algebra knowledge and progress further in your quest.")
        geometry_challenge()
    else:
        print("\nThat's not correct. Keep trying to answer the algebra challenge.")
        algebra_challenge()

def geometry_challenge():
    print("\nYou encounter a geometry puzzle:")
    time.sleep(1)
    print("What is the area of a circle with radius 5? (Use π ≈ 3.14)")
    answer = input("Your answer: ")
    if answer == '78.5':
        print("\nExcellent! You've successfully solved the geometry challenge.")
        time.sleep(1)
        print("You learn about geometric principles and move forward in your adventure.")
        calculus_challenge()
    else:
        print("\nIncorrect. Keep exploring to find the answer to the geometry challenge.")
        geometry_challenge()

def calculus_challenge():
    print("\nYou face a calculus question:")
    time.sleep(1)
    print("What is the derivative of x^2?")
    answer = input("Your answer: ")
    if answer.lower() == '2x':
        print("\nCorrect! You've answered the calculus challenge.")
        time.sleep(1)
        print("You have expanded your knowledge of math! Go try other subjects")
        gameproject.start_game()
        time.sleep(1)
    else:
        print("\nIncorrect. Keep trying to answer the calculus challenge.")
        calculus_challenge()

def main():
    start_game_meth()
    arithmetic_challenge()
    algebra_challenge()
    geometry_challenge()
    calculus_challenge()
    print("\nCongratulations! You have completed the Math Quest Adventure Game.")
    time.sleep(1)
    print("You have acquired knowledge across various mathematical disciplines. Well done!")

if __name__ == "__main__":
    main()