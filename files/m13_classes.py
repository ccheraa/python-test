class My1:
  prop = 'mine 1'

a = My1()
print(a.prop)

class Animal:
  def __init__(self, legs = 0, name = 'N/A', species = 'N/A'):
    self.legs = legs
    self.name = name
    self.species = species
  def print(self):
    print('{} is a {} that has {} leg(s)'.format(self.name, self.species, self.legs))

a = Animal()
a.print()
a = Animal(name='dog', species='mammal', legs=4)
a.print()

class Cat(Animal):
  def __init__(self, color='N/A', species='cat'):
    super().__init__(name='cat', legs=4, species=species)
    self.color = color
  def print(self):
    super().print()
    print(' - its color is', self.color)

a = Cat()
a.print()
a = Cat(species='sphynx', color='white')
a.print()