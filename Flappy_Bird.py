'''		Flappy Bird Game Replica Attempt	'''

import pygame
import random
import sys




#______________________ COLOURS _________________________

WHITE  = (255,255,255)
BLACK  = (0  ,0  ,0  )
RED    = (255,0  ,0  )
GREEN  = (0  ,255,0  )
BLUE   = (0  ,0  ,255)
YELLOW = (255,255,0  )

#_____________________ PARAMETERS _______________________

BIRD_COL = YELLOW
SCREEN_COL = BLACK
OBST_COL = RED



class Flappy_Bird:
	def __init__(self,
				 win_width = 640,
				 win_height = 480,
				 bird_size = 20,
				 obst_size = 40, # obstacle_size
				 gravity = 10,
				 flight_force = 50,
				 h_move_speed = 10
				):
			# Predefined vars
		self.win_width  = win_width
		self.win_height = win_height

		self.bird_size  = bird_size
		self.obst_size  = obst_size
		self.gravity    = gravity
		self.flight_force = flight_force
		self.h_move_speed = h_move_speed

			# Newly defined
		self.score = 0



		def draw_scene(self):
			pass

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
			pass

		def is_collision(self):
			pass

		def game_over(self):
			pass


def main():
	pass




if __name__ == '__main__':
	main()
