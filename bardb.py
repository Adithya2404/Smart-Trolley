import sqlite3

class dbMgt:
    def __init__(self):
        try:
            self.conn = sqlite3.connect('testdb.db')
            self.c = self.conn.cursor()
            check_table = (""" SELECT count(name) FROM sqlite_master WHERE type='table' AND name='BARCODE_DB' """)
            self.c.execute(check_table)   
            if self.c.fetchone()[0]==1 :
                print('Table exists')
            else:
                create_table = (''' CREATE TABLE BARCODE_DB 
                ([Barcode] INTEGER PRIMARY KEY, [Product] text, [Price] integer, [Weight] integer)''')
                self.c.execute(create_table)
        except:
            print("Error while initialising DB")

    def barcode_check(self, barcode):
        try:
            typeVar = str(barcode)
            check_barcode = ("SELECT * from BARCODE_DB WHERE Barcode={}".format(typeVar))
            self.c.execute(check_barcode)
            codes = self.c.fetchall()
            print(codes)
            return True
        except:
            return False

    def insert_db(self, barcode,pdt_name,amt,wt):
        try:
            insert_data = (""" INSERT INTO BARCODE_DB (Barcode, Product, Price, Weight) VALUES (?, ?, ?, ?)""", (barcode, pdt_name, amt,wt))
            self.c.execute(insert_data)
            return True
        except:
            return False
    
    def completeDb(self):
        try:
            self.conn.commit()
            self.conn.close()
            return True
        except:
            return False

obj = dbMgt()
obj.insert_db(1231,"britto",100,40)
obj.completeDb()