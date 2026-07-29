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


minimum_score = 2
minimum_match_ratio = 0.5
top_k = 2

results = []


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
        match_ratio = score / len(question_words)

        if (
            score >= minimum_score
            and match_ratio >= minimum_match_ratio
        ):
            results.append(
                (
                    score,
                    file_path.name,
                    chunk_number,
                    matched_words,
                    chunk.strip()
                )
            )


results.sort(reverse=True)


if results:
    print("\nTop relevant results:")

    for result in results[:top_k]:
        score, file_name, chunk_number, matched_words, chunk = result

        print("\nSource:", file_name)
        print("Chunk number:", chunk_number)
        print("Matched words:", sorted(matched_words))
        print("Text:")
        print(chunk)
        print("Score:", score)
        print(
            "Match ratio:",
            round(score / len(question_words), 2)
        )
else:
    print("\nNo relevant text was found.")