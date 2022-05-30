def number(a):
    try:
        fhand=open(a)
    except:
        print("no such file found")
    count=""
    for line in fhand:
        if line.isdigit():
            count = count + 1
        print(count, line)
        
a=number(input("enter text file name \n"))
