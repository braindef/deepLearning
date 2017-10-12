#coding=utf-8

from __future__ import print_function

import sys
import argparse
import gensim

from gensim.models import word2vec

#print "========================================="



def parseArgs():
    parser = argparse.ArgumentParser(description='Sucht in einer word2vec binary nach ähnlichen wörtern, Beispiel: python suchen.py --bin forum.txt.bin --positive welt haus --negative schizo xeplion')
    parser.add_argument('--bin', action="store", dest="bin", help='angegben der word2vec bin datei')
    parser.add_argument('--positive', action="store", dest="positive", nargs='+', help='elemente nach denen gesucht wird')
    parser.add_argument('--negative', action="store", dest="negative", nargs='+', help='elemente die ausgeschlossen werden')
    args = parser.parse_args()
    if (args.bin is None):
        print("Es muss eine BIN Datei angegeben werden")
        exit(1)
    from gensim.models import word2vec
    model = word2vec.KeyedVectors.load_word2vec_format(args.bin, binary=True, unicode_errors='ignore')
    #model = gensim.models.Word2Vec.load(args.bin)
    print(args.bin)
    for key, value in model.most_similar(positive=args.positive, negative=args.negative):
        print( '%16s ' % key ,end='')
    print("")

parseArgs()
