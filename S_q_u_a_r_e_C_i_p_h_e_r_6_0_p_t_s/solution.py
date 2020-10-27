from string import ascii_lowercase  # ascii_uppercase[0]='a'
from string import ascii_uppercase  # ascii_uppercase[0]='A'
from bs4 import BeautifulSoup
import requests
import bs4
from selenium import webdriver


import subprocess


def run(commands):
    subprocess.run([commands], shell=True)
    return


run('rm -rfv *.txt *.png;')

baseUrl = 'https://ksnctf.sweetduet.info/problem/22'
response = requests.get(baseUrl)
soup = bs4.BeautifulSoup(response.text, 'html.parser')

e_text = soup.find('div', {'class': 'well'}).find(
    'pre').find(text=True, recursive=False)

e_text = str(e_text)

letter2index = {}

for i in range(26):
    letter2index[ascii_lowercase[i]] = i
    e_text = e_text.replace(ascii_lowercase[i], str(1))
    e_text = e_text.replace(ascii_uppercase[i], str(0))


fw = open('qrCode.txt', 'a+')
fw.write(e_text)
fw.close()


fr = open('qrCode.txt', 'r')

lines = fr.readlines()
fw = open('bin.txt', 'a+')


for i in lines:
    j = list(i)
    s1 = ''
    for k in j:
        s1 += (k+' ')
    s1 = s1[0:len(s1)-1]
    fw.write(s1)
fw.close()


run('python3 bin2QR.py')


