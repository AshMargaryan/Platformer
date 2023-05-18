import pygame
from pygame.locals import *
from pygame import mixer

import pickle
from os import path

from settings import *

from world import *
from text import *

from buttons import *
from player import *

from lava import *
from exit import *
from enemy import *
from coins import *
from moving_platforms import *

pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()
pygame.init()

clock = pygame.time.Clock()

pygame.display.set_caption('Platformer')
# fonts sounds
font = pygame.font.SysFont("Bauhaus 93", 70)
font_score = pygame.font.SysFont("Bauhaus 93", 25)

pygame.mixer.music.load("../sounds/sinnesloschen-beam-117362.mp3")
pygame.mixer.music.play(-1, 0.0, 5000)

coin_fx = pygame.mixer.Sound("../sounds/coin.wav")
coin_fx.set_volume(0.5)

jump_fx = pygame.mixer.Sound("../sounds/jump.wav")
jump_fx.set_volume(0.5)

game_over_fx = pygame.mixer.Sound("../sounds/game_over.wav")
game_over_fx.set_volume(0.5)

# function to reset level
def reset_level(level):
	player.reset(100, screen_height - 130)
	blob_group.empty()
	lava_group.empty()
	exit_group.empty()
	platform_group.empty()
	coin_group.empty()

	# load in level data and create world
	if path.exists(f'../levels/level{level}_data'):
		pickle_in = open(f'../levels/level{level}_data', 'rb')
		world_data = pickle.load(pickle_in)
	world = World(world_data)

	return world


player = Player(100, screen_height - 130)

# load in level data and create world
if path.exists(f'../levels/level{level}_data'):
	pickle_in = open(f'../levels/level{level}_data', 'rb')
	world_data = pickle.load(pickle_in)
world = World(world_data)


run = True
while run:

	clock.tick(fps)

	screen.blit(bg_img, (0, 0))
	screen.blit(sun_img, (100, 100))

	if main_menu == True:
		if exit_button.draw():
			run = False
		if start_button.draw():
			main_menu = False
	else:
		world.draw()

		if game_over == 0:
			blob_group.update()
			platform_group.update()
			if pygame.sprite.spritecollide(player, coin_group, True):
				score += 1
				coin_fx.play()
			draw_text("%s" %score, font_score, "white",  tile_size, 5)
			screen.blit(coin, (10, 8))

		blob_group.draw(screen)
		platform_group.draw(screen)
		lava_group.draw(screen)
		exit_group.draw(screen)
		coin_group.draw(screen)

		game_over = player.update(game_over, world, jump_fx, game_over_fx)

		# if player has died
		if game_over == -1:
			draw_text("GAME OVER!", font, "red",  (screen_width // 2) - 170, screen_height // 2)
			if restart_button.draw():
				world_data = []
				world = reset_level(level)
				game_over = 0
				score = 0

		# if player has completed the level
		if game_over == 1:
			# reset game and go to next level
			level += 1
			if level <= max_levels:
				# reset level
				world_data = []
				world = reset_level(level)
				game_over = 0
			else:
				draw_text("You Win", font, "blue", (screen_width // 2) - 140, screen_height // 2)
				if restart_button.draw():
					score = 0
					level = 1
					# reset level
					world_data = []
					world = reset_level(level)
					game_over = 0

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False


	pygame.display.update()

pygame.quit()