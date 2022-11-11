import pygame
pygame.init()
class Bola (pygame.sprite.Sprite): # aqui se 
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("E: /").convert_alpha()
        self.rect = self.image.get_rect()
#-------------------------------------- MUROS------------------------------------------------
def construir_mapa (mapa):
    listaMuros = []
    x = 0
    y = 0
    for fila in mapa:
        for muro in fila:
            listaMuros.append(pygame.Rect(x,y,80,80))
            x
class Pared (pygame.sprite.Sprite): # aqui se carga una imagencon sprite
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("E: /").convert_alpha()
        self.rect = self.image.get_rect()
ancho =1200
alto = 700
movil = pygame.Rect(600,400,40,40)
x = 0
y=0
vel = 0
alt = 0
negro  = (0,0,0)
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

            Bola.rect.x = movil.x
            Bola.rect.y = movil.y

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
                        Pared.rect.x=x
                        Pared.rect.y=y
                        listaPared.add(Pared)
                        listaPared.draw(ventana)
                    x += 80
                x =0
                y +=80
            lista.Bola.draw(ventana)
            pygame.display.flip()
        pygame.quit()
