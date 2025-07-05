# Initiate a class

class Employee:
    # special method/ magic method/ fdunder method - constructor
    def __init__(self):
        print("Starting executing attributes/data")
        self.id = 1
        self.salary = 50000
        self.designation = "Software developer"
        print("Atrribute/data has been initiated")

    # Method (Pr h ek function)
    def tavel(self, destination):
        print("This travel function was called manually")
        print(f"Employee is travelling to {destination}")

# Create an object/ instance of the class
sam = Employee()

# Printing the attributes
# print(sam.salary)

# Calling a method
# sam.tavel("Kerala")

print(type(sam))