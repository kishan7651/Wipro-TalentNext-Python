#Write a function to return the reverse of a string. Sample String : "1234abcd" Expected Output : "dcba4321"

def reverse_string(s):
    return s[::-1]

sample_string = "1234abcd"

print("Reversed String:", reverse_string(sample_string))