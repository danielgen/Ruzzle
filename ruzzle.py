
import random
import pyautogui
from time import sleep
from config import Frame, get_vocabulary, check
        
WORDS = get_vocabulary()
                
def play_ruzzle(frame, how_many):
    words = [word for word in WORDS if set(word).issubset(flat_frame)]
    words = sorted(words, key=len, reverse=True)
    
    results = {}
    for word in words:
        starts = [c for c in frame.frame if c.letter == word[0]]
        tries = [check(s, 1, {}, []) for s in starts]
        found = [t for t in tries if t]
        if found:
            solution = random.choice(found)
            solve = []
            for cell in solution:
                cell.real_x = random.randint(cell.gui["xmin"], cell.gui["xmax"])
                cell.real_y = random.randint(cell.gui["ymin"], cell.gui["ymax"])
                solve.append(cell)
                
            results[word] = solve
            
    pyautogui.moveTo(532, 63)
    pyautogui.click()
    counter = 0
    
    word_list = list(results.items())
    longest_first = input("If you want to shuffle words found, press Y: ")
    if longest_first.upper() == "Y":
        random.shuffle(word_list)
    results = dict(word_list)
    
    for word, eureka in results.items():
        if counter < how_many:
            print(counter, word)
            pyautogui.mouseDown(eureka[0].real_x, eureka[0].real_y)
            for cell in eureka[1:]:
                sleep(0.01)
                pyautogui.moveTo(cell.real_x, cell.real_y, 0.10)
            pyautogui.mouseUp()
            counter += 1
        else:
            break
        
if __name__ == "__main__":
    flat_frame = input("What's the Game Frame? ")
    frame = Frame(flat_frame)
    
    how_many = int(input("How many words do you want me to guess? "))
    play_ruzzle(frame, how_many)
    
   

#eipcerecnsrtnobi
#    paint = (1187, 320)
#    pyautogui.moveTo(paint)
#    pyautogui.click()
#    