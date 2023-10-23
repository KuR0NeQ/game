import pygame

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((1280,920)) #создание экрана
pygame.display.set_caption("лютый марио") #название игры в окошке
icon = pygame.image.load("icongame.png") #подгрузка иконки
pygame.display.set_icon(icon) #постанвка иконки
pikch = pygame.image.load("pikcher.jpg")
walk_left = [
    pygame.image.load("linkleft/game_now_1.png"), # подгрузка всех картинок
    pygame.image.load("linkleft/game_now_2.png"),
    pygame.image.load("linkleft/game_now_3.png"),
    pygame.image.load("linkleft/game_now_4.png"),
    #pygame.image.load("linkleft/link5.png"),
]
walk_right = [
    pygame.image.load("linkrit/link1.png").convert_alpha(),
    pygame.image.load("linkrit/link2.png").convert_alpha(),
    pygame.image.load("linkrit/link3.png").convert_alpha(),
    pygame.image.load("linkrit/link4.png").convert_alpha(),
    pygame.image.load("linkrit/link5.png").convert_alpha(),
]


ghost = pygame.image.load("linkleft/link1-transformed.png").convert_alpha()
ghost_x = 620


player_anim_count = 0
bg_x = 0
player_speed = 5
player_x = 150
player_y = 600
is_jump = False
jump_count = 7

bg_sound = pygame.mixer.Sound("saunt/OST Remastered — Lost Woods (From _Legend of Zelda_ Ocarina of Time_) (www.lightaudio.ru).mp3")
bg_sound.play() #добавление музыка при запуке
ranning = True
while ranning:


    screen.blit(pikch,(bg_x,0)) #вывод фона
    screen.blit(pikch, (bg_x-1280, 0))
    screen.blit(ghost, (ghost_x,600))

    player_rect = walk_left[0].get_rect(topleft=(player_x,player_y))
    ghost_rect = ghost.get_rect(topleft=(ghost_x,600))


    if player_rect.colliderect(ghost_rect):
        print("You lose")



    keys = pygame.key.get_pressed()#добовление клваши ходьбы
    if keys[pygame.K_d]: #проверка на сторону передвижения
        screen.blit(walk_right[player_anim_count],(player_x,player_y))# ПОДГРУЗКА ПЕРСООНАЖА
    else:
        screen.blit(walk_left[player_anim_count], (player_x, player_y))




    if keys[pygame.K_a] and player_x > 50:
        player_x -= player_speed # передвижение и ограничения
    elif keys[pygame.K_d] and player_x < 1230:
        player_x += player_speed

    if not is_jump:
        if keys[pygame.K_w]:
            is_jump = True
    else:
        if  jump_count >= -7:
            if jump_count > 0:
                player_y -= (jump_count ** 2) / 2
            else :
                player_y += (jump_count ** 2) / 2
            jump_count -= 1
        else:
            is_jump = False
            jump_count = 7
    ghost_x-=10


    if player_anim_count == 3:
        player_anim_count = 0
    else:
        player_anim_count += 1 #смена анимаций

    bg_x +=2
    if bg_x == 1280:
        bg_x = 0 #  перемещение фона




    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ranning = False
            pygame.quit()
    clock.tick(10)#фрейтам(количесво анимаций за 1 секунду )