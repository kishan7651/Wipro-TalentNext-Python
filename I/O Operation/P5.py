#Write a program to find the longest word from the txt file contents, assuming that the file will have only one longest word in it.

# Find the longest word from a text file

file = open("sample.txt", "r")

text = file.read()
words = text.split()

longest = ""

for word in words:
    if len(word) > len(longest):
        longest = word

file.close()

print("Longest word:", longest)