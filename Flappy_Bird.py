'''		Flappy Bird Game Replica Attempt	'''

import pygame
import random
import sys
import time




#______________________ COLOURS _________________________

WHITE  = (255,255,255)
BLACK  = (0  ,0  ,0  )
RED    = (255,0  ,0  )
GREEN  = (0  ,255,0  )
BLUE   = (0  ,0  ,255)
YELLOW = (255,255,0  )

SKY_BLUE_1 = (132,235,232)
SKY_BLUE_2 = (150,235,221)
SKY_BLUE_3 = (162,235,213)

#_______________ SET PARAMETERS/COLOURS _________________

FPS = 60

BIRD_COL = YELLOW
SCREEN_COL = BLACK
OBST_COL = RED



class Flappy_Bird:
	def __init__(self,			   # Aspect ratio 4:3
				 win_width = 800,  # 640
				 win_height = 600, # 480
 				 bird_size = 20,
				 obst_size = 40, # obstacle_size
				 gravity = 10,
				 flight_force = 50,
				 h_move_speed = 10,
				 fps = FPS
				):
			# Predefined vars
		self.win_width  = win_width
		self.win_height = win_height

		self.bird_size  = bird_size
		self.obst_size  = obst_size
		self.gravity    = gravity
		self.flight_force = flight_force
		self.h_move_speed = h_move_speed
		self.fps = fps

			# Newly defined
		self.score = 0
		self.bird_position = []  # Set initial position for the bird
		self.obst_position = []  # Set positions for the obstacles 

			# ***Initialize pygame and dependencies***
		pygame.init()
		self.screen = pygame.display.set_mode((self.win_width, self.win_height))
		pygame.display.set_caption('Flappy Bird Reincarnate')

		self.my_font = pygame.font.SysFont('consolas', 30)
		self.clock = pygame.time.Clock()

			# Init variable to calculate delta time
		self.time_prev = time.time()



	def draw_scene(self):
		rect_top = pygame.Rect((0,0), (self.win_width, self.win_height/3))
		rect_mid = pygame.Rect((0,self.win_height/3), (self.win_width, self.win_height/3))
		rect_bot = pygame.Rect((0,(self.win_height/3)*2), (self.win_width, self.win_height/3))

		pygame.draw.rect(self.screen, SKY_BLUE_1, rect_top)
		pygame.draw.rect(self.screen, SKY_BLUE_2, rect_mid)
		pygame.draw.rect(self.screen, SKY_BLUE_3, rect_bot)

	def draw_bird(self):
		pass

	def draw_obstacles(self):
		pass

	def move_bird(self):
		pass

	def move_obstacle(self):
		pass

	def score(self):
		pass

	def write_score(self):
		pass

	def handle_keys(self):
		for event in pygame.event.get():
				# QUIT
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

				# CONTROLS
			# if event.type == pygame.key_pressed():
			# 	pass 

	def is_collision(self):
		pass

	def game_over(self):
		pass

	def reset_game(self):
		pass

	def delta_time(self):
		pass


def main():
	flappy = Flappy_Bird()

	while True:
		flappy.draw_scene()
		flappy.handle_keys()
	
		pygame.display.update()




if __name__ == '__main__':
	main()
