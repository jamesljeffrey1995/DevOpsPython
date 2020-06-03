import random
import pytest
import time

WelcomeMessage = ["---------------------","| RUBIKS CUBE CONSOLE |","---------------------"]
rotateSide = [[4, 1, 5, 3], [1, 5, 3, 4]] #These are algorithms to iterate through the sides
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
            [5, 5, 5]], #This creates 6x3x3 list which imitates a rubiks cube

    }

    def __init__(self):
        for i in range(350):
            a = random.randint(0, 5) #This randomises the cube but doesnt change the middle square of each
            b = random.randint(0, 2) #face
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
            tempRot = [self.rubiksCube[5][0], #tempstorage to allow for rotation of a face
                       self.rubiksCube[5][1],
                       self.rubiksCube[5][2]]
            temp = ["", "", "", ""]
            for i in range(4):
                if i < 3:
                    temp[i + 1] = self.rubiksCube[i][2]
                else:
                    temp[0] = self.rubiksCube[i][2] #shifts everything to the right and puts last to first
            for i in range(len(temp)):
                self.rubiksCube[i][2] = temp[i] #Replaces the bottom row for all relevant sides
            for i in range(len(tempRot)):
                self.rubiksCube[5][i] = [tempRot[0][2-i], tempRot[1][2-i], tempRot[2][2-i]]#This rotates anti-clockwise
                #self.rubiksCube[5][i] = [tempRot[2][i], tempRot[1][i], tempRot[0][i]] #This rotates clockwise
        elif move == "u": #Same as d but for top line and top face
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
            tempRot = [self.rubiksCube[2][0],#Same before for face rotation
                       self.rubiksCube[2][1],
                       self.rubiksCube[2][2]]
            for i in range(4):
                tempLeft.append([self.rubiksCube[int(rotateSide[0][i])][0][0], #uses the algorithm stored in a list
                                 self.rubiksCube[int(rotateSide[0][i])][1][0], #to iterate through certain faces
                                 self.rubiksCube[int(rotateSide[0][i])][2][0]]) #and store them
            for i in range(4):
                for e in range(3):
                    self.rubiksCube[int(rotateSide[1][i])][e][0] = tempLeft[i][e] #iterates through memory val 1 of the
                    #algorthim allowing for the right values to be stored in the right place
            for i in range(len(tempRot)):
                #self.rubiksCube[2][i] = [tempRot[0][2-i], tempRot[1][2-i], tempRot[2][2-i]]
                self.rubiksCube[2][i] = [tempRot[2][i], tempRot[1][i], tempRot[0][i]]
        elif move == "r":
            tempLeft = [] #Same as l
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
            tempXAxis = [] #All the same concept as l and r
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
        elif move == "f":
            tempRotFront = [self.rubiksCube[1][0],
                            self.rubiksCube[1][1],
                            self.rubiksCube[1][2]]
            for i in range(len(tempRotFront)):
                self.rubiksCube[1][i] = [tempRotFront[2][i], tempRotFront[1][i], tempRotFront[0][i]]
        elif move == "b":
            tempRotBack = [self.rubiksCube[3][0],
                           self.rubiksCube[3][1],
                           self.rubiksCube[3][2]]
            for i in range(len(tempRotBack)):
                self.rubiksCube[3][i] = [tempRotBack[0][2-i], tempRotBack[1][2-i], tempRotBack[2][2-i]]


    def main(self):
        self.displayCube() #infinite loop to allow for updated cube
        while True:
            move = input()
            self.step(move)
            self.displayCube()

def introduction():
    print("l = Left face rotate clockwise \nr = Right face rotate anti-clockwise")
    print("u = Top Face rotate clockwise \nd = Bottom face rotate anti-clockwise")
    print("f = Front face rotate clockwise \nb = Back face rotate anti-clockwise")
    print("x = Rotate on x axis towards you \ny = Rotate on y axis to the left")
    print("z = Rotates on z axis to the left")
    time.sleep(10)
    for i in range(len(WelcomeMessage)):
        print(WelcomeMessage[i].center(127," "))


if __name__ == "__main__":
    introduction()
    cube = rubiksEnv()
    cube.main()
