import pickle
import sys
with open(sys.argv[1],"rb") as f:
	try:
		while True:
			print(pickle.load(f))
	except EOFError:
		print("done")
