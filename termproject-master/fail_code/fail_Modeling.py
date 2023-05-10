#_*_coding: utf-8 _*_
#한글 코드 실행시키기 위한 코드

from gensim.models import word2vec
import os
import codecs
from konlpy.tag import Okt
from konlpy.utils import pprint

okt = Okt()
#Twitter클래스 선언
DirName = os.listdir('text3')
#text3폴더에 있는 모든 파일 제목을 읽어옴

AllToken =[] #전체 문단
token = []#문단(한 파일의 모든 텍스트내용)
temp = [] #한글 토큰
line= []#문장   

print("Now loading....")
for FileName in DirName:
    token = []
    AbsFileName = os.path.join(os.path.abspath('text3'),FileName)
    #text3파일에 있는 파일을 순서대로 절대경로로 변환하여 저장한다.
    with codecs.open(AbsFileName,'r','utf-8-sig')as f:
        text = f.read()
    #읽어온 파일의 모든 문장을 다 가져온다.
    if len(text) < 100:
        f.close()
        #만약 텍스트 전체 글자수가 100자를 못넘어가면 데이터로 쓸 가치가 없다고 판단
    else:
        temp = []
        SplitText = text.split('.')
        #.을 기준으로 문장이므로 문단을 문장으로 split한다.
        for i in range(0,len(SplitText)):
            temp.append(okt.pos(SplitText[i]))
        #형태소 단위로 나누어서 temp에 저장
        del(SplitText)
        for ko1 in range(0,len(temp)):
            for ko2 in range(0,len(temp[ko1])):
                line.append(temp[ko1][ko2][0])
                #형태소 단위로 나누었던 문장을 다시 병합한다.
            token.append(list(line))
            #모은 문장들로 문단을 만든다.
            line = []
        f.close()
    AllToken.append(token)
#[[문[문장]단],[문[문장]단]...]이런 형식으로 결과가 나옴 즉 3차원 배열
print("Now start Word2Vec....")
WordModel=word2vec.Word2Vec(token, sg=1, size=300,workers= 4,alpha=0.1,
                            min_alpha=0.02,min_count=3,batch_words=10000,window=5)

##sg:1일 경우 skip gram 모델 제작
##size: 제작하는 벡터의 차원
##worker: 제작하는데 사용 할 병렬 처리 쓰레드 수
##alpha : 첫 훈련 rate
##min_alpha: 최소 alpha값
##min_count: min_count 보다 단어의 출현빈도가 작을 경우 word2vec에 포함하지 않는다.
##batch_words: 한 번에 처리할 단어 수
##window: 컨텍스트 윈도우의 크기

print("Loading Success")

WordModel.save("W2V.model")
##모델링 완성된것을 W2V.model파일로 저장
