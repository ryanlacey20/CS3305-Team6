import json
def readLevel(path):
	f = open(path)
	data = json.load(f)
	f.close()
	return data