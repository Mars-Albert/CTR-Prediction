___author__ = 'mars'
import sys,subprocess,os,math

if len(sys.argv) != 3:
    print('wrong arg')
    exit(1)

data_path=sys.argv[1]
result_path=sys.argv[2]

cmd='python feature_engineering/csv2libfm.py {0} {1}'.format(data_path,result_path)
csv2vw=subprocess.call(cmd,shell=True,stdout=sys.stdout)




cmd='./utils/libFM -task r -train {train} -test {test} -out {out} -dim \'1,1,8\' -iter 100 -validation {train}'.format(train=result_path+'train.sparse',test=result_path+'test.sparse',out=result_path+'preds.txt')
csv2vw=subprocess.call(cmd,shell=True,stdout=sys.stdout)


def zygmoid(x):
	return 1 / (1 + math.exp(-x))

with open(result_path+'submission.csv','w') as outfile:
	outfile.write('Id,Predicted\n')
	for line in open(result_path+'preds.txt'):
		outfile.write('{0},{1}\n'.format('anything',zygmoid(float(line.strip()))))