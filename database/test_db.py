##This is exclusively for running tests on the database.

import os
import db
import unittest
import sqlite3 as sql

class TestDatabase(unittest.TestCase):
    def setUp(self):
        if (os.path.exists("db1.db")):
            os.remove("db1.db")
        if (os.path.exists("db2.db")):
            os.remove("db2.db")
        open("db1.db", "w").close()
        open("db2.db", "w").close()
    def test_createNewConnection(self):
        database = db.Database(":memory:")
        self.assertTrue(database.createNewConnection(":memory:"), sql.connect(":memory:"))
    
    def test_initializeWithDefaults(self):
        db1 = db.Database("db1.db")
        db2 = db.Database("db2.db")

        dbparamscheck = [
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
        db2.initializeWithDefaults("db2.db")
        con1 = db1.connection
        cur1 = con1.cursor()
        cur1.execute('''CREATE TABLE tables (gesturename text, gesturedata blob)''')
        cur1.executemany('''INSERT INTO tables values (? , ?)''', dbparamscheck)
        db1.saveCurrentState(db1.connection)

        ##Now to fetch parameters to make sure they are equal.
        for pair in dbparamscheck:
            self.assertEqual(db1.obtainParameter(pair[0], db1.connection), db2.obtainParameter(pair[0], db2.connection))
            

        db1.saveAndClose(db1.connection)
        db2.saveAndClose(db2.connection)
    def tearDown(self):
        os.remove("db1.db")
        os.remove("db2.db")

unittest.main()