import sqlite3 as sql
import os
import traceback
class Database:
	def __init__(self, connection):
		self.connection = self.createNewConnection(connection)
	
	def createNewConnection(self, dbpath):
		return sql.connect(dbpath)

	def saveCurrentState(self, connection):
		try:
			connection.commit()
			return True
		except: 
			return False

	def saveAndClose(self, connection):
		try:
			if (self.saveCurrentState(connection)):
				connection.close()
				return True
		except: 
			print(traceback.format_exc())
			return False

	def initializeWithDefaults(self, connectionpath):
		#THIS IS THE RESET FUNCTION. SHOULD ONLY BE DONE ON FIRST TIME INITIALIZATION. IT WILL ALSO CLOSE THE CONNECTION SO RELAUNCH WITH NEW CONNECTION AFTERWARDS.
		
		
		con = self.connection
		cur = con.cursor()
		cur.execute('''CREATE TABLE tables (gesturename text, gesturedata blob)''')
		argumentlist = [
			("is_left_thumb_raised", "y_pos_of_thumb_4_left < y_pos_of_thumb_3_left and y_pos_of_thumb_3_left < y_pos_of_thumb_2_left and y_pos_of_thumb_2_left < y_pos_of_thumb_1_left"),
			("is_right_thumb_raised", "y_pos_of_thumb_4_right < y_pos_of_thumb_3_right and y_pos_of_thumb_3_right < y_pos_of_thumb_2_right and y_pos_of_thumb_2_right < y_pos_of_thumb_1_right"),
			("is_left_index_out", "x_pos_of_index_4_left < x_pos_of_index_3_left and x_pos_of_index_3_left < x_pos_of_index_2_left and x_pos_of_index_2_left < x_pos_of_index_1_left"),
			("is_right_index_out", "x_pos_of_index_4_right > x_pos_of_index_3_right and x_pos_of_index_3_right > x_pos_of_index_2_right and x_pos_of_index_2_right > x_pos_of_index_1_right"),
			("is_thumb_closed", "y_pos_of_thumb_4_right > y_pos_of_thumb_3_right"),
			("is_right_index_closed", "x_pos_of_index_4_right < x_pos_of_index_2_right"),
			("is_left_index_closed", "x_pos_of_index_4_left > x_pos_of_index_2_left"),
			("is_right_thumb_closed", "y_pos_of_thumb_4_right > y_pos_of_thumb_3_right"),
			("is_left_thumb_closed", "y_pos_of_thumb_4_left > y_pos_of_thumb_3_left"),
			("is_right_index_closed", "x_pos_of_index_4_right < x_pos_of_index_2_right"),
			("is_left_index_closed", "x_pos_of_index_4_left > x_pos_of_index_2_left")
		]
		cur.executemany("INSERT into tables values (? , ?)", argumentlist)

		self.saveCurrentState(con)
		return True
	##Function take in the parameter and does a table lookup to return the appropriate equality.
	def obtainParameter(self, parameters, connection):
		try:
			cur = connection.cursor()
			cur.execute("""SELECT gesturedata FROM tables WHERE gesturename=(?)""", (parameters,))
			return cur.fetchone() #There should only be one result per gesture. 

		except: 
			print(traceback.format_exc())

		

