
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

    def __intersectsX(self, other):
        otherPosition = other.getPosition()
        otherSize = other.getSize()

        if self.__position[0] >= otherPosition[0] and self.__position[0] <= (otherPosition[0] + otherSize[0]):
            return True
        if (self.__position[0] + self.__size[0]) >= otherPosition[0] and (self.__position[0] + self.__size[0]) <= (
                otherPosition[0] + otherSize[0]):
            return True
        return False

    def __intersectsY(self, other):
        otherPosition = other.getPosition()
        otherSize = other.getSize()

        if self.__position[1] >= otherPosition[1] and self.__position[1] <= (otherPosition[1] + otherSize[1]):
            return True
        if (self.__position[1] + self.__size[1]) >= otherPosition[1] and (self.__position[1] + self.__size[1]) <= (
                otherPosition[1] + otherSize[1]):
            return True
        return False

    def intersects(self, other):
        if self.__intersectsX(other) and self.__intersectsY(other):
            return True
        return False
