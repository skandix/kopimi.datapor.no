#!/usr/bin/env python3
import os
from pathlib import Path
forbidden_ = ["md", "html"]
legal = ["pdf", "txt", "py"]


class Kopimi:
    def __init__(self):
        self.path = Path("./docs/")
        self.code_files = ['c', 'h' 'py']
        self.text_files = ["pdf", "txt", "docx"]

        # mkdocs vital files
        self.forbidden_files = ["index.md", "lists.md"]
        self.forbibben_folders = ["stylesheets"]
        
    def tree(self, directory):
        print(f'+ {directory}')
        for path in sorted(directory.rglob('*')):
            depth = len(path.relative_to(directory).parts)
            spacer = '    ' * depth
            print(f'{spacer}+ {path.name}')


    def list_files(self):
        for _file in self.path.iterdir():
            #print (self.tree(x))
            if _file.name not in self.forbidden_files and _file.name  not in self.forbibben_folders:
                print("\n")
                for k in (_file.rglob('*')):
                    if k.is_file():
                        print(k, k.suffix)

    def write_to_md(self, fileType:str):
        if fileType in self.text_files:
            # generate_md_list()
            ...
        elif fileType in self.code_files:
            # ta innholdet i .py eller .c og skriv til .md fil med sammenavn og legg koden mellom markdown codeblocks
            ...
  
    def generate_md_list(self, path, folder:str):
        for file in folder:
            file_ext = file.split('.')[-1]
        ...

k = Kopimi()
print (k.list_files())

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