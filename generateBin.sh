#!/bin/bash

time word2vec -train $1 -output $1.bin -min-count 2 -skipgram 10 -size 200 -window 5 -negative 0 -hs 1 -sample 1e-3 -threads 16 -binary 1 -save-vocab defull-vocab.txt 
