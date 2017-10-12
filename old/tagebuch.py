#let's get Gensim. I am assuming you have successfully installed it

import sys
import pprint

from gensim.models import word2vec
#model = word2vec.KeyedVectors.load_word2vec_format('./forum4.txt.bin',binary=True)
#model = word2vec.KeyedVectors.load_word2vec_format('./forum4.txt.bin', binary=True, encoding='utf-8', unicode_errors='ignore')
model = word2vec.KeyedVectors.load_word2vec_format('./tagebuch.txt.bin', binary=True, unicode_errors='ignore')

#print model.most_similar(positive=[sys.argv[1], sys.argv[2], sys.argv[3]], negative=[sys.argv[4], sys.argv[5], sys.argv[6]])
#print model.most_similar(positive=[sys.argv[1], sys.argv[2]])

print "========================================="
print "Suche: " + sys.argv[1] + " " + sys.argv[2] +" "+ sys.argv[3]
print "-----------------------------------------"
print "ausschliessen: " + sys.argv[4] + " " + sys.argv[5] + " " + sys.argv[6]
print "-----------------------------------------"

pp = pprint.PrettyPrinter(indent=4)
for key, value in  model.most_similar(positive=[sys.argv[1], sys.argv[2], sys.argv[3]], negative=[sys.argv[4], sys.argv[5], sys.argv[6]]):
    print key

print "========================================="
