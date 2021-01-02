# -*- coding: utf-8 -*-
import json
import os
import re

from loguru import logger as log

docs_folder = "./docs"
no_code = ['.docx', '.pdf']
legal_file = [".py", ".c", ".h"]+no_code


def indexer():
    uniq_folder = {}
    for r, d, f in sorted(os.walk(docs_folder)):
        files = []
        for file in f:
            if True in [file.endswith(ext) for ext in legal_file]:
                files.append(file)
                uniq_folder[r] = files
    return uniq_folder

def md_format(file, data, type=""):
    if type == "code":
        fileext = file.split(".")[-1]
        return f"## {file}\n```{fileext}\n{data}\n```\n"
    elif type == "file":
        return (f"* [{file}]({file})\n")

def dupe_checker(file, data):
    if re.findall(fr"\#\# {file}", data) or re.findall(fr'^\* \[[file]+\]\([file]+\)$', data):
        return True
    else:
        return False

# TODO: split up into two smaller functions maybe ?!?
def generate():
    for path, files in indexer().items():
        for file in files:
            with open(f"{path}/{file}") as f:
                file_ext = "."+file.split('.')[-1]
                print (file_ext, file_ext in no_code)
                if file_ext in no_code:
                    md_file = f"{path}/files.md"
                    
                    file_ext = file.split('.')[-1]

                    with open(md_file, "a+") as mf:
                        mf.write('# Code')
                        dupes = open(md_file, "r").read()
                        if dupe_checker(file, dupes):
                            log.debug(f"{file} is already indexed")
                            
                        else:
                            log.info(f"Indexing {file} to {md_file}")
                            mf.write(md_format(file, "", type="file"))

                else:    
                    md_code = f"{path}/code.md"
                    file_ext = file.split('.')[-1]

                    with open(md_code, "a+") as mf:
                        dupes = open(md_code, "r").read()
                        if dupe_checker(file, dupes):
                            log.debug(f"{file} is already indexed")
                            
                        else:
                            log.info(f"Indexing {file} to {md_code}")
                            mf.write(md_format(file, f.read(), type="code"))

generate()