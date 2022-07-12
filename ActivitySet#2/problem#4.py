
def get_cs():
    string  = input("enter string \n")
    return string

def cs_to_lot(cs):
    q=[]
    x=cs.split(";")
    for i in x:
        q.append(tuple(i.split("=")))
    return q

def lot_to_cs(cs_to_lot):
    for i in cs_to_lot:
      a = "=".join(i)
      print(a, end=";")

def main():
    cs=get_cs()

    lot=cs_to_lot(cs)
    print(lot)

    lot_to_cs(lot)
    print(cs)
   

if __name__ == '__main__':
    main()
 