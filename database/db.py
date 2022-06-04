import sqlite3 as sql
import os
import traceback
class Database:
	def __init__(self, connection):
		self.connection = self.createNewConnection(connection)
	#Creates a new connection given the path specified. This function is automatically invoked during new Object Creation. 
	def createNewConnection(self, dbpath):
		return sql.connect(dbpath)
	#Save any progress in the database. Returns True if successful, False if otherwise. 
	def saveCurrentState(self, connection):
		try:
			connection.commit()
			return True
		except: 
			return False
	#Save any progress in the database and then close. Returns True if successful, False if otherwise. 
	def saveAndClose(self, connection):
		try:
			if (self.saveCurrentState(connection)):
				connection.close()
				return True
		except: 
			print(traceback.format_exc())
			return False
	#Initializes the default database structure with the default gestures. You want to use this to reset back to factory settings. 
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
	##Function take in the parameter and does a table lookup to return the appropriate equality. If found, returns the equality. If not, returns False.
	def obtainParameter(self, parameters, connection):
		try:
			cur = connection.cursor()
			cur.execute("""SELECT gesturedata FROM tables WHERE gesturename=(?)""", (parameters,))
			try:
				result = cur.fetchone()[0]	
				return result
			except:
				return False

		except: 
			print(traceback.format_exc())

	##Function inserts a gesture. Returns True if successful, false if otherwise. 
	def insertGesture(self, gesturename, gestureparameters):
		try:
			cur = self.connection.cursor()
			cur.execute("INSERT INTO tables VALUES (?, ?)", (gesturename, gestureparameters))
			self.saveCurrentState(self.connection)
			return True
		except:
			print(traceback.format_exc())
			return False
	##Function deletes a gesture. Returns True if successful, False if otherwise. 	
	def deleteGesture(self, gesturename):
		try:
			cur = self.connection.cursor()
			cur.execute("""DELETE FROM tables WHERE gesturename=(?)""", (gesturename,))
			self.saveCurrentState(self.connection)
			return True
		except:
			return False

		

