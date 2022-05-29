# actually not very much code of mine:
# https://github.com/cverdence/simplennet

import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

# 6 samples formed by 3 inputs
input_train = np.array([[0,1,0],[0,1,1],[0,0,0],[10,0,0],[10,1,1],[10,0,1]])
output_train = np.array([[0],[0],[0],[1],[1],[1]])
input_pred = np.array([1,1,0])

# test samples for the network
input_test = np.array([[1,1,1],[10,0,1],[0,1,10],[10,1,10],[0,0,0],[0,1,1]])
output_test = np.array([[0],[1],[0],[1],[0],[0]])

# we nedd to scale inputs and outputs because otherwise 
# the network can mismatch the values between inputs
scaler = MinMaxScaler()
input_train_scaled = scaler.fit_transform(input_train)
output_train_scaled = scaler.fit_transform(output_train)
input_test_scaled = scaler.fit_transform(input_test)
output_test_scaled = scaler.fit_transform(output_test)

class NeuralNetwork():
	def __init__(self, ):
		# number of input nodes
		self.inputSize = 3
		# number of output nodes
		self.outputSize = 1
		# number of inermediate nodes
		self.hiddenSize = 3

		# adding weights
		self.W1 = np.random.rand(self.inputSize, self.hiddenSize)
		self.W2 = np.random.rand(self.hiddenSize, self.outputSize)

		# error list
		self.error_list = []
		# setting limit to select the good outputs
		self.limit = 0.5
		# various outpus
		self.true_positives = 0
		self.false_positives = 0
		self.true_negatives = 0
		self.false_negatives = 0

	# preview of the future propagation
	def forward(self, X):
		# forwards the first weight
		self.z = np.matmul(X, self.W1)
		self.z2 = self.sigmoid(self.z)
		# forwards the second weight
		self.z3 = np.matmul(self.z2, self.W2)
		o = self.sigmoid(self.z3)
		return o

	# statistic sigmoids
	def sigmoid(self, s):
		return 1 / (1 + np.exp(-s))
	def sigmoidPrime(self, s):
		return s * (1 - s)

	# it adjusts the wiìeights of the network in order to reduce the error
	def backward(self, X, y, o):
	 # getting the error of the first weight
		self.o_error = y - o
		#using error to balance the second weight
		self.o_delta = self.o_error * self.sigmoidPrime(o)
		# getting the error of the second weight
		self.z2_error = np.matmul(self.o_delta, np.matrix.transpose(self.W2))
		# using error to balance the first weight
		self.z2_delta = self.z2_error * self.sigmoidPrime(self.z2)
		# weigths adjustment
		self.W1 += np.matmul(np.matrix.transpose(X), self.z2_delta)
		self.W2 += np.matmul(np.matrix.transpose(self.z2), self.o_delta)

	# it goes forward and backword in order to balance the weights
	def train(self, X, y, epochs):
		for epoch in range(epochs):
			# every loop tries balace the weights on the network
			o = self.forward(X)
			self.backward(X, y, o)
			self.error_list.append(np.abs(self.o_error).mean())

	# predicts the output
	def predict(self, x_predicted):
		return self.forward(x_predicted).item()

	# plots the error developement
	def view_error_development(self):
		plt.plot(range(len(self.error_list)), self.error_list)
		plt.title('Mean Sum Squared Loss')
		plt.xlabel('Epoch')
		plt.ylabel('Loss')

	# calculate the accuracy and its components
	def test_evaluation(self, input_test, output_test):
		for i, test_element in enumerate(input_test):
			# validates the outpus
			if self.predict(test_element) > self.limit and output_test[i] == 1:
				self.true_positives += 1
			if self.predict(test_element) < self.limit and output_test[i] == 1:
				self.false_negatives += 1
			if self.predict(test_element) > self.limit and output_test[i] == 0:
				self.false_positives += 1
			if self.predict(test_element) < self.limit and output_test[i] == 0:
				self.true_negatives += 1
		print('True positives: ', self.true_positives, '\nTrue negatives: ', self.true_negatives,
				'\nFalse positives: ', self.false_positives, '\nFalse negatives: ', self.false_negatives,
				'\nAccuracy: ', (self.true_positives + self.true_negatives) /
				(self.true_positives + self.true_negatives + self.false_positives + self.false_negatives))

def main():
	# creates the neural network
	NN = NeuralNetwork()
	# trains the NN with 200 epochs
	NN.train(input_train_scaled, output_train_scaled, 200)
	# predicts the NN output
	NN.predict(input_pred)
	# plots the error
	NN.view_error_development()
	# test the NN
	NN.test_evaluation(input_test_scaled, output_test_scaled)
	plt.show()

if __name__ == '__main__':
	main()