import pygame

class OnePlayerPG(object):
	def __init__(self, width=640, height=400, fps=30):
		pygame.init()
		pygame.display.set_caption("HangMan.v2")
		self.width = width
		self.height = height
		#self.height = width // 4
		self.screen = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF)
		self.background = pygame.image.load('Images/background.png')  # ../HangMan_pygame/Images/
		# self.background = pygame.Surface(self.screen.get_size()).convert()
		# self.clock = pygame.time.Clock()
		# self.fps = fps
		# self.playtime = 0.0
		self.font = pygame.font.SysFont('mono', 20, bold=True)
		self.mouse_pos_click = 0

	def run(self):
		running = True
		while running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						running = False
				elif event.type == pygame.MOUSEBUTTONDOWN:
					self.mouse_pos_click = event.pos
					
			# milliseconds = self.clock.tick(self.fps)
			# self.playtime += milliseconds / 1000.0
			# self.draw_text("FPS: {:6.3}{}PLAYTIME: {:6.3} SECONDS".format(
			#                self.clock.get_fps(), " "*5, self.playtime))
			
			pygame.display.flip()
			self.screen.blit(self.background, (0, 0))
			# self.draw_text(str(self.mouse_pos_click))
			self.draw_start_screen()
			
			
			
			
		pygame.quit()
		
	def draw_text(self, text):
		fw, fh = self.font.size(text)
		surface = self.font.render(text, True, (255, 0, 0))
		self.screen.blit(surface, (0, 0)) #((self.width - fw) // 2, (self.height - fh) // 2))
		
	def draw_start_screen(self):
		# create a rectangular surface for the ball
		# ballsurface = pygame.Surface((200, 200), pygame.SRCALPHA)
		# ballsurface = ballsurface.convert_alpha()
		# draw blue filled circle on ball surface
		# pygame.draw.circle(ballsurface, (0, 0, 255), (25, 25), 25)
		# pygame.draw.rect(ballsurface, (0, 0, 255), (25, 25, 100, 50))
		ballsurface = pygame.image.load('Images/play_button.png')
		self.screen.blit(ballsurface, (500, 400))
	def draw_ask_w_l(self):
		
		pass
	
	def draw_ask_l(self):
		pass
	
	def draw_ask_w(self):
		pass
	
	def draw_game_over(self, win_loos = True):
		pass
	
	def draw_ask_again(self):
		pass
	
	
	