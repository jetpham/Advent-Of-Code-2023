from typing import List

with open("input.txt", "r") as file:
    input = file.readlines()

def trebuchet(noisyValues: List[str]) -> int:
    total = 0
    valid = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9
    }
    for string in noisyValues:
        values = []
        i = 0
        while i < len(string):
            for key in valid:
                if string[i:].startswith(key):
                    values.append(valid[key])
                    i += len(key)
                    break
            else:
                i += 1
        total += values[0] * 10 + values[-1]
    return total

print(trebuchet(input))
