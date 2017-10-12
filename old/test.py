#let's get Gensim. I am assuming you have successfully installed it

from gensim.models import word2vec
model = word2vec.KeyedVectors.load_word2vec_format('./de3E9.bin',binary=True)

print model.most_similar(positive=['koenig', 'frau'], negative=['mann'])
