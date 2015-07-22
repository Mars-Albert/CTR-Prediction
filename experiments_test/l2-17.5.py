____author__ = 'mars'


import sys,subprocess,os
if len(sys.argv) != 3:
    print('wrong arg')
    exit(1)

data_path=sys.argv[1]
result_path=sys.argv[2]


cmd='python feature_engineering/csv2vw_all_categorical.py {0} {1} -train'.format(data_path,result_path)
train=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
cmd='python feature_engineering/csv2vw_all_categorical.py {0} {1} -test'.format(data_path,result_path)
test=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)

train.communicate()
cmd='vw {path}train.vw  -f {path}model --bfgs -c -k --passes 25 -b 20  --quiet --loss_function logistic --l2 17.5 --termination 1e-5  --holdout_off'.format(path=result_path)

subprocess.call(cmd,shell=True,stdout=subprocess.PIPE)

test.communicate()
cmd='vw {path}test.vw  -t -i {path}model  -p {path}preds.txt --quiet --loss_function logistic'.format(path=result_path)
subprocess.call(cmd,shell=True,stdout=subprocess.PIPE)

cmd='rm {path}train.vw {path}test.vw {path}train.vw.cache'.format(path=result_path)
subprocess.call(cmd,shell=True,stdout=subprocess.PIPE)


cmd='python utils/vw_to_kaggle.py {path}'.format(path=result_path)
subprocess.call(cmd,shell=True,stdout=subprocess.PIPE)