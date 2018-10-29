'''
Roll no    : 16ME30035	
Name       : Het Shah
Assignment : 3
Instructions to run the code: python 16ME30035_3.py
'''

#Imports
import math
import numpy as np

def dataRead(filename):
	'''
	Read data from csv file
	'''
	data = np.genfromtxt(filename, delimiter = ',')	
	return data 

def probc(X):
	'''
	Calculates the probability p(c) for class
	'''
	n = float(X.shape[0])
	n1 = float(np.count_nonzero(X))
	p1 = float(n1/n)
	p0 = 1 - p1
	return p0, p1

def probx_c(X,Y):
	'''
	Calculates probabilities of p(x|c)
	'''
	n11 = 0   #n_classvalue_attributevalue
	n10 = 0
	n01 = 0
	n00 = 0
	pc0 = np.zeros((2,8), dtype = float)
	pc1 = np.zeros((2,8), dtype = float)
	n_data = X.shape[0]  		# n_data = 20
	n_features = X.shape[1]     # n_features = 8
	for i in range(0, n_features):
			for j in range(0, n_data):
				if Y[j] == 0:
					if X[j][i] == 0:
						n00 += 1    
					if X[j][i] == 1:
						n01 += 1
				if Y[j] == 1:
					if X[j][i] == 0:
						n10 += 1    
					if X[j][i] == 1:
						n11 += 1
			#Laplacian smooting of alpha = 1
			pc0[0][i] = (float(n00)+1.0)/(n00+n01+2.0)
			pc0[1][i] = (float(n01)+1.0)/(n00+n01+2.0)
			pc1[0][i] = (float(n10)+1.0)/(n10+n11+2.0)
			pc1[1][i] = (float(n11)+1.0)/(n10+n11+2.0)
			n00 = n01 = n10 = n11 = 0
	return pc0, pc1

def train(X, Y):
	'''
	Takes input the dataset and Calculates the probabilities
	'''
	p0, p1 = probc(Y)
	pc0, pc1 = probx_c(X, Y)
	return p0, p1, pc0, pc1

def predict(X, p0, p1, pc0, pc1):
	'''
	Takes test data and probabilities to give the output
	'''
	ans = []
	for i in range(0, X.shape[0]):
		prob0 = float(p0)
		for j in range(0, X.shape[1]):
			if X[i][j] == 0:
				prob0 *= pc0[0][j]
			if X[i][j] == 0:
				prob0 *= pc0[1][j]
		prob1 = float(p1)
		for j in range(0, X.shape[1]):
			if X[i][j] == 0:
				prob1 *= pc1[0][j]
			if X[i][j] == 0:
				prob1 *= pc1[1][j]
		if prob0 > prob1:
			ans.append(0)
		if prob0 < prob1:
			ans.append(1)
	#print ans[0], ans[1], ans[2], ans[3]		
	output(ans)

def output(ans):
	'''
	Makes the output file
	'''
	file = open('16ME30035_3.out', 'w')
	for i in ans:
		file.write(str(i) + ' ')
	file.close()

def main():
	train_data = dataRead('data3.csv')
	X = train_data[:, 0 : train_data.shape[1] - 1]
	Y = train_data[:, train_data.shape[1] - 1]
	n_features = X.shape[1]
	p0, p1, pc0, pc1 = train(X, Y)

	testData = dataRead('test3.csv')
	predict(testData, p0, p1, pc0, pc1) 

main()