import sys, string, pickle, os 
import numpy as np
from sklearn import svm
from sklearn.externals import joblib
import warnings
warnings.filterwarnings("ignore")

#-1 = rock, 0 = paper, 1 =scissors

def main():
	clf = svm.SVC()
	trainingSet = joblib.load(sys.argv[1])
	indexTypes = joblib.load(sys.argv[2])
	moves = joblib.load('prev_moves.pkl')
	clf.fit(trainingSet, indexTypes)
	if not (len(moves) < 5):
		aboutToAdd = []
		for x in range(0,5):
			aboutToAdd.append(moves[len(moves)-x-1])
		currentMove = int(sys.argv[3])
		prediction = int(clf.predict(aboutToAdd))
		winningMove = ((prediction+2)%3)-1
		# print "Prediction: " + str(prediction)
		# print "Computer's move: " + str(winningMove)
		if int(currentMove) == prediction:
			print("win")
		elif int(currentMove) == winningMove:
			print("tie")
		else:
			print("lose")
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
		currentMove = sys.argv[1]
		moves.append(currentMove)
	joblib.dump(trainingSet, sys.argv[1])
	joblib.dump(indexTypes, sys.argv[2])
	joblib.dump(moves, 'prev_moves.pkl')
	m = joblib.load('prev_moves.pkl')

main()
