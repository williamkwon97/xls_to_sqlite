#!/usr/bin/env python
from db_table import db_table
import sys
#usage: specify the two arguments with "" to warp them when there is space in the arguments
#exp: ./lookup_agenda.py "location" "Coral Lounge"
def select():
	users = db_table("agenda", { "id": "integer PRIMARY KEY", 
	                            "date": "string NOT NULL", 
	                            "time_start": "string NOT NULL",
	                            "time_end": "string NOT NULL", 
	                           "title":"string NOT NULL",
	                           "location": "string",
	                           "description":"string"})

	column = sys.argv[1]
	val = sys.argv[2]
	rows = users.select(where = {column:val})
	for row in rows:
	    print(row)


	# In[32]:

	users.close()

if __name__ == '__main__':
    select()

# In[ ]:



