CREATE_AUTHOR_TABLE="""
    CREATE TABLE AUTHOR(
        id INTEGER PRIMARY KEY,
        name TEXT)
"""

CREATE_BOOKS_TABLE="""
    CREATE TABLE BOOKS(
        id INTEGER PRIMARY KEY,
        title TEXT,
        genre TEXT,
        author_id=INTEGER,
        copies INTEGER,
        FOREIGNKEY(author_id) REFERENCES AUTHOR(id) 
        )
"""

CREATE_BORROWER_TABLE="""
    CREATE TABLE BORROWER(
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT
        )
    """
    
CREATE_BORROW_RECORD_TABLE="""
    CREATE TABLE BORROW_RECORD(
        id INTEGER PRIMARY KEY,
        book_id INTEGER,
        borrower_id INTEGER,
        borrow_date TEXT,
        return_date TEXT
        FOREIGN KEY (book_id) REFERENCES BOOKS(id),
        FOREIGN KEY (borrower_id) REFERENCE BORROWER(id)
        )
    """
