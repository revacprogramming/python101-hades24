def Files(text):
    try:
        fhand=open(text)
    except:
        print("NO FILE FOUND")
    num=""
    for line in fhand:
        line=line.rstrip()
        if line.startswith("X-DSPAM-Confidence:"):
            num=num+1
            print(num,line)

text = input("enter the text file : \n")
a=Files(text)