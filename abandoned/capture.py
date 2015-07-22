__author__ = 'mars'


import os, sys
if len(sys.argv) != 5:
    print('wrong arg')
    exit(1)
src_path, dst_path, start_str,num_str = sys.argv[1:]
start_pos=int(start_str)
if(start_pos<0):start_pos=0
num=int(num_str)

count=0;
with open(dst_path,'w') as file:
    for line in open(src_path,'r'):
        if(count%10000==0):print(count,' processed!')
        if(count==0):
            file.write(line)
        if(count<=start_pos):
            count+=1
            continue
        else:
            file.write(line)
            if(count-start_pos>=num):
                file.close()
                break
            count+=1

print('finished!')