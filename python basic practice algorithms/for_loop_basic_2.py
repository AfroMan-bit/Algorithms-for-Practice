# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]

# def big_size(positive):
#     for i in range(len(positive)):
#         if positive[i]>0:
#             positive[i] = "Big"
#     return positive
# print(big_size([-2,-1,4,7,-2,8,-3,-2,4,-5]))


# Count Positives - Given a list of numbers, create a function to replace the last value in the list(array) with the number of positive values in the list. 
# (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it

# def count_p(last_positive):
#     count = 0
#     for i in range(len(last_positive)):
#         if last_positive[i]>0:
#             count += 1
#     last_positive[len(last_positive)-1] = count
#     return last_positive
# print(count_p([2,4,6,8,10,12,14,-5,-4,-2]))


# Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7

# def sum_ttl(number):
#     keep = 0
#     for i in range(len(number)):
#         keep += number[i]
#     return keep
# print(sum_ttl([2,4,6,8,12,45]))

# Average - Create a function that takes a list and returns the average of all the values.
# Example: average([1,2,3,4]) should return 2.5

# def avg(number):
#     hold = 0
#     for i in range(len(number)):
#         hold += number[i]
#     avg = hold/len(number)
#     return avg
# print(avg([2,4,4,7,6,2,5,6,74,3,4,5,]))


# Length - Create a function that takes a list(array) and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0

# def length(number):
#     return len(number)
# print(length([1,2,3,4,5,6,7,8,9,3,3,3]))
    

# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, 
# have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False

# def minimum(number):
#     min_num = number[0]
#     for i in range(len(number)):
#         if number[i] < min_num:
#             min_num = number[i]
#     return min_num
# print(minimum([5,9,2,7,9,-2,8,-3]))



# Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, 
# have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False

# def maximum(number):
#     max_num = number[0]
#     for i in range(len(number)):
#         if number[i] > max_num:
#             max_num = number[i]
#     return max_num
# print(maximum([5,9,2,7,9,-2,8,-3]))



# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the 
# sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }

# def ultimate_analysis(somelist):
#     new_dictionary = {}
#     sumtotal = 0
#     minimum = somelist[0]
#     maximum = somelist[0]
#     for val in somelist:
#         sometoltal += val
#     average = sumtotal/len(somelist)

#     for i in range(0, len(somelist)):
#         if somelist[i] < minimum:
#             minimum = somelist[i]

#     for i in range(0, len(somelist)):
#         if somelist[i] > maximum:
#             maximum = somelist[i]

#     new_dictionary = {
#         "sometotal": sumtotal,
#         "avg": average,
#         "min": minimum,
#         "max": maximum,
#     }
#     return new_dictionary
# print(ultimate_analysis([37,2,1,-9]))











                        #   VERY IMPORTANT 
# Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. 
# (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]

# def rev_list(number):
#     for i in range(int(len(number)/2)):
#         temp = number[i]
#         number[i] = number[len(number)-1-i]
#         number[len(number)-1-i]=temp
#     return number
# print(rev_list([7,1,8,23,4,6,12,1,6]))

