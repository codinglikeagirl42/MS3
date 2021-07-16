import sqlite3

# Initialise the database ane cursor objects here:

db = sqlite3.connect('game.db')
cursor = db.cursor()

# If i need to completely delete tables to redo, uncomment
#cursor.execute("DROP TABLE IF EXISTS mines")
#cursor.execute("DROP TABLE IF EXISTS board")

# Write SQL queries to create the 'mines' and 'board' tables:

sql_query = """
    CREATE TABLE IF NOT EXISTS mines 
    (mine_id INTEGER PRIMARY KEY, coordinates TEXT NOT NULL)
"""

cursor.execute(sql_query)

sql_query = """
    CREATE TABLE IF NOT EXISTS board
    (cell_id INTEGER PRIMARY KEY,  coordinates TEXT NOT NULL,
    surr_mines INT, guessed BOOL, mine_id INT)
"""

cursor.execute(sql_query)

# The game is played on a 10x10 grid, but part of the logic requires the program
# to check the squares surrounding a cell. Rather than code different logic for
# edge and corner cells, adding an empty layer around the grid helps!

# Rows X and Y, and columns 0 and 11 remain empty and unseen to the players.
board_rows = 'XABCDEFGHIJY'
board_columns = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# Use nested for loops to add rows to the 'board' table:

for row in board_rows:
    for column in board_columns:
        location = row + str(column)
        sql_query = f"INSERT INTO board (coordinates, guessed) VALUES ('{location}', False)"
        cursor.execute(sql_query)

db.commit()
db.close()
