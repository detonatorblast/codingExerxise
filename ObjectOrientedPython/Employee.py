"""
Python object oriented programming
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


"""
Note about class variables:
If a variable is accessed via instance/self, then the variable is first looked in that 
particular instance, if it is not available in instance, then only that variable will be
accessed from class 
"""


def main():
    emp1 = Employee('Muktesh', 'Mukul', 80000)
    # emp2 = Employee('Amrita', 'Yadav', 50000)
    emp2str = 'Amrita-Yadav-50000'
    emp2 = Employee.from_string(emp2str)

    # Below are two ways we may call the methods for a instance
    print(Employee.fullname(emp1))   # 1
    print(emp1.fullname())           # 2, this one actually resolves to above call internally

    # we can check available members for any instance/class
    # using a special attribute __dict__
    print(emp1.__dict__)
    emp1.raise_amount = 1.05         # only reflects to emp1 object, this will also add raise_amount as member of emp1
    print(emp1.__dict__)

    Employee.raise_amount = 1.06     # Will not affect emp1

    print(emp1.raise_amount)
    print(emp2.raise_amount)
    print(Employee.raise_amount)

    print(emp2.fullname())

    import datetime
    my_date = datetime.date(2019, 3, 17)
    print(Employee.isworkday(my_date))


if __name__ == '__main__':
    main()