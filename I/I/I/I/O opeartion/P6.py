#Write a program to count the frequency of a user entered word in a txt file.

# Count the frequency of a user-entered word in a text file

file = open("sample.txt", "r")

text = file.read().lower()

word = input("Enter the word to search: ").lower()

words = text.split()

count = words.count(word)

file.close()

print("Frequency of", word, "is", count)