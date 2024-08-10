# How Many Vowels?

# Create a function that takes a string and returns the number (count)
# of vowels contained within it.
# Examples

# count_vowels("Celebration") ➞ 5

# count_vowels("Palm") ➞ 1

# count_vowels("Prediction") ➞ 4




# def count_vowels(txt):
#     vowels = ["a","e","o","i","u"]
   
#     for i in txt:
#         if i in vowels:
#             num += i
#     return num
# print(count_vowels("Celebration"))




def count_vowels(txt):
    vowels = ["a", "e", "i", "o", "u"]
    num = 0  # Initialize the counter
    
    for i in txt.lower():  # Convert text to lowercase to handle case-insensitive comparison
        if i in vowels:
            num += 1  # Increment the counter by 1 for each vowel found
    return num

print(count_vowels("Celebration"))
print(count_vowels("Prediction"))
print(count_vowels("Palm"))

def count_vowels(txt):
    vowels = "aeiou"
    return sum(1 for char in txt.lower() if char in vowels)

print(count_vowels("Celebration"))
