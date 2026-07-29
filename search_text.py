import string
from pathlib import Path


def clean_text(text):
    return text.lower().translate(
        str.maketrans("", "", string.punctuation)
    )


question = input("Enter your question: ")
question_words = set(clean_text(question).split())


if not question_words:
    print("Please enter a question.")
    exit()


best_chunk = ""
best_file = ""
best_chunk_number = 0
best_score = 0
best_matched_words = []

minimum_score = 2
minimum_match_ratio = 0.5


for file_path in Path("documents").glob("*.txt"):
    text = file_path.read_text(encoding="utf-8")
    chunks = text.split("\n\n")

    for chunk_number, chunk in enumerate(chunks, start=1):
        chunk_words = clean_text(chunk).split()

        matched_words = []

        for word in question_words:
            if word in chunk_words:
                matched_words.append(word)

        score = len(matched_words)

        print(
            file_path.name,
            "- Chunk",
            chunk_number,
            "- Score:",
            score
        )

        if score > best_score:
            best_score = score
            best_chunk = chunk.strip()
            best_file = file_path.name
            best_chunk_number = chunk_number
            best_matched_words = matched_words.copy()


match_ratio = best_score / len(question_words)


if (
    best_score >= minimum_score
    and match_ratio >= minimum_match_ratio
):
    print("\nSource:", best_file)
    print("Chunk number:", best_chunk_number)
    print("Matched words:", sorted(best_matched_words))
    print("Most relevant text:")
    print(best_chunk)
    print("Best score:", best_score)
    print("Match ratio:", round(match_ratio, 2))
else:
    print("\nNo relevant text was found.")