from Game.Bricks import Brick
from Game.Shared import GameConstants


class LifeBrick(Brick):
    def __init__(self, position, sprite, game):
        super(LifeBrick, self).__init__(position, sprite, game)

    def hit(self):
        game = self.getGame()
        game.increaseLife()

        super(LifeBrick, self).hit()

    def getHitSound(self):
        return GameConstants.soundLifeBrickHit