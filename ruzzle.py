
import random
import pyautogui
from game_objects import Frame
from config import get_vocabulary, check
from drawing import draw_word   

# importing the list of words from vocabulary file, defaults to Italian    
WORDS = get_vocabulary()

# defining Main function to be executed when file is run
def play_ruzzle(frame, how_many, longest_first):
    
    # excluding words that contain letters not present in game frame
    words = [word for word in WORDS if set(word).issubset(flat_frame)]
    
    # sorting by length of the word
    words = sorted(words, key=len, reverse=True)
    
    # looping through word list
    results = {}
    for word in words:
        
        # find all potential starting cells for that word in current frame
        starts = [c for c in frame.frame if c.letter == word[0]]
        
        # check for each start point if word can be traced
        tries = [check(word, start, 1, {}, []) for start in starts]
        
        # listing solutions and picking a random one
        found = [t for t in tries if t]
        if found:
            solution = random.choice(found)
            solve = []
            
            # press a random point of each cell touched to draw the word
            # this is done to dissimulate that the player is a bot
            for cell in solution:
                cell.real_x = random.randint(cell.gui["xmin"], cell.gui["xmax"])
                cell.real_y = random.randint(cell.gui["ymin"], cell.gui["ymax"])
                solve.append(cell)
                
            results[word] = solve
    
    # bring focus on emulator window by clicking on it     
    pyautogui.moveTo(532, 63)
    pyautogui.click()

    word_list = list(results.items())
    if longest_first.upper() == "Y":
        random.shuffle(word_list)
    results = dict(word_list)
    
    # draw the words
    counter = 0
    for word, eureka in results.items():
        if counter < how_many:
            print(counter, word)
            draw_word(eureka)
            counter += 1
        else:
            break

if __name__ == "__main__":
    flat_frame = input("What's the Game Frame? ")
    how_many = int(input("How many words do you want me to guess? "))
    longest_first = input("If you want to shuffle words found, press Y: ")

    frame = Frame(flat_frame)
    play_ruzzle(frame, how_many, longest_first)
   
