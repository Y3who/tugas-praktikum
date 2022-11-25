import string
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re

alfabet = {" ": "*"}

for v in range(len(string.ascii_lowercase)):
    alfabet[string.ascii_lowercase[v]] = v+1

for q in range(len(string.ascii_lowercase)):
    alfabet[str(q)] = string.ascii_lowercase[q]

encrypted = ""

file = open("2729-8439-2-PB.txt", "r")

for line in file:
    for alfa in line:
        if alfa in alfabet.keys():
            alfa = alfa.lower()
            encrypted += str(alfabet[alfa])
            encrypted += " "

file.close()

print(encrypted)