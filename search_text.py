with open("sample.txt", "r", encoding="utf-8") as file:
    text = file.read()

keyword = input("Enter a keyword: ")

if keyword.lower() in text.lower():
    print("The keyword was found.")
else:
    print("The keyword was not found.")