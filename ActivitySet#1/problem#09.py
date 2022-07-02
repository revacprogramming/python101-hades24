def filedata(text):
    fhand=open(text)
    output=(fhand.split(""))
    return output

text='romeo.txt'
a=filedata(text)
print(a) 