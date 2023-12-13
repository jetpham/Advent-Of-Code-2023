MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

from typing import List

with open("C:\\Users\\Jet Pham\\Advent-Of-Code-2023\\Day2\\input.txt", "r") as file:
    input = file.readlines()

class ContinueLoop(Exception):
    pass

def Conundrum(games: List[str]) -> int:
    sumOfIDS = 0
    for game in games:
        try:
            parts = game.split(":")
            gameID = int(parts[0][5:])
            rounds = parts[1].split(";")
            for round in rounds:
                for cubes in round.split(","):
                    values = cubes.split(" ")
                    if "green" in values or "green\n" in values:
                        if int(values[1]) > MAX_GREEN:
                            raise ContinueLoop
                    elif "red" in values or "red\n" in values:
                        if int(values[1]) > MAX_RED:
                            raise ContinueLoop
                    elif "blue" in values or "blue\n" in values:
                        if int(values[1]) > MAX_BLUE:
                            raise ContinueLoop
            sumOfIDS += gameID
        except ContinueLoop:
            continue
    return sumOfIDS

    
print(Conundrum(input))
