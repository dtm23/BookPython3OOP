import sys
from notebook import Notebook, Note

class Menu:
    """
    Display a menu and respond to choices
    
    """
    
    def __init__(self):
        self.notebook = Notebook()
        
        self.choices = {
            "1": self.show_notes,
            "2": self.search_notes,
            "3": self.add_note,
            "4": self.modify_note,
            "5": self.quit_notebook
                
            }
    def display_menu(self):
        print("""
        Notebook Menu
        
        1. Show all Notes
        2. Search Note
        3. Add Note
        4. Modify Note
        5. Quit
        
        """)
    
    def run(self):
        ''' Display the menu and respond to choices '''
        
        while True:
            self.display_menu()
            
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))
                
    def show_notes(self, note=None):
        
        if len(self.notebook.notes) <= 0:
            print("NO Notes Found")
            
        if not note:
            note = self.notebook.notes
            
        for note in note:
            print(f"{note.id}: {note.tags} > {note.memo}")
        
    def search_notes(self):
        find = input("Search for: ")
        notes = self.notebook.search_note(find)
        self.show_notes(notes)
        
    def add_note(self):
        new_memo = input("Enter your new note: ")
        self.notebook.new_note(new_memo)
        print("Your new note is added")
    
    def modify_note(self):
        note_id = int(input("Enter note id: "))
        new_memo = input("Enter a memo: ")
        new_tag = input("Enter a tag: ")
        
        if new_memo:
            self.notebook.modify_note(note_id, new_memo)
            return True
        if new_tag:
            self.notebook.modify_tag(note_id, new_tag)
            return True
        return False
        print("\nYour notebook is updated")
         
    def quit_notebook(self):
        print("Thank you for using notebook today")
        sys.exit(0)
        
if __name__ == "__main__":
    Menu().run()


