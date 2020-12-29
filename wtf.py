#!/usr/bin/env python3
import os
import json

from pathlib import Path
from loguru import logger as log


class Kopimi:
    def __init__(self):
        self.path = Path("./docs/")
        self.md_code_style = {"py": "python", "c": "c", "h": "h"}

        self.code_f = [".py", ".c", ".h"]
        self.text_f = [".pdf", ".docx"]

        # mkdocs vital files
        self.forbidden_files = ["index.md", "lists.md", "extra.css"]
        self.forbidden_folders = ["stylesheets"]
        self.forbidden_suffix = [".html", ".txt", ".png", ".md", ".db"]

    def _json_pretty(self, data: dict) -> dict:
        return json.dumps(data, indent=4)

    def return_markdown_lang(self, suffix: str) -> str:
        """ if code language exists in list, return the dict with the rigth value """
        if suffix in self.code_f:
            suffix = suffix.split(".")[-1]
            return self.md_code_style[suffix]
        return

    def dead_end(self, statement) -> bool:
        if statement.is_dir():
            return statement.name in self.forbidden_folders
        elif statement.is_file():
            return not (
                statement.name in self.forbidden_files
                or statement.suffix in self.forbidden_suffix
            )

    def list_files(self):
        indexed_struct = {}
        for _dir in self.path.iterdir():
            if self.dead_end(_dir):
                for _file in sorted(_dir.rglob("*")):
                    if self.dead_end(_file):
                        print(_dir.resolve())
                        indexed_struct[_dir.parent] = [_file.name]
        return self._json_pretty(indexed_struct)

    def tree(self, directory):
        fuck = {}
        for path in sorted(directory.rglob("**/*")):
            if self.dead_end(path):
                # print(path.parent, path.is_file())
                fuck[path.parent] = path.name if path.is_file()

            # print(f"{spacer}+ {path.name}")
        return fuck

    def razzia(self):
        # return self.list_files()
        return self.tree(self.path)

    def generate_md_list(self, path, folder: str):
        for file in folder:
            file_ext = file.split(".")[-1]
        ...


k = Kopimi()
print(k.razzia())
