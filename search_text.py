import string


def clean_text(text):
    cleaned_text = text.lower().translate(
        str.maketrans("", "", string.punctuation)
    )
    return cleaned_text


with open("sample.txt", "r", encoding="utf-8") as file:
    text = file.read()

question = input("Enter your question: ")

clean_question = clean_text(question)
clean_document = clean_text(text)

question_words = clean_question.split()
text_words = clean_document.split()

found_words = []

for word in question_words:
    if word in text_words:
        found_words.append(word)

if found_words:
    print("Found words:", found_words)
else:
    print("No words were found.")