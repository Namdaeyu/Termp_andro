#-*- coding: utf-8 -*- ::코드 내의 한글을 인식하기 위한 코드 
 
from gensim.models import word2vec
##학습된 Word2Vec의 model을 받아오기 위한 라이브러리 
 
import os
from konlpy.tag import Okt
##txt를 token화 시키기 위한 라이브러리 
 
from konlpy.utils import pprint
##유니코드인 한글을 한글로 출력하기 위한 라이브러리 
 
import codecs
##txt파일을 유니코드로 불러오기 위한 import 
 
import numpy as np
##list 사이의 계산을 위한 라이브러리 
 
import math 
 
class Neuron:
    w_distence = [] 
 
    def __init__(self):
        self.w_distence = np.zeros(300) 
 
    def learning(self, r_distence):
        alpha = 0.02
        error =(r_distence-self.w_distence)
        self.w_distence = self.w_distence + error * alpha

    def setDistence(self,i_distence):
        self.w_distence = i_distence

    def getDistence(self):
        return self.w_distence

okt = Okt()
WVmodel = word2vec.Word2Vec.load('W2V.model')

MyLearn = Neuron()

token=[]
temp=[]

TempVec = np.zeros(300)
#한 단어의 벡터값이 들어갈 변수
TempAb = np.zeros(300)
#한 단어의 절대값을 씌운 벡터값이 들어갈 변수 
NSum = np.zeros(300)
#한 문단의 모든 단어의 벡터의 합 
UpMid = np.zeros(300)
#한 문단의 모든 단어의 벡터의 가중평균 
distence = np.zeros(300)
#오류 문장과 현재 문단 가중 평균 사이의 거리 
LastSen1 = np.zeros(300)
LastSen2 = np.zeros(300)
#이전 문장을 저장해 두기 위한 변수

AwkSentence = []
#문단 내의 어색한 문장 list

SentenceCounter = 0 #문단 내의 문장 갯수를 count 하는 변수
WordCounter = 0 #문단내의 모든 단어의 갯수를 저장

cosSentenceVec = [] #각문장과 문단평균과의 cos값을 저장
num = 0.0

InputSentence = input("문단을 입력해주세요 : ")
VecSum = 0.0   
InputLine = InputSentence.split("다.")
InputLine.pop() #split 함수를 쓰면 리스트 끝에 공백 리스트가 하나 들어가서 pop해줌
for i in range(InputLine):
    InputLine[i] += "다."

temp = []
for line in InputLine:
    SentenceCounter += 1
    token = okt.pos(line, stem=True, norm=True) #형태소 토큰화
    for word in token:
        if word[1] in ["Noun"]: #명사일때만 추출
            if word[0] in WVmodel:
                temp.append(word[0])
                WordCounter += 1
            #단어가 word2vec 모델 안에 있으면 append
    del(token)
    if temp:    #temp에 아무것도 없으면 무시
        result.append(temp) 
    del(temp)
    # result에 문장을 형태소 단위로 쪼갠 값이 들어감.
    
SentenceSum = [0]*SentenceCounter
SentenceAverage = [0]*SentenceCounter
cosSentenceVec = [0]*SentenceCounter #각문장과 문단평균과의 cos값을 저장

k = 0
#얘는 무슨 용도야?

for i in range(0,SentenceCounter):
    SentenceSum[i] = np.zeros(300) #문장마다 평균값을 구하기위함
    SentenceAverage[i] = np.zeros(300) #문장마다 평균값을 저장
    
    AwkSentence[i] = np.zeros(300) #어색한 문장을 저장하기위한 list; 크기는 전체 문장의 수로 할당하였음
    
    for j in range(0,len(result[i])):
        #n_sum = np.zeros(300)#문단마다 초기화하기 위함
        WordCounter++ #단어를 찾을때 마다 count, 이것은 위의 초기화 과정에서도 가능
        
        for v in range(0,300):
            SentenceSum[i][v] += WVmodel[result[i][j]][v] #각 문장마다 벡터의 평균값을 구하기위해 각 문장의 벡터합을 구함
            
    for v in range(0,300):
        SentenceAverage[i][v] = SentenceSum[i][v] / len(result[i]) #문장의 벡터값을 구함
        
        NSum[v] += SentenceAverage[i][v] #문단 전체의 벡터합을 구함

for v in range(0,300): #NSum을 이용하여 문단전체의 평균값 UpMid를 구함
    UpMid[v] = NSum[v] / SentenceCounter
    
for i in range(0,SentenceCounter):
    cosVec = 0.0 #두 벡터간의 cos값 
    innerProd = 0.0 #두 벡터 간의 내적값
    
    for v in range(0,300): #현재의 문장과 평균값을 나타내는 UpMid와의 cos값을 구하기위한 식
        PreSentenceSum += pow(SentenceAverage[i][v]-UpMid[v], 2) 
        PreInnerProd += (SentenceAverage[i][v]*UpMid[v])
        
    cosSentenceVec[i] = PreInnerProd / sqrt(PreSentenceSum) #현재의 문장과 UpMidVec와의 cos값
    
    if( cosSentenceVec[i] < cos(math.pi/2.0): #기준값(90도를 기준)보다 cos값이 작은 문장들을 AwkSentence에 저장
        AwkSentence[k] = i
        k++

for i in range(0,len(AwkSentence)): #평균과의 cos값이 기준보다 작은 값을 가지는 문장을 출력
print(result[AwkSentence[i]])
    
    
    
    




