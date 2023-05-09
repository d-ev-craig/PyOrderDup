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
    with open('USAK9DM.csv', newline='') as csvfile:
        data = list(csv.reader(csvfile))

    #output file
    with open('USAK9DM_Final.csv', 'w', newline='') as file:
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
            #Terms
            Terms = row[3]
            #Program Code
            ProgramCd = row[4]
            #ProjectID
            #ProjectID = row[5]
            #Discount Code
            DiscountCd = row[5]
            #Assembly Checkbox
            #AssemblyCB = row[7]
##            if AssemblyCB == "Y":
##                Assembly = "1"
##            else:
##                Assembly = "0"
            if UniqueIdent != row[0]:
                UniqueIdent = row[0]
                writer.writerow(["LEVEL1","FREIGHT - WHOLEGOODS", 1])
                
                writer.writerow(["LEVEL0","WSO",CustomerID,Terms,ProgramCd])
                
                if (KitValidate(InvtID) == "False"):
                    writer.writerow(["LEVEL1", InvtID, QtyOrd, DiscountCd])
                    
            else:
                if (KitValidate(InvtID) == "False"):
                    writer.writerow(["LEVEL1",InvtID,QtyOrd,DiscountCd])
        writer.writerow(["LEVEL1","FREIGHT - WHOLEGOODS", 1])

if __name__ == "__main__":
    main()
