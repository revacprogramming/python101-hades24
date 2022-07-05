def input_function(n):
    q=[]
    x=n.split(";")
    for i in x:
        a=q.append(tuple(i.split("=")))
    return(q)
def main():
    n="system=s;database=d;username=u;password=p"
    b=input_function(n)
    print(b)

main()