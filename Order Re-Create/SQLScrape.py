import csv as csv
import pandas as pds
import pyodbc as pyodbc

print("WE'RE WORKIN ON IT")

#filepath = r'<insert_file_path>\BackOrder Items US.csv'
usdata = pds.read_table(r'<insert_file_path>\BackOrders000.txt')
usdatastring=usdata["OrdNbr"].str.cat(sep=' ')
sql_usdata = f"select h.OrdNbr as OldOrdNbr, h.CustID, h.CustOrdNbr,l.ChainDisc,h.user3,h.user1,h.authnbr,h.termsid, l.SiteID, l.invtid, l.QtyOrd, l.QtyShip, l.QtyOrd - l.QtyShip as QtyToOrd from soheader h left join soline l on l.OrdNbr = h.OrdNbr where l.QtyOrd <> l.QtyShip and h.OrdNbr in {usdatastring}"


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

df.to_csv(path_or_buf=r'<insert_file_path>\2465upload.csv', index=False)



PrevOrdNbr = ''
r = 0
c = 0
with open(r'<insert_file_path>2465Upload.csv','w', newline = '') as file:
    writer = csv.writer(file)
    for ind in df.index:
              
        
        OldOrdNbr = df.iat[r,c]
        CustID = df.iat[r,c+1]
        CustOrdNbr = df.iat[r,c+2]
        ChainDisc = df.iat[r,c+3]
        User3 = df.iat[r,c+4]
        User1 = df.iat[r,c+5]
        AuthNbr = df.iat[r,c+6]
        TermsID = df.iat[r,c+7]
        SiteId = df.iat[r,c+8]
        InvtId = df.iat[r,c+9]
        QtyToOrd = df.iat[r,c+12]
        
        if (PrevOrdNbr == OldOrdNbr):
            writer.writerow(["LEVEL1",InvtId,QtyToOrd,ChainDisc])
        else:
            writer.writerow(["LEVEL0",CustID,CustOrdNbr,User1,TermsID,User3,OldOrdNbr,AuthNbr])
            writer.writerow(["LEVEL1",InvtId,QtyToOrd,ChainDisc,SiteId])
            PrevOrdNbr = OldOrdNbr
        r=r+1
print("Done")

        
        
            
    
    

    



# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

