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
 				 bird_size = 35,
				 obst_w = 60, # obstacle_size
				 obst_h = 400,
				 gravity = 17,
				 flight_force = 11,
				 h_move_speed = 10,
				 fps = FPS
				):
			# Predefined vars
		self.win_width  = win_width
		self.win_height = win_height

		self.bird_size  = bird_size
		self.obst_w  = self.bird_size * 3
		self.obst_h  = obst_h
		self.gravity    = gravity
		self.flight_force = flight_force
		self.h_move_speed = h_move_speed
		self.fps = fps

			# Newly defined
		self.score = 0
		self.bird_position = [[self.win_width/4, self.win_height/4]]  # Set initial position for the bird
		self.obst_position = [[self.win_width+10, -200]]  # Set positions for the obstacles 
		self.jump = 0
		self.obst_move_speed = 5
		self.space_between_obst = self.bird_size * 6
			# Not that optimized as it doesnt take a simple number, rather when the obstacle will spawn
			# in relation to the position on the previous obstacle
		self.obstacle_spawn_rate = self.win_width - (self.win_width/3) # When obst passes 1/3 of width the second one will spawn in this case

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
		rect = pygame.Rect((self.bird_position[0][0], self.bird_position[0][1]), (self.bird_size, self.bird_size))
		pygame.draw.rect(self.screen, YELLOW, rect)

	def move_bird(self):
		# Implementing force of gravity to the y axis of bird position
		self.bird_position.insert(0, (self.bird_position[0][0], self.bird_position[0][1] + self.gravity))

		if self.jump > 0:
			self.bird_position.insert(0, (self.bird_position[0][0], self.bird_position[0][1] - self.jump))
			self.jump -= 1

	def draw_obstacles(self):
		for obst in self.obst_position:
			rect_top = pygame.Rect((obst[0], obst[1]), (self.obst_w, self.obst_h))
			rect_bot = pygame.Rect((obst[0], obst[1]+(self.obst_h+self.space_between_obst)), (self.obst_w, self.obst_h))
			
			pygame.draw.rect(self.screen, BLUE, rect_top)		
			pygame.draw.rect(self.screen, BLUE, rect_bot)

		# Moves obstacles from right to left
	def move_obstacles(self):
		spawn_ready = False
		for i in range(len(self.obst_position)):
			# Moves obstacles from right to left at constant rate
			self.obst_position[i][0] -= self.obst_move_speed 
		
		# Adds obstacles to the right for the bird to pass through
	def add_obstacles(self):
		height_change = random.randint(-350, -50)
		if self.obst_position[-1][0] < self.obstacle_spawn_rate:
			self.obst_position.append([self.win_width+200, height_change])

		# Removes obstacles that are out of view/succesfully passed to the left
		# so the list does not get cluttered and keeps performance high(ish)
	def remove_obstacles(self):
		if self.obst_position[0][0] < -100: # -100
			self.obst_position.pop(0)

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

				# KEYBOARD INPUTS
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					self.jump = 35 

	def is_collision(self):
			# Giving a little buffer zone with +50 so bird has more chance to go further down and up
		if self.bird_position[0][1] > self.win_height + 100:
			return True
		if self.bird_position[0][1] < -300:
			return True

		return False

	def game_over(self):
		pass

		# Sends bird to the initial position
	def reset_game(self):
		self.bird_position = [(self.win_width/4, self.win_height/4)]

	def delta_time(self):
		pass

		# Main functions which combines all others in order to play the game
	def play_game(self):
		self.draw_scene()
		self.draw_bird()
		self.move_bird()
		self.draw_obstacles()
		self.move_obstacles()
		self.add_obstacles()
		self.remove_obstacles()
		self.handle_keys()
	
		pygame.display.update()
		self.clock.tick(self.fps)

		if self.is_collision():
			self.reset_game()


def main():
	flappy = Flappy_Bird()

	while True:
		flappy.play_game()
		# flappy.draw_scene()
		# flappy.draw_bird()
		# flappy.move_bird()
		# flappy.handle_keys()
	
		# pygame.display.update()




if __name__ == '__main__':
	main()
