import pygame

class OnePlayerPG(object):
	def __init__(self, width=640, height=400, fps=30):
		pygame.init()
		pygame.display.set_caption("HangMan.v2")
		self.width = width
		self.height = height
		#self.height = width // 4
		self.screen = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF)
		# self.background = pygame.Surface(self.screen.get_size()).convert()
		# self.clock = pygame.time.Clock()
		# self.fps = fps
		# self.playtime = 0.0
		self.font = pygame.font.SysFont('mono', 20, bold=True)
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
					if self.with_screen == 'ask_w_l' and self.a_box.collidepoint(event.pos):
						print('a')
					self.mouse_pos_click = event.pos
					# print(self.mouse_pos_click)
				
			# milliseconds = self.clock.tick(self.fps)
			# self.playtime += milliseconds / 1000.0
			# self.draw_text("FPS: {:6.3}{}PLAYTIME: {:6.3} SECONDS".format(
			#                self.clock.get_fps(), " "*5, self.playtime))
			
			pygame.display.flip()
			# self.screen.blit(self.background, (0, 0))
			# self.draw_text(str(self.mouse_pos_click))
			
			self.draw_start(self.mouse_pos_click)
			# print(self.with_screen)
			self.draw_ask_w_l(self.mouse_pos_click)
			self.draw_ask_l(self.mouse_pos_click)
			self.draw_ask_w(self.mouse_pos_click)
			
			
		pygame.quit()
		
		
	def draw_text(self, text, X = 0, Y = 0, R = 255, G = 0, B = 0):
		# fw, fh = self.font.size(text)
		surface = self.font.render(text, True, (R, G, B))
		self.screen.blit(surface, (X, Y)) #((self.width - fw) // 2, (self.height - fh) // 2))
		
	def draw_start(self, mouse_click_pos):
		# create a rectangular surface for the ball
		# ballsurface = pygame.Surface((200, 200), pygame.SRCALPHA)
		# ballsurface = ballsurface.convert_alpha()
		# draw blue filled circle on ball surface
		# pygame.draw.circle(ballsurface, (0, 0, 255), (25, 25), 25)
		# pygame.draw.rect(ballsurface, (0, 0, 255), (25, 25, 100, 50))
		if self.with_screen == 'start':
			ballsurface = pygame.image.load('Images/play_button.png')
			self.background = pygame.image.load('Images/background.png')  # ../HangMan_pygame/Images/
			
			self.screen.blit(self.background, (0, 0))
			self.draw_text(str(self.mouse_pos_click))
			self.screen.blit(ballsurface, (500, 400))
			if (505 < mouse_click_pos[0] < 544) and (405 < mouse_click_pos[1] < 428):
				self.with_screen = 'ask_w_l'

			
			
	def draw_ask_w_l(self, mouse_click_pos):
		if self.with_screen == 'ask_w_l':
			w_surface = pygame.image.load('Images/w_button.png')
			l_surface = pygame.image.load('Images/l_button.png')
			# a_surface = pygame.image.load('Images/a.png')
			self.screen.blit(self.background, (0, 0))
			self.draw_text(str(self.mouse_pos_click))
			self.screen.blit(w_surface, (200, 400))
			self.screen.blit(l_surface, (100, 400))
			# self.screen.blit(a_surface, (350, 50))
			self.draw_alphabet()
			self.draw_text('Will you guess a letter or word? (Esc to quit):', 5, 380, 200,200,200)
			if (104 < mouse_click_pos[0] < 145) and (404 < mouse_click_pos[1] < 431):
				self.with_screen = 'ask_l'
			if (205 < mouse_click_pos[0] < 245) and (404 < mouse_click_pos[1] < 431):
				self.with_screen = 'ask_w'
	
	def draw_ask_l(self, mouse_click_pos):
		if self.with_screen == 'ask_l':
			self.screen.blit(self.background, (0, 0))
			input_box = pygame.Rect(100, 100, 140, 32)
			color_inactive = pygame.Color('lightskyblue3')
			color_active = pygame.Color('dodgerblue2')
			color = color_inactive
			self.active = False
			
			txt_surface = self.font.render('texttdtdt', True, color)
			width = max(200, txt_surface.get_width() + 10)
			input_box.w = width
			self.screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
			pygame.draw.rect(self.screen, color, input_box, 2)
			print(self.input_l_txt)
			
			# for event in pygame.event.get():
			# 	if event.type == pygame.MOUSEBUTTONDOWN:
			# 		# If the user clicked on the input_box rect.
			# 		if input_box.collidepoint(event.pos):
			# 			# Toggle the active variable.
			# 			self.active = not self.active
			# 		else:
			# 			self.active = False
			# 		# Change the current color of the input box.
			# 		color = color_active if self.active else color_inactive
			# 	if event.type == pygame.KEYDOWN:
			# 		if self.active:
			# 			if event.key == pygame.K_RETURN:
			# 				print(self.input_l_txt)
			# 				self.input_l_txt = ''
			# 			elif event.key == pygame.K_BACKSPACE:
			# 				text = self.input_l_txt[:-1]
			# 			else:
			# 				self.input_l_txt += event.unicode
			
			
			# print('draw_ask_l')
			
	
	def draw_ask_w(self, mouse_click_pos):
		if self.with_screen == 'ask_w':
			print('draw_ask_w')
		
	
	def draw_game_over(self, win_loos = True):
		pass
	
	def draw_ask_again(self):
		pass
	
	def draw_alphabet(self):
		self.a_box = pygame.Rect(350, 50, 40, 33)
		self.a_surface = pygame.image.load('Images/a.png')
		# self.a_surface.blit(self.a_box.screen, (350, 50))
		self.screen.blit(self.a_surface, (350, 50))
		
		
	