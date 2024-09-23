class Animal:
    alive = True
    # fed = False  #теперь у каждого животного своя степень сытости

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self

    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False


class Plant:
    edible = False

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self


class Mammal(Animal):
    fed = False


class Predator(Animal):
    fed = False


class Flower(Plant):
    edible = False


class Fruit(Plant):
    edible = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)