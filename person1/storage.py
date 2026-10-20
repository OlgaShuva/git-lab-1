from notes import notes

def save(filename):
    with open(filename, "w", encoding="utf-8") as f:
        for n in notes:
            f.write(n + "\n")

def load(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read().splitlines()
