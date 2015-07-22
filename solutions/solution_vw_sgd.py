__author__ = 'mars'

import subprocess,time,sys,os


results_path='output/results/online/solution_vw_sgd.py/'

os.makedirs(results_path)


#训练
cmd='vw output/online.vw -p {path}preds.txt -P 20000 --sgd --loss_function logistic'.format(path=results_path)
subprocess.call(cmd,shell=True,stdout=subprocess.PIPE)


#转换格式
cmd='python utils/vw_to_kaggle.py {path}'.format(path=results_path)
subprocess.call(cmd,shell=True,stdout=subprocess.PIPE)

#验证结果
cmd='python utils/evaluate.py {data} {result}'.format(data='output/',result=results_path)
p=subprocess.call(cmd,shell=True,stdout=sys.stderr)
