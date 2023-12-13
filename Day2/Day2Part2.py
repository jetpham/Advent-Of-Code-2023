from typing import List
import os

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "input.txt")

with open(file_path, "r") as file:
    input = file.readlines()


def Conundrum(games: List[str]) -> int:
    sumOfPowers = 0
    for game in games:
        leastRed = None
        leastBlue = None
        leastGreen = None
        parts = game.split(":")
        rounds = parts[1].split(";")
        for round in rounds:
            for cubes in round.split(","):
                values = cubes.split(" ")
                if "green" in values or "green\n" in values:
                    if leastGreen is None:
                        leastGreen = int(values[1])
                    else:
                        if int(values[1]) > leastGreen:
                            leastGreen = int(values[1])
                elif "red" in values or "red\n" in values:
                    if leastRed is None:
                        leastRed = int(values[1])
                    else:
                        if int(values[1]) > leastRed:
                            leastRed = int(values[1])
                elif "blue" in values or "blue\n" in values:
                    if leastBlue is None:
                        leastBlue = int(values[1])
                    else:
                        if int(values[1]) > leastBlue:
                            leastBlue = int(values[1])
        if leastBlue is not None and leastGreen is not None and leastRed is not None:
            sumOfPowers += leastBlue * leastGreen * leastRed

    return sumOfPowers


print(Conundrum(input))
