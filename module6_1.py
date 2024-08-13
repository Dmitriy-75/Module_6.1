class Animal():
    alive = True
    fed = False


class Plant():
    edible = False


class Mammal(Animal):
    def __init__(self, name):
        self.name = name
    def eat(self,food):
        self.food = food
        if self.food.edible:
            print(f'{self.name} съел {food.name}')
            Mammal.fed = True

        else:
            print(f'{self.name}  не стал есть {food.name}')
            Mammal.alive = False


class Predator(Animal):
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        self.food = food
        if self.food.edible:
            print(f'{self.name} съел {self.food.name}')
            Predator.fed = True

        else:
            print(f'{self.name}  не стал есть {self.food.name}')
            Predator.alive = False

class Flower(Plant):
    def __init__(self, name):
        self.name = name

class Vegetables(Plant):
    def __init__(self, name):
        self.name = name


a1 = Predator('Волк с Ну погоди')
a2 = Mammal('Заинька серенький (типа с песни)')
p1 = Flower('Ромашка')
p2 = Vegetables('Морковка')
Vegetables.edible = True


print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)

a1.eat(p1)
a2.eat(p2)

print(a1.alive)
print(a2.fed)






