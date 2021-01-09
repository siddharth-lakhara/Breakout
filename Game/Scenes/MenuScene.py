import pygame
from Game.Scenes.Scene import Scene
from Game.Shared import GameConstants


class MenuScene(Scene):
    def __init__(self, game):
        super(MenuScene, self).__init__(game)

        self.addText("S - Start Game", x=300, y=200, size=30)
        self.addText("H - High score", x=300, y=240, size=30)
        self.addText("Q - Quit", x=300, y=280, size=30)

        self.__menuSprite = pygame.image.load(GameConstants.spriteMenu)

    def render(self):
        self.getGame().screen.blit(self.__menuSprite, (50, 50))

        super(MenuScene, self).render()

    def handleEvents(self, events):
        super(MenuScene, self).handleEvents(events)

        for event in events:
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()

                if event.key == pygame.K_s:
                    self.getGame().changeScene(GameConstants.playingScene)

                if event.key == pygame.K_h:
                    self.getGame().changeScene(GameConstants.highScoreScene)

                if event.key == pygame.K_q:
                    exit()
