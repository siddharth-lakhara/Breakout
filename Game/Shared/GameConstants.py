import os


class GameConstants:
    screenWidth = 800
    screenHeight = 600
    screenSize = (screenWidth, screenHeight)
    brickSize = [100, 30]
    ballSize = [16, 16]
    padSize = [139, 13]

    spriteBall = os.path.join("Assets", "img", "ball.png")
    spritePad = os.path.join("Assets", "img", "pad.png")
    spriteBrick = os.path.join("Assets", "img", "standard.png")
    spriteSpeedBrick = os.path.join("Assets", "img", "speed.png")
    spriteLifeBrick = os.path.join("Assets", "img", "life.png")
    spriteHighScore = os.path.join("Assets", "img", "highscore.png")

    soundFileBrickHit = os.path.join("Assets", "sounds", "BrickHit.wav")
    soundFileLifeBrickHit = os.path.join("Assets", "sounds", "ExtraLife.wav")
    soundFileSpeedBrickHit = os.path.join("Assets", "sounds", "SpeedUp.wav")
    soundFileWallHit = os.path.join("Assets", "sounds", "WallBounce.wav")
    soundFilePadHit = os.path.join("Assets", "sounds", "PadBounce.wav")
    soundFileGameOver = os.path.join("Assets", "sounds", "GameOver.wav")

    soundGameOver = 0
    soundBrickHit = 1
    soundLifeBrickHit = 2
    soundSpeedBrickHit = 3
    soundWallHit = 4
    soundPadHit = 5


    playingScene = 0
    gameOverScene = 1
    highScoreScene = 2
    menuScene = 3
