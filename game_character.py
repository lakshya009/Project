import sys

import pygame

class DoIt:
	"""My Fav."""

	def __init__(self):
		"""Initaializing the image."""

		pygame.init()

		self.screen = pygame.display.set_mode((1200,700))
		self. image = pygame.image.load('pm.bmp')

		self.screen_rect = self.screen.get_rect()
		self.img_rect = self.image.get_rect()

		self.bg_color = (173, 216, 230)


	def runme(self):
		"""Runnin' it."""

		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

			self.screen.fill(self.bg_color)
			self.img_rect.center = self.screen_rect.center
			self.screen.blit(self.image, self.img_rect)

			pygame.display.flip()


if __name__ == '__main__':
	di = DoIt()
	di.runme()