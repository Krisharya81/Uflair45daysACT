# srting is immutable -> cannot change


# print(name.upper())
# print(name.lower())
# print(name.title())
# print(name.capitalize()) # print(name.swapcase())  # swaps uppercase to lowercase and vice versa
# print(name.casefold())  # converts to lowercase and removes case distinctions

#name = "Upflairpvt1"
# print(name.strip())  # removes leading and trailing spaces
# print(name.lstrip())  # removes leading spaces  
# print(name.rstrip())  # removes trailing spaces
#print(name.replace("Upflair", "Upflair pvt ltd"))  # replaces a substring with another
#print(name.split("f"))  # splits the string into a list of words
#print(name.partition("f"))  # splits the string into a tuple of three parts: before, separator, after
# print(name.startswith("U"))  # checks if the string starts with a substring
# print(name.endswith("t"))  # checks if the string ends with a substring
# print(name.isalpha())  # checks if the string contains only alphabetic characters
# print(name.isalnum())  # checks if the string contains only alphanumeric characters

#print(name.encode("utf-8"))  # encodes the string to bytes using utf-8 encoding
# print(name.removeprefix("Upflair"))  # removes the specified prefix from the string
# print(name.removesuffix("pvt1"))  # removes the specified suffix from the string

# print(name.zfill(20))  # pads the string with zeros on the left to make it 20 characters long
# print(name.center(30, "*"))  # centers the string in a field of 30 characters, padding with '*'
# print(name.ljust(30, "*"))  # left-justifies the string in a field of 30 characters, padding with '*'
# print(name.rjust(30, "*"))  # right-justifies the string in a field of 30 characters, padding with '*'

#INDEXING AND SLICING

## indexing --> accessing a single character in a string
## slicing --> accessing a range of characters in a string

# name = "Upflairpvt"
# print(name[0])  # prints the first character
# print(name[-1])  # prints the second character
# print(name[0:7])  # prints characters from index 0 to 7 (7 is excluded)

#formatted_string --> f-strings
# age = 10
# #text = "my age is" + age
# #print(text)  # This will raise an error because age is an integer
# text = f"my age is {age}"  # Using f-string to format the string
# print(text)

# text = "my age is \"krish\""
# print(text)