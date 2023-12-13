import os
import http.cookiejar
import urllib
import urllib.request

# Your session cookie
cookie = "53616c7465645f5febe3d984cce84e291be670a3f3c1066580dd0c8dc54b31925931a4d0b54a8be146534d52c9863ee26a428a05e9a3ca4555e28353863c51d4"

# Create a cookie jar and add your cookie
cj = http.cookiejar.CookieJar()

cj.set_cookie(
    http.cookiejar.Cookie(
        version=0,
        name="session",
        value=cookie,
        port=None,
        port_specified=False,
        domain="adventofcode.com",
        domain_specified=False,
        domain_initial_dot=False,
        path="/",
        path_specified=True,
        secure=True,
        expires=None,
        discard=True,
        comment=None,
        comment_url=None,
        rest={},
        rfc2109=False,
    )
)

# Create an opener that will use the cookie jar
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "template.txt")

with open(file_path, "r") as file:
    template = file.readlines()

# Find the directory with the largest number
max_day = max(
    [int(dir_name[3:]) for dir_name in os.listdir() if dir_name.startswith("Day")],
    default=0,
)
print(max_day)
# Set the range to start from the largest number + 1
start_day = max_day + 1

for day in range(start_day, start_day + 1):
    dir_name = f"Day{day}"
    os.makedirs(dir_name, exist_ok=True)

    content = "".join([line.replace("{day}", str(day)) for line in template])

    files = {
        f"Day{day}Part1.py": content,
        f"Day{day}Part2.py": content,
        "input.txt": "",
    }

    for file_name, content in files.items():
        if file_name == "input.txt":
            input_url = f"https://adventofcode.com/2023/day/{day}/input"
            file_name = "input.txt"

            try:
                # Use the opener to fetch the URL
                response = opener.open(input_url)
                content = response.read().decode()

                print(f"Input file for Day {day} downloaded successfully.")
            except Exception as e:
                print(f"Failed to download input for Day {day}: {str(e)}")

        with open(os.path.join(dir_name, file_name), "w") as f:
            f.write(content)
