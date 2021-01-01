from Game.Shared import *


class Pad(GameObject):
    def __init__(self, position, sprite):
        super(Pad, self).__init__(position, GameConstants.padSize, sprite)

    def setPosition(self, position):
        size = self.getSize()
        newPosition = [position[0], position[1]]
        if newPosition[0] + size[0] > GameConstants.screenSize[0]:
            newPosition[0] = GameConstants.screenSize[0] - size[0]

        super(Pad, self).setPosition(newPosition)
