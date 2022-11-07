import pygame
pygame.init()
class Pared(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("")
ancho =1200
alto = 700
movil = pygame.Rect(600,400,40,40)
x = 0
y=0
vel = 0
alt = 0
negro (0,0,0)
ventana = pygame.display.set_mode((ancho,alto))
pygame.display.set_caption("muro")
reloj = pygame.time.Clock()
mapa =[
    "XXXXXXXXXXX",
    "X         X",
    "X XXXXXXX X",
    "X XXXXXXXXX",
    "X    X    X",
    "XX XX XX XX",
    "XXXXXXXXXXX",

]
gameOver = False
while not gameOver:
    reloj.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                vel =-5
            elif event.key == pygame.K_RIGHT:
                vel =+5
            elif event.key == pygame.K_UP:
                alt =-5
            elif event.key == pygame.K_DOWN:
                alt =+5
            else:
                vel = 0
                alt = 0
            movil.x += vel
            movil.y += alt

            bola.rect.x = movil.x
            bola.rect.y = movil.y

            for muro in listaMuro :
                if movil.colliderect(muro):
                    movil.x -= vel
                    movil.y -= alt
            ##################################
            ventana.fill(NEGRO)
            ##################################
            x = 0
            y = 0
            for fila in mapa:
                for muro in fila:
                    if muro == "X":
                        pared.rect.x=x
                        pared.rect.y=y
                        listaPared.add(Pared)
                        listaPared.draw(ventana)
                    x += 80
                x =0
                y +=80
            listaBola.draw(ventana)
            pygame.display.flip()
        pygame.quit()
