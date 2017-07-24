class Employee:
    pay_increase = 1.10
    emp_count = 0

    def __init__(self, first, last, age, pay):
        self.first = first
        self.last = last
        #self.email = first + '.' + last + "@company.com"
        self.age = age
        self.pay = pay

        Employee.emp_count += 1

    @property
    def email(self):
        return '{}.{}@company.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    def __str__(self):
        return '{} {}'.format(self.first, self.last)

    def raisePayAmount(self):
        self.pay = int(self.pay * Employee.pay_increase)

    @classmethod
    def setRaiseAmount(cls, amount):
        cls.pay_increase = amount

    #@staticmethod

class Developer(Employee, object):
    pay_increase = 1.20

    def __init__(self, first, last, age, pay, prog_lang):
        super(Developer, self).__init__(first, last, age, pay)
        self.prog_lang = prog_lang

class Manager(Employee, object):
    def __init__(self, first, last, age, pay, employees=None):
        super(Manager, self).__init__(first, last, age, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)
        else:
            print 'Employee ' + employee.first + ' already exists'

    def remove_emp(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)
        else:
            print 'Employee ' + employee.first + ' not existing'