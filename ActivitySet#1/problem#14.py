# Using Web Services
# https://www.py4e.com/lessons/servces
import re
hand=open("actual.txt")
count=0
total=0
for line in hand:
    line=line.strip("") 
    num=re.findall('[0-9]+',line)
    try:
        for i in num:
            if int(i):
                print(i)
                total=total+int(i)
                count=count+1
    except:
        continue
print("TOTAL COUNT:- ",count)
print("SUM:- ",total)