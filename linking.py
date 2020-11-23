#!/usr/bin/env python3
import os

forbidden_ = ['md', 'html']
legal = ['pdf', 'txt']

for dir_ in os.listdir("./docs"):
	print ("=========")
	print(dir_)
	print ("=========")
	listing = os.listdir(f"./docs/{dir_}")

	open(f"./docs/{dir_}/Files.md", "w")
	file = open(f"./docs/{dir_}/Files.md", 'a+')
	file.write('#Files\n')
	for l in listing:
		file_ext = l.split('.')[-1]
		if file_ext not in forbidden_:
			...
		elif file_ext in legal:
			file.write(f"* [{l}]({l})\n")
			#print(f"* [{l}]({l})\r")
		else:
			...
	


"""
	print(os.getcwd())
	os.chdir(f"./docs/{dir_}")
	print(os.getcwd())
	os.chdir(f"./docs/{dir_}")
	
	os.chdir(f"./docs/{dir_}")
	open(f"./Files.md", "w")
	file = open(f'./Files.md', 'a+')
	file.write('#Files\n')
	for l in listing:
		file_ext = l.split('.')[-1]
		if file_ext not in forbidden_:
			file.write(f"* [{l}]({l})\n")
		os.chdir('..')
	"""