from notes import add_note, list_notes
from storage import save

def main():
    add_note("Первая заметка")
    add_note("Вторая заметка")
    list_notes()
    save("notes.txt")
    print("Заметки сохранены в notes.txt")

if __name__ == "__main__":
    main()
