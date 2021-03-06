import pygame, time
from HangMan_pygame.Modules.hangman_logic_pg import One_Game
from HangMan_pygame.Modules.from_file_pg import random_words


class OnePlayerPG(object):
	
	def __init__(self):
		pygame.init()
		# Graphics
		self.background = pygame.display.set_mode((640, 480), pygame.DOUBLEBUF)
		self.background_image = pygame.image.load('Images/background.png')
		pygame.display.set_caption("HangMan.v2")
		self.FPS = 60
		self.fpsClock = pygame.time.Clock()
		
		# Sounds
		pygame.mixer.pre_init(44100, 16, 2)
		pygame.mixer.music.load('Sounds/KlangKuenstler - Barfuss Auf Wolken.mp3')
		pygame.mixer.music.set_volume(0.1)
		pygame.mixer.music.play(-1, 0.0)
		
		# Operators
		self.with_screen = 'start'
		self.mouse_click_letter = ''
		self.first_time_in___show_progress = True
		self.time_stop = ''
	
		# Inbox
		self.input_box = pygame.Rect(350, 400, 140, 32)
		self.font = pygame.font.Font(None, 32)
		self.input_text = ''
		self.input_text_state = True
		self.color_inactive = pygame.Color(100,100,180,100)
		self.color_active = pygame.Color(245,245,245,100)
		self.color = self.color_inactive
		self.active = True
		
		# Buttons
		self.reverse_button_click = False
		self.reverse_button_box = pygame.Rect(560, 395, 80, 71)

	
	def run(self):
		running = True
		while running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						running = False
					if self.active:
						if event.key == pygame.K_RETURN:
							self.__play_klick_ok()
							if self.with_screen == 'ask_w_l':
								self.input_text = self.input_text.upper()
								self.with_screen = self.player.guess_the_capital(self.input_text)
								self.input_text = ''
							elif self.with_screen == 'win' and self.input_text_state:
								self.input_text = self.input_text.upper()
								self.player.add_your_score(self.input_text)
								self.input_text = ''
								self.input_text_state = False
						elif event.key == pygame.K_BACKSPACE:
							self.input_text = self.input_text[:-1]
						else:
							if len(self.input_text) < 20:
								self.input_text += event.unicode
				elif event.type == pygame.MOUSEBUTTONDOWN:
					if self.with_screen == 'ask_w_l':
						for char in self.alphabet_box:
							if self.alphabet_box[char].collidepoint(event.pos):
								self.mouse_click_letter = char.upper()
					if self.input_box.collidepoint(event.pos):
						self.active = not self.active
					else:
						self.active = False
					self.color = self.color_active if self.active else self.color_inactive
					
					if self.first_time_in___show_progress == True and self.playbatton_rect.collidepoint(event.pos):
						self.with_screen = 'ask_w_l'
						self.__play_klick_ok()
					elif self.reverse_button_box.collidepoint(event.pos):
						self.with_screen = 'start'
						self.__play_klick_ok()
		
						
					
					
			self.draw_start()
			self.draw_ask_w_l()
			self.draw_game_over()
			
			pygame.display.update()
			self.fpsClock.tick(self.FPS)
		
		pygame.mixer.music.stop()
		pygame.quit()
	
	
	def draw_start(self):
		if self.with_screen == 'start':
			self.input_text = ''
			self.input_text_state = True
			self.first_time_in___show_progress = True
			self.player = One_Game(random_words('Data/countries_and_capitals.txt'))
			
			# Graphhics
			self.background.blit(self.background_image, (0, 0))
			playbatton = pygame.image.load('Images/play_button.png')
			self.playbatton_rect = playbatton.get_rect()
			self.playbatton_rect.topleft = (565, 405)
			self.background.blit(playbatton, self.playbatton_rect)#(560, 400))
			self.__draw_text('Assignment: Let\'s Hang Somebody!', 100, 100, 200, 200, 200)
			self.__draw_text('The Hangman Game Implementation', 100, 120, 200, 200, 200)
			self.__draw_text('Player\'s life: 5', 100, 140, 200, 200, 200)
				
	
	def draw_ask_w_l(self):
		if self.with_screen == 'ask_w_l':
			# Graphhics
			self.background.blit(self.background_image, (0, 0))
			if self.mouse_click_letter:
				self.with_screen = self.player.guess_the_letter(self.mouse_click_letter)
				self.mouse_click_letter = ''
			
			# TXT in Graphics
			self.__draw_alphabet()
			self.__show_progress()
			
			if self.player.lives <= 0:
				self.with_screen = 'lose'
				
			# HangMan Grapfhics
			self.__draw_hangman()
			
			# Whole Word
			self.__draw_text('Write whole word above', 320, 440, 200, 200, 200)
			self.__draw_inbox()
	
	def draw_game_over(self):
		if self.with_screen == 'lose':
			self.background.blit(self.background_image, (0, 0))
			self.__draw_hangman()
			self.__draw_play_again()
			self.__show_progress(True)
			self.__show_high_scores()
			
		if self.with_screen == 'win':
			self.background.blit(self.background_image, (0, 0))
			self.__draw_play_again()
			self.__show_progress(True)
			self.__show_high_scores()
			if self.input_text_state:
				self.__draw_text('Write your name above', 320, 440, 200, 200, 200)
				self.__draw_inbox()
		
		
		
	def __draw_alphabet(self):
		alphabet = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
		            'U', 'V', 'W', 'X', 'Y', 'Z')
		
		self.alphabet_box = {}
		x = 320
		y = 50
		for char in alphabet:
			if x > 550:
				x = 370
				y += 40
				if char not in self.player.added_leteres:
					self.alphabet_box.update({char: pygame.Rect(x, y, 40, 33)})
			else:
				x += 50
				if char not in self.player.added_leteres:
					self.alphabet_box.update({char: pygame.Rect(x, y, 40, 33)})
		
		self.alphabet_surface = {}
		file_name = 'Images/{}.png'
		for char in alphabet:
			if char not in self.player.added_leteres:
				self.alphabet_surface.update({char: pygame.image.load(file_name.format(char))})
			
		# Graphics
		self.background.blit(self.background_image, (0, 0))
		for char in alphabet:
			if char not in self.player.added_leteres:
				self.background.blit(self.alphabet_surface[char], self.alphabet_box[char])
		
		
	def __draw_text(self, text, X = 0, Y = 0, R = 255, G = 0, B = 0, font = 20, background = None):
		font = pygame.font.SysFont('mono', font, bold=True)
		surface = font.render(text, True, (R, G, B), background)
		self.background.blit(surface, (X, Y))
		
		
	def __play_klick_ok(self, sound ='Sounds/play.wav'):
		play_sound = pygame.mixer.Sound(sound)
		play_sound.play()
		time.sleep(0.2)
		play_sound.stop()
		
		
	def __draw_hangman(self):
		if self.player.lives == 1:
			self.__draw_text(self.player.country)
		if self.player.lives < 0:
			self.player.lives = 0
		hang_man = pygame.image.load('Images/{}.png'.format(self.player.lives))
		self.background.blit(hang_man, (30, 100))
		

	def __draw_inbox(self):
		self.txt_surface = self.font.render(self.input_text, True, self.color)
		width = max(200, self.txt_surface.get_width() + 10)
		self.input_box.w = width
		self.background.blit(self.txt_surface, (self.input_box.x + 5, self.input_box.y + 5))
		pygame.draw.rect(self.background, self.color, self.input_box, 2)
		
		
	def __draw_play_again(self):
		a_b_syrface = pygame.image.load('Images/reverse_button.png')
		self.background.blit(a_b_syrface, self.reverse_button_box)
		
		
	def __show_progress(self, game_over = False):
		progress = self.player.show_progress_hangman()
		y = 380
		if game_over == False:
			# TODO w trakcie gry
			for line in self.player.show_progress_hangman()[:-1]:
				self.__draw_text(line, 10, y, 200, 200, 200)
				y += 30
				self.progress__buf = progress[:]
		elif self.first_time_in___show_progress:
			self.first_time_in___show_progress = False
			# TODO game over PIERWSZY obieg
			self.time_stop = progress[2]
			for line in self.player.show_progress_hangman()[1:]:
				self.__draw_text(line, 10, y, 200, 200, 200)
				y += 30
		else:
			# TODO game over KOLEJNE obiegi
			for line in self.player.show_progress_hangman()[1:]:
				if 'Guessing time' in line:
					line = self.time_stop
				self.__draw_text(line, 10, y, 200, 200, 200)
				y += 30
				
		self.__draw_text('_____________________', 10, y, 200, 200, 200)
		
		
	def __show_high_scores(self):
		y = 0
		for line in self.player.display_high_score()[:9]:
			self.__draw_text(line, 5, 30 + y, 255,25,0, font = 12, background=(0,0,0))
			y += 10
			
