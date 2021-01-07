import fileinput
import hashlib
import os
import operator

class Highscore:
    def __init__(self):
        self.__highscore = self.load()

    def getScores(self):
        return self.__highscore

    def load(self):
        highScore = []
        highScoreFilePath = os.path.join("Assets", "highscore.dat")
        for line in fileinput.input(highScoreFilePath):
            name, score, md5 = line.split('[::]')
            md5 = md5.replace('\n', '')

            encodedScoreString = str.encode(str(name+score+"pygame"))
            expectedScoreHash = hashlib.md5(encodedScoreString).hexdigest()
            if str(expectedScoreHash == str(md5)):
                highScore.append([str(name), int(score), str(md5)])

        highScore.sort(key=operator.itemgetter(1), reverse=True)
        highScore = highScore[0:11]

        return highScore

    def add(self, name, score):
        encodedScore = str(name+str(score)+"pygame").encode("utf-8")
        scoreHash = hashlib.md5(encodedScore)
        self.__highscore.append([name, str(score), scoreHash.hexdigest()])

        highScoreFilePath = os.path.join("Assets", "highscore.dat")
        f = open(highScoreFilePath, 'w')
        for name, score, md5 in self.__highscore:
            data = str(name) + '[::]' + str(score) + '[::]' + str(md5)
            f.write(data)

        f.close()
