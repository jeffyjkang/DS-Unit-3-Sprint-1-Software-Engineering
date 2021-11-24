# Object Oriented Programming Examples

import pandas as pd

df = pd.DataFrame(['tree frog', 'white rhino', 'zebra'])

class MyDataFrame(pd.DataFrame):
    def num_cells(self):
        return self.shape[0] * self.shape[1]

cDf = MyDataFrame(df)
print(cDf.num_cells())

class BareMinimumClass:
    pass

class Complex:
    def __init__(self, real_part, imag_part):
        # constructor for complex numbers
        # complex numbers have a real part and imaginary part
        self.r = real_part
        self.i = imag_part

    def add(self, other_complex):
        self.r += other_complex.r
        self.i += other_complex.i

    def __repr__(self):
        return "{}, {}".format(self.r, self.i)

class SocialMediaUser:
    def __init__(self, name, location, upvotes=0):
        self.name = str(name)
        self.location = location
        self.upvotes = int(upvotes)

    def receive_upvotes(self, num_upvotes=1):
        self.upvotes += num_upvotes

    def is_popular(self):
        return self.upvotes > 100

class Animal:
    # general rep of animals
    def __init__(self, name, weight, diet_type):
        self.name = str(name)
        self.weight = float(weight)
        self.diet_type = diet_type

    def run(self):
        return 'Vroom, Vroom, I go quick'

    def eat(self, food):
        return 'Huge fan of that' + food

class Sloth(Animal):
    def __init__(self, name, weight, diet_type, num_naps=104):
        super().__init__(name, weight, diet_type)
        self.num_maps = float(num_naps)

    def run(self):
        return 'I am a slow guy'
    def eat(self):
        return 'I like leaves'
    def say_something(self):
        return 'This is a sloth typing'

# only gets run if file is run, not on imports
if __name__ == '__main__':
    num1 = Complex(3, -5)
    num2 = Complex(2, 6)

    num1.add(num2)
    print('num1.r: {}, num1.i: {}'.format(num1.r, num1.i))

    user1 = SocialMediaUser('John', 'LA', 500)
    user2 = SocialMediaUser('Carl', 'Mississippi')
    user3 = SocialMediaUser('George', 'Djibouti', 4000)
    user4 = SocialMediaUser('Carlos', 'Argentina', 5)
    print(user1.is_popular())
    print(user2.is_popular())
    user2.receive_upvotes(101)
    print('received {} upvotes'.format(user2.upvotes))
    print(user2.is_popular())
