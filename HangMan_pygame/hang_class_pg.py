import pygame, time
from HangMan_pygame.Modules.one_game_pg import One_Game
from HangMan_pygame.Modules.from_file_pg import random_words

# ballsurface = pygame.Surface((200, 200), pygame.SRCALPHA)
# ballsurface = ballsurface.convert_alpha()
# self.background = pygame.Surface(self.screen.get_size()).convert()
# self.draw_text("FPS: {:6.3}{}PLAYTIME: {:6.3} SECONDS".format(self.clock.get_fps(), " "*5, self.playtime))

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
		
		self.mouse_pos_click = [0, 0]
		self.with_screen = 'start'
		self.active = False
		self.input_l_txt = ''
		self.input_w_txt = ''
	
	
	def run(self):
		running = True
		while running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						running = False
					else:
						self.input_l_txt = event.unicode
				elif event.type == pygame.MOUSEBUTTONDOWN:
					self.mouse_pos_click = event.pos #TODO patrz linijka z TODO evanty
					if self.with_screen == 'ask_w_l':
						for char in self.alphabet_box:
							if self.alphabet_box[char].collidepoint(event.pos):
								self.mouse_click_letter = char
								print(self.mouse_click_letter)
					
					
					# if self.with_screen == 'ask_w_l' and self.a_box.collidepoint(event.pos):
					# 	print('a')
					# self.mouse_pos_click = event.pos
			
			
			self.draw_start(self.mouse_pos_click)
			self.draw_ask_w_l(self.mouse_pos_click)
			# self.draw_ask_l(self.mouse_pos_click)
			# self.draw_ask_w(self.mouse_pos_click)
			
			pygame.display.update()
			self.fpsClock.tick(self.FPS)
		
		pygame.mixer.music.stop()
		pygame.quit()
	
	
	def draw_text(self, text, X = 0, Y = 0, R = 255, G = 0, B = 0):
		font = pygame.font.SysFont('mono', 20, bold=True)
		surface = font.render(text, True, (R, G, B))
		self.background.blit(surface, (X, Y))
	
	def draw_start(self, mouse_click_pos):
		if self.with_screen == 'start':
			
			self.player = One_Game(random_words('countries_and_capitals.txt'))
			
			# Graphhics
			self.background.blit(self.background_image, (0, 0))
			playbatton = pygame.image.load('Images/play_button.png')
			self.background.blit(playbatton, (500, 400))
			self.draw_text(str(self.mouse_pos_click))
			self.draw_text("There we will write short story", 100, 100, 200, 200, 200)
			self.draw_text("and instructions", 100, 120, 200, 200, 200)
		
			# TODO na eventy !!!!!!!!
			if (505 < mouse_click_pos[0] < 544) and (405 < mouse_click_pos[1] < 428):
				self.with_screen = 'ask_w_l'
			# Sounds
				play_sound = pygame.mixer.Sound('Sounds/start.wav')
				play_sound.play()
				time.sleep(0.5)
				play_sound.stop()
	
	def draw_ask_w_l(self, mouse_click_pos):
		if self.with_screen == 'ask_w_l':
			# Graphhics
			self.background.blit(self.background_image, (0, 0))
			self.draw_alphabet()
		
		# w_surface = pygame.image.load('Images/w_button.png')
		# l_surface = pygame.image.load('Images/l_button.png')
		# # a_surface = pygame.image.load('Images/a.png')
		# self.screen.blit(self.background, (0, 0))
		# self.draw_text(str(self.mouse_pos_click))
		# self.screen.blit(w_surface, (200, 400))
		# self.screen.blit(l_surface, (100, 400))
		# # self.screen.blit(a_surface, (350, 50))
		# self.draw_alphabet()
		# self.draw_text('Will you guess a letter or word? (Esc to quit):', 5, 380, 200,200,200)
		# if (104 < mouse_click_pos[0] < 145) and (404 < mouse_click_pos[1] < 431):
		# 	self.with_screen = 'ask_l'
		# if (205 < mouse_click_pos[0] < 245) and (404 < mouse_click_pos[1] < 431):
		# 	self.with_screen = 'ask_w'
	
	# def draw_ask_l(self, mouse_click_pos):
	# 	if self.with_screen == 'ask_l':
	# 		self.screen.blit(self.background, (0, 0))
	# 		input_box = pygame.Rect(100, 100, 140, 32)
	# 		color_inactive = pygame.Color('lightskyblue3')
	# 		color_active = pygame.Color('dodgerblue2')
	# 		color = color_inactive
	# 		self.active = False
	#
	# 		txt_surface = self.font.render('texttdtdt', True, color)
	# 		width = max(200, txt_surface.get_width() + 10)
	# 		input_box.w = width
	# 		self.screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
	# 		pygame.draw.rect(self.screen, color, input_box, 2)
	# 		print(self.input_l_txt)
	#
	# 	# for event in pygame.event.get():
	# 	# 	if event.type == pygame.MOUSEBUTTONDOWN:
	# 	# 		# If the user clicked on the input_box rect.
	# 	# 		if input_box.collidepoint(event.pos):
	# 	# 			# Toggle the active variable.
	# 	# 			self.active = not self.active
	# 	# 		else:
	# 	# 			self.active = False
	# 	# 		# Change the current color of the input box.
	# 	# 		color = color_active if self.active else color_inactive
	# 	# 	if event.type == pygame.KEYDOWN:
	# 	# 		if self.active:
	# 	# 			if event.key == pygame.K_RETURN:
	# 	# 				print(self.input_l_txt)
	# 	# 				self.input_l_txt = ''
	# 	# 			elif event.key == pygame.K_BACKSPACE:
	# 	# 				text = self.input_l_txt[:-1]
	# 	# 			else:
	# 	# 				self.input_l_txt += event.unicode
	#
	#
	# 	# print('draw_ask_l')
	
	
	def draw_ask_w(self, mouse_click_pos):
		if self.with_screen == 'ask_w':
			print('draw_ask_w')
	
	
	def draw_game_over(self, win_loos = True):
		pass
	
	def draw_ask_again(self):
		pass
	
	def draw_alphabet(self):
		alphabet = ('a', 'b', 'c', 'd', 'e', 'f')#, 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
		            #'u', 'v', 'w', 'x', 'y', 'z')
		
		self.alphabet_box = {}
		x = 320
		y = 50
		for char in alphabet:
			if x > 550:
				x = 320
				y += 40
				self.alphabet_box.update({char: pygame.Rect(x, y, 40, 33)})
			else:
				self.alphabet_box.update({char: pygame.Rect(x, y, 40, 33)})
				x += 50
		
		self.alphabet_surface = {}
		file_name = 'Images/{}.png'
		for char in alphabet:
			self.alphabet_surface.update({char: pygame.image.load(file_name.format(char))})
			
		# Graphics
		self.background.blit(self.background_image, (0, 0))
		for char in alphabet:
			self.background.blit(self.alphabet_surface[char], self.alphabet_box[char])
		
		
	