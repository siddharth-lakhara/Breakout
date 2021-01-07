import pygame
from Game.Scenes.Scene import Scene
from Game.Shared import GameConstants
from Game import Highscore

class HighscoreScene(Scene):
    def __init__(self, game):
        super(HighscoreScene, self).__init__(game)
        self.__highscoreSprite = pygame.image.load(GameConstants.spriteHighScore)

    def render(self):
        self.getGame().screen.blit(self.__highscoreSprite, (50, 50))
        self.clearText()
        highScores = Highscore()

        x = 350
        y = 100

        for score in highScores.getScores():
            self.addText(score[0], x, y, size=30)
            self.addText(str(score[0]), x+200, y, size=30)
            y += 30

        self.addText("Press Enter to restart the game", x, y+60, size=30)

        super(HighscoreScene, self).render()


    def handleEvents(self, events):
        super(HighscoreScene, self).handleEvents(events)

        for event in events:
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game = self.getGame()
                    # Highscore().add(self.__playerName, game.getScore())
                    game.reset()
                    game.changeScene(GameConstants.playingScene)