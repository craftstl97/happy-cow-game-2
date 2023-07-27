# Test.py
# generates random grids for testing purposes

import sys
import random

# handles command line input
def getFileNames(argv):
    gridSize = int(argv[0])
    iFile = argv[1]

    return (gridSize, iFile)

# writes to output file
def writeToFile(fileName: str, gridSize: int, grid: list):
    file = open(fileName, "w")
    # grid size
    file.write(str(gridSize) + "\n")

    # grid
    for line in grid:
        file.write(line + "\n")

    file.close()

def placeHay(grid: list, gridSize: int):
    # generate random coordinates
    x = random.randint(0, gridSize - 1)
    y = random.randint(0, gridSize - 1)

    # check if the placement is valid
    while grid[x][y] != ".":
        x = random.randint(0, gridSize - 1)
        y = random.randint(0, gridSize - 1)

    # place a cow there
    line = list(grid[x])
    line[y] = "@"
    grid[x] = "".join(line)

def placePond(grid: list, gridSize: int):
    # generate random coordinates
    x = random.randint(0, gridSize - 1)
    y = random.randint(0, gridSize - 1)

    # check if the placement is valid
    while grid[x][y] != ".":
        x = random.randint(0, gridSize - 1)
        y = random.randint(0, gridSize - 1)

    # place a cow there
    line = list(grid[x])
    line[y] = "#"
    grid[x] = "".join(line)

# fills the grid
def generateRandomGrid(grid: list, gridSize: int) -> list:
    # generate a random grid
    for x in range(gridSize):
        line = ""
        for y in range(gridSize):
            line += "."
        grid.append(line)

    # add haystacks
    haystacks = random.randint(3,7)
    for x in range(haystacks):
        placeHay(grid, gridSize)
    # add ponds
    ponds = random.randint(2,6)
    for x in range(ponds):
        placePond(grid, gridSize)


# main driver function
if __name__ == "__main__":
    grid = []
    IO = getFileNames(sys.argv[1:])

    grid = []
    generateRandomGrid(grid, IO[0])

    writeToFile(IO[1], IO[0], grid)
