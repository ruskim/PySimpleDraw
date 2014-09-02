import pygame


class PySimpleDraw(object):
    def __init__(self):
        self.X = 1000
        self.Y = 1000
        self.R = 0
        self.G = 0
        self.B = 0
        self.W = 1

        pygame.init()
        self.window = pygame.display.set_mode((self.X, self.Y))
        self.white = pygame.Color(255, 255, 255)
        self.black = pygame.Color(0, 0, 0)
        self.window.fill(self.white)

    def tr_x(self, x, y):
        return x + self.X/2

    def tr_y(self, x, y):
        return self.Y/2 - y

    def draw_line(self, x1, y1, x2, y2, w):
        pygame.draw.line(self.window, pygame.Color(self.R, self.G, self.B),
                          (self.tr_x(x1, y1), self.tr_y(x1,y1)), (self.tr_x(x2, y2), self.tr_y(x2, y2)), w)

    def set_color(self, r, g, b):
        self.R = r
        self.G = g
        self.B = b

    def event_loop(self):
        pygame.display.flip()

        do_tick = 'tick' in globals()
        do_exit = False

        clock = pygame.time.Clock()

        while not do_exit:
            clock.tick(50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    do_exit = True
                    break

            if do_tick:
                self.window.fill(self.white)
                tick()
                pygame.display.flip()

psd = PySimpleDraw()


def l(x1, y1, x2, y2, w=psd.W):
    psd.draw_line(x1, y1, x2, y2, w)


def c(r, g, b):
    psd.set_color(r, g, b)

execfile("picture.py")

psd.event_loop()
