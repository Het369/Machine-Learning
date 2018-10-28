# Roll No. - 16ME30035
# Name     - Het Shah
# Assgn No - 1
# Execution - python 16ME30035_1.py --help
#			  python 16ME30035_1.py -f filename.csv	

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--filename", type=str)

args = parser.parse_args()
data_path = args.filename

def data_loader(path):
    data = []
    with open(path, 'r') as f:
        for line in f:
            words = line.split(',')
            data.append((words))
    for i in xrange(len(data)):
        for j in xrange(len(data[0])):
            data[i][j] = int(data[i][j])

    return data

data = data_loader(data_path)

h = [1]*8

for i in range(len(data)):
	if data[i][len(h)] == 1:
		for j in range(len(h)):
			h[j] = data[i][j]
	break

for i in range(len(data)):
	if data[i][len(h)] == 1:
		for j in range(len(h)):
			if data[i][j] != h[j]:
				h[j] = 99    #not viable 
count = 0
for i in range(len(h)):
	if h[i] == 0 or h[i] == 1:
		count += 1
print (count),	

for i in range(len(h)):
	if h[i] == 1:
		print "," + str(i+1),
	if h[i] == 0:
		print "," + str((i+1)*-1),

		





    
