import pygame.font

class ScoreBoard():

	def __init__(self, ai_settings, screen, stats):
		"""initialize score related attributes"""
		self.ai_settings = ai_settings
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.stats = stats

		# font setting of sb
		self.text_color = (30, 30, 30)
		self.font = pygame.font.SysFont(None, 48)

		# prepare starting image
		self.pre_score()

	def pre_score(self):
		"""convert score string to image"""
		score_str = str(self.stats.score)
		self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

		# put score at top right coner
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20

	def show_score(self):
		"""show score on the screen"""
		self.screen.blit(self.score_image, self.score_rect)