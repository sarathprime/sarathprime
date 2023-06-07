# x=str(input('enter the number'))
# for i in x:
#     if i=='s':
#
#
#                 print(i)
#                 print('crt')
#     else:
#         print(i)
#         print('not correct')



# x=3
# y=0
# try:
#     c=x/y
#     print(c)
#
#
# except:
#     print('zero error')



# def calculator(a,*b):
#     print(a+b)
# calculator(1,2,3,4,5,6)



#  palindrome
# for i in range(0,3):
#     a=input('please enter the the first string: ')
#     a1=a.lower()
#     b=a1[::-1]
#     if a1==b:
#         print('1')
#     else:
#         print('0')


# decorators

# def outerfunction0():
#     print('this is outer function')
#     def innerfunction():
#         print('this is a inner function')
#     return innerfunction()


# x=outerfunction0()



# for i in range(0,i+1):
#     pass
# print(i)


# replace sreting
# s='data science'
# y=s.replace(' ','_')
# print(y)


# append vowels in strating  string
# l=[]
# vowels=['a','e','i','o','u']
# a=input('enter the string')
# for i in vowels:
#     if i in a:
#         vowels = ['a', 'e', 'i', 'o', 'u']
#         l.append(a)
#         l.remove(vowels)
#         print(l)


# vowels

# a='prime'
# v=['a','e','i','o','u']
# A1=[]
# t=a[0]
# for i in a:
#     if i in v:
#      # print(i)
#      A1.append(i)
#      print(A1)
#      for j in A1:
#          print(j)
#          x=j.join(a)
#          print(x)
#          y=set(x)
#          print(y)


# anangrams

# s=input('enter the 1st string: ')
# g=input('enter the 2nd string: ')
# t=s[::]
# p=g[::]
# s1=[]
# g2=[]
# s2=list(s)
# gp=list(g)
# s1.append(s)
# g2.append(g)

# print(s)
# for i in s:
#     if i in g:
#         print(t, 'is angrams')
#     else:
#         print('false')





# map function
# x=(1,2,3)
# t=list(filter(lambda x:x+3,x))
# print(t)

# l=[1,2,3,4]
# t=[1,2,3,4]
# x1=map(lambda x,y:x+y,l,t)
# print(list(x1))







# reduce function
# import functools
# l=[1,2,3,4]
# x=functools.reduce(lambda x,y:x+y,l)
# print(x)

# import numpy as np
# a=10
# b=20
# def np():
#     c=a+b
#     return c
# x=np()
# print(x)









