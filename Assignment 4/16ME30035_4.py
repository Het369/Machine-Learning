'''
Roll no    : 16ME30035	
Name       : Het Shah
Assignment : 4
Instructions to run the code: python 16ME30035_4.py
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

def knn_classify(X, Y, Z, K):
	'''
	Function to classify 
	'''
	ans = []
	for i in range (n_test):
		A = np.zeros((n_train,1))
		dist = np.concatenate((A, Y ), axis=1)
		score0 = 0
		score1 = 0

		# Calculating the distance
		for j in range(n_train):
			for k in range(n_features):
				dist[j][0] += (Z[i][k] - X[j][k])**2

		# Sorting the distances 
		dist = dist[dist[:,0].argsort()]

		for l in range (K):
			if dist[l-1][1] == 0:
				score0 += 1
			if dist[l-1][1] == 1:
				score1 += 1

		# Comparing the score for both labels
		if score0 > score1:
			ans.append(0)
		elif score0 < score1:
			ans.append(1)

	return ans


def output(ans):
	'''
	Makes the output file
	'''
	file = open('16ME30035_4.out', 'w')
	for i in ans:
		file.write(str(i) + ' ')
	file.close()

def main():
	global n_features
	global n_test
	global n_train
	global K

	# Taking KNN parameter K=5
	K = 5	

	# Reading training data and test data
	train_data = dataRead('data4.csv')
	X = train_data[:, 0 : train_data.shape[1] - 1]
	Y = train_data[:, train_data.shape[1] - 1]
	testData = dataRead('test4.csv')
	
	n_features = X.shape[1]
	n_train = X.shape[0]
	n_test = testData.shape[0]
	Y = np.reshape(Y, (n_train,1) )
	
	ans = knn_classify(X, Y, testData, K)
	output(ans)

main()