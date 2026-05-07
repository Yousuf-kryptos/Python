# # Inner Classes - is a class defined inside another class and it has access to methods and properties of outer class

# class Outer:
#     def __init__(self):
#         self.name = "Outer Class"

#     class Inner:
#         def __init__(self):
#             self.name = "Inner Class"
        
#         def display(self):
#             print("This is an inner class")

# outer = Outer()                                    # creating object for outer class
# inner = outer.Inner()                              # creating object for inner class
# print(outer.name)
# inner.display()                                    # Access inner class from outer

# class Outer:
#     def __init__(self):
#         self.name = "Yousuf"

#     class Inner:
#         def __init__(self,outer):
#             self.outer = outer
        
#         def display(self):
#             print(f"This is an inner class with other class name: {self.outer.name}")

# outer = Outer()
# inner = outer.Inner(outer)
# inner.display()

# class Car:
#     def __init__(self,model,brand):
#         self.model = model
#         self.brand = brand
#         self.engine = self.Engine()

#     class Engine:
#         def __init__(self):
#             self.status = "Off"

#         def start(self):
#             self.status = "Running"

#         def stop(self):
#             self.status = "Off"

#     def drive(self):
#         if self.engine.status == "Running":
#             print(f"Driving the {self.brand} {self.model}")
#         else:
#             print("Engine is Off!")

# c1 = Car("Ford","Mustang")
# c1.drive()
# c1.engine.start()
# c1.drive()

# class Computer:
#     def __init__(self):
#         self.cpu = self.Cpu()
#         self.ram = self.Ram()

#     class Cpu():
#         def process(self):
#             print("Processing the data")

#     class Ram():
#         def store(self):
#             print("Storing the data")

# c1 = Computer()
# c1.cpu.process()
# c1.ram.store()