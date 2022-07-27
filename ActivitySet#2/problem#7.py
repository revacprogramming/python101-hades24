class Menu:
    def _init_(self,x='',y=''):
        self.x=x
        self.y=y
    def _add_(self,other):
        return self.x + other.x ,self.y + other.y

#==============METHOD 1==========
a= Menu("idly ", 'vada ')
b= Menu("10", '20')
c=a+b
for i in c:
    print(i)
#==============METHOD 2==========
m = Menu("idly ", 'vada ') + Menu("10", '20')
print(m)
#123
