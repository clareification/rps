
import sys, string, pickle, os 
import numpy as np
from sklearn import svm
from sklearn.externals import joblib
import warnings
warnings.filterwarnings("ignore")
trainingSet = []
indexTypes = []
moves = []

#-1 = rock, 0 = paper, 1 =scissors

def setupBaseSet(textfile): #adds data from textfiles line by line into an list of floats, which is added to the list of vectors in the training set
	with open(textfile) as f:
		for x in f.readlines():
			line = (x.strip("[]\n")).split(", ")
			outline = []
			for char in line:
				outline.append(int(char))
			trainingSet.append(outline)
			indexTypes.append(int(os.path.splitext(textfile)[0]))
		f.close()

def setup():
	for index in range(1,len(sys.argv)):
		setupBaseSet(sys.argv[index])
	print "Loaded base set"


def main():
	setup()
	clf = svm.SVC()
	clf.fit(trainingSet, indexTypes)
	pickle_file = open('training_data.pkl', 'wb')
	pickle.dump(trainingSet, pickle_file)
	pickle_file.close()
	pf2 = open('index_types.pkl', 'wb')
	pickle.dump(indexTypes, pf2)
	pf2.close()
	while(True):
		if not (len(moves) < 5):
			aboutToAdd = []
			for x in range(0,5):
				aboutToAdd.append(moves[len(moves)-x-1])
			currentMove = input()
			prediction = int(clf.predict(aboutToAdd))
			winningMove = ((prediction+2)%3)-1
			#print "Prediction: " + str(prediction)
			#print "Computer's move: " + str(winningMove)
			if int(currentMove) == prediction:
				print("right")
			else:
				print("wrong")
			trainingSet.append(aboutToAdd)
			if currentMove == -1:
				indexTypes.append(-1)
			elif currentMove == 0:
				indexTypes.append(0)
			else:
				indexTypes.append(1)
			moves.append(currentMove)
			clf.fit(trainingSet, indexTypes)
		else:
			currentMove = input()
			moves.append(currentMove)

main()
