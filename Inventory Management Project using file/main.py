import time
#reading inventory
fd = open('Inventory.txt', 'r')
products = fd.read().split('\n')
fd.close()

#taking user input
ui_username = input("Enter your Name: ")
ui_phone = input("Enter your phone no.: ")
ui_mail = input("Enter mail id:")
ui_prod_id = input("Enter product ID: ")
ui_prod_qn = input("Enter product quantity: ")
updated_prod_details = []

#Going through product details
for product in products:
    prod_details = product.split(',')
    #checking product exists or not
    if(prod_details[0] == ui_prod_id):
        #checking if we have enough product quantity
        if int(ui_prod_qn) <= int(prod_details[3]):
            print("Product Name     : ", prod_details[1])
            print("Price            : ", prod_details[2])
            print("Quantity         : ", ui_prod_qn)
            print("-" * 20)
            print("Billing Amount   : ", int(ui_prod_qn)*int(prod_details[2]))
            print("-"*20)
            prod_details[3] = str(int(prod_details[3]) - int(ui_prod_qn))
            #generating sales details
            fd = open("sales.txt", 'a')
            sales_detail = ui_username + "," + ui_phone + "," + ui_mail + "," + ui_prod_id + "," + ui_prod_qn + "," + str(int(ui_prod_qn)*int(prod_details[2])) + "," + time.ctime() + "\n"
            fd.write(sales_detail)
            fd.close()

        else:
            print(f"Sorry we have only {prod_details[3]} {prod_details[1]}")
            print("Would you like to purchase it")

            ch = input("y or n: ")
            #if we want to purchase entire inventory or not

            if ch=='y':
                print("Product Name     : ", prod_details[1])
                print("Price            : ", prod_details[2])
                print("Quantity         : ", prod_details[3])
                print("-" * 20)
                print("Billing Amount   : ", int(prod_details[3]) * int(prod_details[2]))
                print("-" * 20)
                fd = open("sales.txt", 'a')
                sales_detail = ui_username + "," + ui_phone + "," + ui_mail + "," + ui_prod_id + "," + ui_prod_qn + "," + str(
                    int(ui_prod_qn) * int(prod_details[2])) + "," + time.ctime() + "\n"
                fd.write(sales_detail)
                fd.close()
                prod_details[3] = '0'
            else:
                print("Thanks")
    #updating inventory list
    updated_prod_details.append(prod_details)

lst = []
#updating inventory string
for i in updated_prod_details:
    prod = i[0] + "," + i[1] + "," + i[2] + "," + i[3] + "\n"
    lst.append(prod)

lst[-1] = lst[-1][:-1]
#updating inventory file
fd = open("Inventory.txt", 'w')
for i in lst:
    fd.write(i)
fd.close()

print("-"*20)
print("Inventory Updated")