__author__ = 'mars'

import sys,subprocess,os
from csv import DictReader,DictWriter
if len(sys.argv) != 3:
    print('wrong arg')
    exit(1)

data_path=sys.argv[1]
result_path=sys.argv[2]


cmd='python feature_engineering/csv2vw_quadratic.py {0} {1} -train'.format(data_path,result_path)
train=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
cmd='python feature_engineering/csv2vw_quadratic.py {0} {1} -test'.format(data_path,result_path)
test=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)


train.communicate()
cmd='vw {path}train.vw  -f {path}model -k -b 21 --loss_function logistic -q AB -q AC --l1 1e-7'.format(path=result_path)
cmd='vw {path}train.vw  -f {path}model --bfgs -c -k --passes 22 -b 21  --loss_function logistic -q AB -q AC --l2 25 --termination 1e-5  --holdout_off'.format(path=result_path)

subprocess.call(cmd,shell=True,stdout=subprocess.PIPE)

test.communicate()
cmd='vw {path}test.vw  -t -i {path}model  -p {path}preds.txt --loss_function logistic --invert_hash {path}look'.format(path=result_path)
subprocess.call(cmd,shell=True,stdout=subprocess.PIPE)

cmd='python utils/vw_to_kaggle.py {path}'.format(path=result_path)
subprocess.call(cmd,shell=True,stdout=subprocess.PIPE)
