__author__ = 'mars'

import os, sys
if len(sys.argv) != 3:
    print('wrong arguments in prepare_dataset.py')
    exit(1)




num=int(sys.argv[1])
output=sys.argv[2]

if(num>=4000000):
    print('too many data.py')
    exit(1)


count=0;


with open(output,'w') as file:
    for line in open('dataset.csv','r'):
        if(count%10000==0):print(count,' processed!')
        file.write(line)
        if(count>=num):
            file.close()
            break
        count+=1

print('dataSet prepared!')