class Dog():
    #Class object attribute
    taxClass = "mammal"
    def __init__(self,breed,name):
        self.breed=breed
        self.name=name

class Circle():
    pi = 3.141592
    def __init__(self,radius=1):
        self.radius=radius

    def area(self):
        return self.radius*self.radius*Circle.pi

    def set_radius(self,new_radius):
        self.radius = new_radius

my_dog=Dog(breed='Cocker Spaniel',name='Mila')
neighbor_dog=Dog(breed='French pitbull',name='Jagger')
print('dogs')
print(my_dog.name)
print(neighbor_dog.name)

myCircle=Circle(2)
print('circles')
print(myCircle.area())
myCircle.set_radius(10)
print(myCircle.area())
