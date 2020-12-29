from Game.Shared import *


class Pad(GameObject):
    def __init__(self, position, sprite, game):
        super(Pad, self).__init__(position, GameConstants.padSize, sprite)

    def setSpeed(self, newSpeed):
        self.__speed = newSpeed

    def resetSpeed(self):
        self.setSpeed(3)

    def getSpeed(self):
        return self.__speed

    def isInMotion(self):
        return self.__inMotion

    def setMotion(self, isMoving):
        self.__inMotion = isMoving
        self.resetSpeed()

    def changeDirection(self, gameObject):
        pass

    def updatePosition(self):
        pass

    def isBallDead(self):
        pass
