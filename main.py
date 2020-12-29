#!/usr/bin/env python3
import os
from pathlib import Path
from loguru import logger as log

""" 
In advance, this was made after not sleeping one nigth, this is kind of a
structured mess, but mostly just a mess...

Kind Regards 
sleepless skandix
"""


class Kopimi:
    def __init__(self):
        self.path = Path("./docs/")
        self.code_files = [".py", ".c", ".h"]
        self.markdown_code = {"py": "python", "c": "c", "h": "h"}
        self.text_files = [".pdf", ".docx"]

        # mkdocs vital files
        self.forbidden_files = ["index.md", "lists.md", "CMakeLists.txt"]
        self.forbidden_folders = ["stylesheets"]
        self.joe_biden = "THIS IS A AMERICA"

        self.filecollect_name = "Filer.md"
        self.codecollect_name = "Kode.md"

    def list_files(self):
        for _file in self.path.iterdir():
            if (
                _file.name not in self.forbidden_files
                and _file.name not in self.forbidden_folders
            ):
                for path_obj in sorted(_file.rglob("**/*")):
                    if path_obj.is_file() and path_obj.suffix in self.code_files:
                        open(
                            f"{path_obj.resolve().parent}/{self.codecollect_name}"
                        ).write(f"# Kode \n")
                        with open(
                            f"{path_obj.resolve().parent}/{self.codecollect_name}", "a"
                        ) as code:
                            code.write(
                                f"* {path_obj.name}\n```{self.markdown_code[path_obj.suffix.split('.')[-1]]}\n{open(path_obj).read()}\n```\n"
                            )
                            log.info(
                                f"Writing Code to  {path_obj.resolve().parent}/{path_obj.name} -> {self.codecollect_name}"
                            )

                    if path_obj.is_file() and path_obj.suffix in self.text_files:
                        open(
                            f"{path_obj.resolve().parent}/{self.filecollect_name}", "w"
                        ).write(f"# Filer \n")
                        with open(
                            f"{path_obj.resolve().parent}/{self.filecollect_name}", "w"
                        ) as files:
                            files.write(f"* [{path_obj.name}]({path_obj.name})\n")
                            log.info(
                                f"Writing File to {path_obj.resolve().parent}/{path_obj.name} -> {self.filecollect_name}"
                            )
                        # print(path_obj.parent)
                        # print(f"\t{path_obj}")

    def generate_md_list(self, path, folder: str):
        for file in folder:
            file_ext = file.split(".")[-1]
        ...


k = Kopimi()
print(k.list_files())

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