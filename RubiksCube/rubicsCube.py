import random
import pytest

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
        if move == "e":
            temp = ["", "", "", ""]
            for i in range(4):
                if i < 3:
                    temp[i + 1] = self.rubiksCube[i][0]
                else:
                    temp[0] = self.rubiksCube[i][0]
            for i in range(len(temp)):
                self.rubiksCube[i][0] = temp[i]
            for i in range(len(self.rubiksCube[4][i])):


    def main(self):
        self.displayCube()
        while True:
            move = input()
            self.step(move)
            self.displayCube()


if __name__ == "__main__":
    cube = rubiksEnv()
    cube.main()
