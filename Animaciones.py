import pygame,sys
def move(last_update,current_time,cooldown,frame):
    if current_time - last_update >= cooldown:
        frame += 1
        last_update = current_time
        if frame >= len(walk_right):
            frame = 0

pygame.init()

screen_size = (1200,800)

screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()

pos_x = 10
pos_y = 100
vel_x = 3
vel_y = 0
direction = 0

animations = []
init_pose_right = [pygame.image.load("pose_inicial_derecha/Mago_pose_inicial_animado1.png"),
                   pygame.image.load("pose_inicial_derecha/Mago_pose_inicial_animado2.png"),
                   pygame.image.load("pose_inicial_derecha/Mago_pose_inicial_animado3.png"),
                   pygame.image.load("pose_inicial_derecha/Mago_pose_inicial_animado4.png")]
init_pose_left = [pygame.image.load("pose_inicial_izquierda/Mago_pose_inicial_animado1.png"),
                   pygame.image.load("pose_inicial_izquierda/Mago_pose_inicial_animado2.png"),
                   pygame.image.load("pose_inicial_izquierda/Mago_pose_inicial_animado3.png"),
                   pygame.image.load("pose_inicial_izquierda/Mago_pose_inicial_animado4.png")]
walk_right = [pygame.image.load("caminar_derecha/Mago_caminando1.png"),
              pygame.image.load("caminar_derecha/Mago_caminando2.png"),
              pygame.image.load("caminar_derecha/Mago_caminando3.png"),
              pygame.image.load("caminar_derecha/Mago_caminando4.png")]
walk_left =  [pygame.image.load("caminar_izquierda/Mago_caminando_izq1.png"),
              pygame.image.load("caminar_izquierda/Mago_caminando_izq2.png"),
              pygame.image.load("caminar_izquierda/Mago_caminando_izq3.png"),
              pygame.image.load("caminar_izquierda/Mago_caminando_izq4.png")]

animations = [init_pose_right,init_pose_left,walk_right,walk_left]

frame = 0
cooldown = 100
last_update = pygame.time.get_ticks()
lose = False

while not lose:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYUP:
            direction = 0
    screen.fill((0, 0, 0))
    #Logica
    current_time = pygame.time.get_ticks()

    keys = pygame.key.get_pressed()
    if current_time - last_update >= cooldown:
        frame += 1
        last_update = current_time
        if frame >= len(walk_right):
            frame = 0
    if keys[pygame.K_RIGHT]:
        direction = 1
        pos_x += vel_x
    if keys[pygame.K_LEFT]:
        direction = 2
        pos_x -= vel_x
    #Pintar Pantalla
    #Zona de dibujo
    if direction == 0:
        screen.blit(animations[0][frame], (pos_x, pos_y))
    if direction == 1:
        screen.blit(animations[2][frame], (pos_x, pos_y))
    if direction == 2:
        screen.blit(animations[3][frame], (pos_x, pos_y))
    #Refrescar Pantalla
    pygame.display.flip()
    clock.tick(27)
