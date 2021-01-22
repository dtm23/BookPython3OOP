import datetime

#Store the next available id for all new notes

last_id = 0

class Note:
    """
    Represent a note in the notebook. Match against a
    string in searches and store tags for each note.

    """
    
    def __init__(self, memo, tags = ""):
        """
        initialize a note with a memo and optional
        space-separated tags, Automatically set the creation
        date and a unique id
        """
        x = datetime.date.today()
        self.memo = memo
        self.tags = tags
        self.create_date = x.strftime('%d %b %Y')
        global last_id # access to global attributes
        last_id += 1
        self.id = last_id
        
    def match(self, filter):
        '''Determine if this note matches the filter
        text. Return True if it matches, False otherwise.
        Search is case sensitive and matches both text and
        tags.'''
        
        return filter in self.memo or filter in self.tags

class Notebook:
    """Represent a collection of notes that
    can be tagged, modified and searched."""
    
    def __init__(self):
        '''
            Initialize a notebook with an empty list
        '''
        self.notes = [] # empty list
        
    def new_note(self, memo, tags=""):
        ''' create new note with a given memo and tags
            tags, can be blank'''
        self.notes.append(Note(memo,tags))
            
    def modify_note(self, note_id, new_memo):
        '''find a note by id and enter a new memo'''
        self.search_note(note_id).memo = new_memo
        
    def modify_tag(self, note_id, new_tags):
        '''find a note by id and enter a new memo'''
        self.search_note(note_id).tags = new_tags
                        
    def search_note(self, note_id):
        
        for note in self.notes:
            if note.id == note_id:
                return note
        
        return None
