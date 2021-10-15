import pygame

BLUE = (0, 0, 255)
GRAYBLUE = (50, 120, 120)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class Repository:
    def __int__(self):
        pass

    def displayWithPath(self, image, path):
        mark = pygame.Surface((20, 20))
        mark.fill(GREEN)
        for move in path:
            image.blit(mark, (move[1] * 20, move[0] * 20))
        drone = pygame.image.load("drona1.png")
        image.blit(drone, (path[-1][1] * 20, path[-1][0] * 20))
        return image
