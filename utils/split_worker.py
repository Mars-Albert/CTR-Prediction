__author__ = 'mars'

import os, sys
from csv import DictReader,DictWriter
import random



#待分割源文件，存放目录，折数
src_file,dest_path,FOLD= sys.argv[1:]
FOLD=int(FOLD)

def isTest():
    return random.randint(0,FOLD-1)==0



os.makedirs(dest_path)
#print('mkdirs '+root_path)

FIELDS_train=['Id','Label','I1','I2','I3','I4','I5','I6','I7','I8','I9','I10','I11','I12','I13','C1','C2','C3','C4','C5','C6','C7','C8','C9','C10','C11','C12','C13','C14','C15','C16','C17','C18','C19','C20','C21','C22','C23','C24','C25','C26']

FIELDS_test=['Id','I1','I2','I3','I4','I5','I6','I7','I8','I9','I10','I11','I12','I13','C1','C2','C3','C4','C5','C6','C7','C8','C9','C10','C11','C12','C13','C14','C15','C16','C17','C18','C19','C20','C21','C22','C23','C24','C25','C26']




writer_train=DictWriter(open(dest_path+'/train.csv','w'), fieldnames=FIELDS_train)
writer_train.writeheader()
writer_test=DictWriter(open(dest_path+'/test.csv','w'), fieldnames=FIELDS_test)
writer_test.writeheader()
writer_validation=open(dest_path+'/validation.csv','w')
writer_validation.write('Id,Label\n')



for t,row in enumerate(DictReader(open(src_file))):
    if(isTest()==False):
        writer_train.writerow(row)
    else:
        writer_validation.write('%s,%s\n'%(row['Id'],row['Label']))
        del row['Label']
        writer_test.writerow(row)
#    if((t+1)%5000==0):
#        print(str(t+1)+' completed!')

print('worker{id} finished!'.format(id=id))