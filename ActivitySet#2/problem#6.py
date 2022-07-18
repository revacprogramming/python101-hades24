class Menu:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

x = Menu("idly", 10)
y = Menu("vada", 20)

print(x.name, ":", x.quantity)
print(y.name, ":", y.quantity)