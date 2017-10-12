#coding=utf-8


import sys
import os

from gensim.models import word2vec
from gensim import corpora, models, similarities

#print "========================================="


class MySentences(object):
    def __init__(self, dirname):
        self.dirname = dirname
 
    def __iter__(self):
        for fname in os.listdir(self.dirname):
            for line in open(os.path.join(self.dirname, fname)):
                yield line.split()
 
sentences = MySentences('.') # a memory-friendly iterator
model = word2vec.Word2Vec(sentences)

#sentences = word2vec.Text8Corpus("forum.txt")
#model = word2vec.Word2Vec(sentences)

#model = Word2Vec(text, size=100, window=5, min_count=2, workers=4)
#model.build_vocab(text)
model.save('mdlObj')


