__author__ = 'mars'
import sys,subprocess,os

if len(sys.argv) != 3:
    print('wrong arg')
    exit(1)

data_path=sys.argv[1]
result_path=sys.argv[2]


cmd='python csv2vw_gbdt.py {0} {1}'.format(data_path,result_path)
csv2vw=subprocess.call(cmd,shell=True,stdout=sys.stdout)



#trian&test

cmd='vw {path}train.vw  -f {path}model --bfgs  -c -k --passes 22 -b 21  --quiet --loss_function logistic --l2 70 --termination 1e-5  --holdout_off'.format(path=result_path)
subprocess.call(cmd,shell=True,stdout=subprocess.PIPE)

cmd='vw {path}test.vw  -t -i {path}model  -p {path}preds.txt  --quiet --loss_function logistic'.format(path=result_path)
subprocess.call(cmd,shell=True,stdout=subprocess.PIPE)

cmd='python utils/vw_to_kaggle.py {path}'.format(path=result_path)
subprocess.call(cmd,shell=True,stdout=subprocess.PIPE)


