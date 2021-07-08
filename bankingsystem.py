import os

os.system("cls")
name = input("ENTER USER'S NAME: ")
email = input("ENTER USER'S EMAIL: ")
phone = input("ENTER USER'S PHONE NO: ")
amount = int(input("ENTER AMOUNT: "))

def at_start():
    os.system("cls||clear")
    menu()    

def menu():
    flag = True
    while(flag):
        print("\nPRESS 1 TO ADD AMOUNT" "\nPRESS 2 TO WIDTHRAW AMOUNT" 
                "\nPRESS 3 FOR BALANCE INQUIRY" "\nPRESS 4 TO EXIT")
        option = input("ENTER YOUR CHOICE HERE: ")
        if(option == '1'):
            add_amount()
        elif(option == '2'):
            widthraw_amount()
        elif(option == '3'):
            balance_inquiry()
        elif(option == '4'):
            exit()
        else:
            print('PLEASE ENTER VALID OPTION!!!')
            os.system("cls||clear")
            menu()

def add_amount():
    os.system("cls||clear")
    global amount
    amount_to_add = int(input("ENTER THE AMOUNT TO ADDED: "))
    amount += amount_to_add
    print("AMOUNT ADDED SUCCESSFULLY!!!")
    print("CURRENT AMOUNT IS: ", amount)
    asking()

def widthraw_amount(): 

    os.system("cls||clear")
    global amount
    amount_to_widthraw = int(input("ENTER THE AMOUNT TO ADDED: "))
    amount -= amount_to_widthraw
    print("WIDTHRAWED AMOUNT IS: ", amount_to_widthraw)
    print("CURRENT AMOUNT IS: ", amount)
    asking()

def balance_inquiry():
    
    os.system("cls||clear")    
    global amount
    global name
    global email
    global phone
    print("NAME: ", name, "\nEMAIL: ", email, "\nPHONE NO: ", phone, "\nCURRENT AMOUNT: ", amount)
    asking()

def asking():    
    print("\nPRESS 1 TO GOTO MENU" "\nPRESS 2 TO EXIT")
    choice = input("ENTER YOUR CHOICE: ")
    if(choice == '1'):
        os.system("cls")
        menu()
    elif(choice == '2'):
        os.system("cls")
        exit()
    else:
        print('\nENTER VALID OPTION!')
        os.system("cls")
        asking()
        
at_start()
