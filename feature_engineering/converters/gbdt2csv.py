#!/usr/bin/env python3
import argparse, csv, sys

from common import *

if len(sys.argv) == 1:
    sys.argv.append('-h')

from common import *

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--threshold', type=int, default=int(10))
parser.add_argument('csv_path', type=str)
parser.add_argument('gbdt_path', type=str)
parser.add_argument('additional',type=str)
args = vars(parser.parse_args())


#对每个特征值单独进行哈希，并输出哈希值



#出现频率超过10次的特征值集合
frequent_feats = read_freqent_feats(args['threshold'])


def gen_hashed_fm_feats(feats, nr_bins):
    feats = [(field, hashstr(feat, nr_bins)) for (field, feat) in feats]
    feats.sort()
    feats = ['{0}'.format(idx) for (field, idx) in feats]
    return feats


header=True
with open(args['additional'], 'w') as f :
    for row, line_gbdt in zip(csv.DictReader(open(args['csv_path'])), open(args['gbdt_path'])):
        feats = []
        for feat in gen_feats(row):
            field = feat.split('-')[0]
            type, field = field[0], int(field[1:])
            #type=I Or C ,Field=1~39
            if type == 'C' and feat not in frequent_feats:
                feat = feat.split('-')[0]+'-less'
            #生成特征如 C1less、C2less
            if type == 'C':
                field += 13
             #   if(feat.split('-')[0]=='C1' or feat.split('-')[0]=='C2' or feat.split('-')[0]=='C3'):
            feats.append((field, feat))



        for i, feat in enumerate(line_gbdt.strip().split()[1:], start=1):
            field = i + 39
            feats.append((field, str(i)+"-"+feat))

        if(header==True):
            f.write('Label,Id,'+','.join(['{0}'.format(feat.split('-')[0]) for (field,feat) in feats])+'\n')
            header=False

        #将结合的特征向量进行哈希
        f.write(row['Label'] + ','+row['Id'] + ','+','.join(['{0}'.format(feat.split('-')[1]) for (field,feat) in feats])+'\n')
