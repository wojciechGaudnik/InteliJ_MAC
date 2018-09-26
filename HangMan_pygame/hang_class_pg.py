import pygame, time
from HangMan_pygame.Modules.one_game_pg import One_Game
from HangMan_pygame.Modules.from_file_pg import random_words

# ballsurface = pygame.Surface((200, 200), pygame.SRCALPHA)
# ballsurface = ballsurface.convert_alpha()
# self.background = pygame.Surface(self.screen.get_size()).convert()
# self.__draw_text("FPS: {:6.3}{}PLAYTIME: {:6.3} SECONDS".format(self.clock.get_fps(), " "*5, self.playtime))

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
		# self.active = False
		# self.input_l_txt = ''
		# self.input_w_txt = ''
	
		# Inbox
		self.input_box = pygame.Rect(350, 400, 140, 32)
		self.font = pygame.font.Font(None, 32)
		self.text = ''
		self.color_inactive = pygame.Color('lightskyblue3')
		self.color_active = pygame.Color('dodgerblue2')
		self.color = self.color_inactive
		self.active = True
		
		# Buttons
		self.reverse_button_click = False
		self.a_b_box = pygame.Rect(550, 400, 80, 71)

		# self.a_b_box =
	# self.txt_surface = self.font.render(self.text, True, self.color)
		# Resize the box if the text is too long.
		# width = max(200, self.txt_surface.get_width() + 10)
		# self.input_box.w = width
		# self.background.blit(self.txt_surface, (self.input_box.x + 5, self.input_box.y + 5))
		# pygame.draw.rect(self.background, self.color, self.input_box, 2)
	
	def run(self):
		running = True
		while running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						running = False
					# else:
					# 	self.input_l_txt = event.unicode
					if self.active:
						if event.key == pygame.K_RETURN:
							self.text = self.text.upper()
							self.with_screen = self.player.guess_the_capital(self.text)
							self.text = ''
						elif event.key == pygame.K_BACKSPACE:
							self.text = self.text[:-1]
						else:
							self.text += event.unicode
				elif event.type == pygame.MOUSEBUTTONDOWN:
					self.mouse_pos_click = event.pos #TODO patrz linijka z TODO evanty
					if self.with_screen == 'ask_w_l':
						for char in self.alphabet_box:
							if self.alphabet_box[char].collidepoint(event.pos):
								self.mouse_click_letter = char.upper()
								self.__play_klick()
								# print(self.mouse_click_letter)
					if self.input_box.collidepoint(event.pos):
						self.active = not self.active
					else:
						self.active = False
					self.color = self.color_active if self.active else self.color_inactive
					if self.a_b_box.collidepoint(event.pos):
						self.with_screen = 'start'
						print(self.with_screen)
					
					# if self.with_screen == 'ask_w_l' and self.a_box.collidepoint(event.pos):
					# 	print('a')
					# self.mouse_pos_click = event.pos
			
			
			self.draw_start(self.mouse_pos_click)
			self.draw_ask_w_l(self.mouse_pos_click)
			self.draw_game_over(self.mouse_pos_click)
			# self.draw_ask_l(self.mouse_pos_click)
			# self.draw_ask_w(self.mouse_pos_click)
			
			pygame.display.update()
			self.fpsClock.tick(self.FPS)
		
		pygame.mixer.music.stop()
		pygame.quit()
	
	
	def draw_start(self, mouse_click_pos):
		if self.with_screen == 'start':
			self.player = One_Game(random_words('countries_and_capitals.txt'))
			
			# Graphhics
			self.background.blit(self.background_image, (0, 0))
			playbatton = pygame.image.load('Images/play_button.png')
			self.background.blit(playbatton, (500, 400))
			self.__draw_text(str(self.mouse_pos_click))
			self.__draw_text("There we will write short story", 100, 100, 200, 200, 200)
			self.__draw_text("and instructions", 100, 120, 200, 200, 200)
		
			# TODO na eventy !!!!!!!!
			if (505 < mouse_click_pos[0] < 544) and (405 < mouse_click_pos[1] < 428):
				self.with_screen = 'ask_w_l'
				
	
	def draw_ask_w_l(self, mouse_click_pos):
		if self.with_screen == 'ask_w_l':
			# Graphhics
			self.background.blit(self.background_image, (0, 0))
			if self.mouse_click_letter:
				self.with_screen = self.player.guess_the_letter(self.mouse_click_letter)
				self.mouse_click_letter = ''
			
			# TXT in Graphics
			self.__draw_alphabet()
			progress = self.player.show_progress_hangman()
			y = 430
			for line in progress:
				self.__draw_text(line, 10, y, 200, 200, 200)
				y += 30
			self.__draw_text('_____________________', 10, y, 200, 200, 200)
			if self.player.lives <= 0:
				self.with_screen = 'lose'
				
			# HangMan Grapfhics
			self.__draw_hangman(self.player.lives)
			# print(self.text)
			
			# Whole Word
			self.__draw_inbox()
			# self.txt_surface = self.font.render(self.text, True, self.color)
			# width = max(200, self.txt_surface.get_width() + 10)
			# self.input_box.w = width
			# self.background.blit(self.txt_surface, (self.input_box.x + 5, self.input_box.y + 5))
			# pygame.draw.rect(self.background, self.color, self.input_box, 2)
			
	
	def draw_game_over(self, mouse_click_pos):
		if self.with_screen == 'lose':
			# Graphhics
			self.background.blit(self.background_image, (0, 0))
			self.__draw_hangman(self.player.lives)
			# hang_man = pygame.image.load('Images/{}.png'.format(self.player.lives))  # .convert()
			# self.background.blit(hang_man, (30, 50))
			
		if self.with_screen == 'win':
			self.background.blit(self.background_image, (0, 0))
			self.__draw_text('Congratulation !!! you WIN !!!')
			# print('wineeee')
			self.__draw_play_again()
			pass
		pass
	
	def draw_ask_again(self):
		pass
	
	def __draw_alphabet(self):
		alphabet = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
		            'U', 'V', 'W', 'X', 'Y', 'Z')
		# print(len(alphabet))
		
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
		
		
	def __draw_text(self, text, X = 0, Y = 0, R = 255, G = 0, B = 0):
		font = pygame.font.SysFont('mono', 20, bold=True)
		surface = font.render(text, True, (R, G, B))
		self.background.blit(surface, (X, Y))
		
		
	def __play_klick(self, sound ='Sounds/start.wav'):
		play_sound = pygame.mixer.Sound(sound)
		play_sound.play()
		time.sleep(0.3)
		play_sound.stop()
		
	def __draw_hangman(self, lives):
		if self.player.lives <= 1:
			print('podpowiedz') #TODO !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
		hang_man = pygame.image.load('Images/{}.png'.format(lives)) #.convert()
		self.background.blit(hang_man, (30, 100))

	def __draw_inbox(self):
		self.txt_surface = self.font.render(self.text, True, self.color)
		width = max(200, self.txt_surface.get_width() + 10)
		self.input_box.w = width
		self.background.blit(self.txt_surface, (self.input_box.x + 5, self.input_box.y + 5))
		pygame.draw.rect(self.background, self.color, self.input_box, 2)
		
	def __draw_play_again(self):
		# self.a_b_box = pygame.Rect(550, 400, 40, 33)
		a_b_syrface = pygame.image.load('Images/reverse_button.png')
		self.background.blit(a_b_syrface, self.a_b_box)
		
		# self.reverse_button_click
		pass
# ballsurface = pygame.Surface((200, 200), pygame.SRCALPHA)
# ballsurface = ballsurface.convert_alpha()
# self.background = pygame.Surface(self.screen.get_size()).convert()