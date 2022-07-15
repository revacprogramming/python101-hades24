def get_cs():
  string = print("enter the string \n")
  return string  

def cs_to_dict(cs):
  q=[]
  x=cs.split(";")
  for i in x:
        q.append(tuple(i.split("=")))
  d=dict(q)
  return d

def dict_to_cs(d):
  a=d.items()
  b=list(a)
  for i in b:
    z="=".join(i)
    print(z,end=";")
  
def main():
  cs = get_cs()
  d = cs_to_dict(cs)
  print(d)
  cs = dict_to_cs(d) 
  print(cs)

main()
 