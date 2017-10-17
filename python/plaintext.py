#coding=utf-8
import io
from bs4 import BeautifulSoup


data =""

with open('10153423461669785.html', 'r') as myfile:
        html=myfile.readlines()

soup = BeautifulSoup(open('10153423461669785.html', 'r'), "lxml")
#soup = BeautifulSoup(html)
text = soup.get_text()

text_file = io.open("Output.txt", "w",  encoding='utf8')
text_file.write(text)
text_file.close()
