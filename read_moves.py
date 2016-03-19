# given: txt files of format 5 comma-separated values per line representing each move
import sys
import pickle
def format_training(String filename):
	infile = open(filename, 'r')
	data = infile.read()
	