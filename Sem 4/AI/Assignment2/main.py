
# import the pygame module, so you can use it
import pickle ,pygame ,time
from pygame.locals import *
from random import random, randint
import numpy as np

# Creating some colors
from Entities.drone import Drone
from Entities.map import Map
from Repository.repository import *
from Service.controller import Controller
from UI.ui import UI

BLUE  = (0, 0, 255)
GRAYBLUE = (50 ,120 ,120)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# define directions
UP = 0
DOWN = 2
LEFT = 1
RIGHT = 3

# define indexes variations
v = [[-1, 0], [1, 0], [0, 1], [0, -1]]




# define a main function
def main():
    repository = Repository()
    controller = Controller(repository)
    # we create the map
    m = Map()
    # m.randomMap()
    # m.saveMap("test2.map")
    m.loadMap("test1.map")

    ui = UI(controller)

    # we position the drone somewhere in the area
    x = randint(0, 19)
    y = randint(0, 19)
    # create drona
    d = Drone(x, y)

    ui.run(d,m)


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()
