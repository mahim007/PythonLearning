my_dict = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "0": "Zero",
}

inp = input("Type a number: ")
converted = ""
for char in inp:
    converted += my_dict.get(char, "")
    converted += " "

print(converted)