import datetime
import time

import pygame
from pygame import KEYDOWN

BLUE  = (0, 0, 255)
GRAYBLUE = (50 ,120 ,120)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class UI:
    def __init__(self, controller):
        self.__controller=controller
        # initialize the pygame module
        pygame.init()
        # load and set the logo
        logo = pygame.image.load("logo32x32.png")
        pygame.display.set_icon(logo)
        pygame.display.set_caption("Path in simple environment")

    def run(self, d, m):
        # create a surface on screen that has the size of 400 x 480
        screen = pygame.display.set_mode((400, 400))
        screen.fill(WHITE)

        # define a variable to control the main loop
        running = True
        begin_time = datetime.datetime.now()
        path = self.__controller.searchAStar(m.surface, d, d.x, d.y, 19, 19)
        # path= dummysearch()
        print(datetime.datetime.now() - begin_time)
        print(path)
        # main loop
        while running:
            # event handling, gets all event from the event queue
            for event in pygame.event.get():
                # only do something if the event is of type QUIT
                if event.type == pygame.QUIT:
                    # change the value to False, to exit the main loop
                    running = False

                if event.type == KEYDOWN:
                    d.move(m)  # this call will be erased

            screen.blit(d.mapWithDrone(m.image()), (0, 0))
            pygame.display.flip()

        screen.blit(self.__controller.getDisplayImage(m.image(), path), (0, 0))

        pygame.display.flip()
        time.sleep(5)
        pygame.quit()
