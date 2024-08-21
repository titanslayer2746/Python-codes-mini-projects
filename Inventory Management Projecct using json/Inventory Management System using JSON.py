#importing the libraries

import json
import time

# Loading the records from JSON to string
fd = open("records.json", "r")                     # Opening file to update inventory
js = fd.read()                                     # In string format
fd.close()

#converting string records to JSON/dictionaries
record = json.loads(js)                            # In dictionary format

#Displaying Menu
print("\n------------------------------MENU--------------------------------\n")
for key in record.keys():
    print(key, ":", record[key]["Name"], "|", record[key]["Price"], "|",  record[key]["Qn"])
print("\n------------------------------------------------------------------\n ")

#Taking User Input about the Purchase and User details
ui_name = input("Enter your name         : ")
ui_mail = input("Enter your MAIL ID      : ")
ui_ph = input("Enter your phone number : ")
ui_pr = str(input("Enter Product ID: "))
ui_qn = int(input("Enter Quantity: "))

#If we are having equal or more quantity than user wants
if record[ui_pr]['Qn'] >= ui_qn:

    #Displaying Purchase Details
    print("                                BILL\n")
    print("Name                   : ", record[ui_pr]["Name"])
    print("Price (Rs)             : ", record[ui_pr]["Price"], "Rs")
    print("Quantity               : ", ui_qn)
    print("------------------------------------------------------------------")
    print("Billing Amount         : ",record[ui_pr]["Price"]*ui_qn, "Rs")
    print("------------------------------------------------------------------")

    # Updating inventory quantity
    record[ui_pr]["Qn"] = record[ui_pr]["Qn"] - ui_qn

    #Generating sales structure in CSV
    sales = ui_name + "," + ui_mail + "," + ui_ph + "," + ui_pr + "," + record[ui_pr]['Name'] + "," + str(ui_qn) + "," + str(record[ui_pr]['Price']) + "," + str(ui_qn*record[ui_pr]['Price']) + "," + time.ctime()

    # Saving records in sales file
    fd = open("sales.csv", "a")
    fd.write(sales)
    fd.close()

#If we are not having enough quantity
else:
    #Displaying info about the quantity
    print("Sorry we are not having enough quantity in our inventory.")
    print("We are only having ", record[ui_pr]['Qn']," quantity.")
    print("------------------------------------------------------------------")

    #if user wants to purchase whole quantity of that product
    ch = input("Press Y/y to purchase: ")
    if ch == 'y' or ch == 'Y':
        # Displaying Purchase Details
        print("                                BILL\n")
        print("Name                   : ", record[ui_pr]["Name"])
        print("Price (Rs)             : ", record[ui_pr]["Price"], "Rs")
        print("Quantity               : ", record[ui_pr]['Qn'])
        print("------------------------------------------------------------------")
        print("Billing Amount         : ",record[ui_pr]["Price"]*record[ui_pr]['Qn'], "Rs")
        print("------------------------------------------------------------------")

        # Generating sales structure in CSV
        sales = '1' + "," + ui_name + "," + ui_mail + "," + ui_ph + "," + ui_pr + "," + record[ui_pr]['Name'] + "," + str(record[ui_pr]['Qn']) + "," + str(record[ui_pr]['Price']) + "," + str(record[ui_pr]['Qn']*record[ui_pr]['Price'])+ "," + time.ctime()

        # Saving records in sales file
        fd = open("sales.csv", "a")
        fd.write(sales)
        fd.close()

        #Udpating records dictionary
        record[ui_pr]['Qn'] = 0
    #If user pressed other than y/Y
    else:
        print("Thanks!!")

#converting dictionary to string
js = json.dumps(record)

#Saving records in JSON file
fd = open("records.json", 'w')
fd.write(js)
fd.close()

print("---------------------------------------------------------------")
print("Thanks for your order, Inventory Updated")
print("---------------------------------------------------------------")






