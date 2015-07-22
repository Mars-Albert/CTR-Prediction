
from datetime import datetime
from csv import DictReader
import sys

if len(sys.argv) != 3:
    print('wrong arg')
    exit(1)


path,type=sys.argv[1:]



train=True
if(type=='-test'):
    train=False


def csv_to_vw(path,train=True):

  start = datetime.now()
#  print('\nTurning %s into %s. Is_train_set? %s'%(loc_csv,loc_output,train))


  if(train):
     with open(path+'train.vw','w') as outfile:
        for e, row in enumerate( DictReader(open(path+'train.csv')) ):

	     #Creating the features
            numerical_features = []
            categorical_features = []
            for k,v in row.items():
                if k not in ['Label','Id']:
                    if 'I' in k: # numerical feature, example: I5
                        if len(str(v)) > 0: #check for empty values
                            numerical_features.append('{0}:{1}'.format(k,v))
                    if 'C' in k: # categorical feature, example: C2
                        if len(str(v)) > 0:
                            categorical_features.append('{0}.{1}'.format(k,v))


            if row['Label'] == '1':
                label = 1
            else:
                label = -1 #we set negative label to -1
            outfile.write( '{0} \'{1} |numerical {2} |categorical {3}\n'.format(label,row['Id'],' '.join(['{0}'.format(val) for val in numerical_features]),' '.join(['{0}'.format(val) for val in categorical_features])) )



        if e % 1000 == 0:
            print('%s\t%s'%(e, str(datetime.now() - start)))
  else:
     validation=open(path+'validation.csv')
     validation.__next__()
     with open(path+'test.vw','w') as outfile:
        for e, row in enumerate( DictReader(open(path+'test.csv')) ):

	     #Creating the features
            numerical_features = []
            categorical_features = []
            for k,v in row.items():
                if k not in ['Label','Id']:
                    if 'I' in k: # numerical feature, example: I5
                        if len(str(v)) > 0: #check for empty values
                            numerical_features.append('{0}:{1}'.format(k,v))
                    if 'C' in k: # categorical feature, example: C2
                        if len(str(v)) > 0:
                            categorical_features.append('{0}.{1}'.format(k,v))


            if validation.readline().strip().split(',')[1] =='1':
                label=1
            else:
                label=-1

            outfile.write( '{0} \'{1} |numerical {2} |categorical {3}\n'.format(label,row['Id'],' '.join(['{0}'.format(val) for val in numerical_features]),' '.join(['{0}'.format(val) for val in categorical_features])) )



        if e % 1000 == 0:
            print('%s\t%s'%(e, str(datetime.now() - start)))
  print('\n Task execution time:\n\t%s'%(str(datetime.now() - start)))



csv_to_vw(path,train)

#csv_to_vw('/home/mars/test.csv', '/home/mars/test.vw',train=False)

#csv_to_vw('d:\\Downloads\\train\\train.csv', "c:\\click.train.vw",train=True)
#csv_to_vw("d:\\Downloads\\test\\test.csv", "d:\\click.test.vw",train=False)
