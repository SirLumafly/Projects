import pygame
import random
pygame.init()
pygame.display.set_caption('flappy bird')

DISPLAY = pygame.display.set_mode((500, 500))
#gravity vars
pipe_offset = random.randint(-40, 40)
flapforce = -2
velocity = 0
bird_x = 235
bird_y = 0
acc = 0.05
top_pipe_x = 500
top_pipe_y = -50 + (pipe_offset * 2)
pipe_offset = random.randint(0, 20)
bottom_pipe_x = 500
bottom_pipe_y = 350 + (pipe_offset * 2)

#variables
the_end = False
Score = 0
clock = pygame.time.Clock()
replay = False

while True:
	#screen
	DISPLAY.fill((255, 255, 255))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit()

	#keys
	keys=pygame.key.get_pressed()

	#sprites
	pre_bird = pygame.image.load("res/gfx/bird.png")
	bird = pygame.transform.scale(pre_bird, (83.9, 72.1))
	DISPLAY.blit(bird, (bird_x, bird_y))

	pre_top_pipe_sprite = pygame.image.load("res/gfx/top_pipe.png")
	top_pipe_sprite = pygame.transform.scale(pre_top_pipe_sprite, (80.6, 238))
	DISPLAY.blit(top_pipe_sprite, (top_pipe_x, top_pipe_y))
	pre_bottom_pipe_sprite = pygame.image.load("res/gfx/bottom_pipe.png")
	bottom_pipe_sprite = pygame.transform.scale(pre_bottom_pipe_sprite, (80.6, 238))
	DISPLAY.blit(bottom_pipe_sprite, (bottom_pipe_x, bottom_pipe_y))

	the_end_sprite = pygame.image.load("res/gfx/lose_screen.png")

	#Colliders
	bird_collider = [
		pygame.Rect((bird_x+15, bird_y+15 , 50, 50))
	]
	top_pipe_collider = [
		pygame.Rect((top_pipe_x, top_pipe_y, 80.6, 238))
	]
	bottom_pipe_collider = [
		pygame.Rect((bottom_pipe_x, bottom_pipe_y, 80.6, 238))
	]

	#collision detection
	for a in top_pipe_collider:
		if a.colliderect(bird_collider[0]):
			the_end = True
	for b in bottom_pipe_collider:
		if b.colliderect(bird_collider[0]):
			the_end = True

	#gravity and keyboard input
	if event.type == pygame.MOUSEBUTTONDOWN or keys[pygame.K_SPACE]:
		velocity = flapforce

	bird_y += velocity
	velocity += acc

	bottom_pipe_x -= 1.7
	top_pipe_x -= 1.7
	if bottom_pipe_x and top_pipe_x < -200:
		Score += 1
		pipe_offset = random.randint(0, 20)
		bottom_pipe_y = 350 + (pipe_offset * 2)
		top_pipe_y = -50 + (pipe_offset * 2)
		bottom_pipe_x = 500
		top_pipe_x = 500

	#Score
	font = pygame.font.Font("res/font/font.otf", 50)
	score_display = font.render(str(Score), True, (0, 0, 0))
	DISPLAY.blit(score_display, (250, 0))

	#end screen
	if the_end == True:
		DISPLAY.fill((255, 255, 255))
		DISPLAY.blit(the_end_sprite, (100, 250))
		if event.type == pygame.MOUSEBUTTONDOWN or keys[pygame.K_SPACE]:
			replay = True
	if replay == True:
		bird_x = 235
		bird_y = 0
		Score = 0
		the_end = False
		replay = False
	pygame.display.update()
