"""
Program to showcase decorators available in python
"""

class Employee:

    def __init__(self, first, last, id):
        self.first = first
        self.last = last
        self.id = id

    def __str__(self):
        return self.fullname

    def __repr__(self):
        return 'Employee({}, {}, {})'.format(self.first, self.last, self.id)

    # We use property decorator to treat a method as attribute
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    # For setter method, we need to use attributes declared with property decorator,
    # and define function with same name as property
    # E.g.
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    # similar to setter , there is deleter available in python as well
    # used to delete an attribute
    @fullname.deleter
    def fullname(self):
        print('DELETE.!')
        self.first = None
        self.last = None


def main():
    emp1 = Employee("Muktesh", "Mukul", 103)
    emp2 = Employee("Amrita", "Yadav", 104)

    print(emp1.fullname)
    print(emp2)

    emp2.fullname = "Balli Yadav"
    print(emp2.email)

    del emp1.fullname
    print(emp1)
    emp1.fullname = "Monu Kumar"
    print(emp1)

    
if __name__ == '__main__':
    main()
