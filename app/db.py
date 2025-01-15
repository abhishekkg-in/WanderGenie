import sqlite3


"""
Creating connection to DB(travel.db)
"""
def connect_db():
    conn = sqlite3.connect('travel.db')
    cursor = conn.cursor()
    return cursor



"""
Creating 'travel_knowledge_base_table' 
"""
def create_travel_knowledge_base_table():
    cursor = connect_db()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS travel_knowledge_base (
            id INTEGER PRIMARY KEY,
            destination TEXT,
            description TEXT,
            details TEXT,
            metadata TEXT,
            embeding TEXT
        )
    ''')








if __name__=="__main__":
    print(" Started ".center(100, "-"))
    # create_travel_knowledge_base_table()
    
