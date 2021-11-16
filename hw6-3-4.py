# Author CCG 11/15/2021

numbs = input("Enter a list of numbers separated by spaces: ")
numbers = list(numbs)
length = len(numbers)
mid = int(length - 1)
end = int(length - 1)
choice = input("Do you want the middle or ends of your input? ")

if choice == "middle":
     print("The middle of your input is " + str(numbers[1:mid]) + '.')
if choice == "ends":
    print("The ends of your input are " + str(numbers[0]) + " and " + numbers[end] + ".")