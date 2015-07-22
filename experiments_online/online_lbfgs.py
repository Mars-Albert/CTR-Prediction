__author__ = 'b1605'

from csv import DictReader,DictWriter




ONEDAY=6500000

def day_split():



    last=0
    this=0
    write=open('output/day1.csv','w')
    t=0
    for line in open('dataset.csv'):
        this=int(t/ONEDAY)

        if(last!=this):
            write.close()
            last=this
            write=open('output/day{0}.csv'.format(this+1),'w')
            print('day{0} completed!'.format(this))

        write.write(line)
        t+=1




TRAIN=['Id','Label','I1','I2','I3','I4','I5','I6','I7','I8','I9','I10','I11','I12','I13','C1','C2','C3','C4','C5','C6','C7','C8','C9','C10','C11','C12','C13','C14','C15','C16','C17','C18','C19','C20','C21','C22','C23','C24','C25','C26']
TEST=['Id','I1','I2','I3','I4','I5','I6','I7','I8','I9','I10','I11','I12','I13','C1','C2','C3','C4','C5','C6','C7','C8','C9','C10','C11','C12','C13','C14','C15','C16','C17','C18','C19','C20','C21','C22','C23','C24','C25','C26']

#
def day_split2():



    last=0
#    this=0
    train=open('output/day1.csv','w')
#    write.write(','.join('{0}'.format(i) for i in FIELDS)+'\n')
    test=open('output/day1_test.csv','w')
    validation=open('output/day1_val.csv','w')
#    validation.write('Id,Label\n')
    for t,line in enumerate(DictReader(open('dataset.csv'),fieldnames=TRAIN)):
        this=int(t/ONEDAY)

        if(last!=this):
            print('got! this={0} last={1}'.format(this,last))
            train.close()
            last=this
            train=open('output/day{0}.csv'.format(this+1),'w')
            train.write(','.join('{0}'.format(i) for i in TRAIN)+'\n')

            test.close()
            test=open('output/day{0}_test.csv'.format(this+1),'w')
            test.write(','.join('{0}'.format(i) for i in TEST)+'\n')

            validation.close()
            validation=open('output/day{0}_val.csv'.format(this+1),'w')
            validation.write('Id,Label\n')
            print('day{0} completed!'.format(this))

#        print(line)
        train.write(','.join('{0}'.format(line[i]) for i in TRAIN)+'\n')
        test.write(','.join('{0}'.format(line[i]) for i in TEST)+'\n')
        validation.write('{0},{1}\n'.format(line['Id'],line['Label']))
        #t+=1


#day_split()
day_split2()

last=0
dataset=open('day1.vw')
validation=open('day1_val.csv')
for e, row in enumerate(DictReader(open(input)) ):
        categorical_features = []
        for k,v in row.items():
            if k not in ['Label','Id']:
                if len(str(v)) > 0 :
                    categorical_features.append('{0}.{1}'.format(k,v)) #这里连‘-’导致测试不通过，很奇怪，无视之

        if(type=='-train'):
            if row['Label']=='1':
                label = 1
            else:
                label = -1
        else:
            if validation.readline().strip().split(',')[1] =='1':
                label = 1
            else:
                label =-1
        this=int(e/ONEDAY)
        if(last!=this):
            dataset.close()


        dataset.write('{0} \'{1} |categorical {2}\n'.format (label,row['Id'],' '.join(['{0}'.format(val) for val in categorical_features])))
        validation.write('{0},{1}\n'.format(row['Id'],row['Label']))





