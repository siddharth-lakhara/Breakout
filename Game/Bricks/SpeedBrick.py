from Game.Bricks import Brick
from Game.Shared import GameConstants


class SpeedBrick(Brick):
    def __init__(self, position, sprite, game):
        super(SpeedBrick, self).__init__(position, sprite, game)

    def hit(self):
        game = self.getGame()

        for ball in game.getBall():
            currentSpeed = ball.getSpeed()
            ball.setSpeed(currentSpeed+1)

        super(SpeedBrick, self).hit()

    def getHitSound(self):
        return GameConstants.soundSpeedBrickHit
