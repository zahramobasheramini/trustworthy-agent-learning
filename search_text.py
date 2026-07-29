# with open("sample.txt", "r", encoding="utf-8") as file:
#     text = file.read()

# keyword = input("Enter a keyword: ")

# if keyword.lower() in text.lower():
#     print("The keyword was found.")
# else:
#     print("The keyword was not found.")

with open("sample.txt", "r", encoding="utf-8") as file:
    text = file.read()

question = input("Enter your question: ")

words = question.lower().split()
text = text.lower()

found_words = []

for word in words:
    if word in text:
        found_words.append(word)

if found_words:
    print("Found words:", found_words)
else:
    print("No words were found.")