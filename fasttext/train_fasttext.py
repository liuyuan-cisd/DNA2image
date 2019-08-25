# -*- coding: UTF-8 -*-

'''
该代码用来训练DNA序列的fasttext模型的词向量
该程序直接将所有语料读入内存，数据量不宜过大
作者：刘园
时间：2019.8.5
'''

from gensim.models import FastText
import argparse
import json
import logging
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
def train_fasttext(conf,seqs,out_name,n_gram):
    f=open(conf,'r')
    conf_dict=json.load(f)
    f.close()
    n_epoch=conf_dict['epoch']
    window=conf_dict['window']
    size=conf_dict['size']
    min_count=conf_dict['min_count']
    workers=conf_dict['workers']
    sg=conf_dict['sg']
    hs=conf_dict['hs']
    min_n=conf_dict['min_n']
    max_n=conf_dict['max_n']
    print("创建模型...")
    model=FastText(size=size,window=window,min_count=min_count,sg=sg,hs=hs,workers=workers,min_n=min_n,max_n=max_n)
    model.build_vocab(sentences=seqs)
    print("词汇表共包含_"+str(len(model.wv.vocab))+"_个单词")
    print("开始训练词向量")
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    model.train(sentences=seqs,total_examples=len(seqs),epochs=n_epoch)
    model.save( out_name+'_'+str(n_gram)+'n_'+str(n_epoch)+'e_fasttext_model')
    print("训练结束!!!!")
    print(model.similar_by_word('AACCCC'))


def getopts():
    #该函数用于获取必要的选项
    parse=argparse.ArgumentParser()
    parse.add_argument('-i','--input',type=str,help='DNA序列的文件路径',required=True)
    parse.add_argument('-o','--out_name',type=str,help='要输出的模型名',required=True)
    parse.add_argument('-conf','--configure',type=str,help='用于训练Fasttext的参数配置文件,为json格式',required=True)
    parse.add_argument('-n','--ngram',type=int,help='用于分割为一个单词的核苷酸数',required=True)
    args=parse.parse_args()
    return args
if __name__ == "__main__":
    args=getopts()
    n_gram=args.ngram
    input_dna=args.input
    out_name=args.out_name
    conf_path=args.configure

    list_ngrams=DNA2ngram(input_dna,n_gram)

    train_fasttext(conf_path,list_ngrams,out_name,n_gram)   