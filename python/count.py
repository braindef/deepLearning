# -*- coding: utf-8 -*-

import sys


def split_line(text):
    dictionary = {}
    # for each word in the line:
    words = text.replace('\t',' ').replace('\r', ' ').replace('\n', ' ').replace('  ',' ').replace('  ',' ').split(' ')
    #print words
    for word in words:
	if word in dictionary:
		#print("Doppelt")
		dictionary[word] += 1
	else:
		dictionary[word] = 1
    return dictionary

def print_count(dictionary):
	for k, v in dictionary.iteritems():
		print v, k

def print_sorted_count(dictionary):
	from collections import OrderedDict
	d_sorted_by_value = OrderedDict(sorted(dictionary.items(), key=lambda x: x[1], reverse=True))
        
	for k, v in d_sorted_by_value.items():
		print "\"%s\" (%s)" % (k, v)

text=''
for line in sys.stdin:
    text += line
#print text
#print split_line(text)
#print(dictionary)
#print_count(dictionary)
print_sorted_count(split_line(text))
