# In Python, you can use the enumerate function to iterate over a sequence (such as a list, tuple, or string)
# and get both the index and the corresponding value at that index. Here's how you can use enumerate
# Example with a list
fruits = ['apple', 'banana', 'cherry', 'orange', 'kivy', 'coconut']
print(f"My List is: {fruits}")
for index, value in enumerate(fruits):
    print(f"Index: {index}, Value: {value} ")

# output :
"""
Index: 0, Value: apple
Index: 1, Value: banana
Index: 2, Value: cherry
"""

print()
# Example with a start index
for index, value in enumerate(fruits, start=1):
    print(f"Index: {index}, Value: {value}")

# output
"""
Index: 1, Value: apple
Index: 2, Value: banana
Index: 3, Value: cherry
"""






