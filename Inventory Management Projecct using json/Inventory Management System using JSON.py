import json

fd = open("records.json", "r")                     # Opening file to update inventory
js = fd.read()                                     # In string format
fd.close()


record = json.loads(js)                            # In dictionary format

ex = True

while ex:
    print("\n------------------------------MENU--------------------------------\n")
    for key in record.keys():
        print(key, ":", record[key]["Name"], "|" , record[key]["Price"], "|" ,  record[key]["Qn"])
    print("\n------------------------------------------------------------------\n ")

    ui_pr = input("Enter Product ID: ")
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
    ask = input("Do you want to exit y/n?")
    if ask=="y":
        ex= False




