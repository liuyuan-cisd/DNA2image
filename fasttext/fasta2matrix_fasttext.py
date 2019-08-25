'''
@Description: 用来把fasta转化为词向量的张量，得到的结果可用于1D卷积神经网络。
@Author: your name
@Date: 2019-08-06 10:15:38
@LastEditTime: 2019-08-06 14:15:05
@LastEditors: Please set LastEditors
'''

from gensim.models import FastText
import argparse
import numpy as np
import pandas as pd 
def DNA2ngram(dna_file,k):
    '''
    @description: 用于将DNA序列分割成ngram
    @param {type} 
    @return: 
    '''
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

#channel_first得到一个（1，）
def dna2matrix(seqs,model_path,out_name):
    feature=[]
    model=FastText.load(model_path)
    for line in seqs:
        one_line_feature=[]
        for word in line:
            one_line_feature.append(model.wv[word])
        one_line_feature=np.array(one_line_feature)
        feature.append(one_line_feature)
    feature=np.array(feature)
    print(feature[0].shape)   
    np.save(out_name,feature)

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
    dna2matrix(seqs,args.model,args.out_name)
    
