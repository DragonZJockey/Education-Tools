import time
import gameproject
def start_game_geography():
    print("Welcome to the Geography Quest Adventure Game!")
    time.sleep(1)
    print("Your goal is to navigate through different geographical topics and answer correctly to succeed.")
    time.sleep(1)
    country_capital_challenge()

def country_capital_challenge():
    print("\nYou encounter a challenge about countries and capitals:")
    time.sleep(1)
    print("What is the capital of France?")
    answer = input("Your answer: ")
    if answer.lower() == 'paris':
        print("\nCongratulations! You've solved the country-capital challenge.")
        time.sleep(1)
        print("You gain valuable geographical knowledge and advance to the next stage.")
        physical_features_challenge()
    else:
        print("\nIncorrect. Try again to solve the country-capital challenge.")
        country_capital_challenge()

def physical_features_challenge():
    print("\nYou face a question about physical features:")
    time.sleep(1)
    print("Which is the longest river in the world?")
    answer = input("Your answer: ")
    if answer.lower() == 'nile' or answer.lower() == 'amazon':
        print("\nWell done! You've answered the physical features challenge correctly.")
        time.sleep(1)
        print("You acquire geographical knowledge and progress further in your quest.")
        landmarks_challenge()
    else:
        print("\nThat's not correct. Keep trying to answer the physical features challenge.")
        physical_features_challenge()

def landmarks_challenge():
    print("\nYou encounter a landmarks puzzle:")
    time.sleep(1)
    print("Where is the Great Wall located?")
    answer = input("Your answer: ")
    if answer.lower() == 'china':
        print("\nExcellent! You've successfully solved the landmarks challenge.")
        time.sleep(1)
        print("You learn about famous landmarks and move forward in your adventure.")
        continents_challenge()
    else:
        print("\nIncorrect. Keep exploring to find the answer to the landmarks challenge.")
        landmarks_challenge()

def continents_challenge():
    print("\nYou face a question about continents:")
    time.sleep(1)
    print("How many continents are there on Earth?")
    answer = input("Your answer: ")
    if answer == '7':
        print("\nCorrect! You've answered the continents challenge.")
        time.sleep(1)
        print("You have expanded your knowledge of math! Go try other subjects")
        gameproject.start_game()
        time.sleep(1)
    else:
        print("\nIncorrect. Keep trying to answer the continents challenge.")
        continents_challenge()

def main():
    start_game_geography()
    country_capital_challenge()
    physical_features_challenge()
    landmarks_challenge()
    continents_challenge()
    print("\nCongratulations! You have completed the Geography Quest Adventure Game.")
    time.sleep(1)
    print("You have acquired knowledge across various geographical themes. Well done!")

if __name__ == "__main__":
    main()