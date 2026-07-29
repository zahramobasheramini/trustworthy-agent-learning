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


if not question_words:
    print("Please enter a question.")
    exit()


best_chunk = ""
best_score = 0
minimum_score = 2


for chunk_number, chunk in enumerate(chunks, start=1):
    chunk_words = clean_text(chunk).split()

    score = 0

    for word in question_words:
        if word in chunk_words:
            score += 1

    print("Chunk", chunk_number, "score:", score)

    if score > best_score:
        best_score = score
        best_chunk = chunk.strip()


match_ratio = best_score / len(question_words)


if best_score >= minimum_score and match_ratio >= 0.5:
    print("\nMost relevant text:")
    print(best_chunk)
    print("Best score:", best_score)
    print("Match ratio:", round(match_ratio, 2))
else:
    print("\nNo relevant text was found.")