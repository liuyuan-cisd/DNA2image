# DNA2image
该文件夹下包含了三种将DNA序列转换成多通道1维图片的程序，生成的数据格式为channel_last,
可以直接用于tensorflow中的conv1D，或者以tensoflow为基的keras中的Conv1d.
## word2vec
  word2vec文件夹中共有三个程序
  首先使用train_word2vec.py进行词向量的训练
  用法：
      python train_word2vec.py -i 输入fasta -o 输出模型名 -conf 配置文件 -n ngram
      
      配置文件解读：
        {
            "size":100,     生成词向量的维度
            "epoch":10,     迭代的次数
            "window":6,     滑动窗口的大小
            "min_count":1,  词最小出现的次数，数据集小的时候推荐设置为1
            "workers":5,    启用的线程数
            "sg":1,         用于设置训练算法，默认为0，对应CBOW算法；sg=1则采用skip-gram算法。
            "hs":1          如果为1则会采用hierarchica·softmax技巧。如果设置为0（defaut），则negative sampling会被使用。
          }
      
   训练好模型以后就可以提取特征了
   提取用于卷积神经网络的特征使用fasta2matrix_w2v.py
   
    用法:python fasta2matrix_w2v.py -i 输入的fasta文件 -o 输出的文件名（输出格式为npy） -m 上一步训练得到的模型 -n ngram
   
   提取用于全连接神经网络或者svm使用的一维特征使用 get_mean_feature_w2v.py 
   
    用法：python get_mean_feature_w2v.py -i 输入的fasta文件 -o 输出的文件名（输出格式为npy） -m 上一步训练得到的模型 -n ngram
    
## fasttext 
   参照word2vec使用
   
## one hot 
  
  将DNA序列转换为（seq_len,4)的矩阵，同样可以用于卷积
    
     用法： python dna2onehot.py -i 输入的fasta -o 输出
