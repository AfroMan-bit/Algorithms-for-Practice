#1
# def a():
#     return 5
# print(a())

# output is 5 because a function is whatever it returns


#2
# def a():
#     return 5
# print(a()+a())

# output is 10 because a() was called twice to be added together to give a single value of that function

#3
# def a():
#     return 5
#     return 10
# print(a())

# output is 5 because a() returns 5. the first return is 5 attached to the function a(), the return 10 does not count


#4
# def a():
#     return 5
#     print(10)
# print(a())

# output is 5 because a() returns 5 and print(10) is under the code-block of the function because of the indentation so it does not count. 


#5
# def a():
#     print(5)
# x = a()
# print(x)

# output is 5 because the function a() prints 5 and x is the same as a()


#6
# def a(b,c):
#     print(b+c)
# print(a(1,2) + a(2,3))

# output is undefined because the function called at the end does not satisfy the parameter set at the begining

#7
# def a(b,c):
#     return str(b)+str(c)
# print(a(2,5))

# output is 2 and 5 as a string given as 25 because str b is 2 and str c is 5. the + in the return statement 
# jions both strings but not the sum of both strings to satisfy the function called


#8
# def a():
#     b = 100
#     print(b)
#     if b < 10:
#         return 5
#     else:
#         return 10
#         return 7
# print(a())

# output is 100 for b and 10 for a() because 100 < 10 is false so we do not return 5, instead we return 10 for the called function a()

#9
# def a(b,c):
#     if b<c:
#         return 7
#     else:
#         return 14
#     return 3
# print(a(2,3))
# print(a(5,3))
# print(a(2,3) + a(5,3))

# output is 7 because b < 3 is true and 14 because b < 3 is false and 21 because print(a(2,3) + a(5,3)) is asking us to sum the values of the two
# previous function outputs.

#10
# def a(b,c):
#     return b+c
#     return 10
# print(a(3,5))

# output is 8 because the second return does not count since it is still inside the code block of the function called.


#11
# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
# print(b)
# a()
# print(b)

# output is 500 for print b outside the defined function a() and 500 again for print b outside the defined function and then 300 for a() because it is in the same code block as the function defined 
# and 500 again for print b


#12
# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
#     return b
# print(b)
# a()
# print(b)

# output is 500 for print b outside the defined function a() and 500 for print b and 300 for a() and 500 again for print b


#13
# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
#     return b
# print(b)
# b=a()
# print(b)

# output is 500 outside the defined function and 500 for print b and 300 since b = 300 and returns b for b=a() and 300 for print b


#14
# def a():
#     print(1)
#     b()
#     print(2)
# def b():
#     print(3)
# a()

# output is 1 for function call a() and 3 for print 3 but was not called and 2 for print 2 for the function b() inside the defined function a()
# but was not called the second time.


#15
# def a():
#     print(1)
#     x = b()
#     print(x)
#     return 10
# def b():
#     print(3)
#     return 5
# y = a()
# print(y)

# output is 1 for print 1 in function a() and 3 for print 3 in function b() and 5 for print x since x = b() and returns 5 
# in function b() and then 10 for print y because y = a() but returns 10 as it is defined in function a()
