# -*- coding: utf-8 -*-
"""
Created on Sat May 16 20:04:16 2020

@author: genti
"""
import pyautogui
from time import sleep

# defining function to draw a word using pyautogui on screen
def draw_word(word, draw_speed=0.01, pause=0.05):
    pyautogui.mouseDown(word[0].real_x, word[0].real_y)
    for cell in word[1:]:
        sleep(draw_speed)
        pyautogui.moveTo(cell.real_x, cell.real_y, pause)
    pyautogui.mouseUp()