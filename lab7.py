class person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname, self.lastname)

class student(person):
    def __init__(self,fname,lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year
    
    def printgraduation(self):
        print(self.graduationyear)

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

class teacher(person):
    def __init__(self, fname, lname, year):
        # Initialize person attributes without super()
        person.__init__(self, fname, lname)
        self.joining_year = year

    def printteacher(self):
        print("Welcome", self.firstname, self.lastname, "joined in", self.joining_year)

class admin(person):
    def __init__(self, fname, lname, year):
        # Initialize person attributes without super()
        person.__init__(self, fname, lname)
        self.join_year = year

    def printadmin(self):
        print(self.join_year)

class alumni(student):
    def __init__(self, fname, lname, jyear):
        super().__init__(fname, lname, jyear)
        self.passingyear = 2026
    
    def passyear(self):
        print(self.passingyear)

class cstudent(student):
    def __init__(self, fname, lname, jyear):
        super().__init__(fname, lname, jyear)
        self.currentsemester = 6
    
    def passyear(self):
        print(self.currentsemester)

class Employee(teacher, admin):
    def __init__(self, fname, lname, year, id):
        # Initialize person, teacher, and admin directly
        person.__init__(self, fname, lname)
        teacher.__init__(self, fname, lname, year)
        admin.__init__(self, fname, lname, year)
        self.id = id

    def display(self):
        print(self.id)

        
p1 = person("AAA", "BBB")
x = student("Mike", "olsen", 2024)
x1 = teacher("mike", "olsen", 2025)
x2 = Employee("mike", "olsen",2025, 5)

x.welcome()
x1.printteacher()
p1.printname()
x2.display()