def fsa_ends_with_ab(string):
    if string.endswith("ab"):
        return "Accepted"
    else:
        return "Rejected"

text = input("Enter a string: ")
print(fsa_ends_with_ab(text))