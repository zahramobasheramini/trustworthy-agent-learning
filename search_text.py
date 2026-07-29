import string


def clean_text(text):
    return text.lower().translate(
        str.maketrans("", "", string.punctuation)
    )


with open("sample.txt", "r", encoding="utf-8") as file:
    text = file.read()


chunks = text.split("\n\n")

question = input("Enter your question: ")
question_words = clean_text(question).split()

best_chunk = ""
best_score = 0


for chunk in chunks:
    chunk_words = clean_text(chunk).split()

    score = 0

    for word in question_words:
        if word in chunk_words:
            score += 1

    if score > best_score:
        best_score = score
        best_chunk = chunk.strip()


if best_score > 0:
    print("Most relevant text:")
    print(best_chunk)
    print("Score:", best_score)
else:
    print("No relevant text was found.")