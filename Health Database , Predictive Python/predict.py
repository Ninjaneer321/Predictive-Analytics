import random

file_name = "data/apples_oranges.txt"

def predict_class_blind():
	coin_value = random.randrange(0,2)
	if coin_value == 0:
		return "Apple"
	else:
		return "Orange"

def predict_class_count(file_name):
	f = open(file_name)
	oranges = 0
	apples = 0	
	for line in f:
		line = line.strip()
		if len(line) > 0:
			features = line.split('\t')
			cls = features[-1]
			if cls == "orange":
				oranges += 1
			else:
				apples += 1

	if apples > oranges:
		return "Apple"
	else:
		return "Orange"
	f.close()	


def predict_class(file_name, shape, smell):
	f = open(file_name)
	for line in f:
		line = line.strip()
		if len(line) > 0:
			features = line.split('\t')
			mshape = features[1]
			msmell = features[-2]	
			if mshape == shape and msmell == smell:
				print line
	f.close()


def count_uniq(names):
	counts={}
	for name in names:
		if name in counts:
			counts[name] += 1
		else:
			counts[name] = 1
	return counts


print predict_class(file_name, 'round', 'sweet')









