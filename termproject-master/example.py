from gensim.models import word2vec
import pprint
model = word2vec.Word2Vec.load("W2V.model")
print("입력 단어: 컴퓨터")
pprint.pprint(model.wv.most_similar(u"컴퓨터",topn=20))

