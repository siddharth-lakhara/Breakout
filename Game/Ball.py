import pygame
from Game.Shared import *


class Ball(GameObject):
    def __init__(self, position, sprite, game):
        self.__game = game
        self.__speed = 3
        self.__increment = [2, 2]
        self.__direction = [1, 1]
        self.__inMotion = 0

        super(Ball, self).__init__(position, GameConstants.ballSize, sprite)

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
        position = self.getPosition()
        size = self.getSize()
        objectPosition = gameObject.getPosition()
        objectSize = gameObject.getSize()

        if position[1] > objectPosition[1] and \
                position[1] < objectPosition[1] + objectSize[1] and \
                position[0] > objectPosition[0] and \
                position[0] < objectPosition[0] + objectSize[0]:
            self.__direction[1] *= -1

        elif position[1] + size[1] > objectPosition[1] and \
                position[1] + size[1] < objectPosition[1] + objectSize[1] and \
                position[0] > objectPosition[0] and \
                position[0] < objectPosition[0] + objectSize[0]:
            self.__direction[1] *= -1

        elif position[0] + size[0] > objectPosition[0] and \
                position[0] + size[0] < objectPosition[0] + objectSize[0]:
            self.__direction[0] *= -1

        else:
            self.__direction[0] *= -1

    def updatePosition(self):
        if not self.isInMotion():
            padPosition = self.__game.getPad().getPosition()
            self.setPosition((
                padPosition[0] + (GameConstants.padSize[0] / 2),
                GameConstants.screenSize[1] - GameConstants.padSize[1] - GameConstants.ballSize[1]
            ))
            return

        position = self.getPosition()
        size = self.getSize()

        newPosition = [position[0] + (self.__increment[0] * self.__speed) * self.__direction[0],
                       position[1] + (self.__increment[1] * self.__speed) * self.__direction[1]]

        if newPosition[0] + size[0] >= GameConstants.screenSize[0]:
            self.__direction[0] *= -1
            newPosition = [GameConstants.screenSize[0] - size[0], newPosition[1]]

        if newPosition[0] <= 0:
            self.__direction[0] *= -1
            newPosition = [0, newPosition[1]]

        if newPosition[1] + size[1] >= GameConstants.screenSize[1]:
            self.__direction[1] *= -1
            newPosition = [newPosition[0], GameConstants.screenSize[1] - size[1]]

        if newPosition[1] <= 0:
            self.__direction[1] *= -1
            newPosition = [newPosition[0], 0]

        self.setPosition(newPosition)

    def isBallDead(self):
        pass
