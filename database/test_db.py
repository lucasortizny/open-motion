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
        if (os.path.exists("insertiontest.db")):
            os.remove("insertiontest.db")
        if (os.path.exists("deletiontest.db")):
            os.remove("deletiontest.db")
        open("db1.db", "w").close()
        open("db2.db", "w").close()
        open("insertiontest.db", "w").close()
        open("deletiontest.db", "w").close()
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
    def test_insertGesture(self):
        insertdb = db.Database("insertiontest.db")
        insertdb.initializeWithDefaults("insertiontest.db")
        insertdb.insertGesture("something1", "something2")
        response = insertdb.obtainParameter("something1", insertdb.connection)
        insertdb.saveAndClose(insertdb.connection)
        self.assertEqual(response, "something2")
    def test_deleteGesture(self):
        deletedb = db.Database("deletiontest.db")
        deletedb.initializeWithDefaults(deletedb.connection)
        deletedb.insertGesture("something1", "something2")
        deletedb.deleteGesture("something1")
        deletedb.saveCurrentState(deletedb.connection)
        testedvalue = deletedb.obtainParameter("something1", deletedb.connection)
        deletedb.saveAndClose(deletedb.connection)
        if (testedvalue != False):
            self.fail("The deleted value is still in the database.")
    
    def tearDown(self):
        os.remove("db1.db")
        os.remove("db2.db")
        os.remove("insertiontest.db")
        os.remove("deletiontest.db")

unittest.main()