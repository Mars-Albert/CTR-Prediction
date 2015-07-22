__author__ = 'mars'
import sys,subprocess,os
from csv import DictReader,DictWriter
if len(sys.argv) != 2:
    print('wrong arg')
    exit(1)

path=sys.argv[1]



cmd='python csv_to_vw_all_categorical.py {path} -train'.format(path=path)
#train=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
cmd='python csv_to_vw_all_categorical.py {path}  -test'.format(path=path)
#test=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)


#train.communicate()
#train

#test.communicate()

#bfgs  记得加-k，不用之前的cache！
#cmd='vw {path}train.vw  -f {path}model --bfgs --progress 100000 -c -k --passes 25 -b 21  --loss_function logistic --l2 50 --termination 1e-6  --holdout_off'.format(path=path)

#online (one pass) sgd !!但结果非常差  需要仔细的调学习率参数
cmd='vw {path}train.vw  -f {path}model -b 21 --loss_function logistic --progress 5000 --sgd'.format(path=path)

#batch sgd 病态下（参数为 -l 3.5e-6  --power_t 0.7）（未标准化的数值特征与分类特征混合）收敛很慢,全分类特征收敛数度可以   要加l2
#cmd='vw {path}train.vw  -f {path}model -b 21 --loss_function logistic --progress 50000 --sgd -c  --passes 20 --holdout_off'.format(path=path)

#默认online 学习法，效果最好
cmd='vw {path}train.vw  -f {path}model -b 22  -p {path}preds.txt --loss_function logistic  --progress 500'.format(path=path)

subprocess.call(cmd,shell=True,stdout=subprocess.PIPE)


print('step 1 completed!\n')
#test


#标准测试语句
cmd='vw {path}test.vw  -t -i {path}model  -p {path}preds.txt -P 500 --loss_function logistic'.format(path=path)

#sgd 在线测试语句
#cmd='vw {path}test.vw  -i {path}model -p {path}preds.txt --loss_function logistic  -l 1e-6 --power_t 0.8 --progress 500 --sgd'.format(path=path)

#默认online学习测试
#cmd='vw {path}test.vw  -i {path}model  -p {path}preds.txt -P 1 --loss_function logistic --audit '.format(path=path)


#subprocess.call(cmd,shell=True,stdout=subprocess.PIPE)

#转换
cmd='python utils/vw_to_kaggle.py {path}'.format(path=path)
subprocess.call(cmd,shell=True,stdout=subprocess.PIPE)


cmd='rm {path}model {path}preds.txt'.format(path=path)
#subprocess.call(cmd,shell=True,stdout=subprocess.PIPE)