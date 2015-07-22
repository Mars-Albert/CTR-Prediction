#!/usr/bin/env python3

import argparse, sys
from common import *

def parse_args():

    if len(sys.argv) == 1:
        sys.argv.append('-h')

    parser = argparse.ArgumentParser()
    parser.add_argument('-s', dest='nr_thread', default=12, type=int)
    parser.add_argument('src_path')
    parser.add_argument('dst_path')
    args = vars(parser.parse_args())

    return args

def main():

    args = parse_args()

    nr_thread = args['nr_thread']

    #scr1原始特征
    split(args['src_path'], nr_thread, True)

#    cmd='python feature_engineering/converters/gbdt2csv.py {0} {1} {2}'.format(args['src1_path'],args['src2_path'],args['addition'])
#    subprocess.call(cmd, shell=True, stdout=subprocess.PIPE)

    parallel_convert('feature_engineering/converters/normalized2ffm.py', [args['src_path'],  args['dst_path']], nr_thread)
    cat(args['dst_path'],nr_thread)
    #线程大于2时，会吧csv的头连接过去！！有错误


    delete(args['src_path'], nr_thread)

    delete(args['dst_path'], nr_thread)

main()