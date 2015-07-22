__author__ = 'mars'
import subprocess,time,sys
from csv import DictReader,DictWriter

if len(sys.argv) != 2:
    print('wrong arguments in batch_experiments.py')
    exit(1)


EXAMPLES=int(sys.argv[1])


SOURCE='output/online.csv'
SOURCE='dataset.csv'
#if(EXAMPLES>10000000):
 #   print('too many for this experiments!')


start_time=time.time()
print('Start the online experiments!')


def prepare_data():
    cmd = 'python utils/prepare_dataset.py {0} output/online.csv'.format(EXAMPLES)
    #subprocess.call(cmd, shell=True)


    #输出validation.csv
    writer_validation=open('output/validation.csv','w')
    writer_validation.write('Id,Label\n')
    for t,row in enumerate(DictReader(open(SOURCE))):
        writer_validation.write('%s,%s\n'%(row['Id'],row['Label']))
        if (t%100000 ==0):
            print('{0} validation data completed!'.format(t))
    writer_validation.close()



    #csv to vw    全类别属性转换
    with open('output/online.vw','w') as outfile:
        for e, row in enumerate(DictReader(open(SOURCE)) ):
            categorical_features = []
            for k,v in row.items():
                if k not in ['Label','Id']:
                    if len(str(v)) > 0 :
                        categorical_features.append('{0}.{1}'.format(k,v)) #这里连‘-’导致测试不通过，很奇怪，无视之

            if row['Label']=='1':
                label = 1
            else:
                label = -1

            outfile.write('{0} \'{1} |categorical {2}\n'.format (label,row['Id'],' '.join(['{0}'.format(val) for val in categorical_features])))
            if(e%100000==0):
                print('{0} vw data completed!'.format(e))







    print('Online data prepared!')



#prepare_data()

cmd = 'python experiments_online/online_lbfgs.py'.format(EXAMPLES)
subprocess.call(cmd, shell=True)


'''


time_temp=time.time()
cmd='python {solution}'.format(solution='solutions/solution_vw_default_sgd.py')
subprocess.call(cmd,shell=True,stdout=sys.stdout)
print('Time spent {0:.2f}s'.format(time.time()-time_temp))


time_temp=time.time()
cmd='python {solution}'.format(solution='solutions/solution_vw_sgd.py')
subprocess.call(cmd,shell=True,stdout=sys.stdout)
print('Time spent {0:.2f}s'.format(time.time()-time_temp))


time_temp=time.time()
cmd='python {solution}'.format(solution='solutions/solution_vw_pistol.py')
subprocess.call(cmd,shell=True,stdout=sys.stdout)
print('Time spent {0:.2f}s'.format(time.time()-time_temp))

time_temp=time.time()
cmd='python {solution}'.format(solution='solutions/solution_vw_ftrl.py')
subprocess.call(cmd,shell=True,stdout=sys.stdout)
print('Time spent {0:.2f}s'.format(time.time()-time_temp))

'''