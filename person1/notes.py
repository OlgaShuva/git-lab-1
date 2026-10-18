notes = []

def add_note(text):
    notes.append(text)

def list_notes():
    print("Список заметок:")
    for n in notes:
        print(" -", n)

def clear_notes():
    notes.clear()
    print("Все заметки удалены")
