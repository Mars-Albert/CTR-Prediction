__author__ = 'mars'

from datetime import datetime
from csv import DictReader
import sys,subprocess,os

if len(sys.argv) != 3:
    print('wrong arg')
    exit(1)
NR_THREAD=1
#=2时，cat有错误！！

data_path=sys.argv[1]
save_path=sys.argv[2]



'''

对特征进行标准化处理

数值属性，大于2的，v<-|_log(v)**2_|，变为分类属性
分类属性，出现次数少于10次的转为特殊值


pre-c


'''

#-----------------------------------normalize------------------------

cmd = 'feature_engineering/converters/add_dummy_label.py {data}test.csv {data}test.tmp.csv'.format(data=data_path)
subprocess.call(cmd, shell=True)
print('dummy label to test.csv added!\n')



#tr.csv原始特征，tr.gbdt.out增强（gbdt）特征
cmd = 'feature_engineering/converters/parallelizer-normalization2ffm.py -s {nr_thread}  {data}train.csv {save}tr.sp'.format(nr_thread=NR_THREAD,data=data_path,save=save_path)
subprocess.call(cmd, shell=True)

print('normalized features added to train dataSet\n')

cmd = 'feature_engineering/converters/parallelizer-normalization2ffm.py -s {nr_thread} {data}test.tmp.csv {save}te.sp'.format(nr_thread=NR_THREAD,data=data_path,save=save_path)
subprocess.call(cmd, shell=True)
print('normalized features added to test dataSet\n')


#-----------------------------------normalize------------------------

print('gbdt process completed!')


#to ffm__author__ = 'mars'

cmd = './ffm -k 4 -t 11 -s {nr_thread} {save}te.sp {save}tr.sp'.format(nr_thread=NR_THREAD,save=save_path)
subprocess.call(cmd, shell=True)
cmd = './make_ffm_submission.py {save}te.sp.out {save}submission.csv'.format(nr_thread=NR_THREAD,save=save_path)
subprocess.call(cmd, shell=True)

