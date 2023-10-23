import pygame

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((1920,1080))#здание экрана
pygame.display.set_caption("лютый марио") #название игры в окошке
#icon = pygame.image.load("icongame.png") #подгрузка иконки
#pygame.display.set_icon(icon) #постанвка иконки
mup = pygame.image.load("linkleft/mup.png")

walk_left = [
    pygame.image.load("linkleft/game_now_1.png"), # подгрузка всех картинок
    pygame.image.load("linkleft/game_now_2.png"),
    pygame.image.load("linkleft/game_now_3.png"),
    pygame.image.load("linkleft/game_now_4.png"),
]
player_anim_count = 1
player_speed = 10
player_x = 300
player_y = 600


ranning = True
while ranning:
    screen.blit(mup , (0,50))

    keys = pygame.key.get_pressed()  # добовление клваши ходьбы
    screen.blit(walk_left[player_anim_count], (player_x, player_y))

    if keys[pygame.K_a] and player_x > 50:
        player_x -= player_speed
    if keys[pygame.K_d] and player_x < 1230:
        player_x += player_speed
    if keys[pygame.K_w] and player_y > 50:
        player_y -= player_speed
    if keys[pygame.K_s] and player_y < 870:
        player_y += player_speed

    if player_anim_count == 3:
        player_anim_count = 0
    else:
        player_anim_count += 1 #смена анимаций

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ranning = False
            pygame.quit()
    clock.tick(16)  # фрейтам(количесво анимаций за 1 секунду )