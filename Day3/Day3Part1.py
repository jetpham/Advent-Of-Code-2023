from typing import List
import os

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "input.txt")

with open(file_path, "r") as file:
    inputFile = [line.rstrip() for line in file.readlines()]


# The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)

# Here is an example engine schematic:

# 467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..

# In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

# Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?

# loop over every line and then every character in the line, once you find a number, save the column then keep going through the line until you find a non-number. use that to calculate the length of the number that you found. now using the index and the length check the chars at the
# input[row][column - 1 and column + length + 1]
# input[row - 1][column - 1 through  column + length + 1]
# input[row + 1][column - 1 through  column + length + 1]
# if any of those are symbols then add the number to the total and skip to the end of the number/ keep going.


def isSymbol(row: int, column: int) -> bool:
    return (
        row >= 0
        and row < len(inputFile)
        and column >= 0
        and column < len(inputFile[row])
        and not (inputFile[row][column].isdigit() or inputFile[row][column] == ".")
    )


def hasSymbolNeighbor(row: int, column: int) -> bool:
    return (
        isSymbol(row, column - 1)
        or isSymbol(row, column + 1)
        or isSymbol(row - 1, column - 1)
        or isSymbol(row - 1, column)
        or isSymbol(row - 1, column + 1)
        or isSymbol(row + 1, column - 1)
        or isSymbol(row + 1, column)
        or isSymbol(row + 1, column + 1)
    )


def Day3(input: List[str]) -> int:
    total = 0
    for rowIndex, row in enumerate(input):
        goodNumber = None
        currentNumberStartingIndex = None
        for columnIndex, char in enumerate(row):
            if char.isdigit():
                if currentNumberStartingIndex is None:
                    currentNumberStartingIndex = columnIndex
                    goodNumber = hasSymbolNeighbor(rowIndex, columnIndex)
                else:
                    goodNumber = goodNumber or hasSymbolNeighbor(rowIndex, columnIndex)
            elif currentNumberStartingIndex is not None:
                if goodNumber:
                    total += int(
                        input[rowIndex][currentNumberStartingIndex:columnIndex]
                    )
                goodNumber = None
                currentNumberStartingIndex = None
    return total


answer = Day3(inputFile)
print("answer is: " + str(answer))
print("Changed" if answer != 537710 else "Not Changed")
