import pygame

def main():
	pygame.init()
	
	logo = pygame.image.load('logo32x32.png')
	pygame.display.set_icon(logo)
	pygame.display.set_caption('bq666 first')
	
	screen_width = 320
	screen_hight = 240
	screen = pygame.display.set_mode((screen_width, screen_hight))
	
	
	# logo = pygame.image.load('foo.jpg').convert_alpha()
	image = pygame.image.load('01_image.png')
	image.set_colorkey((255,0,255))
	# image.set_alpha(128)
	bgd_image = pygame.image.load('background.png')
	
	screen.blit(bgd_image,(0,0))
	screen.blit(image, (50,50))
	
	xpos = 50
	ypos = 50
	step_x = 0.5
	step_y = 0.5


	# screen.blit(image, (50, 50))
	# screen.fill((r,g,b))
	# pygame.NOFRAME
	
	# box = pygame.Rect(10, 10, 50, 50)
	# keys = pygame.key.get_pressed()
	# if keys[pygame.K_d]:
	# 	box.x += 1

	
	running = True
	
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
		if xpos > screen_width - 64 or xpos < 0:
			step_x = - step_x
		if ypos > screen_hight - 64 or ypos < 0:
			step_y = - step_y
		xpos += step_x
		ypos += step_y
		screen.blit(bgd_image, (0, 0))
		screen.blit(image, (xpos, ypos))
		pygame.display.flip()
		# pygame.display.update()
	
# draw method from pygame.sprites.RenderUpdates
def draw(self, surface):
   spritedict = self.spritedict               # {sprite:old_rect}
   surface_blit = surface.blit                # speed up
   dirty = self.lostsprites                   # dirty rects (from removed sprites)
   self.lostsprites = []
   dirty_append = dirty.append                # speed up
   for s in self.sprites():
       r = spritedict[s]                      # get the old_rect
       newrect = surface_blit(s.image, s.rect)# draw it
       if r is 0:                             # first time the old_rect is 0
           dirty_append(newrect)              # add the rect from the blit, nothing else to do
       else:
           if newrect.colliderect(r):         # if the old_rect and the newrect overlap, case 3
               dirty_append(newrect.union(r)) # append the union of these two rects
           else:
               dirty_append(newrect)          # not overlapping so append both, newrect and
               dirty_append(r)                # old_rect to the dirty list, case 5
       spritedict[s] = newrect                # replace the old one with the new one
   return dirty
	
	
main()