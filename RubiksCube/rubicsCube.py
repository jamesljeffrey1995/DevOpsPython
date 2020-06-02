import random
import pytest

rotateLeftSide = [[5, 1, 4, 3], [1, 4, 3, 5]]


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
            swap1 = self.rubiksCube[a][b][c]
            swap2 = self.rubiksCube[d][e][f]
            self.rubiksCube[a][b][c] = swap2
            self.rubiksCube[d][e][f] = swap1

    def displayCube(self):
        for i in range(3):
            print("Right: ", self.rubiksCube[0][i], "   ", "Front: ", self.rubiksCube[1][i], "   ", "Left: ",
                  self.rubiksCube[2][i]
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
                # self.rubiksCube[4][i] = [tempRot[0][2-i], tempRot[1][2-i], tempRot[2][2-i]] This makes it go
                # antiClockwise
                self.rubiksCube[5][i] = [tempRot[2][i], tempRot[1][i], tempRot[0][i]]
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
                # self.rubiksCube[4][i] = [tempRot[0][2-i], tempRot[1][2-i], tempRot[2][2-i]] This makes it go
                # antiClockwise
                self.rubiksCube[4][i] = [tempRot[2][i], tempRot[1][i], tempRot[0][i]]
        elif move == "l":
            tempLeft = []
            tempRot = [self.rubiksCube[2][0],
                       self.rubiksCube[2][1],
                       self.rubiksCube[2][2]]
            for i in range(4):
                tempLeft.append([self.rubiksCube[int(rotateLeftSide[0][i])][0][0],
                                 self.rubiksCube[int(rotateLeftSide[0][i])][1][0],
                                 self.rubiksCube[int(rotateLeftSide[0][i])][2][0]])
            print(tempLeft)
            for i in range(4):
                for e in range(3):
                    self.rubiksCube[int(rotateLeftSide[1][i])][e][0] = tempLeft[i][e]
            for i in range(len(tempRot)):
                self.rubiksCube[2][i] = [tempRot[0][2-i], tempRot[1][2-i], tempRot[2][2-i]]
                #self.rubiksCube[2][i] = [tempRot[2][i], tempRot[1][i], tempRot[0][i]]
        elif move == "r":
            tempLeft = []
            tempRot = [self.rubiksCube[0][0],
                       self.rubiksCube[0][1],
                       self.rubiksCube[0][2]]
            for i in range(4):
                tempLeft.append([self.rubiksCube[int(rotateLeftSide[0][i])][0][2],
                                 self.rubiksCube[int(rotateLeftSide[0][i])][1][2],
                                 self.rubiksCube[int(rotateLeftSide[0][i])][2][2]])
            print(tempLeft)
            for i in range(4):
                for e in range(3):
                    self.rubiksCube[int(rotateLeftSide[1][i])][e][2] = tempLeft[i][e]
            for i in range(len(tempRot)):
                self.rubiksCube[0][i] = [tempRot[0][2-i], tempRot[1][2-i], tempRot[2][2-i]]
                #self.rubiksCube[2][i] = [tempRot[2][i], tempRot[1][i], tempRot[0][i]]

    def main(self):
        self.displayCube()
        while True:
            move = input()
            self.step(move)
            self.displayCube()


if __name__ == "__main__":
    cube = rubiksEnv()
    cube.main()
