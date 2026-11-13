
def search_notes(notes, keyword):
    """Search notes using case-insensitive keyword matching."""

    if not isinstance(keyword, str):
        return []

    keyword = keyword.strip().lower()

    if not keyword:
        return []

    return [
        note for note in notes
        if isinstance(note, str) and keyword in note.lower()
    ]