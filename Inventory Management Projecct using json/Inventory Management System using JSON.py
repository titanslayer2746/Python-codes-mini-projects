import json

record = {1001 : {"Name" : "5 Star"         , "Price": 10  , "Qn": 200},
          1002 : {"Name" : "BarOne"         , "Price": 20  , "Qn": 100},
          1003 : {"Name" : "Candy"          , "Price": 2   , "Qn": 1000},
          1004 : {"Name" : "Chocolate Cake" , "Price": 550 , "Qn": 8},
          1005 : {"Name" : "Blueberry Cake" , "Price": 650 , "Qn": 5}
         }

print("\n------------------------------MENU--------------------------------\n")
for key in record.keys():
    print(key, ":", record[key]["Name"], "|" , record[key]["Price"], "|" ,  record[key]["Qn"])
print("\n------------------------------------------------------------------\n ")

ui_pr = int(input("Enter Product ID: "))
ui_qn = int(input("Enter Quantity: "))

record[ui_pr]["Qn"] = record[ui_pr]["Qn"] - ui_qn

print("                                BILL\n")

print("Name                   : ", record[ui_pr]["Name"])
print("Price (Rs)             : ", record[ui_pr]["Price"], "Rs")
print("Quantity               : ", ui_qn)

print("------------------------------------------------------------------")
print("Billing Amount         : ",record[ui_pr]["Price"]*ui_qn, "Rs")
print("------------------------------------------------------------------")


js = json.dumps(record)
fd = open("records.json", 'w')
fd.write(js)
fd.close()