from classdef import Employee, Manager, Developer
from PIL import Image

image1 = Image.open('march_id_pic.jpg')
image1.show()



# with open('input.txt', 'r') as f:
#     help(f.read)
#     print(f.name)
#
#     size_to_read = 10
#
#     line = f.read(size_to_read)
#     while( len(line) != 0 ):
#         print line
#         line = f.read(size_to_read)




 
# add commit
# def square_nums(input):
#     for i in input:
#         yield (i*i)
#
#
# my_nums = square_nums([1,2,3,4,5])
#
# print(next(my_nums))
# print(next(my_nums))
#
#
# print __name__


# student = {'name': 'Ryan', 'pay': '12000'}
# student['phone'] = '0478-008959'
#
# emp = Employee('Ryan', 'Mateo', 33, 102000)
#
# print(emp.fullname)
# print(emp.email)
#
# emp.fullname = 'Cindy Garces'
#
# print(emp.fullname)





# def func(*args, **kwargs):
#     print(args)
#     print('\n')
#     print(kwargs)
#
# courses = ['Math', 'English']
# students = { 'fname':'ryan', 'lname':'mateo' }
#
# func(*courses, **students)


























#student.update({'name': 'Amats'})
#del student['pay']

# print(student.__len__())
# print(student.items())
# print(student.keys())
# print(student.values())


# for i in range(1,11):
#     print i

# x = 0
# while x < 10:
#     x += 1
#     print(x)

#print(student.get('name', 'Not Found'))

# Main
# emp = Employee('Ryan', 'Mateo', 33, 102000)
# dev = Developer('Brian', 'Destura', 27, 55000, 'Python')

# print(emp)
# print(dev)
# print(dev.prog_lang)
# print('Emp Count = ' + str(Employee.emp_count))
# print dev.pay
# dev.raisePayAmount()
# print dev.pay
# man = Manager('Manager first', 'Manager second', 27, 55000, {emp})
# man.add_emp(emp)
# man.remove_emp(emp)
# man.remove_emp(emp)

# def fib(n):
#     a,b = 0,1
#     for i in range(n):
#         a, b = b, a+b
#     return a
#
# def fact(n):
#     product = 1
#     for i in range(2,n+1):
#         product *= i
#     return product
#
# print(fact(2))

# import unittest
#
# class MyTest(unittest.TestCase):
#     def test_fib(self):
#         self.assertEqual( fib(0), 0 )
#         self.assertEqual( fib(1), 1 )
#         self.assertEqual(fib(2), 1)
#         self.assertEqual(fib(3), 2)
# unittest.main()















#n = 10
#for i in range(n):
#    print i



# def fib(n):
#     a,b = 0,1
#     for i in range(n):
#         a, b = b, a+b
#     return a
#
# print (fib(3))
#
# def factorial(n):
#     result = 1
#     for i in range(2,n+1):
#         result *= i
#
#     return result
#
# print factorial(4)
