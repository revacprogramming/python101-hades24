def grades(a):
    if a>0.9:
        return 1
    elif a>0.8 and a<=0.9:
        return 2
    elif a>0.7 and a<=0.8:
        return 3
    elif a>0.6 and a<=0.7:
        return 4
    elif a<0.6:
        return 5
a=float(input("enter the score : "))
b=grades(a)
if b==1:
    print("A")
elif b==2:
    print("B")
elif b==3:
    print("C")
elif b==4:
    print("D")
else:
    print("F")