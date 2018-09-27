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
		self.mouse_pos_click = [0, 0]
		self.with_screen = 'start'
		self.mouse_click_letter = ''
		self.first_time_in___show_progress = True
		self.time_stop = ''
	
		# Inbox
		self.input_box = pygame.Rect(350, 400, 140, 32)
		self.font = pygame.font.Font(None, 32)
		self.input_text = ''
		self.input_text_state = False
		self.color_inactive = pygame.Color('lightskyblue3') # TODO kolorki popraw
		self.color_active = pygame.Color('dodgerblue2')
		self.color = self.color_inactive
		self.active = True
		
		# Buttons
		self.reverse_button_click = False
		self.a_b_box = pygame.Rect(550, 400, 80, 71)

	
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
						if event.key == pygame.K_RETURN: #todo -----------------------
							if self.with_screen == 'ask_w_l':
								self.input_text = self.input_text.upper()
								self.with_screen = self.player.guess_the_capital(self.input_text)
								self.input_text = ''
							elif self.with_screen == 'win':
								print('test')
								self.input_text = self.input_text.upper()
								self.player.add_your_score(self.input_text)
								# self.with_screen = self.player.guess_the_capital(self.input_text)
								self.input_text = ''
								self.input_text_state = True
						elif event.key == pygame.K_BACKSPACE:
							self.input_text = self.input_text[:-1]
						else:
							self.input_text += event.unicode
				elif event.type == pygame.MOUSEBUTTONDOWN:
					self.mouse_pos_click = event.pos #TODO patrz linijka z TODO evanty
					if self.with_screen == 'ask_w_l':
						for char in self.alphabet_box:
							if self.alphabet_box[char].collidepoint(event.pos):
								self.mouse_click_letter = char.upper()
								self.__play_klick()
					if self.input_box.collidepoint(event.pos):
						self.active = not self.active
					else:
						self.active = False
					self.color = self.color_active if self.active else self.color_inactive
					if self.a_b_box.collidepoint(event.pos):
						self.with_screen = 'start'
					
			self.draw_start(self.mouse_pos_click)
			self.draw_ask_w_l()
			self.draw_game_over()
			
			pygame.display.update()
			self.fpsClock.tick(self.FPS)
		
		pygame.mixer.music.stop()
		pygame.quit()
	
	
	def draw_start(self, mouse_click_pos):
		if self.with_screen == 'start':
			self.first_time_in___show_progress = True
			self.player = One_Game(random_words('countries_and_capitals.txt'))
			
			# Graphhics
			self.background.blit(self.background_image, (0, 0))
			playbatton = pygame.image.load('Images/play_button.png')
			self.background.blit(playbatton, (500, 400))
			self.__draw_text("There we will write short story", 100, 100, 200, 200, 200) #TODO dorób historie
			self.__draw_text("and instructions", 100, 120, 200, 200, 200)
		
			# TODO na eventy !!!!!!!!
			if (505 < mouse_click_pos[0] < 544) and (405 < mouse_click_pos[1] < 428):
				self.with_screen = 'ask_w_l'
				
	
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
			self.__draw_inbox()
	
	def draw_game_over(self):
		if self.with_screen == 'lose':
			# Graphhics
			self.background.blit(self.background_image, (0, 0))
			self.__draw_hangman()
			self.__draw_play_again()
			self.__show_progress(True)
			self.__show_high_scores()
			
		if self.with_screen == 'win':
			self.background.blit(self.background_image, (0, 0))
			# self.__draw_text('Congratulation !!! you WIN !!!')
			self.__draw_play_again()
			self.__show_progress(True)
			self.__draw_inbox() # TODO-------------------------------
			if self.input_text_state:
				self.__show_high_scores()
				# self.input_text_state = False
		
		
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
		
		
	def __draw_text(self, text, X = 0, Y = 0, R = 255, G = 0, B = 0, font = 20):
		font = pygame.font.SysFont('mono', font, bold=True)
		surface = font.render(text, True, (R, G, B))
		self.background.blit(surface, (X, Y))
		
		
	def __play_klick(self, sound ='Sounds/start.wav'):
		play_sound = pygame.mixer.Sound(sound)
		play_sound.play()
		time.sleep(0.3)
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
		self.background.blit(a_b_syrface, self.a_b_box)
		
		
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
		pl = 1
		self.__draw_text(self.player.display_high_score()[0], font=20)
		for line in self.player.display_high_score()[1:]:
			text = '{}. '.format(str(pl))
			pl += 1
			for li in line:
				text += str(li)
				text += ' | '
			self.__draw_text(text, 5, 30 + y, font = 15)
			y += 30
			
