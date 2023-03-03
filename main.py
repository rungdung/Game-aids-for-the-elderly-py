# GUI based snake and ladder game
# cloned from Jay Polra
# copyassignment.com

import gameBoard as gb
# importing tkinter module
import random
from tkinter import *
import time
from PIL import Image, ImageTk
import cv
bgScale = 25




#class for matcing the dice number with the snake and ladder
class matching_position():
    def find_snake_or_ladder(self, block, turn, position):
        x = 35*(turn>=3)
        y = (turn%3)*35
        if(block == 3):
           return 305+x, 150+y, 22
        elif(block == 5):
            return 545+x, 390+y, 8
        elif(block == 11):
            return 185+x, 30+y, 26
        elif(block == 20):
            return 545+x, 30+y, 29
        elif(block == 17):
           return 425+x, 510+y, 4
        elif(block == 19):
           return 665+x, 390+y, 7
        elif(block == 21):
           return 425+x, 390+y, 9
        elif(block == 27):
           return 65+x, 510+y, 1
        else:
            return position[0], position[1], block
        
 
#defining the main function    
def main():
    #cv.startInference() # Start using the webcam to detect the dice number
    master = Tk()
    master.title("Snake and Ladder")
    master.geometry("900x1980")
    img = Image.open("assets/board.png")
    img = ImageTk.PhotoImage(img.resize((30*bgScale, 40*bgScale)))
    x = gb.game_board(master,img)
    master.mainloop()

main()