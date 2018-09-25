# import pygame
#
# class OnePlayerPG(object):
# 	def __init__(self, width=640, height=400, fps=30):
# 		pygame.init()
# 		pygame.display.set_caption("HangMan.v2")
# 		self.width = width
# 		self.height = height
# 		#self.height = width // 4
# 		self.screen = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF)
# 		self.background = pygame.image.load('Images/background.png')  # ../HangMan_pygame/Images/
# 		# self.background = pygame.Surface(self.screen.get_size()).convert()
# 		# self.clock = pygame.time.Clock()
# 		# self.fps = fps
# 		# self.playtime = 0.0
# 		self.font = pygame.font.SysFont('mono', 20, bold=True)
#
#
# 	def run(self):
# 		running = True
# 		while running:
# 			for event in pygame.event.get():
# 				if event.type == pygame.QUIT:
# 					running = False
# 				elif event.type == pygame.KEYDOWN:
# 					if event.key == pygame.K_ESCAPE:
# 						running = False
# 			self.draw_text('HangMan')
# 			pygame.display.flip()
# 			self.screen.blit(self.background, (0, 0))
# 		pygame.quit()
#
# 	def draw_text(self, text):
# 		fw, fh = self.font.size(text)
# 		surface = self.font.render(text, True, (0, 255, 0))
# 		self.screen.blit(surface, ((self.width - fw) // 2, (self.height - fh) // 2))
#
#
# OnePlayerPG(640, 480).run()