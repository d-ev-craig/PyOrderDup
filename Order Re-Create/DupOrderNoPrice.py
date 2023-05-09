import csv as csv
import pandas as pds
import pyodbc as pyodbc

print("WE'RE WORKIN ON IT")

#filepath = r'<insert_file_path>BackOrder Items US.csv'
usdata = pds.read_table(r'<insert_file_path>\Group3.txt')
usdatastring=usdata["OrdNbr"].str.cat(sep=' ')
sql_usdata = f"select h.ordnbr as OldOrdNbr, h.CustId,h.User2, h.CustOrdNbr,so.ChainDisc,h.User3,h.User1,h.AuthNbr,h.TermsID,so.SiteID,so.Invtid, so.QtyOrd,so.QtyCloseShip,so.QtyOrd-so.QtyCloseShip as QtyToOrd from soheader h join soline so on so.OrdNbr = h.OrdNbr where so.QtyOrd<>so.QtyCloseShip and h.OrdNbr in ({usdatastring})"


#df = pds.read_csv(filepath, header=0,names=['Dup','NBN0','B0','BN0'])



consus = ''
kma = ''
username = ''
password = ''
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL SERVER};'
                          'SERVER='+ consus +';'
                         'Database='+ kma + ';'
                          'UID='+ username +';'
                          'PWD='+ password +';')
# 000BO = 'select h.OrdNbr,h.CustID into #000BO from soheader join soline l on h.OrdNbr = l.OrdNbr where l.SiteID in ('000','301') and l.QtyOrd <> l.QtyShip and h.OrdNbr in (select max(OrdNbr) from #USDataSet group by OrdNbr)'


df = pds.read_sql_query(sql =sql_usdata, con = cnxn)


df_obj = df.select_dtypes(['object'])
df[df_obj.columns] = df_obj.apply(lambda x: x.str.strip())

df.to_csv(path_or_buf=r'<insert_file_path>\Group3.csv', index=False)



PrevOrdNbr = ''
r = 0
c = 0
with open(r'<insert_file_path>\Group3format.csv','w', newline = '') as file:
    writer = csv.writer(file)
    for ind in df.index:
              
        
        OldOrdNbr = df.iat[r,c]
        CustID = df.iat[r,c+1]
        WebOrder = df.iat[r,c+2]
        CustOrdNbr = df.iat[r,c+3]
        ChainDisc = df.iat[r,c+4]
        User3 = df.iat[r,c+5]
        User1 = df.iat[r,c+6]
        AuthNbr = df.iat[r,c+7]
        TermsID = df.iat[r,c+8]
        SiteId = df.iat[r,c+9]
        InvtId = df.iat[r,c+10]
        QtyToOrd = df.iat[r,c+13]   
        
        
        
        if (PrevOrdNbr == OldOrdNbr):
            writer.writerow(["LEVEL1",InvtId,QtyToOrd,ChainDisc,SiteId])
        else:
            writer.writerow(["LEVEL0",CustID,CustOrdNbr,User1,TermsID,User3,OldOrdNbr,AuthNbr])
            writer.writerow(["LEVEL1",InvtId,QtyToOrd,ChainDisc,SiteId])
            PrevOrdNbr = OldOrdNbr
        r=r+1
print("Done")


#usdata.to_csv(path_or_buf=r'<insert_file_path>\NewOrders.csv', index=False)   
    
#OldOrdNbr.to_csv(path_or_buf=r'<insert_file_path>\OldOrders.csv', index=False)  
   

    



# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

