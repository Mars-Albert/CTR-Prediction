__author__ = 'mars'
import subprocess
import os,time,sys,shutil



BATCH=1000000
ONLINE=200000

start_time=time.time()



def delete():
    if(os.path.exists('output/')):
        filelist=os.listdir('output/')
        for f in filelist:
            filepath = os.path.join( 'output/', f )
            if os.path.isfile(filepath):
                os.remove(filepath)
                print(filepath+' removed!')
            elif os.path.isdir(filepath):
                shutil.rmtree(filepath,True)
                print('dir '+filepath+' removed!')




delete()

cmd = 'python batch_experiments.py {num}'.format(num=BATCH)
#subprocess.call(cmd, shell=True)



cmd = 'python online_experiments.py {num}'.format(num=ONLINE)
subprocess.call(cmd, shell=True)




print('All completed! Total time spent {0:.2f}s'.format(time.time()-start_time))