import os
import fileinput
import pygame
import random
from Game.Bricks import *
from Game.Shared import GameConstants


class Level:
    def __init__(self, game):
        self.__game = game
        self.__bricks = []
        self.__amountOfBricksLeft = 0
        self.__currentLevel = 0

    def getBricks(self):
        return self.__bricks

    def getAmountOfBricksLeft(self):
        return self.__amountOfBricksLeft

    def brickHit(self):
        self.__amountOfBricksLeft -= 1

    def loadNextLevel(self):
        self.__currentLevel += 1
        fileName = os.path.join("Assets", "Levels", "level"+str(self.__currentLevel) + ".dat")

        if not os.path.exists(fileName):
            self.loadRandom()
        else:
            self.load(self.__currentLevel)

    def loadRandom(self):
        self.__bricks = []

        x, y = 0, 0

        maxBricks = int(GameConstants.screenSize[0] / GameConstants.ballSize[0])
        rows = random.randint(2, 8)

        amountOfSuperPowerBricks = 0
        for row in range(0, rows):
            for brick in range(0, maxBricks):
                brickType = random.randint(0, 3)
                if brickType == 1 or amountOfSuperPowerBricks >= 2:
                    brick = Brick([x, y], pygame.image.load(GameConstants.spriteBrick), self.__game)
                    self.__bricks.append(brick)
                    self.__amountOfBricksLeft += 1

                elif brickType == 2:
                    brick = SpeedBrick([x, y], pygame.image.load(GameConstants.spriteSpeedBrick), self.__game)
                    self.__bricks.append(brick)
                    self.__amountOfBricksLeft += 1
                    amountOfSuperPowerBricks += 1

                elif brickType == 3:
                    brick = LifeBrick([x, y], pygame.image.load(GameConstants.spriteLifeBrick), self.__game)
                    self.__bricks.append(brick)
                    self.__amountOfBricksLeft += 1
                    amountOfSuperPowerBricks += 1

                x += GameConstants.brickSize[0]

            x = 0
            y += GameConstants.brickSize[1]

    def load(self, level):
        self.__currentLevel = level
        self.__bricks = []

        x, y = 0, 0

        levelFile = os.path.join("Assets", "Levels", "level"+str(level) + ".dat")
        for line in fileinput.input(levelFile):
            for currentBrick in line:
                if currentBrick == "1":
                    brick = Brick([x, y], pygame.image.load(GameConstants.spriteBrick), self.__game)
                    self.__bricks.append(brick)
                    self.__amountOfBricksLeft += 1

                elif currentBrick == "2":
                    brick = SpeedBrick([x, y], pygame.image.load(GameConstants.spriteSpeedBrick), self.__game)
                    self.__bricks.append(brick)
                    self.__amountOfBricksLeft += 1

                elif currentBrick == "3":
                    brick = LifeBrick([x, y], pygame.image.load(GameConstants.spriteLifeBrick), self.__game)
                    self.__bricks.append(brick)
                    self.__amountOfBricksLeft += 1

                x += GameConstants.brickSize[0]

            x = 0
            y += GameConstants.brickSize[1]




