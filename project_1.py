#Andy Chuong
#TA: Aaron Davis
#February 25,2014
#Project 1
#Robot playing soccer game using ideas from bug_game.py
#and formatted similiar to pygame_skeleton.py

"""
The goal of this game is for the player(robot) to make the ball into the
goal without letting the ball hit the cones. If the ball hits the cones,
the ball returns to the starting point and the player must start over. 
After each goal is scored, the score(upper right of window) increases
by one, and the map is reset for another round. To quit the game the 
player must press q.
"""

# Import this to have Python 2.7 behave like Python 3.2
from __future__ import division, absolute_import, print_function, unicode_literals

# Common modules to import
import time
import pygame
from pygame.locals import *
import random

# Some constants for use later 
GAME_TITLE = "Robot Soccer" #Game Title
DISPLAY_SIZE = (640,480)	#Game size
DESIRED_FPS = 30   			#Game FPS

# Initialize pygame
pygame.init()
pygame.font.init()

# Create a display for the game (this creates a window)
screen = pygame.display.set_mode(DISPLAY_SIZE)
pygame.display.set_caption(GAME_TITLE)

# Create a clock to try to keep the game running at however many FPS
fps_clock = pygame.time.Clock()

game_running = True 

# Initial game variables

	#Score
score = 0
	#loading images
player = pygame.image.load("images/robot2.png")
ball = pygame.image.load("images/PixarBall.png")
goal = pygame.image.load("images/goal1.png")
background = pygame.image.load("images/grass123.jpg")
goalsign = pygame.image.load("images/goalsign.png")
cone = pygame.image.load("images/cone.png")
cone2 = pygame.image.load("images/cone.png")
cone3 = pygame.image.load("images/cone.png")
cone4 = pygame.image.load("images/cone.png")
myfont = pygame.font.SysFont("monospace", 20)
label = myfont.render("Score:", 1, (0,0,0))
label2 = myfont.render(score, 1, (0,0,0))

	#ball starting location
ballX = 280
ballY = 100
	#Player starting location
playerX = 0
playerY = 0
	#Goal Location
goalX = 220
goalY = 400
	#Goal Banner Location
goalSignX = 90
goalSignY = 220


	#Cone Location found by random.randint
coneY = random.randint(142, DISPLAY_SIZE[1] - cone.get_height() - goal.get_height())
coneY2 = random.randint(142, DISPLAY_SIZE[1] - cone.get_height() - goal.get_height())
coneY3 = random.randint(142, DISPLAY_SIZE[1] - cone.get_height() - goal.get_height())
coneY4 = random.randint(142, DISPLAY_SIZE[1] - cone.get_height() - goal.get_height())
coneX = random.randint(0, DISPLAY_SIZE[0] - cone.get_width())
coneX2 = random.randint(0, DISPLAY_SIZE[0] - cone.get_width())
coneX3 = random.randint(0, DISPLAY_SIZE[0] - cone.get_width())
coneX4 = random.randint(0, DISPLAY_SIZE[0] - cone.get_width())

#Global variable for goalScore to be used later
goalScored = False

#Functions
def moveLess(x):
	return x - 2
def moveMore(x):
	return x + 2
def ballDefaultX():
	return 280 
def ballDefaultY():
	return 100

##########################
### The main game loop ###
##########################


while game_running:
	
    ##########################
    ### Capture user input ###
    ##########################
	user_input = pygame.event.get()
	pressed_keys = pygame.key.get_pressed()
	mouse_position = pygame.mouse.get_pos()
	mouse_buttons = pygame.mouse.get_pressed()
    
    #############################
    ### Update the game model ###
    #############################
    #Quit game
	if pressed_keys[K_q]:
		game_running = False
	#Move player
	if pressed_keys[K_UP]:
		playerY = moveLess(playerY)
	if pressed_keys[K_DOWN]:
		playerY = moveMore(playerY)
	if pressed_keys[K_LEFT]:
		playerX = moveLess(playerX)
	if pressed_keys[K_RIGHT]:
		playerX = moveMore(playerX)
    
    #invisible boxes around objects to sense other objects
	ball_box = Rect( (ballX, ballY), ball.get_size())
	player_box = Rect( (playerX, playerY), player.get_size())
	goal_box = Rect( (goalX, goalY), goal.get_size())
	cone1_box = Rect( (coneX, coneY), cone.get_size())
	cone2_box = Rect( (coneX2, coneY2), cone.get_size())
	cone3_box = Rect( (coneX3, coneY3), cone.get_size())
	cone4_box = Rect( (coneX3, coneY4), cone.get_size())
	
    #player pushing ball
	if player_box.colliderect(ball_box):       # The two are touching
		topBottom = False
		leftRight = False
		#Ranges to test collision spot
		ballxRange = range(ballX,ballX + ball.get_width() + 1)
		ballyRange = range(ballY, ballY + ball.get_height() + 1)
		playeryRange = range(playerY, playerY + player.get_height() + 1)
		playerxRange = range(playerX, playerX + player.get_width() + 1)
		#Test of player is on top/bottom or left/right of ball
		for x in ballxRange:
			if x in playerxRange:
				topBottom = True
			else:
				leftRight = True
		#Tests of player is above or below ball
		if topBottom == True:
			if playerY < ballY:
				ballY = moveMore(ballY)
			elif playerY > ballY:
				ballY = moveLess(ballY)
		#Tests if player os to the right or left of ball
		if leftRight == True:
			if playerX < ballX:  # player to left
				ballX = moveMore(ballX)
			elif playerX > ballX:
				ballX = moveLess(ballX)
	#if ball makes it into goal
	if ball_box.colliderect(goal_box):        # The two are touching
		#increase score
		score = score + 1
		#print score in the terminal
		print ("Current Score is", score)
		#sets goalScore to true for while loop
		goalScored = True
		#while loop displays the goalsign saying "GOAL" for 1 second
		while goalScored:
			screen.blit(goalsign, (goalSignX,goalSignY))
			#print("in while")
			pygame.display.flip()
			time.sleep(1)
			goalScored = False
		#initializes another round of the game
		ballX = ballDefaultX()
		ballY = ballDefaultY()
		coneY = random.randint(142, DISPLAY_SIZE[1] - cone.get_height() - goal.get_height())
		coneY2 = random.randint(142, DISPLAY_SIZE[1] - cone.get_height() - goal.get_height())
		coneY3 = random.randint(142, DISPLAY_SIZE[1] - cone.get_height() - goal.get_height())
		coneY4 = random.randint(142, DISPLAY_SIZE[1] - cone.get_height() - goal.get_height())
		coneX = random.randint(0, DISPLAY_SIZE[0] - cone.get_width())
		coneX2 = random.randint(0, DISPLAY_SIZE[0] - cone.get_width())
		coneX3 = random.randint(0, DISPLAY_SIZE[0] - cone.get_width())
		coneX4 = random.randint(0, DISPLAY_SIZE[0] - cone.get_width())
		
	#if ball hits cone, ball returns to starting position
	if ball_box.colliderect(cone1_box):
		ballX = ballDefaultX()
		ballY = ballDefaultY()
	if ball_box.colliderect(cone2_box):
		ballX = ballDefaultX()
		ballY = ballDefaultY()
	if ball_box.colliderect(cone3_box):
		ballX = ballDefaultX()
		ballY = ballDefaultY()
	if ball_box.colliderect(cone4_box):
		ballX = ballDefaultX()
		ballY = ballDefaultY()

	#labels for the score overlay and quit overlay
	label2 = myfont.render(str(score), 1, (0,0,0))
	label3 = myfont.render("Press q to quit", 1, (225,0,0))
	
    #####################################
    ### Redraw the game on the screen ###
    #####################################
	screen.blit(background, (0,0))
	screen.blit(goal, (goalX, goalY))  
	screen.blit(cone, (coneX, coneY))
	screen.blit(cone2, (coneX2, coneY2))
	screen.blit(cone3, (coneX3, coneY3))
	screen.blit(cone4, (coneX4, coneY4))
	screen.blit(player, (playerX, playerY)) 
	screen.blit(ball, (ballX, ballY))
	screen.blit(label, (540,0))
	screen.blit(label2, (610,0))
	screen.blit(label3, (450, 455))

	pygame.display.flip()
	# Wait until this frame is finished (as per the FPS clock)
	#fps_clock.tick(DESIRED_FPS)
	

# All done!  Cleanup time
pygame.quit()
