from pathlib import Path

ROOT_DIR = Path(__file__).absolute().parent.parent

file = open(ROOT_DIR / "rockyou.txt", "r", encoding="utf-8")

text = file.readlines()

results = []

for word in text:
    words = file.readline()
    if word.startswith("user"):
        input_if = input("Ви хочете додати слово?(Так або ні)")
        if input_if == "Так":
            results.append(word)
        else:
            print("Ви обрали не додавати слово")

file.close()

results_word = len(results)

print(f"Кількість слів {results_word}")
