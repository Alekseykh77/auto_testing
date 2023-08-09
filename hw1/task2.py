import string

s = "Hello, world! Hello, world!"
print("The original string is : " + s)

output = s.translate(str.maketrans('', '', string.punctuation))

print(output)
