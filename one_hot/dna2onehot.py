'''
@Description: In User Settings Edit
@Author: your name
@Date: 2019-08-11 10:34:33
@LastEditTime: 2019-08-14 15:33:42
@LastEditors: Please set LastEditors
'''
''''将DNA转化为channel_last的图片'''
import pickle as pkl
import numpy as np
import argparse

acgt2num = {'A': 0,
            'C': 1,
            'G': 2,
            'T': 3}
def seq2mat(seq):
    seq = seq.upper()
    h = 4
    w = len(seq)
    mat = np.zeros((h, w), dtype=float)  # True or False in mat
    for i in range(w):
        if seq[i]=='N':
            continue
        mat[acgt2num[seq[i]], i] = 1.
    return mat
def one_hot_encode(sequence):
    seqs=open(sequence,'r')
    #count=1
    seq_list=[]
    for line in seqs:
    	if line.startswith('>'):
    		continue
    	else:
            seq_list.append(line)
    seq_=[]
    seqs.close()
    for line in seq_list:
        seq_.append(seq2mat(line.strip()).T)
    data=np.array(seq_)
    return data
def getopt():
    parse=argparse.ArgumentParser()
    parse.add_argument('-i','--input',type=str)
    parse.add_argument('-o','--output',type=str)
    args=parse.parse_args()
    return args    
if __name__=="__main__":
    args=getopt() 
    in_path=args.input
    out_path=args.output
    data=one_hot_encode(in_path)
    print(data.shape)
    np.save(out_path,data)