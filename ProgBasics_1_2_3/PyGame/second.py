import sys
import pygame
from PyGame.second_mod import Settings
from PyGame.second_mod import Ship
from PyGame.gf import


def run_game():
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption('Inwacja obcych')
	bg_color = (ai_settings.bg_color)
	
	ship = Ship(ai_settings, screen)
	
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					ship.moving_right = True
				if event.key == pygame.K_LEFT:
					ship.moving_left = True
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_RIGHT:
					ship.moving_right = False
				if event.key == pygame.K_LEFT:
					ship.moving_left = False
			
		
		screen.fill(bg_color)
		ship.update()
		ship.blitme()
		pygame.display.flip()
		
		
		
run_game()