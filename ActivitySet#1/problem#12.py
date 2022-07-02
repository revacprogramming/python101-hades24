# Regular Expressions
# https://www.py4e.com/lessons/regex
import re

a=open("esting.txt")
b=[]
sum=0
for i in a:
    c=re.findall('[0-9]+',i)
    b+=c

for j in b:
    sum+=int(j)
print(sum)  