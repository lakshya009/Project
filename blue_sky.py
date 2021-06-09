import sys

import pygame

from pretty import Pretty

class BlueSky:
	"""Just doing it."""

	def __init__(self):
		"""initializing the window."""
		
		pygame.init()

		self.screen = pygame.display.set_mode((1200, 700))	
		self.pretty = Pretty(self)

		self.bg_color = (173, 216, 230)
		
	def run_game(self):
		"""Running the program."""

		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
			
			self.screen.fill(self.bg_color)
			self.pretty.blitme()
			
			pygame.display.flip()

		
if __name__ == '__main__':
	bs = BlueSky()
	bs.run_game()