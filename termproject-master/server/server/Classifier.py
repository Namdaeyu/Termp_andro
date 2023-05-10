# -*- coding: utf-8 -*-

import os
import tensorflow as tf
import Bi_LSTM as Bi_LSTM
import Word2Vec as Word2Vec
import gensim
import numpy as np
import math
import sys

def Convert2Vec(model_name, sentence):
    word_vec = []
    sub = []
    model = gensim.models.word2vec.Word2Vec.load(model_name)
    for word in sentence:
        if (word in model.wv.vocab):
            sub.append(model.wv[word])
        else:
            sub.append(np.random.uniform(-0.25, 0.25, 300))  # used for OOV words
    word_vec.append(sub)
    return word_vec

def Grade(sentence):
    tokens = W2V.tokenize(sentence)
    embedding = Convert2Vec('Data\\post.embedding', tokens)
    zero_pad = W2V.Zero_padding(embedding, Batch_size, Maxseq_length, Vector_size)
    global sess
    result = sess.run(prediction, feed_dict={X: zero_pad, seq_len: [len(tokens)]}) # tf.argmax(prediction, 1)이 여러 prediction 값중 max 값 1개만 가져옴
##    point = tf.argmax(prediction,1)
    point = result.ravel().tolist()
    percent = []
    Tag = ["IT과학", "경제", "정치", "e스포츠", "골프", "농구", "배구", "야구", "일반 스포츠", "축구", "사회", "생활문화"]
    Tagmodi = ["IT과학", "경제", "정치","e스포츠","스포츠","사회", "생활문화"]
    pointmodi = [point[0],point[1],point[2],point[3],(sum(point[4:10])),point[10],point[11]]
    for t, i in zip(Tagmodi, pointmodi):
##        print(t, round(i * 100, 2),"%")
##        print( t + str(round(i * 100, 2)) + "%")
        percent.append(round(i*100,2))
##    print('----------')
    return percent



W2V = Word2Vec.Word2Vec()

Batch_size = 1
Vector_size = 300
Maxseq_length = 500  # Max length of training data
learning_rate = 0.001
lstm_units = 128
num_class = 12
keep_prob = 1.0

X = tf.placeholder(tf.float32, shape = [None, Maxseq_length, Vector_size], name = 'X')
Y = tf.placeholder(tf.float32, shape = [None, num_class], name = 'Y')
seq_len = tf.placeholder(tf.int32, shape = [None])

BiLSTM = Bi_LSTM.Bi_LSTM(lstm_units, num_class, keep_prob)

with tf.variable_scope("loss", reuse = tf.AUTO_REUSE):
    logits = BiLSTM.logits(X, BiLSTM.W, BiLSTM.b, seq_len)
    loss, optimizer = BiLSTM.model_build(logits, Y, learning_rate)

prediction = tf.nn.softmax(logits)  # softmax

saver = tf.train.Saver()
init = tf.global_variables_initializer()
modelName = "Data\\Bi_LSTM.model"

sess = tf.Session()
sess.run(init)
saver.restore(sess, modelName)

sentence_percent=[]
line_percent=[]
all_error_line=[]
s =sys.argv[1]
string=""
##s=input("문장을 입력하세요:")
sentence_percent=Grade(s)
line_s = s.split(".")
line_s.pop()
for i in range(len(line_s)):
    error_line = []
    line_percent.append(Grade(line_s[i]))
    for j in range(len(sentence_percent)):
        if(abs(line_percent[i][j]-sentence_percent[j]) >= 30):
            error_line.append(1)
        else:
            error_line.append(0)
    if(sum(error_line)>=2):
        all_error_line.append(1)
    else:
        all_error_line.append(0)
for w in all_error_line:
    string += str(w)+','
print(string[:len(string)-1])
