# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 13:50:10 2022

@author: DCraig
"""

import csv as csv
import pandas as pds
import pyodbc as pyodbc
import numpy as np

print("WE'RE WORKIN ON IT")

# Load and clean orders that need duplicates

errordf=pds.read_excel(r'<insert_file_path>\List of Orders without Duplicates.xlsx')


errordf_obj = errordf.select_dtypes(['object'])
errordf[errordf_obj.columns] = errordf_obj.apply(lambda x: x.str.strip())

errordf = errordf_obj

# Load master list to parse lines from

df=pds.read_excel(r'<insert_file_path>\USAll.xlsx')

# Errordf left join df - this should pull all lines from df that contain the same OrdNbr that is contained inside errordf
Lines=pds.merge(errordf,df,on='OrdNbr',how="left")
 

Lines.to_excel(excel_writer=r'<insert_file_path>\ErrorLines.xlsx', index=False)

Lines = pds.read_excel(r'<insert_file_path>\ErrorLines.xlsx')


# This code was previously used to pull lines based on being null/nan values, only useful to see how to handle null/nan values
# =============================================================================
# 
#Retry = Lines[Lines['CustId'].notna()]
# 
# LookAgain = Lines[Lines['CustId'].isna()]
# 
# UniqueLA = np.unique(LookAgain.OrdNbr)
# 
# Retry = Retry.fillna('')
# 
# Retry[0:4]
# 
# =============================================================================
# =============================================================================
# 
# for ord in errordf['OrdNbr']:
# 
#     x=4
# 
#     OrdNbr = errordf.iat[x,0]
#     
#     OrdNbr = 'OE029144'
# 
#     
#     try:
#         df.query('0 == @OrdNbr')
#     except KeyError:
#         f = open(r'L:\)
#         f.close()
# 
#     x=x+1
#         
# ============================================================================
PrevOrdNbr = ''
r = 0
c = 0
with open(r'<insert_file_path>\USErrorFormat.csv','w', newline = '') as file:
    writer = csv.writer(file)
    for ind in Lines.index:
        
        
        
        OldOrdNbr = Lines.iat[r,c]
        CustID = Lines.iat[r,c+1]
        WebOrder = Lines.iat[r,c+2]
        CustOrdNbr = Lines.iat[r,c+3]
        ChainDisc = Lines.iat[r,c+4]
        User3 = Lines.iat[r,c+5]
        User1 = Lines.iat[r,c+6]
        AuthNbr = Lines.iat[r,c+7]
        TermsID = Lines.iat[r,c+8]
        SiteId = Lines.iat[r,c+9]
        InvtId = Lines.iat[r,c+10]
        QtyToOrd = Lines.iat[r,c+13]   
         
        
# Look at adding TaskID & ProjectID
        
        
        
        if (PrevOrdNbr == OldOrdNbr):
            writer.writerow(["LEVEL1",InvtId,QtyToOrd,ChainDisc,SiteId])
        else:
            writer.writerow(["LEVEL0",CustID,CustOrdNbr,User1,TermsID,User3,OldOrdNbr,AuthNbr])
            writer.writerow(["LEVEL1",InvtId,QtyToOrd,ChainDisc,SiteId])
            PrevOrdNbr = OldOrdNbr
        r=r+1
print("Done")



#errorstring=errordf["OrdNbr"].str.cat(sep=' ')





# =============================================================================
# 
# consus = ''
# kma = ''
# username = ''
# password = ''
# cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL SERVER};'
#                           'SERVER='+ consus +';'
#                          'Database='+ kma + ';'
#                           'UID='+ username +';'
#                           'PWD='+ password +';')
# =============================================================================
# 000BO = 'select h.OrdNbr,h.CustID into #000BO from soheader join soline l on h.OrdNbr = l.OrdNbr where l.SiteID in ('000','301') and l.QtyOrd <> l.QtyShip and h.OrdNbr in (select max(OrdNbr) from #USDataSet group by OrdNbr)'
# =============================================================================
# 
# 
# errorstringdf = pds.read_sql_query(sql =sql_errordata, con = cnxn)
# 
# 
# =============================================================================
