# Author CCG 11/15/2021

numbers = input("Enter a list of 5 numbers seperated by spaces: ")

list1 = list(numbers)
sort1 = list1.copy()
sort1.sort()

start = sort1[4:]

sum = int(start[0]) + int(start[1]) + int(start[2]) + int(start[3]) + int(start[4])
print(sum)
