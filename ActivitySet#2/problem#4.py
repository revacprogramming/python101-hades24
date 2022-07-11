
def get_cs():
    string  = input("enter string \n")
  return string

def cs_to_lot(cs):
    q=[]
    x=cs.split(";")
    for i in x:
        q.append(tuple(i.split("=")))
    return q

def lot_to_cs(lot):
    """convert list of strings to connected string"""


def main():
    cs=get_cs()

    lot=cs_to_lot(cs)  # convert connect string to list of tuples
    print(lot)

    cs=lot_to_cs(lot)  # convert list of strings to connect string
    print(cs)


if __name__ == '__main__':
    main()
