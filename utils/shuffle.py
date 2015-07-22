__author__ = 'mars'


import sys,random


if len(sys.argv) != 3:
    print('wrong arg')
    exit(1)




where,to=sys.argv[1:]


where=open(where)
to=open(to,'w')


lines = where.readlines()
olines=[]
to.write(lines.pop(0))
while lines:
    olines.append(lines.pop(random.randrange(len(lines))))
to.write(''.join(olines))

where.close()
to.close()
print('dataSet shuffled!')