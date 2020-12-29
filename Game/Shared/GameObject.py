
class GameObject:
    def __init__(self, position, size, sprite):
        self.__position = position
        self.__size = size
        self.__sprite = sprite

    def setPosition(self, newPosition):
        self.__position = newPosition

    def getPosition(self):
        return self.__position

    # def setSize(self, newSize):
    #     self.__size = newSize

    def getSize(self):
        return self.__size

    # def setSprite(self, newSprite):
    #     self.__sprite = newSprite

    def getSprite(self):
        return self.__sprite

    def intersect(self, other):
        pass
