'''
@Description: In User Settings Edit
@Author: your name
@Date: 2019-08-25 18:07:24
@LastEditTime: 2019-08-25 19:03:25
@LastEditors: Please set LastEditors
'''
# -*- coding: UTF-8 -*-

from gensim.models import Word2Vec
import argparse
import numpy as np
import pandas as pd 
def DNA2ngram(dna_file,k):
    f=open(dna_file,'r')
    lines=f.readlines()
    f.close()
    print("运行DNA2ngram...")
    list_ngrams=[]
    for line in lines:
        if line.startswith('>'):
            continue
        else:
            line=line.strip().upper()
            l=len(line)
            list_ngram=[]
            for i in range (0,l-k+1):
                list_ngram.append(line[i:i+k])
            list_ngrams.append(list_ngram)
    return list_ngrams
def get_mean_feature(seqs,model_path,out_name):
    feature=[]
    model=Word2Vec.load(model_path)
    for line in seqs:
        one_line_feature=[]
        for word in line:
            one_line_feature.append(model.wv[word])
        one_line_feature=np.array(one_line_feature)
        feature.append(np.mean(one_line_feature,axis=0))
    pd.DataFrame(feature).to_csv(out_name,header=None,index=False)

def getopts():
    #该函数用于获取必要的选项
    parse=argparse.ArgumentParser()
    parse.add_argument('-i','--input',type=str,help='DNA序列的文件路径',required=True)
    parse.add_argument('-m','--model',type=str,help='fasttext模型的路径',required=True)
    parse.add_argument('-o','--out_name',type=str,help='要输出的模型名',required=True)
    parse.add_argument('-n','--ngram',type=int,help='用于分割为一个单词的核苷酸数',required=True)
    args=parse.parse_args()
    return args
if __name__ == "__main__":
    args=getopts()
    seqs=DNA2ngram(args.input,args.ngram)
    get_mean_feature(seqs,args.model,args.out_name)
    
