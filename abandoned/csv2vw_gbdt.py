# -*- coding: UTF-8 -*-

########################################################
# __Author__: Triskelion <info@mlwave.com>             #
# Kaggle competition "Display Advertising Challenge":  #
# http://www.kaggle.com/c/criteo-display-ad-challenge/ #
# Credit: Zygmunt Zając <zygmunt@fastml.com>           #
########################################################

from datetime import datetime
from csv import DictReader
import sys

if len(sys.argv) != 3:
    print('wrong arg')
    exit(1)

csv_path,vw_path=sys.argv[1:]


def csv_to_vw(loc_csv, loc_output):
  """
  Munges a CSV file (loc_csv) to a VW file (loc_output). Set "train"
  to False when munging a test set.
  TODO: Too slow for a daily cron job. Try optimize, Pandas or Go.
  """
  start = datetime.now()
 # print('\nTurning %s into %s. Is_train_set? %s'%(loc_csv,loc_output))
  
  with open(loc_output,'w') as outfile:
    for e, row in enumerate( DictReader(open(loc_csv)) ):
	
	    #Creating the features
        categorical_features = []
        for k,v in row.items():
            if v=='': continue
            if k not in ['Label','Id']:
                if len(str(v)) > 0 :
                    categorical_features.append('{0}.{1}'.format(k,v)) #这里连‘-’导致测试不通过，很奇怪，无视之

	  #Creating the labels
    #  if train: #we care about labels
        if row['Label']=='1':
            label = 1
        else:
            label = -1 #we set negative label to -1

        outfile.write('{0} \'{1} |features {2}\n'.format (label,row['Id'],' '.join(['{0}'.format(val) for val in categorical_features])))

            #   else: #we dont care about labels
         #   outfile.write('1 \'{0} |features {1}\n'.format (row['Id'],' '.join(['{0}'.format(val) for val in categorical_features])))
      
	     #Reporting progress
        if e % 10000 == 0:
             print('%s\t%s'%(e, str(datetime.now() - start)))

    print('\n %s Task execution time:\n\t%s'%(e, str(datetime.now() - start)))



csv_to_vw(csv_path, vw_path)


#csv_to_vw("/home/mars/test.csv", "/home/mars/test.vw",train=False)

#csv_to_vw("d:\\Downloads\\train\\train.csv", "c:\\click.train.vw",train=True)
#csv_to_vw("d:\\Downloads\\test\\test.csv", "d:\\click.test.vw",train=False)
