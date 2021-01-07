import pygame
from Game.Scenes.Scene import Scene
from Game.Shared import GameConstants


class PlayingGameScene(Scene):
    def __init__(self, game):
        super(PlayingGameScene, self).__init__(game)

    def render(self):
        super(PlayingGameScene, self).render()

        game = self.getGame()

        if game.getLife() <= 0:
            game.changeScene(GameConstants.gameOverScene)
        balls = game.getBall()
        pad = game.getPad()

        for ball in balls:
            for brick in game.getLevel().getBricks():
                if not brick.isDestroyed() and ball.intersects(brick):
                    brick.hit()
                    game.increaseScore(brick.getHitPoints())
                    ball.changeDirection(brick)
                    break

            if ball.intersects(pad):
                ball.changeDirection(pad)
            ball.updatePosition()

            if ball.isBallDead():
                ball.setMotion(0)
                game.reduceLife()
            game.screen.blit(ball.getSprite(), ball.getPosition())

        for brick in game.getLevel().getBricks():
            if not brick.isDestroyed():
                game.screen.blit(brick.getSprite(), brick.getPosition())

        pad = game.getPad()
        padPosition = pad.getPosition()
        pad.setPosition((pygame.mouse.get_pos()[0], padPosition[1]))
        game.screen.blit(pad.getSprite(), pad.getPosition())

        self.clearText()
        self.addText("Your score: " + str(game.getScore()),
                     x=0, y=GameConstants.screenSize[1] - 60, size=30)
        self.addText("Your Lives: " + str(game.getLife()),
                     x=0, y=GameConstants.screenSize[1] - 30, size=30)

    def handleEvents(self, events):
        super(PlayingGameScene, self).handleEvents(events)

        for event in events:
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                for ball in self.getGame().getBall():
                    ball.setMotion(1)
