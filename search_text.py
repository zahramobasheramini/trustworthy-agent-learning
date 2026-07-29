import string


def clean_text(text):
    return text.lower().translate(
        str.maketrans("", "", string.punctuation)
    )


with open("sample.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()


question = input("Enter your question: ")

question_words = clean_text(question).split()

best_line = ""
best_score = 0


for line in lines:
    line_words = clean_text(line).split()

    score = 0

    for word in question_words:
        if word in line_words:
            score += 1

    if score > best_score:
        best_score = score
        best_line = line.strip()


if best_score > 0:
    print("Most relevant text:")
    print(best_line)
    print("Score:", best_score)
else:
    print("No relevant text was found.")