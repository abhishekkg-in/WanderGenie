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


"""
Fetch travel_knowledge_travel table data
"""
def fetch_travel_knowledge_base_table():
    cursor = connect_db()
    cursor.execute("SELECT id, description || ' ' || details || ' ' || metadata FROM travel_knowledge_base")
    rows = cursor.fetchall()
    return rows


"""
Update travel_knowledge_travel table with embedings
"""
def update_embeding(id, embedding):
    cursor = connect_db()
    cursor.execute("UPDATE travel_knowledge_base SET embedding = ? WHERE id = ?", (str(embedding), id))
    

"""
Fetch embedings of travel_knowledge_travel table
"""
def fetch_embedings():
    cursor = connect_db()
    cursor.execute("SELECT id, embedding FROM travel_knowledge_base")
    rows = cursor.fetchall()
    return rows



if __name__=="__main__":
    print(" Started ".center(100, "-"))
    create_travel_knowledge_base_table()

