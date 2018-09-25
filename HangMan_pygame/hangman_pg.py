# !/usr/bin/python3.6
import sys
import os
import pygame
import pickle

# from HangMan.from_file import random_words
# from HangMan.one_game import One_Game
# from HangMan_pygame.hang_pygame import OnePlayerPG

from HangMan_pygame.hang_class_pg import OnePlayerPG
from from_file_pg import random_words
from one_game_pg import One_Game



OnePlayerPG(640, 480).run()


sys.exit()
#TODO--------------------------------------------------------------------------------------------
os.system('clear')

player = One_Game(random_words('countries_and_capitals.txt'))
answer_l_w = ''


print("test")
sys.exit()
print("testtt")
while answer_l_w != 'l' and answer_l_w != 'w' and answer_l_w != 'q':
	if player.lives <= 0:
		player = One_Game(random_words('countries_and_capitals.txt'))
	
	player.show_progress_hangman()
	answer_l_w = input('Will you guess a letter or word? (l or w) (q to quit):').lower()
	if answer_l_w == 'l':
		player.guess_the_letter()
	elif answer_l_w == 'w':
		player.guess_the_capital()
	elif answer_l_w == 'q':
		sys.exit('bye bye ')

	
	if player.lives > 0:
		answer_l_w = ''
	if player.lives <= 0:
		answer_l_w = input('If You want quit press q, else play again:')
		
		
