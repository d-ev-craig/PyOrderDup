import csv
from array import *
import pyodbc



def main():
    Kits = [['KitID', 'CmpnentID']]
    #Kit Validation
    def KitValidate(Invt):
        flag = "False"
        for x in Kits:
            if (x[0] == Invt):
                writer.writerow(["LEVEL1",x[1],x[2], DiscountCd])
                flag = "True"
        return flag




    #Database Connection Establishment
    server = ''
    database = ''
    username = ''
    password = ''
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL SERVER};'
                          'SERVER=' + server + ';'
                          'Database=' + database + ';'
                          'UID=' + username + ';'
                          'PWD=' + password + ';')
    cursor = cnxn.cursor()
    cursor.execute("select KitID, CmpnentID, CmpnentQty from Component order by KitID")
    resultset =  cursor.fetchall()
    for rw in resultset:
        Kits.append([rw.KitID.lstrip().rstrip(), rw.CmpnentID.lstrip().rstrip(), rw.CmpnentQty])

    UniqueIdent = ''
    LEVEL = ''
    #input file
    with open('MISSING_USA.csv', newline='') as csvfile:
        data = list(csv.reader(csvfile))

    #output file
    with open('MISSING_USA_Final.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        #iteration of data rows
        for row in data[1:]:
            #Customer ID
            if "4SEASO" in row[0]:
                CustomerID = "4SEASO"
            else:
                CustomerID = row[0].lstrip('0123456789')
            #Part Number
            InvtID = row[1]
            #Quantity Ordered
            QtyOrd = row[2]
            #Assembly
            Assembly = row[3]
            #Terms
            Terms = row[4]
            #Program Code
            ProgramCd = row[5]
            #Project ID
            ProjectID = row[6]
            #Discount Code
            DiscountCd = row[7]
            if UniqueIdent != row[0]:
                UniqueIdent = row[0]
                writer.writerow(["LEVEL1","FREIGHT - WHOLEGOODS", 1])
                
                writer.writerow("LEVEL0","WSO",CustomerID,Terms,ProgramCd,ProjectID)
                
                if (KitValidate(InvtID) == "False"):
                    writer.writerow(["LEVEL1", InvtID, QtyOrd, DiscountCd])
                    
            else:
                if (KitValidate(InvtID) == "False"):
                    writer.writerow(["LEVEL1",InvtID,QtyOrd,DiscountCd])
        writer.writerow(["LEVEL1","FREIGHT - WHOLEGOODS", 1])
        
main()
