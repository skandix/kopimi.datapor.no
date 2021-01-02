import json
import os

docs_folder = "./docs"
#legal = ['.py','.c','.h','.docx', '.pdf' ]
legal = ['.']

def indexer():
    uniq_folder = {}
    for r, d, f in sorted(os.walk(docs_folder)):
        files = []
        for file in f:
            if (True in [file.endswith(ext) for ext in legal]):
                files.append(file)
                uniq_folder[r] = files
    return json.dumps(uniq_folder, indent=4)
print (indexer())