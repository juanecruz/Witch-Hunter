import pygame
pygame.init()
screen_size = (900,500)

screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()

caminata_derecha = [pygame.image.load("Caminata_derecha/Mago_caminando1.png"),
                    pygame.image.load("Caminata_derecha/Mago_caminando2.png"),
                    pygame.image.load("Caminata_derecha/Mago_caminando3.png"),
                    pygame.image.load("Caminata_derecha/Mago_caminando4.png")]
caminata_izquierda = [pygame.image.load("Caminata_izquierda/Mago_caminand_izq1.png"),
                     pygame.image.load("Caminata_izquierda/Mago_caminand_izq2.png"),
                     pygame.image.load("Caminata_izquierda/Mago_caminand_izq3.png"),
                     pygame.image.load("Caminata_izquierda/Mago_caminand_izq4.png")]

x = 0
y = 200
vel = 4
frame = 0
last_update = pygame.time.get_ticks()
print(last_update)
cooldown = 150

while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break

    screen.fill((0,0,0))

    current_time = pygame.time.get_ticks()
    screen.blit(caminata_derecha[frame],[x,y])

    if current_time - last_update >= cooldown:
        frame += 1
        last_update = current_time
        if frame >= len(caminata_derecha):
            frame = 0


    pygame.display.flip()
    clock.tick(60)


pygame.quit()

