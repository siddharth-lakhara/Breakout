import pygame
from Game import *
from Game.Scenes import *
from Game.Shared import GameConstants


class Breakout:
    def __init__(self):
        self.__lives = 5
        self.__score = 0

        self.__level = Level(self)
        self.__level.load(0)

        self.__pad = Pad(
            (GameConstants.screenSize[0]/2, GameConstants.screenSize[1] - GameConstants.padSize[1]),
            pygame.image.load(GameConstants.spritePad)
        )
        self.__balls = [
            Ball((400, 400), pygame.image.load(GameConstants.spriteBall), self)
        ]

        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("Breakout")

        self.__clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode(GameConstants.screenSize,
                                              pygame.DOUBLEBUF, 32)
        pygame.mouse.set_visible(False)
        self.__scenes = (
            PlayingGameScene(self),
            GameOverScene(self),
            HighscoreScene(self),
            MenuScene(self)
        )

        self.__currentScene = 3
        self.__sounds = (
            pygame.mixer.Sound(GameConstants.soundFileGameOver),
            pygame.mixer.Sound(GameConstants.soundFileBrickHit),
            pygame.mixer.Sound(GameConstants.soundFileLifeBrickHit),
            pygame.mixer.Sound(GameConstants.soundFileSpeedBrickHit),
            pygame.mixer.Sound(GameConstants.soundFileWallHit),
            pygame.mixer.Sound(GameConstants.soundFilePadHit),
        )

    def start(self):
        while True:
            self.__clock.tick(30)
            self.screen.fill((0, 0, 0))

            currentScene = self.__scenes[self.__currentScene]
            currentScene.handleEvents(pygame.event.get())
            currentScene.render()

            pygame.display.update()

    def changeScene(self, scene):
        self.__currentScene = scene

    def getLevel(self):
        return self.__level

    def getScore(self):
        return self.__score

    def increaseScore(self, score):
        self.__score += score

    def getLife(self):
        return self.__lives

    def getBall(self):
        return self.__balls

    def getPad(self):
        return self.__pad

    def playSound(self, soundClip):
        sound = self.__sounds[soundClip]

        sound.stop()
        sound.play()

    def increaseLife(self):
        self.__lives += 1

    def reduceLife(self):
        self.__lives -= 1

    def reset(self):
        self.__lives = 5
        self.__score = 0
        self.__level.load(0)



Breakout().start()
