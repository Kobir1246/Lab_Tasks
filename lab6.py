class student: 
    def __init__(self, name, id, cgpa):
        self.name = name
        self.id = id
        self.cgpa = cgpa
    def calculate_cgpa(self):
        print(self.cgpa)
    def do_assignment(self):
        print("assignment anything")
    
s1 = student("sabbir", 1, 3.00)
print(s1.name)
s1.calculate_cgpa()
s1.do_assignment()


class shape:
    def __init__(self, name):
        self.name = name
    def get_name(self):
        return self.name


class Rectangle(shape):
    def __init__(self,name, length, width):
        super().__init__(name)
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2*(self.length + self.width)
    
s = Rectangle("sabbir",20, 15)

a = s.area()
b = s.perimeter()
print(s.get_name())


print(a)
print(b)

class Shape:
    def __init__(self, name):
        self._name = name
        
    def get_name(self):
        return self._name
    
    def __display_shape_type(self):
        print(f"This is a shape of type: {self._name}")
    
    def display_shape_info(self):
        self.__display_shape_type()

class Rectangle(Shape):
    def __init__(self, name, length, width):
        super().__init__(name)
        self.__length = length
        self.__width = width
    
    # Public getter methods
    def get_length(self):
        return self.__length
    
    def get_width(self):
        return self.__width
    
    # Methods for area and perimeter
    def area(self):
        return self.get_length() * self.get_width()
    
    def perimeter(self):
        return 2 * (self.get_length() + self.get_width())

# Creating an instance of Rectangle
s = Rectangle("Rectangle", 20, 15)

# Calculating area and perimeter
a = s.area()
b = s.perimeter()

print(s.get_name()) 
print(f"Area: {a}")
print(f"Perimeter: {b}")
