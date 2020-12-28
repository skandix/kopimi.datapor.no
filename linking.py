#!/usr/bin/env python3
import os
from pathlib import Path

forbidden_ = ["md", "html"]
legal = ["pdf", "txt", "py"]


class K	opimi:
    def __init__(self, kopimi_path: str):
        self.path = Path("./docs/")
        self.allowed_files = ["pdf", "txt", "py"]
        self.forbidden_files = ["md", "html"]

	def write_to_md()
		with open(f"{_path}{dir_}/Files.md", "a+") as file:
			file.write("#Files\n")
			for l in listing:
				file_ext = l.split(".")[-1]
				if file_ext not in forbidden_ and file_ext in legal:
					file.write(f"* [{l}]({l})\n")
					print(f"* [{l}]({l})\r")

for dir_ in os.listdir(f"{_path}"):
    try:
        listing = os.listdir(f"{_path}{dir_}")
        # if file exists, erase content, and write new content
        open(f"{_path}{dir_}/Files.md", "w")
        file = open(f"{_path}{dir_}/Files.md", "a+")
        file.write("#Files\n")
        for l in listing:
            file_ext = l.split(".")[-1]
            if file_ext not in forbidden_ and file_ext in legal:
                file.write(f"* [{l}]({l})\n")
                print(f"* [{l}]({l})\r")
    except NotADirectoryError:
        ...
