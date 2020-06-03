import random
import pytest

rotateSide = [[4, 1, 5, 3], [1, 5, 3, 4]]
rotateTop = [[0,1,2,3],[1,2,3,0]]
rotateFront = [[0,4,2,5],[4,2,5,0]]


class rubiksEnv:
    rubiksCube = {
        0: [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]],
        1: [[1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]],
        2: [[2, 2, 2],
            [2, 2, 2],
            [2, 2, 2]],
        3: [[3, 3, 3],
            [3, 3, 3],
            [3, 3, 3]],
        4: [[4, 4, 4],
            [4, 4, 4],
            [4, 4, 4]],
        5: [[5, 5, 5],
            [5, 5, 5],
            [5, 5, 5]],

    }

    def __init__(self):
        for i in range(350):
            a = random.randint(0, 5)
            b = random.randint(0, 2)
            c = random.randint(0, 2)
            d = random.randint(0, 5)
            e = random.randint(0, 2)
            f = random.randint(0, 2)
            if (b == 1 and c==1) or (e == 1 and f == 1):
                continue
            else:
                swap1 = self.rubiksCube[a][b][c]
                swap2 = self.rubiksCube[d][e][f]
                self.rubiksCube[a][b][c] = swap2
                self.rubiksCube[d][e][f] = swap1

    def displayCube(self):
        for i in range(3):
            print("Left: ", self.rubiksCube[2][i], "   ", "Front: ", self.rubiksCube[1][i], "   ", "Right: ",
                  self.rubiksCube[0][i]
                  , "   ", "Back: ", self.rubiksCube[3][i], "   ", "Top: ", self.rubiksCube[4][i], "   ", "Bottom: ",
                  self.rubiksCube[5][i])

    def step(self, move):
        if move == "d":
            tempRot = [self.rubiksCube[5][0],
                       self.rubiksCube[5][1],
                       self.rubiksCube[5][2]]
            temp = ["", "", "", ""]
            for i in range(4):
                if i < 3:
                    temp[i + 1] = self.rubiksCube[i][2]
                else:
                    temp[0] = self.rubiksCube[i][2]
            for i in range(len(temp)):
                self.rubiksCube[i][2] = temp[i]
            for i in range(len(tempRot)):
                self.rubiksCube[5][i] = [tempRot[0][2-i], tempRot[1][2-i], tempRot[2][2-i]]
                #self.rubiksCube[5][i] = [tempRot[2][i], tempRot[1][i], tempRot[0][i]]
        elif move == "u":
            tempRot = [self.rubiksCube[4][0],
                       self.rubiksCube[4][1],
                       self.rubiksCube[4][2]]
            temp = ["", "", "", ""]
            for i in range(4):
                if i < 3:
                    temp[i + 1] = self.rubiksCube[i][0]
                else:
                    temp[0] = self.rubiksCube[i][0]
            for i in range(len(temp)):
                self.rubiksCube[i][0] = temp[i]
            for i in range(len(tempRot)):
                #self.rubiksCube[4][i] = [tempRot[0][2-i], tempRot[1][2-i], tempRot[2][2-i]] #This makes it go
                # antiClockwise
                self.rubiksCube[4][i] = [tempRot[2][i], tempRot[1][i], tempRot[0][i]]
        elif move == "l":
            tempLeft = []
            tempRot = [self.rubiksCube[2][0],
                       self.rubiksCube[2][1],
                       self.rubiksCube[2][2]]
            for i in range(4):
                tempLeft.append([self.rubiksCube[int(rotateSide[0][i])][0][0],
                                 self.rubiksCube[int(rotateSide[0][i])][1][0],
                                 self.rubiksCube[int(rotateSide[0][i])][2][0]])
            for i in range(4):
                for e in range(3):
                    self.rubiksCube[int(rotateSide[1][i])][e][0] = tempLeft[i][e]
            for i in range(len(tempRot)):
                #self.rubiksCube[2][i] = [tempRot[0][2-i], tempRot[1][2-i], tempRot[2][2-i]]
                self.rubiksCube[2][i] = [tempRot[2][i], tempRot[1][i], tempRot[0][i]]
        elif move == "r":
            tempLeft = []
            tempRot = [self.rubiksCube[0][0],
                       self.rubiksCube[0][1],
                       self.rubiksCube[0][2]]
            for i in range(4):
                tempLeft.append([self.rubiksCube[int(rotateSide[0][i])][0][2],
                                 self.rubiksCube[int(rotateSide[0][i])][1][2],
                                 self.rubiksCube[int(rotateSide[0][i])][2][2]])
            for i in range(4):
                for e in range(3):
                    self.rubiksCube[int(rotateSide[1][i])][e][2] = tempLeft[i][e]
            for i in range(len(tempRot)):
                self.rubiksCube[0][i] = [tempRot[0][2-i], tempRot[1][2-i], tempRot[2][2-i]]
                #self.rubiksCube[2][i] = [tempRot[2][i], tempRot[1][i], tempRot[0][i]]
        elif move =="x":
            tempXAxis = []
            tempRotRight = [self.rubiksCube[0][0],
                            self.rubiksCube[0][1],
                            self.rubiksCube[0][2]]
            tempRotLeft = [self.rubiksCube[2][0],
                           self.rubiksCube[2][1],
                           self.rubiksCube[2][2]]
            for i in range(4):
                tempXAxis.append(self.rubiksCube[int(rotateSide[0][i])])
            for i in range(4):
                    self.rubiksCube[int(rotateSide[1][i])] = tempXAxis[i]
            for i in range(len(tempRotRight)):
                self.rubiksCube[2][i] = [tempRotLeft[2][i], tempRotLeft[1][i], tempRotLeft[0][i]]
                self.rubiksCube[0][i] = [tempRotRight[0][2 - i], tempRotRight[1][2 - i], tempRotRight[2][2 - i]]
                # self.rubiksCube[2][i] = [tempRot[2][i], tempRot[1][i], tempRot[0][i]]
        elif move =="y":
            tempYAxis = []
            tempRotTop = [self.rubiksCube[4][0],
                            self.rubiksCube[4][1],
                            self.rubiksCube[4][2]]
            tempRotBottom = [self.rubiksCube[5][0],
                           self.rubiksCube[5][1],
                           self.rubiksCube[5][2]]
            for i in range(4):
                tempYAxis.append(self.rubiksCube[int(rotateTop[0][i])])
            for i in range(4):
                self.rubiksCube[int(rotateTop[1][i])] = tempYAxis[i]
            for i in range(len(tempRotTop)):
                self.rubiksCube[5][i] = [tempRotBottom[0][2 - i], tempRotBottom[1][2 - i], tempRotBottom[2][2 - i]]
                self.rubiksCube[4][i] = [tempRotTop[2][i], tempRotTop[1][i], tempRotTop[0][i]]
                # self.rubiksCube[2][i] = [tempRot[2][i], tempRot[1][i], tempRot[0][i]]
        elif move == "z":
            tempZAxis = []
            tempRotFront = [self.rubiksCube[1][0],
                          self.rubiksCube[1][1],
                          self.rubiksCube[1][2]]
            tempRotBack = [self.rubiksCube[3][0],
                             self.rubiksCube[3][1],
                             self.rubiksCube[3][2]]
            for i in range(4):
                tempZAxis.append(self.rubiksCube[int(rotateFront[0][i])])
            for i in range(4):
                self.rubiksCube[int(rotateFront[1][i])] = tempZAxis[i]
            for i in range(len(tempRotFront)):
                self.rubiksCube[1][i] = [tempRotFront[2][i], tempRotFront[1][i], tempRotFront[0][i]]
                self.rubiksCube[3][i] = [tempRotBack[0][2-i], tempRotBack[1][2-i], tempRotBack[2][2-i]]
                    # self.rubiksCube[2][i] = [tempRot[2][i], tempRot[1][i], tempRot[0][i]]


    def main(self):
        self.displayCube()
        while True:
            move = input()
            self.step(move)
            self.displayCube()
def introduction():
    print("")

if __name__ == "__main__":
    cube = rubiksEnv()
    cube.main()
