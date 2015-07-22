import math,sys

if len(sys.argv) != 2:
    print('wrong arg')
    exit(1)

path=sys.argv[1]

submission=path+'submission.csv'
preds=path+'preds.txt'


def zygmoid(x):
	#I know it's a common Sigmoid feature, but that's why I probably found
	#it on FastML too: https://github.com/zygmuntz/kaggle-stackoverflow/blob/master/sigmoid_mc.py
	return 1 / (1 + math.exp(-x))

with open(submission,'w') as outfile:
	outfile.write('Id,Predicted\n')
	for line in open(preds):
		row = line.strip().split(' ')
		outfile.write('%s,%f\n'%(row[1],zygmoid(float(row[0]))))
	
