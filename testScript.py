from bardb import dg_mgt
barcode = input()
pdt_name = input()
amt = input()
wt = input()
obj = db_mgt()
obj.insert_db(barcode,pdt_name,amt,wt)
obj.completeDb()
