from bardb import dbMgt
barcode = input()
pdt_name = input()
amt = input()
wt = input()
obj = dbMgt()
obj.insert_db(barcode,pdt_name,amt,wt)
obj.completeDb()
