from text_editor import TextEditor

# Sample implementation for testing
if __name__ == "__main__":
    editor = TextEditor()

    editor.type_text("Hello, ")
    print(editor.get_text()) # Output: Hello,

    editor.type_text("world!")
    print(editor.get_text()) # Output: Hello, world!

    editor.undo()
    print(editor.get_text()) # Output: Hello,

    editor.redo()
    print(editor.get_text()) # Output: Hello, world!

    editor.type_text(" How are you?")
    print(editor.get_text()) # Output: Hello, world! How are you?

    editor.undo()
    print(editor.get_text()) # Output: Hello, world!

    editor.redo()
    print(editor.get_text()) # Output: Hello, world! How are you?