import re

# Input from user
text = input("Enter a sentence: ")
pattern = input("Enter the pattern to search: ")

# Search for pattern
match = re.search(pattern, text)

# Display result
if match:
    print("Pattern Found!")
    print("Matched Text:", match.group())
    print("Start Position:", match.start())
    print("End Position:", match.end())
else:
    print("Pattern Not Found!")