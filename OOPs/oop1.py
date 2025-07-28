# Initiate a class

class Employee:
    # special method/ magic method/ fdunder method - constructor
    def __init__(self):
        print(id(self))     #1800493997936 > Address of self in the ram
        # print("Starting executing attributes/data")
        self.id = 1
        self.salary = 50000
        self.designation = "Software developer"
        # print("Atrribute/data has been initiated")

    # Method (Pr h ek function)
    # def travel(self, destination):
    #     print("This travel function was called manually")
    #     print(f"Employee is travelling to {destination}")

    def travel(self):
        print("This travel function was called manually")
        print(f"Employee is travelling to Jodhpur")

# Create an object/ instance of the class
# sam = Employee()
# print(id(sam))    #1800493997936 > Address of self and sam is same in the ram

# Printing the attributes
# print(sam.salary)

# Calling a method
# sam.tavel("Kerala")
# sam.travel()

# print(type(sam))


# Create an object/instance of the class
sam = Employee()
print(id(sam))

shaktiman = Employee()
print(id(shaktiman))