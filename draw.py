import pygame

X=1000
Y=1000
R=0
G=0
B=0
W=1

pygame.init()
window = pygame.display.set_mode((X, Y))
white = pygame.Color(255, 255, 255)
black = pygame.Color(0, 0, 0)
window.fill(white)

def trX(x):
    return x+X/2

def trY(y):
    return Y/2-y



def l(x1, y1, x2, y2, w=W):
    pygame.draw.line(window, pygame.Color(R, G, B), (trX(x1), trY(y1)), (trX(x2), trY(y2)), w)


def c(r, g, b):
    global R
    global G
    global B

    R = r
    G = g
    B = b


execfile("picture.py")

pygame.display.flip()

exit = False
while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
            break
