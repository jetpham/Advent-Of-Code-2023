import os

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "template.txt")

with open(file_path, "r") as file:
    template = file.readlines()


for day in range(4, 26):
    dir_name = f"Day{day}"
    os.makedirs(dir_name, exist_ok=True)

    content = "\n".join([line.replace("{day}", str(day)) for line in template])

    files = {
        f"Day{day}Part1.py": content,
        f"Day{day}Part2.py": content,
        "input.txt": "",
    }

    for file_name, content in files.items():
        with open(os.path.join(dir_name, file_name), 'w') as f:
            f.write(content)
