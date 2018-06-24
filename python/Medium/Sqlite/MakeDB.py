import sqlite3 #import the module
conn = sqlite3.connect('lvls.db') #Make the connection
xp.lvlC.execute("""CREATE TABLE table_name ( #Make the tabke
				text_name text, #A sample text
				number_ integer, #number is a type, so u need a different char somewhere

				)""")