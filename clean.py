import os
import os.path
import sys

def dot_clean(folder):
	files = os.listdir(folder)
	for file in files:
		full_name = folder + "/" + file
		if os.path.isdir(full_name):
			dot_clean(full_name)
		elif file.startswith("._"):
			os.remove(full_name)

dot_clean(sys.argv[1])          
