# # SIMPLE HERITANCE

# # Base Class
# class Animal:
#     # Constructor
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         print(f"{self.name} makes a sound.")


#     # Non-Private Methods and Non -Private Attributes > Encapsulation
#     # def __init__(self, name):
#     #     self.__name = name

#     # def speak1(self):
#     #     print(f"{self.__name} makes a sound.")

# # Derived class
# class Dog(Animal):
#     # def __init__(self):
#     #     self.behaviour = 'Freindly'

#     # def speak(self):
#     #     print(f"Buddy barks. He is very {self.behaviour}")
   
#    # Constructor Overriding
#     def speak(self):
#         print(f"{self.name} barks")

#     # Constructor Overloading


# # Create an instance of Animal
# # animal = Animal("Rex")
# # animal.speak()  # Output: Rex makes a sound.

# # Create an instance of Dog
# # dog = Dog()
# # dog.speak()  # Output: Buddy barks.

# dog = Dog("Buddy")
# dog.speak()  # Output: Buddy barks.



# Super KeyWord: 
#   > Used to call the method of the parent class from the child class.
#   > 

class Animal:
    def __init__(self):
        self.name = 'Buddy'

    def speak(self):
        print(f"{self.name} makes a sound.")

# Derived Class
class Dog(Animal):
    def __init__(self, breed):
        super().__init__()
        self.breed = breed

    def speak(self):
        super().speak()     # Call the base class method
        print(f"{self.name} barks. It is a {self.breed}")

# Create a instance of Dog
dog = Dog("Golden Retriever")
dog.speak()  

# Output: Buddy makes a sound. Buddy barks. 
# It is a Golden Retriever.