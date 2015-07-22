__author__ = 'mars'
import os, sys,subprocess

import copy
import shutil
if len(sys.argv) != 3:
    print('wrong arguments in k-fold_loo_split.py')
    exit(1)

FOLD = int(sys.argv[2])
src=sys.argv[1]

rootdir='output/cross_validation_split/'



os.makedirs(rootdir)

workers=[]


#并行执行

for i in range(FOLD):
    cmd='python utils/split_worker.py {src_file} {dest_path} {fold}'.format(src_file=src,dest_path=rootdir+'split_{id}/'.format(id=i),fold=FOLD)
    worker=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
    workers.append(worker)
for worker in workers:
    print(worker.communicate())







