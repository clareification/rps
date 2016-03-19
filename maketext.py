import sys, string, pickle, os 
from random import randint

moves = []
rock=[]
paper=[]
scissors=[]

#-1 = rock, 0 = paper, 1 =scissors




def main():
	for x in range(0,int(sys.argv[1])):
		moves.append(randint(-1,1))
	for x in range(1,len(moves)-5):
		lastFiveMoves = moves[len(moves)-x-5:len(moves)-x]
		if moves[len(moves)-x] == -1:
			rock.append(lastFiveMoves)
		elif moves[len(moves)-x] == 0:
			paper.append(lastFiveMoves)
		else:
			scissors.append(lastFiveMoves)
	f = open("-1",'w')
	for item in rock:
		f.write(str(item) + "\n")
	f.close()
	f = open("0",'w')
	for item in paper:
		f.write(str(item) + "\n")
	f.close()
	f = open("1",'w')
	for item in scissors:
		f.write(str(item) + "\n")
	f.close()

main()