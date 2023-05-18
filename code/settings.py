import pygame.time
screen_width = 700
screen_height = 700

screen = pygame.display.set_mode((screen_width, screen_height))

fps = 60
tile_size = 35
game_over = 0
main_menu = True
level = 1
max_levels = 7

# load images
sun_img = pygame.image.load('../img/sun.png')
bg_img = pygame.image.load('../img/sky.png')
restart_img = pygame.image.load('../img/restart_btn.png')
start_img = pygame.image.load('../img/start_btn.png')
exit_img = pygame.image.load('../img/exit_btn.png')
coin_img = pygame.image.load('../img/coin.png')
coin = pygame.transform.scale(coin_img, (20, 20))

score = 0
