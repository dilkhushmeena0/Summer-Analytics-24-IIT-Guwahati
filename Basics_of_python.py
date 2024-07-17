# print & Slicing strings
# m = 'Hello World'
# print(m)
# print(m.lower())
# print(m.upper())
# print(m.count('l'))
# print(m.find('World'))
# m = m.replace('World','Universe')
# print(m)
# g = 'Hello'
# n = 'World'
# gn = g+','+n
# print(gn)

# Integers & Floats
# print(3//2)
# num_1 = 1
# num_2 = 2
# print(num_1+num_2)
# print(num_1<= num_2)

# Lists,Tuples and Sets
# courses = ['H','M','P','C']
# print(courses[3])
# print(courses[0:2])
# courses.append('Art')
# courses.insert(0,'Home')
# popp = courses.pop()
# print(popp)

# nums = [1,2,3,4,5]
# nums.sort(reverse=True)
# print(nums)
# print(courses.index('C'))
# print('H' in courses)

# for index,item in enumerate(courses, start=1):
#     print(index,item)
    
# c_str = '-'.join(courses)
# print(c_str)
# new_lst = c_str.split(' - ')
# print(new_lst)

#Python Dictionaries
# stu= {'name':'John','age':'34','cs':['M','P']}
# print(stu['name'])
# print(stu.get('name'))
# print(len(stu))

# for key,val in stu.items():
#     print(key,val)

#COnditions and booleans
# if True:
#     print('right')

# ln = 'Java'
# if ln == 'Java':
#     print('right')
# elif ln == 'py':
#     print('no mt')
# else:
#     print('do ag')
 
# a=[1,2,3]
# b=[4,5,6]
# print(id(a))  

#Loops & Iterations
# nums = [1,2,3,4,5,6,7]

# for num in nums:
#     if num==3:
#         print('fnj')
#         continue
#     print(num)
    
# for i in nums:
#     for let in 'abc':
#         print(i,let)
       
# for i in range(1,11):
#     print(i)
    
#while loop
# x=0
# while True:
#     print(x)
#     x+=1    

# Functions
# def hello_func(gr):
#     return'{} Function.'.format(gr)

# print(hello_func('hi'))

# def stud_info(*args,**kwargs):
#     print(args)
#     print(kwargs)
    
# cus = ['M','A']
# inf = {'name':'John','age':22}
    
# stud_info('M','A',name='John',age=22)
# stud_info(*cus,**inf)

# from my_mod import find_ind as fi, test
# import sys
# import datetime
# import math
# import os

# courses = ['h','m','k']
# idx = fi(courses,'m')
# print(idx)
# print(test)
# print(sys.path)
# print(os.getcwd())

# Operating System Modules
# import os
# print(os.getcwd())
# print(os.listdir())

