__author__ = 'mars'

import subprocess,time,sys

if len(sys.argv) != 2:
    print('wrong arguments in batch_experiments.py')
    exit(1)


EXAMPLES=int(sys.argv[1])
#10折交叉验证数据集划分
FOLD=10


def prepare_data():
    if(EXAMPLES>10000000):
        print('too many for this experiments!')

    start_time=time.time()
    print('Start the batch experiments!')
    #截取数据集
    cmd = 'python utils/prepare_dataset.py {0} output/tmp.csv'.format(EXAMPLES)
    subprocess.call(cmd, shell=True)
    #打乱顺序
    cmd = 'python utils/shuffle.py {0} {1}'.format('output/tmp.csv','output/batch.csv')
    subprocess.call(cmd, shell=True)
    #为gbdt建立频繁表
    cmd = 'feature_engineering/converters/count.py output/batch.csv > output/fc.trva.t10.txt'
    subprocess.call(cmd, shell=True)
    print('frequent value data table completed!')



    print('Time spent: {0:.2f}s\n'.format(time.time()-start_time))
    time_temp=time.time()
    print('-----------------------------------')
    print('Starting {0}-fold dataSet split!'.format(FOLD))

    #call()有阻塞，
    # popen无阻塞，可以加.wait()去等待
    #交叉验证分折划分
    cmd='python utils/k-fold_loo_split.py {src} {FOLD}'.format(src='output/batch.csv',FOLD=FOLD)
    subprocess.call(cmd,shell=True,stdout=subprocess.PIPE)

    print('Split finished! Time spent {0:.2f}s'.format(time.time()-time_temp))
    print('-----------------------------------\n')





prepare_data()

print('Start the {0}-fold cross validations:'.format(FOLD))


'''

time_temp=time.time()
cmd='./utils/cross_validator.py {fold} {solution}'.format(fold=FOLD,solution='experiments_hash/lbfgs_b12.py')
subprocess.call(cmd,shell=True,stdout=sys.stdout)
print('Time spent {0:.2f}s'.format(time.time()-time_temp))


time_temp=time.time()
cmd='./utils/cross_validator.py {fold} {solution}'.format(fold=FOLD,solution='experiments_hash/lbfgs_b17.py')
subprocess.call(cmd,shell=True,stdout=sys.stdout)
print('Time spent {0:.2f}s'.format(time.time()-time_temp))

time_temp=time.time()
cmd='./utils/cross_validator.py {fold} {solution}'.format(fold=FOLD,solution='experiments_hash/lbfgs_b18.py')
subprocess.call(cmd,shell=True,stdout=sys.stdout)
print('Time spent {0:.2f}s'.format(time.time()-time_temp))

time_temp=time.time()
cmd='./utils/cross_validator.py {fold} {solution}'.format(fold=FOLD,solution='experiments_hash/lbfgs_b19.py')
subprocess.call(cmd,shell=True,stdout=sys.stdout)
print('Time spent {0:.2f}s'.format(time.time()-time_temp))

time_temp=time.time()
cmd='./utils/cross_validator.py {fold} {solution}'.format(fold=FOLD,solution='experiments_hash/lbfgs_b20.py')
subprocess.call(cmd,shell=True,stdout=sys.stdout)
print('Time spent {0:.2f}s'.format(time.time()-time_temp))

time_temp=time.time()
cmd='./utils/cross_validator.py {fold} {solution}'.format(fold=FOLD,solution='experiments_hash/lbfgs_b21.py')
subprocess.call(cmd,shell=True,stdout=sys.stdout)
print('Time spent {0:.2f}s'.format(time.time()-time_temp))

time_temp=time.time()
cmd='./utils/cross_validator.py {fold} {solution}'.format(fold=FOLD,solution='experiments_hash/lbfgs_b22.py')
subprocess.call(cmd,shell=True,stdout=sys.stdout)
print('Time spent {0:.2f}s'.format(time.time()-time_temp))






'''


time_temp=time.time()
cmd='./utils/cross_validator.py  {fold} {solution}'.format(fold=FOLD,solution='experiments_preprocessing/4.py')
subprocess.call(cmd,shell=True,stdout=sys.stdout)
print('Time spent {0:.2f}s'.format(time.time()-time_temp))



time_temp=time.time()
cmd='./utils/cross_validator.py  {fold} {solution}'.format(fold=FOLD,solution='experiments_preprocessing/4-lbfgs.py')
subprocess.call(cmd,shell=True,stdout=sys.stdout)
print('Time spent {0:.2f}s'.format(time.time()-time_temp))



#找出最佳l2系数
time_temp=time.time()
cmd='./utils/cross_validator.py  {fold} {solution}'.format(fold=FOLD,solution='experiments_test/l2-0.py')
subprocess.call(cmd,shell=True,stdout=sys.stdout)
print('Time spent {0:.2f}s'.format(time.time()-time_temp))

time_temp=time.time()
cmd='./utils/cross_validator.py  {fold} {solution}'.format(fold=FOLD,solution='experiments_test/l2-1.py')
subprocess.call(cmd,shell=True,stdout=sys.stdout)
print('Time spent {0:.2f}s'.format(time.time()-time_temp))

time_temp=time.time()
cmd='./utils/cross_validator.py  {fold} {solution}'.format(fold=FOLD,solution='experiments_test/l2-2.5.py')
subprocess.call(cmd,shell=True,stdout=sys.stdout)
print('Time spent {0:.2f}s'.format(time.time()-time_temp))

time_temp=time.time()
cmd='./utils/cross_validator.py  {fold} {solution}'.format(fold=FOLD,solution='experiments_test/l2-5.py')
subprocess.call(cmd,shell=True,stdout=sys.stdout)
print('Time spent {0:.2f}s'.format(time.time()-time_temp))

time_temp=time.time()
cmd='./utils/cross_validator.py  {fold} {solution}'.format(fold=FOLD,solution='experiments_test/l2-7.5.py')
subprocess.call(cmd,shell=True,stdout=sys.stdout)
print('Time spent {0:.2f}s'.format(time.time()-time_temp))

time_temp=time.time()
cmd='./utils/cross_validator.py  {fold} {solution}'.format(fold=FOLD,solution='experiments_test/l2-10.py')
subprocess.call(cmd,shell=True,stdout=sys.stdout)
print('Time spent {0:.2f}s'.format(time.time()-time_temp))

time_temp=time.time()
cmd='./utils/cross_validator.py  {fold} {solution}'.format(fold=FOLD,solution='experiments_test/l2-12.5.py')
subprocess.call(cmd,shell=True,stdout=sys.stdout)
print('Time spent {0:.2f}s'.format(time.time()-time_temp))

time_temp=time.time()
cmd='./utils/cross_validator.py  {fold} {solution}'.format(fold=FOLD,solution='experiments_test/l2-15.py')
subprocess.call(cmd,shell=True,stdout=sys.stdout)
print('Time spent {0:.2f}s'.format(time.time()-time_temp))

time_temp=time.time()
cmd='./utils/cross_validator.py  {fold} {solution}'.format(fold=FOLD,solution='experiments_test/l2-17.5.py')
subprocess.call(cmd,shell=True,stdout=sys.stdout)
print('Time spent {0:.2f}s'.format(time.time()-time_temp))

time_temp=time.time()
cmd='./utils/cross_validator.py  {fold} {solution}'.format(fold=FOLD,solution='experiments_test/l2-20.py')
subprocess.call(cmd,shell=True,stdout=sys.stdout)
print('Time spent {0:.2f}s'.format(time.time()-time_temp))

time_temp=time.time()
cmd='./utils/cross_validator.py  {fold} {solution}'.format(fold=FOLD,solution='experiments_test/l2-22.5.py')
subprocess.call(cmd,shell=True,stdout=sys.stdout)
print('Time spent {0:.2f}s'.format(time.time()-time_temp))

time_temp=time.time()
cmd='./utils/cross_validator.py  {fold} {solution}'.format(fold=FOLD,solution='experiments_test/l2-25.py')
subprocess.call(cmd,shell=True,stdout=sys.stdout)
print('Time spent {0:.2f}s'.format(time.time()-time_temp))


time_temp=time.time()
cmd='./utils/cross_validator.py  {fold} {solution}'.format(fold=FOLD,solution='experiments_test/l2-30.py')
subprocess.call(cmd,shell=True,stdout=sys.stdout)
print('Time spent {0:.2f}s'.format(time.time()-time_temp))

time_temp=time.time()
cmd='./utils/cross_validator.py  {fold} {solution}'.format(fold=FOLD,solution='experiments_test/l2-35.py')
subprocess.call(cmd,shell=True,stdout=sys.stdout)
print('Time spent {0:.2f}s'.format(time.time()-time_temp))

time_temp=time.time()
cmd='./utils/cross_validator.py  {fold} {solution}'.format(fold=FOLD,solution='experiments_test/l2-40.py')
subprocess.call(cmd,shell=True,stdout=sys.stdout)
print('Time spent {0:.2f}s'.format(time.time()-time_temp))

time_temp=time.time()
cmd='./utils/cross_validator.py  {fold} {solution}'.format(fold=FOLD,solution='experiments_test/l2-50.py')
subprocess.call(cmd,shell=True,stdout=sys.stdout)
print('Time spent {0:.2f}s'.format(time.time()-time_temp))






'''


time_temp=time.time()
cmd='./utils/cross_validator.py {fold} {solution}'.format(fold=FOLD,solution='experiments_test/normalized.py')
subprocess.call(cmd,shell=True,stdout=sys.stdout)
print('Time spent {0:.2f}s'.format(time.time()-time_temp))



time_temp=time.time()
cmd='./utils/cross_validator.py {fold} {solution}'.format(fold=FOLD,solution='experiments_test/LRLBFGS.py')
subprocess.call(cmd,shell=True,stdout=sys.stdout)
print('Time spent {0:.2f}s'.format(time.time()-time_temp))




time_temp=time.time()
cmd='./utils/cross_validator.py {fold} {solution}'.format(fold=FOLD,solution='experiments_lrvsgbdt/LRXGB.py')
subprocess.call(cmd,shell=True,stdout=sys.stdout)
print('Time spent {0:.2f}s'.format(time.time()-time_temp))


time_temp=time.time()
cmd='./utils/cross_validator.py {fold} {solution}'.format(fold=FOLD,solution='experiments_lrvsgbdt/GBDT1.py')
subprocess.call(cmd,shell=True,stdout=sys.stdout)
print('Time spent {0:.2f}s'.format(time.time()-time_temp))

time_temp=time.time()
cmd='./utils/cross_validator.py {fold} {solution}'.format(fold=FOLD,solution='experiments_lrvsgbdt/GBDT2.py')
subprocess.call(cmd,shell=True,stdout=sys.stdout)
print('Time spent {0:.2f}s'.format(time.time()-time_temp))


'''





'''

time_temp=time.time()
cmd='./utils/cross_validator.py  {fold} {solution}'.format(fold=FOLD,solution='experiments_preprocessing/3.py')
subprocess.call(cmd,shell=True,stdout=sys.stdout)
print('Time spent {0:.2f}s'.format(time.time()-time_temp))

time_temp=time.time()
cmd='./utils/cross_validator.py {fold} {solution}'.format(fold=FOLD,solution='experiments_preprocessing/5.py')
subprocess.call(cmd,shell=True,stdout=sys.stdout)
print('Time spent {0:.2f}s'.format(time.time()-time_temp))

time_temp=time.time()
cmd='./utils/cross_validator.py  {fold} {solution}'.format(fold=FOLD,solution='experiments_preprocessing/6.py')
subprocess.call(cmd,shell=True,stdout=sys.stdout)
print('Time spent {0:.2f}s'.format(time.time()-time_temp))


time_temp=time.time()
cmd='./utils/cross_validator.py  {fold} {solution}'.format(fold=FOLD,solution='experiments_fm/fm1.py')
subprocess.call(cmd,shell=True,stdout=sys.stdout)
print('Time spent {0:.2f}s'.format(time.time()-time_temp))

time_temp=time.time()
cmd='./utils/cross_validator.py  {fold} {solution}'.format(fold=FOLD,solution='experiments_fm/fm2.py')
subprocess.call(cmd,shell=True,stdout=sys.stdout)
print('Time spent {0:.2f}s'.format(time.time()-time_temp))




cmd='./utils/cross_validator.py {fold} {solution}'.format(fold=FOLD,solution='solution_simple_sgd.py')
subprocess.call(cmd,shell=True,stdout=sys.stdout)
print('Time spent {0:.2f}s'.format(time.time()-time_temp))

time_temp=time.time()
cmd='./utils/cross_validator.py {fold} {solution}'.format(fold=FOLD,solution='solution_vw_default_all_categorical.py')
subprocess.call(cmd,shell=True,stdout=sys.stdout)
print('Time spent {0:.2f}s'.format(time.time()-time_temp))

time_temp=time.time()
#无处理全分类属性
cmd='./utils/cross_validator.py {fold} {solution}'.format(fold=FOLD,solution='solution_vw_lbfgs_all_categorical.py')
subprocess.call(cmd,shell=True,stdout=sys.stdout)
print('Time spent {0:.2f}s'.format(time.time()-time_temp))

time_temp=time.time()
#特征处理过，全分类属性
cmd='./utils/cross_validator.py {fold} {solution}'.format(fold=FOLD,solution='solution_vw_lbfgs_normalized_categorical.py')
subprocess.call(cmd,shell=True,stdout=sys.stdout)
print('Time spent {0:.2f}s'.format(time.time()-time_temp))

time_temp=time.time()
cmd='./utils/cross_validator.py {fold} {solution}'.format(fold=FOLD,solution='solution_vw_lbfgs_gbdt.py')
subprocess.call(cmd,shell=True,stdout=sys.stdout)
print('Time spent {0:.2f}s'.format(time.time()-time_temp))

time_temp=time.time()
cmd='./utils/cross_validator.py {fold} {solution}'.format(fold=FOLD,solution='solution_ffm_gbdt.py')
subprocess.call(cmd,shell=True,stdout=sys.stdout)
print('Time spent {0:.2f}s'.format(time.time()-time_temp))

time_temp=time.time()
cmd='./utils/cross_validator.py {fold} {solution}'.format(fold=FOLD,solution='solution_ffm_normalized.py')
subprocess.call(cmd,shell=True,stdout=sys.stdout)
print('Time spent {0:.2f}s'.format(time.time()-time_temp))

time_temp=time.time()
cmd='./utils/cross_validator.py {fold} {solution}'.format(fold=FOLD,solution='solution_vw_quadratic_features.py')
subprocess.call(cmd,shell=True,stdout=sys.stdout)
print('Time spent {0:.2f}s'.format(time.time()-time_temp))

time_temp=time.time()
cmd='./utils/cross_validator.py {fold} {solution}'.format(fold=FOLD,solution='solution_xgboost_gbdt.py')
subprocess.call(cmd,shell=True,stdout=sys.stdout)
print('Time spent {0:.2f}s'.format(time.time()-time_temp))

time_temp=time.time()

cmd='./utils/cross_validator.py {fold} {solution}'.format(fold=FOLD,solution='solution_xgboost_gbdt_onehotencoding.py')
subprocess.call(cmd,shell=True,stdout=sys.stdout)
print('Time spent {0:.2f}s'.format(time.time()-time_temp))

time_temp=time.time()
cmd='./utils/cross_validator.py {fold} {solution}'.format(fold=FOLD,solution='solution_libfm.py')
subprocess.call(cmd,shell=True,stdout=sys.stdout)
print('Time spent {0:.2f}s'.format(time.time()-time_temp))


'''
