#!/usr/bin/env python3

import argparse, sys

from common import *

def parse_args():

    if len(sys.argv) == 1:
        sys.argv.append('-h')

    parser = argparse.ArgumentParser()
    parser.add_argument('-s', dest='nr_thread', default=12, type=int)
    parser.add_argument('src1_path')
    parser.add_argument('src2_path')
    parser.add_argument('dst_path')
    args = vars(parser.parse_args())

    return args

def main():

    args = parse_args()

    nr_thread = args['nr_thread']

    #scr1原始特征
    split(args['src1_path'], nr_thread, True)
    #src2为gbdt特征
    split(args['src2_path'], nr_thread, False)



    parallel_convert('feature_engineering/converters/gbdt2csv.py', [args['src1_path'], args['src2_path'], args['dst_path']], nr_thread)
    cat_with_header(args['dst_path'],nr_thread)
    #线程大于2时，默认的cat会吧csv的头连接过去！！已修复为考虑到header的连接


    delete(args['src1_path'], nr_thread)

    delete(args['src2_path'], nr_thread)

    delete(args['dst_path'], nr_thread)


main()
