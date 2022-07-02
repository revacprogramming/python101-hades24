a=[]
while True:
    try:
        num=input("Enter a number: ")
        if num == 'done':
            break;
        n = int(num)
        a.append(n)
        largest=max(a)
        smallest=min(a)
    except:
        print ("Invalid input")
 
print ("Maximum number is ", largest)
print ("Minimum number is ", smallest)