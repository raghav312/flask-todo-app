import sqlite3
DB_PATH = './note.db'

# For data storage we will be using sqlite3. Install it via 'pip install pysqlite3' in the virtualenv
# Open the database and Make a table  
def start():
    try:
        conn = sqlite3.connect('note.db')
        print ("Opened database successfully")

        conn.execute('CREATE TABLE IF NOT EXISTS notes( id TEXT , title TEXT, complete TEXT)')
        print ("Table created successfully")

        conn.close()
    except Exception as e:
        print(e)

# SQLite3 code to insert a row
def add_to_list(id,title):
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute( 'INSERT INTO notes (id,title,complete) VALUES (?,?,?)', (id,title,"False") )
        conn.commit()
        print('Commited note :)')
        conn.close()
        return {"id":id, "note": title , "complete": "False"}
    except Exception as e:
        print('Error: ' , e)
        return None

# SQLite3 code to fetch the table
def get_list():
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('SELECT * FROM notes')
        data = c.fetchall()
        conn.close()
        return { "count": len(data), "list": data }
    except Exception as e:
        print('Error: ' , e)
        return None

# SQLite3 code to update complete of a row
def update_note(status,id):
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('UPDATE notes SET complete=? WHERE id = ?', (status ,id))
        conn.commit()
        print('Committed note :)')
        conn.close()
        return {"id": id , "complete": status}
    except Exception as e:
        print('Error: ' , e)
        return None

# SQLite3 code to delete the table content
def del_list():
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('DELETE FROM notes')
        conn.close()
        return { "msg" : "List deleted" }
    except Exception as e:
        print('Error: ' , e)
        return None
    
# SQLite3 code to delete a single row
def del_note(id):
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('DELETE FROM notes WHERE id =?;' , [id])
        conn.commit()
        conn.close()
        return { "Deleted" : id }
    except Exception as e:
        print('Error: ' , e)
        return None