# Author CCG 11/15/2021

word1 = input("Input a word: ")
word2 = input("Input another word: ")

list1 = list(word1)
list2 = list(word2)

if list1.sort() == list2.sort():
    print("Those words are anagrams")
else:
    print("Those words are not anagrams")
