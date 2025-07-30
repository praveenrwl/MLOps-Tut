# ADVANCE INHERITANCE

# SINGLE INHERITANCE

# Base Class
# class Parent:
#     def __init__(self, name):
#         self.name = name

#     def greet(self):
#         print(f"Hello, my name is {self.name}")

# # Derived Class
# class Child(Parent):
#     def play(self):
#         print(f"{self.name} is playing")


# # Create an instance of child
# child = Child('Alice')
# child.greet()  # Output: Hello, my name is Alice
# child.play()   # Output: Alice is playing


# --------------------------------------------------------------------

# MULTILEVEL INHERITANCE

# class GrandParent:
#     def __init__(self, name):
#         self.name = name

#     def tell_story(self):
#         print(f'{self.name} tells a story.')

# class Parent(GrandParent):
#     def work(self):
#         print(f'{self.name} is working.')

# # Derived Class
# class Child(Parent):

#     def play(self):
#         print(f'{self.name} is playing')


# # Create an instance of child
# child = Child('Ace') 
# child.tell_story() # Output: Alice tells a story.
# child.work()      # Output: Alice is working.
# child.play()      # Output: Alice is playing


# --------------------------------------------------------------------

# HEIRARCHICAL INHERITANCE

# class Parent:
#     def __init__(self, name):
#         self.name = name

#     def greet(self):
#         print(f"Hello, my name is {self.name}")

# # Derived 1
# class Child1(Parent):
#     def play(self):
#         print(f"{self.name} is playing")


# # Derived 2
# class Child2(Parent):
#     def study(self):
#         print(f"{self.name} is studying")

# # Create an instance of child1
# child1 = Child1('Ace')
# child2 = Child2('Bob')

# child1.greet() # Output: Hello, my name is Ace
# child1.play() # Output: Ace is playing

# child2.greet() # Output: Hello, my name is Bob
# child2.study() # Output: Bob is studying


# --------------------------------------------------------------------

# MULTIPLE INHERITANCE (DAIMOND INHERITANCE)

# Common Base Class
# class A:
#     def __init__(self, name):
#         self.name = name

#     def greet(self):
#         print(f"Hello, my name is {self.name} from A")


# # Intermediate Class 1
# class B(A):
#     def greet(self):
#         print(f"Hello, my name is {self.name} from B")
#         super().greet()

# # Intermediate Class 2
# class C(A):
#     def greet(self):
#         print(f"Hello, my name is {self.name} from C")
#         super().greet()

# # Derived Class
# class D(B, C):
#     def greet(self):
#         print(f"Hello, my name is {self.name} from D")
#         super().greet()

# # Create an instance of D
# d = D('Ace')
# d.greet() # Output: Hello, my name is Ace from D
# Output: Hello, my name is Ace from B
# Output: Hello, my name is Ace from A
# Output: Hello, my name is Ace from C

# --------------------------------------------------------------------

# Hybrid Inheritance

# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes a sound.")

# Intermediate class 1 (Hierarchical)
class Mammal(Animal):
    def feed(self):
        print(f"{self.name} is feeding milk.")

# Intermediate class 2 (Multiple)
class Bird(Animal):
    def fly(self):
        print(f"{self.name} is flying.")

# Derived class (Multiple Inheritance)
class Bat(Mammal, Bird):
    def __init__(self, name):
        Mammal.__init__(self, name)  # Explicitly calling the constructor

    def nocturnal(self):
        print(f"{self.name} is nocturnal.")

# Create an instance of Bat
bat = Bat("Bruce")
bat.sound()     # Output: Bruce makes a sound.
bat.feed()      # Output: Bruce is feeding milk.
bat.fly()       # Output: Bruce is flying.
bat.nocturnal() # Output: Bruce is nocturnal.