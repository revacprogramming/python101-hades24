class Menu:
    def __init__(self):
        self.d={}

    def __setitem__(self, key, value):
        self.d[key]=value
        
    def __str__(self):
        return self.d.__str__()

m = Menu()
m["idly"] = 10
m["vada"] = 20

print(m)
#dd