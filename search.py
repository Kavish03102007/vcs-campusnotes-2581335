
def search_notes(notes, keyword):
    """Return the notes that contain the keyword, ignoring case and surrounding spaces."""

    if not isinstance(keyword, str):
        return []

    keyword = keyword.strip().lower()

    if not keyword:
        return []

    return [
        note for note in notes
        if isinstance(note, str) and keyword in note.lower()
    ]