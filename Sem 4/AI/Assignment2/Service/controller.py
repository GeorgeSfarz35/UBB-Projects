
class Controller:
    def __init__(self, repo):
        self.__repository = repo

    def searchAStar(self, mapM, droneD, initialX, initialY, finalX, finalY):
        return self.__repository.searchAStar(mapM, droneD, initialX, initialY, finalX, finalY)

    def getDisplayImage(self, image, path):
        return self.__repository.displayWithPath(image, path)