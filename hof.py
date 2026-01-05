#1. Use map() with a lambda to add 5 to every element of the following nested
#list [[1, 2], [3, 4], [5, 6]]
#
# l=[[1,2],[3,4],[5,6]]
# l=[1,2,3,4,5,5,6]
# a=list(map(lambda x:x+5,l))
# print(a)
#
# nested_list = [[1, 2], [3, 4], [5, 6]]
# result = list(map(lambda sub: list(map(lambda x: x + 5, sub)), nested_list))
# print(result)
from operator import is_not

#2. Given a dictionary: d = {"apple": 100, "banana": 40, "cherry": 150} . Use
#filter() to keep only the keys whose values are greater than 50.

#
# d = {"apple": 100, "banana": 40, "cherry": 150}
# k=list(filter(lambda x:d[x]>50,d))
# print(k)

#3. Use functools.reduce() with a lambda to find the largest number from a given
#list Dynamically.

# from functools import reduce
# l=list(map(int,input().split()))
# l_n=reduce(lambda x,y: x if x>y else y,l)
# print(l_n)

#5. Use map() on a string to convert each character into its ASCII value
#(using ord()). Print the result list.

# a=input()
# l=list(map(lambda x:ord(x),a))
# print(l)

#6. Use filter() to remove all vowels from a string and print the final string.

# s=input()
# v=["a","e","i","o","u"]
# l=list(filter(lambda x:x not in v,s))
# print(l)


#7. Use reduce() to concatenate a list of characters into a single string.
#Example input: ['P', 'y', 't', 'h', 'o', 'n'].

# from functools import reduce
# l=["p","y","t","h","o","n"]
# r=reduce(lambda x,y:x+y,l)
# print(r)


#8. Given a list of integers, use map() with id() to print the memory address
#of each element.
#Example: [10, 350, 10, 350, 20] — explain why some addresses repeat
# l=[10, 350, 10, 350, 20]
# l1=list(map(lambda x:id(x),l))
# print(l1)

# 9. Explain the difference between:
# map(str, [1, 2, 3])
# map(lambda x: str(x), [1, 2, 3])
# Which one is faster and why?

#
# l=list(map(str, [1, 2, 3]))
# l2=list(map(lambda x: str(x), [1, 2, 3]))
# print(l)
# print(l2)

#10. Given a list of numbers:
#[5, 10, 15, 20, 25, 30]
#Perform the following in a single pipeline:
##• Use map() to square each number
#• Use filter() to keep only numbers divisible by 5
#• Use reduce() to calculate the sum of remaining numbers

#
# from functools import reduce
# l=[5, 10, 15, 20, 25, 30]
# l1=reduce(lambda x,y:x+y,filter(lambda x:x%5==0,map(lambda x:x*2,l)))
# print(l1)



#//////////////////////////////////////////////////////////////////////////////

#2. Given two lists:
#a = [1, 2, 3, 4] b = [10, 20, 30, 40]
#Use map() with a lambda to create a new list containing the sum of corresponding
#elements.
#What happens if the lists are of unequal length?

a = [1, 2, 3, 4]
b = [10, 20, 30, 40]
l=list(map(lambda x,y:x+y,a,b))
print(l)

#3. Given a list:
#nums = [12, 15, 7, 18, 20, 21, 25]
#Use filter() and lambda to keep numbers that are divisible by 3 OR divisible by
#5 but NOT divisible by both.
#Explain how the logical condition works.

nums = [12, 15, 7, 18, 20, 21, 25]
l=list(filter(lambda x:(x%3==0 or x%5==0) and not(x%3==0 and x%5==0),nums))
print(l)

#4. Given a list:
#nums = [1, 2, 3, 4]
#Use reduce() with a lambda to compute the sum, but start with an initial value
#of 10.
#Explain how the initial value affects the reduction process.


from functools import reduce
nums = [1, 2, 3, 4]
l=reduce(lambda x,y:x+y,nums,10)
print(l)


#5. Consider the code below:
#nums = [[1, 2], [3, 4], [5, 6]] result = list(map(lambda x: x.append(10), nums))
#print("Result:", result) print("Nums:", nums)
#Questions
#• What will be the output of result?
#• What will be the output of nums?
#• Why does map() behave this way with list.append()?
#• How can you modify the lambda so that nums is not changed?


nums = [[1, 2], [3, 4], [5, 6]]
result = list(map(lambda x: x.append(10), nums))
print("Result:", result)
print("Nums:", nums)
