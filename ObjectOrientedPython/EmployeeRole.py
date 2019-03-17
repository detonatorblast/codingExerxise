"""
Python object oriented programming
-- Inheritance
"""


class Employee:

    # class variables
    num_of_employees = 0
    raise_amount = 1.04    # 4%

    def __init__(self, firstname, lastname, pay):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay
        self.email = firstname + '.' + lastname + '@company.com'

        Employee.num_of_employees += 1

    def fullname(self):
        return self.firstname + ' ' + self.lastname

    def apply_raise(self):
        self.pay = (self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amt):
        cls.raise_amount = amt

    @classmethod
    def from_string(cls, empstr):
        first, last, pay = empstr.split('-')
        return cls(first, last, pay)
        # return cls(empstr.split('-'))   # didn't work

    # its recommended to make a method static when no instance/class is accessed in the method
    @staticmethod
    def isworkday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


class Developer(Employee):

    def __init__(self, firstname, lastname, pay, prog_lang):
        super().__init__(firstname, lastname, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, firstname, lastname, pay, employees=None):
        super().__init__(firstname, lastname, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def printEmps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


dev1 = Developer('Muktesh', 'Mukul', 50000, 'Python')
dev2 = Developer('Mukul', 'Muktesh', 50000, 'C++')

mng1 = Manager('Amrita', 'Yadav', 90000, [dev1])

# mng1.printEmps()

dev2 = Developer('Mukul', 'Muktesh', 50000, 'C++')
mng1.add_emp(dev2)
# mng1.printEmps()

# Functions to check if an object is an instance of any class
print(isinstance(dev1, Developer))

# Function to check if a class is subclass of other
print(issubclass(Manager, Employee))

# Function to get all the details about a class. From its inheritance hierarchy to attributes associated
# print(help(Developer))
