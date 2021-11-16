class Point:
    def __init__(self,x,y):#this function gets called when we create a new object
      self.x=x
      self.y=y
     
    def move(self):
        print("move")
        
    def draw(self):
        print("draw")
        

#point1=Point()    #an object is an instance of a class
#point1.x=10
#point1.y=20
#print(point1.x)
#point1.draw()    
#point2=Point()
#point2.x=1
#print(point2.x) 



point=Point(10, 20)

print(point.x) #o/p=10

class Person:
    def __init__(self,name):
        self.name=name
    
    def talk(self):
        print(f'Hi, I am {self.name}')
        
add=Person("Anmol")
print(add.name)
add.talk()
