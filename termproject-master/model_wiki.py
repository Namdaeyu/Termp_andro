#_*_coding: utf-8 _*_
#한글 코드 실행시키기 위한 코드

from gensim.models import word2vec
import os
import codecs
from konlpy.tag import Okt
from konlpy.utils import pprint

okt = Okt()
#Okt클래스 선언
DirName = os.listdir('dataset')
#dataset폴더에 있는 파일 제목을 읽어옴

result = []
token = []
temp = [] 
count = 1
print("Now loading....")
for FileName in DirName:
    token = []
    AbsFileName = os.path.join(os.path.abspath('dataset'),FileName)
    #dataset폴더에 있는 파일을 순서대로 절대경로로 변환하여 저장한다.
    with codecs.open(AbsFileName,'r','utf-8-sig')as f:
        text = f.readlines()
    #읽어온 파일을 제목 단위로 나눈다.
    for line in text:
        if(line == ''):
            continue
        else:
            temp = []
            token = okt.pos(line, stem=True, norm=True) #형태소 토큰화
            for word in token:
                if word[1] in ["Noun"]: #명사일때만 추출
                    temp.append(word[0])
            del(token)
        if temp:    #temp에 아무것도 없으면 무시
            result.append(temp)
        del(temp)
    print(count)    #file하나를 마무리 할때마다 count를 출력해 현재 상황 확인
    count+=1
    f.close()
    
print("Now start Word2Vec....")
WordModel=word2vec.Word2Vec(result, sg=1, size=300,workers= 4,alpha=0.1,
                            min_alpha=0.02,min_count=5,window=5,iter= 10)

##sg:1일 경우 skip gram 모델 제작, 0일경우 CBOW 모델 제작
##size: 제작하는 벡터의 차원
##worker: 제작하는데 사용 할 병렬 처리 쓰레드 수
##alpha : 초기 학습률, 학습이 진행됨에 따라 min_alpha값까지 선형 감소
##min_alpha: 최종 학습률
##min_count: min_count 보다 단어의 출현빈도가 작을 경우 word2vec에 포함하지 않는다.
##window: 학습할 때 사용할 주변 단어 수
##iter : 학습 반복 횟수

print("Loading Success")

WordModel.save("W2V.model")
##모델링 완성된것을 W2V.model파일로 저장
