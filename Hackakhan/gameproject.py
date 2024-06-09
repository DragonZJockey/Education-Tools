import meth
import geography
import history
import science
import time
def start_game():
    print("Welcome to the Adventure Games.")
    time.sleep(2)
    print("You must choose a subject: Math, Science, History, or Geography.")
    choose_game()

def choose_game():
    chosen = input("Enter a subject: ")
    
    if chosen.lower() == 'math':
        meth.start_game_meth()
    elif chosen.lower() == 'geography':
        geography.start_game_geography()
    elif chosen.lower() == 'history':
        history.start_game_history()
    elif chosen.lower() == 'science':
        science.start_game_science()
    else:
        print(chosen)
        print("Invalid answer. Please try again")
        choose_game()
if __name__ == "__main__":
    start_game()