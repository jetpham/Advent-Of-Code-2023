from typing import List

import os



current_dir = os.path.dirname(__file__)

file_path = os.path.join(current_dir, "input.txt")



with open(file_path, "r") as file:

    input = file.readlines()



def Day22(input: List[str]) -> int:



print(Day22(input))