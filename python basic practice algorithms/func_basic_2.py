# Countdown - Create a function that accepts a number as an input. Return a new list (array) that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
# Example: countdown(5) should return [5,4,3,2,1,0]

# def count_down(num):
#     new_list = []
#     for i in range(num, -1, -1):
#         new_list.append(i)
#     return new_list
# print(count_down(20))


# Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
# Example: print_and_return([1,2]) should print 1 and return 2

# def two_list(numbers):
#     print (numbers[0])
#     return numbers[1]
# two_list([54,66]))


# First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
# Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)

# def list_sum(numbers):
#     return numbers[0] + len(numbers)
# print(list_sum([2,4,6,8,10,12]))


# Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
# Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
# Example: values_greater_than_second([3]) should return False

# def grt_sec(numbers):
#     new_list = []
#     if len(numbers)<2:
#         return False
#     else:
#         for i in range(0,len(numbers),1):
#             if (numbers[i] > numbers[1]):
#                 new_list.append(numbers[1])
#         print(len(new_list))
#         return new_list
# print(grt_sec([6,7,3,5,7,9,4,5,4,1]))


# This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
# Example: length_and_value(4,7) should return [7,7,7,7]
# Example: length_and_value(6,2) should return [2,2,2,2,2,2]

# def len_val (size, value):
#     new_list =[]
#     for i in range(size):
#         new_list.append(value)
#     return new_list
# print(len_val(6,10))
# print(len_val(9,3))