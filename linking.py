#!/usr/bin/env python3
import os
from pathlib import Path

forbidden_ = ["md", "html"]
legal = ["pdf", "txt", "py"]


class kopimi:
    def __init__(self, kopimi_path: str):
        self.path = Path("./docs/")
        self.code_files = ['c', 'h' 'py']
        self.allowed_files = ["pdf", "txt", "docx"] + self.code_files
        self.forbidden_files = ["md", "html"]

    def list_files(self):
        

    def write_to_md(self, fileType:str):
        if fileType in self.allowed_files:
            if fileType in self.code_files:
                # ta innholdet i .py eller .c og skriv til .md fil med sammenavn og legg koden mellom markdown codeblocks
            ...
        ...
  
    def generate_md_list(self, path, folder:str):
        for file in folder:
            file_ext = file.split('.')[-1]

            
        ...
"""
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
"""