from stack import Stack

class TextEditor:
    def __init__(self):
        self.undo_stack = Stack()
        self.redo_stack = Stack()

        self.undo_stack.push("")
        
    def type_text(self, text):
        current_text = self.undo_stack.peek()
        new_text = current_text + text
        self.undo_stack.push(new_text)
        
        self.redo_stack = Stack()
        
    def undo(self):
        if self.undo_stack.size() > 1:
            popped_state = self.undo_stack.pop()
            self.redo_stack.push(popped_state)

    def redo(self):
        if not self.redo_stack.is_empty():
            popped_state = self.redo_stack.pop()
            self.undo_stack.push(popped_state)

    def get_text(self):
        return self.undo_stack.peek()
