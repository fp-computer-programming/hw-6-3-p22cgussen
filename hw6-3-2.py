# Author CCG 11/15/2021

numbers = input("Enter a list of numbers: ")

list1 = list(numbers)
sort1 = list1.copy()
sort1.sort()

if sort1 == list1:
    print("Your list (" + numbers + ") is sorted.")
else:
    print("Your list is not sorted.")
