import sqlite3
conn = sqlite3.connect('testdb.db')
c = conn.cursor()

class db_mgt:

    def __init__(self):
        self.conn = sqlite3.connect('testdb.db')
        self.c = conn.cursor()

    def initiate(self,BARCODE_DB):

        check_table = (""" SELECT count(name) FROM sqlite_master WHERE type='table' AND name='BARCODE_DB' """)
        self.c.execute(check_table)
    
        if self.c.fetchone()[0]==1 :
            print('Table exists')
        else:
            create_table = (''' CREATE TABLE BARCODE_DB 
               ([Barcode] INTEGER PRIMARY KEY, [Product] text, [Price] integer, [Weight] integer)''')
            self.c.execute(create_table)

# barcode = input('Barcode :')
# pdt_name = input('Product Name: ')
# amt = input('Price : ')

    def barcode_check(barcode):
        typeVar = str(barcode)
        check_barcode = ("SELECT * from BARCODE_DB WHERE Barcode={}".format(typeVar))
        self.c.execute(check_barcode)
        codes = self.c.fetchall()
        print(codes)

    def insert_db(barcode,pdt_name,amt,wt):
        insert_data = (""" INSERT INTO BARCODE_DB (Barcode, Product, Price, Weight) VALUES (?, ?, ?, ?)""", (barcode, pdt_name, amt,wt))
        self.c.execute(insert_data)



obj = db_mgt()
obj.insert_db(barcode,pdt_name,amt,wt)
conn.commit()
print ('Data entered successfully')
conn.close()

