import qrcode

import xlrd
xlrd.xlsx.ensure_elementtree_imported(False, None)
xlrd.xlsx.Element_has_iter = True

dat=xlrd.open_workbook("Export Data.xlsx")
data=dat.sheet_by_index(0) #1st sheet
#file1= open("Summary.txt","w")

def get_customername(trackingid):
    file1= open("Summary.txt","a+")
    for row in range(100):
        for col in range(15):
            print(str(row)+","+str(col)+"\n")
            if trackingid in str(data.row_values(row)[col]):
                print("Find the code in : row "+str(row)+" and columm : "+str(col))
                break
        else:
            # Continue if the inner loop wasn't broken.
            continue
        # Inner loop was broken, break the outer.
        break
    name=str(data.row_values(row)[3])
    file1.writelines("\n"+"Name: "+name+" ")
    file1.close()
    return name

def get_customernumber(trackingid):
    file1= open("Summary.txt","a+")
    for row in range(100):
        for col in range(15):
            print(str(row)+","+str(col)+"\n")
            if trackingid in str(data.row_values(row)[col]):
                print("Find the code in : row "+str(row)+" and columm : "+str(col))
                break
        else:
            # Continue if the inner loop wasn't broken.
            continue
        # Inner loop was broken, break the outer.
        break
    tel=str(data.row_values(row)[4])
    file1.writelines("Tel: "+tel+" ")
    file1.close()
    return tel

def writetofile(note):
    file1= open("Summary.txt","a+")
    file1.writelines(note)
    file1.close()
    
def generateQrCode():
    for row in range(1,5):
       img = qrcode.make(str(data.row_values(row)[9])) 
       img.save((str(data.row_values(row)[9])+".jpg"))
                

generateQrCode()      
    

           

    




#SEARCHING---------------------------------------------------
# for row in range(100):
#     for col in range(15):
#         print(str(row)+","+str(col)+"\n")
#         if "NVTHMYODE001370261" in str(data.row_values(row)[col]):
#             print("Find the code in : row "+str(row)+" and columm : "+str(col))
#             break
#     else:
#         # Continue if the inner loop wasn't broken.
#         continue
#     # Inner loop was broken, break the outer.
#     break
   
                   
# print(str(data.row_values(row)[col]));
# print("Name : "+str(data.row_values(row)[3]+" Tel: "+str(data.row_values(row)[4])))

#file1.close()
