import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""Class to represent the alien fleet."""

	def __init__(self, ai_game):
		"""Initialization of the alien."""

		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings

		# Loading the alien image and setting it's rect attribute.
		self.image = pygame.image.load("images/alien.bmp")
		self.rect = self.image.get_rect()

		# Start each new alien near the top left corner
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# Storing the exact horizontal position of alien
		self.x = float(self.rect.x)


	def check_edges(self):
		"""Return True if alien is at edge of screeen."""

		screen_rect = self.screen.get_rect()

		if self.rect.right >= screen_rect.right or self.rect.left < 0:
			return True


	def update(self):
		"""Move aliens to the right or left."""

		self.x += (self.settings.alien_speed * self.settings.fleet_direction)
		self.rect.x = self.x