__author__ = 'mars'

import os, sys
from csv import DictReader,DictWriter
if len(sys.argv) != 3:
    print('wrong arg')
    exit(1)

path,src_file = sys.argv[1:]

FIELDS=['Id','I1','I2','I3','I4','I5','I6','I7','I8','I9','I10','I11','I12','I13','C1','C2','C3','C4','C5','C6','C7','C8','C9','C10','C11','C12','C13','C14','C15','C16','C17','C18','C19','C20','C21','C22','C23','C24','C25','C26']

reader=DictReader(open(path+'/'+src_file))

writer=DictWriter(open(path+'/test500k-800k.csv','w'), fieldnames=FIELDS)
writer.writeheader()

with open(path+'/validation500k-800k.csv','w') as result:
    result.write('Id,Label\n')
    for t,row in enumerate(reader):
        id=row['Id']
        label=row['Label']
        del row['Label']
        writer.writerow(row)
        result.write('%s,%s\n'%(id,label))











