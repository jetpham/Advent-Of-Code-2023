from typing import List
import os

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "input.txt")

with open(file_path, "r") as file:
    input = file.readlines()
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


def Day3(input: List[str]) -> int:
    total = 0
    for rowIndex, row in enumerate(input):
        length = 0
        numberStartingIndex = None
        for columnIndex, char in enumerate(row):
            if numberStartingIndex is None:
                if char.isdigit():
                    numberStartingIndex = columnIndex
                    length += 1
                else:
                    continue
            if char.isdigit():
                length += 1
            else:
                if length == 0 and numberStartingIndex is None:
                    continue
                else:
                    borderingSymbols = []
                    if columnIndex != 0:
                        #getting the symbol to the left of the number
                        borderingSymbols.append(
                            input[rowIndex][numberStartingIndex - 1]
                        )
                    if columnIndex + length != len(row):
                        #getting the symbol to the right of the number
                        borderingSymbols.append(
                            input[rowIndex][numberStartingIndex + length]
                        )
                    if rowIndex != 0:
                        #getting the symbol above the number
                        borderingSymbols.append(
                            input[rowIndex - 1][
                                numberStartingIndex - 1 : numberStartingIndex
                                + length
                            ]
                        )
                    if rowIndex + 1 != len(input):
                        #getting the symbol below the number
                        borderingSymbols.append(
                            input[rowIndex + 1][
                                numberStartingIndex - 1 : numberStartingIndex
                                + length
                            ]
                        )

                    print("".join([i for i in borderingSymbols if i != "\n"]))
                    
                    if any(
                        [
                            symbol in borderingSymbols
                            for symbol in ["*", "#", "$", "+", "&", "@"]
                        ]
                    ):
                        substring = input[rowIndex][
                            numberStartingIndex : numberStartingIndex + length
                        ]
                        try:
                            total += int(substring)
                        except ValueError:
                            print(f"Cannot convert {substring} to an integer.")
                    length = 0
                    numberStartingIndex = None
    return total


print(Day3(input))
