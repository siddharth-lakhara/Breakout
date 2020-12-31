import os


class GameConstants:
    screenWidth = 800
    screenHeight = 600
    screenSize = (screenWidth, screenHeight)
    brickSize = [100, 30]
    ballSize = [16, 16]
    padSize = [139, 13]

    spriteBall = os.path.join("Assets", "img", "ball.png")
    spriteBrick = os.path.join("Assets", "img", "standard.png")
    spriteSpeedBrick = os.path.join("Assets", "img", "speed.png")
    spriteLifeBrick = os.path.join("Assets", "img", "life.png")
