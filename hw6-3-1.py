# Author CCG 11/15/2021

word1 = input("Input a word: ")
word2 = input("Input another word: ")

list1 = list(word1)
list2 = list(word2)

sort1 = list1.copy()
sort2 = list2.copy()
sort1.sort()
sort2.sort()

if sort1 == sort2:
    print("The words " + word1 + ' and ' + word2 + " are anagrams.")
else:
    print("The words " + word1 + ' and ' + word2 + " are not anagrams.")