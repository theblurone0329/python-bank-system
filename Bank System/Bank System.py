import datetime
import os

#based on merge sort algorithm that divides problem into sub-problems that solving and merging the solution together
def merge_sort(arr):
    left = []
    right = []
    if len(arr) >  1:
        mid = len(arr) // 2
        left = arr[0: mid] #separate list from items starting index to middle index 
        right = arr[mid: -1] #separate list from items from middle index to end index
        merge_sort(left) #calling function to further separate the list until one  item remains in a single list
        merge_sort(right)
        i = 0
        j = 0
        k = 0
        #Following processes help determine which list (left or right) the items go to after comparison
        while i < len(right) and j < len(left):
            if int(left[j][1]) > int(right[i][1]): #check if first item of left list is larger than first item of right list
                arr[k] = right[i] #inserting larger item to list 
                i += 1
                                
            elif int(right[i][1]) > int(left[j][1]): #check if first item of right list is larger than first item of left list
                arr[k] = left[j] #inserting largere item to list
                j += 1
            k += 1
                            
        while i < len(right): #will run this validation when length of right list is equal to the "i" value
            arr[k] = right[i]
            i += 1
            k += 1

        while j < len(left): #will run this validation when length of right list is equal to the "i" value
            arr[k] = left[j]
            j += 1
            k += 1

#Opens client credentials database to sort 
#Then calls merge_sort function to sort
def client_sorting():
    with open('client_credentials.txt', 'r') as file:
        clients_info = file.read().split(", ")
        file.close()

    lists = []

    while True:
        if len(clients_info) != 0:
            lists.append(clients_info[0:13])
            del clients_info[0:13]
        else:             
            with open('client_credentials.txt', 'w') as file:
                merge_sort(lists)
                for i in lists:
                    for j in i:
                        file.write("%s, " % str(j))
                file.close()
            break

#Opens staff credentials database to sort 
#Then calls merge_sort function to sort
def staff_sorting():
    with open('staff_credentials.txt', 'r') as file:
        staff_info = file.read().split(", ")
        file.close()

    lists = []

    while True:
        if len(staff_info) != 0:
            lists.append(staff_info[0:12])
            del staff_info[0:12]
        else:
            with open('staff_credentials.txt', 'w') as file:
                merge_sort(lists)
                for i in lists:
                    for j in i:
                        file.write("%s, " % str(j))
                file.close()
            break

#Opens admin credentials database to sort 
#Then calls merge_sort function to sort
def admin_sorting():
    with open('admin_credentials.txt', 'r') as file:
        admin_info = file.read().split(", ")
        file.close()

    lists = []

    while True:
        if len(admin_info) != 0:
            lists.append(admin_info[0:11])
            del admin_info[0:11]
        else:
            with open('staff_credentials.txt', 'w') as file:
                merge_sort(lists)
                for i in lists:
                    for j in i:
                        file.write("%s, " % str(j))
                file.close()
            break

#This function will be accessed by admin and staffs
#To create new accounts for clients
#Appending all data from registration form to list then appending it to data file
#Client ID and default password given by account creator and stored in separate data file
def new_acc_client(user_id):
    print("Create New Client Account Menu")
    user = list()
    idpw_list = list()
    with open('staff_idpw_list.txt', 'r') as file:
        idpw = file.read().split(", ")
    with open('admin_idpw_list.txt', 'r') as file:
        admin_idpw = file.read().split(", ")
    if user_id in idpw:
        with open('staff_credentials.txt', 'r') as file:
            item = file.read().split(", ")
            file.close()
        if user_id in item:
            name = item[item.index(user_id) + 2]
    elif user_id in admin_idpw:
        with open('admin_credentials.txt', 'r') as file:
            item = file.read().split(", ")
            file.close()
        if user_id in item:
            name = item[item.index(user_id) + 2]
            
    user.append(f"\nAccount Creator: {name}")
    while True: 
        yn = input("Cancel Process? (Y/N)\nAnswer: ")
        if yn == "Y":
            print('Returning to menu...')
            with open('staff_credentials.txt', 'r') as file:
                staff = file.read().split(", ")
                file.close()
                if user_id in staff:
                    staff_menu(user_id)
                else:
                    super_user_menu(user_id)
        elif yn == "N":
            print("Please fill in all information ACCURATELY.")
            user_pref_salut = input("Preferred Salutation of User: ")
            user.append(user_pref_salut)
            user_first_name = input("First Name: ")
            user.append(user_first_name)
            user_last_name = input("Last Name: ")
            user.append(user_last_name)
            while True:
                user_age = input("Age: ")
                user.append(user_age)
                if len(user_age) == 0:
                    print("Please fill in all columns")
                    continue
                if int(user_age) < 18:
                    print("Company Policy: Ages under 18 are unable to create a Bank Account.")
                    continue
                else: 
                    while True:
                        user_nation = input("Nationality: ")
                        user.append(user_nation)
                        #Registration form for Non-Malaysian clients
                        if user_nation != "Malaysian":
                            while True: 
                                user_passport = input("Passport No.: ")
                                if len(user_passport) == 0:
                                    print("Please fill in all blanks")
                                    continue
                                elif len(user_passport) < 6 or len(user_passport) > 11:
                                    print("Invalid Passport Number. Please try again...")
                                    continue
                                else:
                                    with open('client_credentials.txt', 'r') as file:
                                        info = file.read().split(", ")
                                        file.close()
                                    if user_passport in info:
                                        print("Duplicate Passport Number Found. Please try again...")
                                        continue
                                    else:
                                        user.append(user_passport)
                                        while True: 
                                            user_dob = input("Date of Birth (DD/MM/YYYY): ")
                                            if len(user_dob) == 0:
                                                print("Please fill in all blanks")
                                                continue
                                            else:
                                                tenth_days = int(user_dob[0]) * 10
                                                one_days = int(user_dob[1])
                                                tenth_months = int(user_dob[3]) * 10
                                                one_months = int(user_dob[4])
                                                month = tenth_months + one_months
                                                days = tenth_days + one_days
                                                if days > 31 or days < 0:
                                                    print("Invalid Day input")
                                                    continue
                                                elif month > 12 or month < 0:
                                                    print("Invalid Month input")
                                                    continue
                                                else:
                                                    user.append(user_dob)
                                                    while True:
                                                        user_contact = input("Telephone No.: ")
                                                        if len(user_contact) == 0:
                                                            print("Please fill in all blanks")
                                                            continue
                                                        elif len(user_contact) > 11 and len(user_contact) < 9:
                                                            print("Invalid Phone Number. Please try again...")
                                                            continue
                                                        else:
                                                            user.append(user_contact)
                                                            user_address = input("Address (if none: N/A): ")
                                                            user.append(user_address)
                                                            while True:
                                                                user_occu = input("Occupation: ")
                                                                if len(user_occu) == 0:
                                                                    print("Please fill in all blanks")
                                                                    continue
                                                                else:
                                                                    user.append(user_occu)
                                                                    while True:
                                                                        user_acc_type = input("Account Type: ")
                                                                        if len(user_acc_type) == 0:
                                                                            print("Please fill in all blanks")
                                                                            continue
                                                                        elif user_acc_type != "Savings" and user_acc_type != "Current":
                                                                            print("Invalid Account Type. Please try again...")
                                                                            continue
                                                                        else:
                                                                            user.append(user_acc_type)
                                                                            with open('client_credentials.txt', 'r') as file:
                                                                                info = file.read().split(", ")  
                                                                                file.close()
                                                                            if len(info) == 0:
                                                                                user_ID = 11010111
                                                                            else:             
                                                                                acc = info[27]
                                                                                while True: 
                                                                                    if int(acc) < 22221111 and int(acc) > 11010111:
                                                                                        user_ID = int(acc) + 4
                                                                                        if str(user_ID) in info:
                                                                                            acc = user_ID
                                                                                            continue
                                                                                        else:
                                                                                            break
                                                                                    elif int(acc) < 44443333 and int(acc) > 22221112:
                                                                                        user_ID = int(acc) + 7
                                                                                        if str(user_ID) in info:
                                                                                            acc = user_ID
                                                                                            continue
                                                                                        else:
                                                                                            break   
                                                                                    elif int(acc) > 34443333 and int(acc) < 44443333:
                                                                                        user_ID = int(acc) - 4
                                                                                        if str(user_ID) in info:
                                                                                            acc = user_ID
                                                                                            continue
                                                                                        else:
                                                                                            break
                                                                                    elif int(acc) > 11010111 and int(acc) < 34443333:
                                                                                        user_ID = int(acc) - 2
                                                                                        if str(user_ID) in info:
                                                                                            acc = user_ID
                                                                                            continue
                                                                                        else:
                                                                                            break
                                                                            print(f"Account Number: {user_ID}")
                                                                            idpw_list.append(user_ID)
                                                                            user.insert(1, user_ID)
                                                                            user_pw = input("Password: ")
                                                                            idpw_list.append(user_pw)
                                                                            while True: 
                                                                                user_balance = input("Account Balance: ")
                                                                                if user_acc_type == 'Savings':
                                                                                    if float(user_balance) < 100.00:
                                                                                        print("Invalid Minimum Amount for Savings Account. Please try again...")
                                                                                        continue
                                                                                    else:
                                                                                        break
                                                                                else:
                                                                                    if float(user_balance) < 500.00:
                                                                                        print("Invalid Minimum Amount for Currents Account. Please try again...")
                                                                                        continue
                                                                                    else:
                                                                                        break
                                                                            break
                                                                    break
                                                            break
                                                    break
                                        break
                            break
                        #Registration form for Malaysian clients
                        else: 
                            while True: 
                                user_IC_num = input("IC No.: ")
                                if len(user_IC_num) == 0:
                                    print("Please fill in all blanks")
                                    continue
                                elif len(user_IC_num) != 12:
                                    print("Invalid IC number. Please try again")
                                    continue
                                else:
                                    with open('client_credentials.txt', 'r') as file:
                                        info = file.read().split(", ")
                                        file.close()
                                    if user_IC_num in info:
                                        print("Duplicate IC Number Found. Please try again...")
                                        continue
                                    else:
                                        user.append(user_IC_num)
                                        while True: 
                                            user_dob = input("Date of Birth (DD/MM/YYYY): ")
                                            if len(user_dob) == 0:
                                                print("Please fill in all blanks")
                                                continue
                                            else:
                                                tenth_days = int(user_dob[0]) * 10
                                                one_days = int(user_dob[1])
                                                tenth_months = int(user_dob[3]) * 10
                                                one_months = int(user_dob[4])
                                                month = tenth_months + one_months
                                                days = tenth_days + one_days
                                                if days > 31 or days < 0:
                                                    print("Invalid Day input")
                                                    continue
                                                elif month > 12 or month < 0:
                                                    print("Invalid Month input")
                                                    continue
                                                else:
                                                    user.append(user_dob)
                                                    while True:
                                                        user_contact = input("Telephone No.: ")
                                                        if len(user_contact) == 0:
                                                            print("Please fill in all blanks")
                                                            continue
                                                        elif len(user_contact) > 11 or len(user_contact) < 9:
                                                            print("Invalid Phone Number. Please try again...")
                                                            continue
                                                        else: 
                                                            user.append(user_contact)
                                                            user_address = input("Address (if none: N/A): ")
                                                            user.append(user_address)
                                                            user_occu = input("Occupation: ")
                                                            user.append(user_occu)
                                                            while True:
                                                                user_acc_type = input("Account Type: ")
                                                                if len(user_acc_type) == 0:
                                                                    print("Please fill in all blanks")
                                                                    continue
                                                                elif user_acc_type != "Savings" and user_acc_type != "Current":
                                                                    print("Invalid Account Type. Please try again...")
                                                                    continue
                                                                else:
                                                                    user.append(user_acc_type)
                                                                    with open('client_credentials.txt', 'r') as file:
                                                                        info = file.read().split(", ")
                                                                        file.close()
                                                                    if len(info) == 0:
                                                                        user_ID = 10000000
                                                                    else:    
                                                                        acc = info[27]
                                                                        while True: 
                                                                            if int(acc) < 22221111 and int(acc) > 1101011:
                                                                                user_ID = int(acc) + 4
                                                                                if str(user_ID) in info:
                                                                                    acc = user_ID
                                                                                    continue
                                                                                else:
                                                                                    break
                                                                            elif int(acc) < 44443333 and int(acc) > 22221111:
                                                                                user_ID = int(acc) + 7
                                                                                if str(user_ID) in info:
                                                                                    acc = user_ID
                                                                                    continue
                                                                                else:
                                                                                    break
                                                                            elif int(acc) > 22221111 and int(acc) < 44443333:
                                                                                user_ID = int(acc) - 4
                                                                                if str(user_ID) in info:
                                                                                    acc = user_ID
                                                                                    continue
                                                                                else:
                                                                                    break
                                                                            elif int(acc) > 1101011 and int(acc) < 22221111:
                                                                                user_ID = int(acc) - 2
                                                                                if str(user_ID) in info:
                                                                                    acc = user_ID
                                                                                    continue
                                                                                else:
                                                                                    break
                                                                    print(f"Account Number: {user_ID}")
                                                                    idpw_list.append(user_ID)
                                                                    user.insert(1, user_ID)
                                                                    user_pw = input("Password: ")
                                                                    idpw_list.append(user_pw)
                                                                    while True: 
                                                                        user_balance = input("Account Balance: ")
                                                                        if len(user_balance) == 0:
                                                                            print("Please fill in all blanks")
                                                                            continue
                                                                        elif user_acc_type == 'Savings':
                                                                            if float(user_balance) < 100.00:
                                                                                print("Invalid Minimum Amount for Savings Account. Please try again...")
                                                                                continue
                                                                            else:
                                                                                break
                                                                        else:
                                                                            if float(user_balance) < 500.00:
                                                                                print("Invalid Minimum Amount for Currents Account. Please try again...")
                                                                                continue
                                                                            else:
                                                                                break
                                                                    break
                                                            break
                                                    break
                                        break
                            break
                    break
        else: 
            print("Invalid Response. Please try again...")
            continue
        break
    #open credentials, id & password text file databases to store information on new client
    #create balance database file for each client
    with open('client_credentials.txt', 'r') as file:
        info = file.read().split(", ")
        file.close()
    user.reverse()
    for i in user:
        info.insert(0, i)
    with open('client_credentials.txt', 'w') as file:
        for item in info:
            file.write("%s, " % item)
        file.close()
    for idpw in idpw_list:
        with open('client_idpw_list.txt', 'a') as file:
            file.write("%s, " % idpw)
            file.close()
    with open(f'Balance/{user_ID}_balance.txt', 'w') as file:
        file.write("%s, " % user_balance)
        file.close()   

    dt = datetime.datetime.now()
    day = dt.strftime("%d")
    month = dt.strftime("%m")
    year = dt.strftime("%Y")
    curr_time = dt.strftime("%X")
    dt_now = f"{day}/{month}/{year} {curr_time}"  
    #Create statement of Account file for each new user
    with open(f"SOA/{user_ID}_SOA.txt", 'w') as file:
        file.write(f"Client Name: {user_first_name}\nAccount No.: {user_ID}\nAccount Type: {user_acc_type}\nDate & Time: {dt_now}\n")
        file.write("\n-------------------------------------------------------\n")
        file.write(f"Original/Carried Balance:                    |RM{user_balance}|\n")
        file.write("-------------------------------------------------------")
        file.close()
        print("Client Account Created Successfully\n")
        
    client_sorting()

    with open('staff_credentials.txt', 'r') as file:
        staff = file.read().split(", ")
        if user_id in staff:
            staff_menu(user_id)
        else:
            super_user_menu(user_id)

#This function will only be accessed by admnistrators and managers
#To create new account for new staff
#Appending all data from registration form to list then appending it to data file
#Staff ID and default password given by account creator and stored in separate data file
def new_acc_staff(user_id):
    print("Create Staff Account Menu")
    staff = list()
    idpw_list = list()
    with open('staff_idpw_list.txt', 'r') as file:
        idpw = file.read().split(", ")
        file.close()
    with open('admin_idpw_list.txt', 'r') as file:
        admin_idpw = file.read().split(", ")
        file.close()
    if user_id in idpw:
        with open('staff_credentials.txt', 'r') as file:
            item = file.read().split(", ")
            file.close()
        if user_id in item:
            name = item[item.index(user_id) + 2]
    elif user_id in admin_idpw:
        with open('admin_credentials.txt', 'r') as file:
            item = file.read().split(", ")
            file.close()
        if user_id in item:
            name = item[item.index(user_id) + 2]
    while True:
        yn = input("Cancel Process? (Y/N)\nAnswer: ")
        if yn == "Y":
            print('Returning to menu...')
            with open('staff_credentials.txt', 'r') as file:
                staff = file.read().split(", ")
                file.close()
                if user_id in staff:
                    staff_menu(user_id)
                else:
                    super_user_menu(user_id)
        elif yn == "N":
            staff.append(f"\nAccount Creator: {name}")
            print("Please fill in all information ACCURATELY.")
            staff_pref_salut = input("Preferred Salutation of User: ")
            staff.append(staff_pref_salut)
            staff_first_name = input("First Name: ")
            staff.append(staff_first_name)
            staff_last_name = input("Last Name: ")
            staff.append(staff_last_name)
            staff_age = input("Age: ")
            if len(staff_age) == 0:
                print("Please fill in all blanks")
                continue
            elif int(staff_age) < 18:
                print("Company Policy: Ages under 18 are unable to be hired as staff.")
                continue
            else: 
                staff.append(staff_age)
                staff_nation = input("Nationality: ")
                staff.append(staff_nation)
                #Registration form for Non-Malaysian staffs
                if staff_nation != "Malaysian":
                    while True: 
                        staff_passport = input("Staff Passport No.: ")
                        if len(staff_passport) == 0:
                            print("Please fill in all blanks")
                            continue
                        elif len(staff_passport) < 6 or len(staff_passport) > 11:
                                print("Invalid Passport Number. Please try again...")
                                continue
                        else:
                            with open('staff_credentials.txt', 'r') as file:
                                info = file.read().split(", ")
                                file.close()
                                if staff_passport in info:
                                    print("Duplicate Passport Number Found. Please try again...")
                                    continue
                                else:
                                    staff.append(staff_passport)
                                    while True: 
                                        staff_dob = input("Date of Birth (DD/MM/YYYY): ")
                                        if len(staff_dob) == 0:
                                            print("Please fill in all blanks")
                                            continue
                                        else:
                                            tenth_days = int(staff_dob[0]) * 10
                                            one_days = int(staff_dob[1])
                                            tenth_months = int(staff_dob[3]) * 10
                                            one_months = int(staff_dob[4])
                                            month = tenth_months + one_months
                                            days = tenth_days + one_days
                                            if days > 31 or days < 0:
                                                print("Invalid Day input")
                                                continue
                                            elif month > 12 or month < 0:
                                                print("Invalid Month input")
                                                continue
                                            else:
                                                staff.append(staff_dob)
                                                while True:
                                                    staff_contact = input("Telephone No.: ")
                                                    if len(staff_contact) == 0:
                                                        print("Please fill in all blanks")
                                                        continue
                                                    elif len(staff_contact) > 11 or len(staff_contact) < 9:
                                                        print("Invalid Phone Number. Please try again...")
                                                        continue
                                                    else:
                                                        staff.append(staff_contact)
                                                        staff_address = input("Address (if none: N/A): ")
                                                        staff.append(staff_address)
                                                        while True:
                                                            staff_position = input("Staff Position: ")
                                                            if len(staff_position) == 0:
                                                                print("Please fill in all blanks")
                                                                continue
                                                            elif staff_position == "Manager":
                                                                staff.append(staff_position)
                                                                break
                                                            elif staff_position == "Clerk":
                                                                staff.append(staff_position)
                                                                break
                                                            else:
                                                                print("Invalid position. Please try again...")
                                                                continue
                                                                
                                                        with open('staff_credentials.txt', 'r') as file:
                                                            info = file.read().split(", ")
                                                            file.close()   
                                                        while True:
                                                            if len(info) == 0:
                                                                staff_ID = 44443333
                                                                break
                                                            else:
                                                                acc = info[1]
                                                                while True: 
                                                                    if int(acc) < 57775555 and int(acc) > 44443333:
                                                                        staff_ID = int(acc) + 9
                                                                        if str(staff_ID) in info:
                                                                            acc = staff_ID
                                                                            continue
                                                                        else:
                                                                            break
                                                                    elif int(acc) > 57775555 and int(acc) < 77775555:
                                                                        staff_ID = int(acc) - 7
                                                                        if str(staff_ID) in info:
                                                                            acc = staff_ID
                                                                            continue
                                                                        else:
                                                                            break 
                                                                    break
                                                            print(f"Account Number: {staff_ID}")
                                                            idpw_list.append(staff_ID)
                                                            staff.insert(1, staff_ID)
                                                            staff_pw = input("Password: ")
                                                            idpw_list.append(staff_pw)
                                                            break
                                                    break
                                        break
                                    break
                    break
                #Registration form for Malaysian staffs
                else: 
                    while True: 
                        staff_IC_num = input("IC No.: ")
                        if len(staff_IC_num) == 0:
                            print("Please fill in all blanks")
                            continue
                        elif len(staff_IC_num) != 12:
                            print("Invalid IC number. Please try again")
                            continue
                        else:
                            with open('staff_credentials.txt', 'r') as file:
                                info = file.read().split(", ")
                                file.close()
                                if staff_IC_num in info:
                                    "Duplicate IC Number Found. Please try again..."
                                    continue
                                else:
                                    staff.append(staff_IC_num)
                                    while True: 
                                        staff_dob = input("Date of Birth (DD/MM/YYYY): ")
                                        if len(staff_dob) == 0:
                                            print("Please fill in all blanks")
                                            continue
                                        else:
                                            tenth_days = int(staff_dob[0]) * 10
                                            one_days = int(staff_dob[1])
                                            tenth_months = int(staff_dob[3]) * 10
                                            one_months = int(staff_dob[4])
                                            month = tenth_months + one_months
                                            days = tenth_days + one_days
                                            if days > 31 or days < 0:
                                                print("Invalid Day input")
                                                continue
                                            elif month > 12 or month < 0:
                                                print("Invalid Month input")
                                                continue
                                            else:
                                                staff.append(staff_dob)
                                                while True:
                                                    staff_contact = input("Telephone No.: ")
                                                    if len(staff_contact) == 0:
                                                        print("Please fill in all blanks")
                                                        continue
                                                    elif len(staff_contact) > 11 or len(staff_contact) < 9:
                                                        print("Invalid Phone Number. Please try again...")
                                                        continue
                                                    else:
                                                        staff.append(staff_contact)
                                                        staff_address = input("Address (if none: N/A): ")
                                                        staff.append(staff_address)
                                                        while True:
                                                            staff_position = input("Staff Position: ")
                                                            if len(staff_position) == 0:
                                                                print("Please fill in all blanks")
                                                                continue
                                                            elif staff_position == "Manager":
                                                                staff.append(staff_position)
                                                                break
                                                            elif staff_position == "Clerk":
                                                                staff.append(staff_position)
                                                                break
                                                            else:
                                                                print("Invalid position. Please try again...")
                                                                continue
                                                        with open('staff_credentials.txt', 'r') as file:
                                                            info = file.read().split(", ")
                                                            file.close()  
                                                        while True:
                                                            if len(info) == 1:
                                                                staff_ID = 44443333
                                                                break
                                                            elif len(info) != 1:
                                                                acc = info[1]
                                                                while True: 
                                                                    if int(acc) < 57775555 and int(acc) > 44443333:
                                                                        staff_ID = int(acc) + 9
                                                                        if str(staff_ID) in info:
                                                                            acc = staff_ID
                                                                            continue
                                                                        else:
                                                                            break
                                                                    elif int(acc) > 57775555 and int(acc) < 77775555:
                                                                        staff_ID = int(acc) - 7
                                                                        if str(staff_ID) in info:
                                                                            acc = staff_ID
                                                                            continue
                                                                        else:
                                                                            break
                                                                break
                                                        print(f"Account Number: {staff_ID}")
                                                        idpw_list.append(staff_ID)
                                                        staff.insert(1, staff_ID)
                                                        staff_pw = input("Password: ")
                                                        idpw_list.append(staff_pw)
                                                        break
                                                break
                                    break
                    break
        else: 
            print("Invalid Response. Please try again...")
            continue
    #open credentials, id & password text file databases to store information on new staff
    with open('staff_credentials.txt', 'r') as file:
        info = file.read().split(", ")
        file.close()
    staff.reverse()
    for i in staff:
        info.insert(0, i)
    with open('staff_credentials.txt', 'w') as file:
        for i in info:
            file.write("%s, " % i)
        file.close()
    for idpw in idpw_list:
        with open('staff_idpw_list.txt', 'a') as file:
            file.write("%s, " % idpw)
            file.close()
    print("Staff Account Created Successfully")
    staff_sorting()   
    with open('staff_credentials.txt', 'r') as file:
        staff = file.read().split(", ")
        file.close()
        if user_id in staff:
            staff_menu(user_id)
        else:
            super_user_menu(user_id)

#This function will only be accessed by admnistrators only
#To create new account for new administrator
#Appending all data from registration form to list then appending it to data file
#Staff ID and default password given by account creator and stored in separate data file
def new_acc_admin(user_id):
    print("Create New Admin Account Menu")
    admin = list()
    idpw_list = list()
    while True:
        with open('admin_idpw_list.txt', 'r') as file:
            idpw = file.read().split(", ")
            file.close()
        if user_id in idpw:
            with open('admin_credentials.txt', 'r') as file:
                item = file.read().split(", ")
                file.close()
            if user_id in item:
                name = item[item.index(user_id) + 2]
        while True: 
            yn = input("Cancel Process? (Y/N)\nAnswer: ")
            if yn == "Y":
                print('Returning to menu...')
                super_user_menu(user_id)
            elif yn == "N":
                admin.append(f"\nAccount Creator: {name}")
                print("Please fill in all information ACCURATELY.")
                admin_pref_salut = input("Preferred Salutation of User: ")
                admin.append(admin_pref_salut)
                admin_first_name = input("First Name: ")
                admin.append(admin_first_name)
                admin_last_name = input("Last Name: ")
                admin.append(admin_last_name)
                admin_age = input("Age: ")
                admin.append(admin_age)
                if len(admin_age) == 0:
                    print("Please fill in all blanks")
                    continue
                elif int(admin_age) < 18:
                    print("Company Policy: Ages under 18 are unable to be hired as staff.")
                    break
                else: 
                    admin_nation = input("Nationality: ")
                    admin.append(admin_nation)
                    #Registration form for Non-Malaysian admins
                    if admin_nation != "Malaysian":
                        while True: 
                            admin_passport = input("Passport No.: ")
                            if len(admin_passport) == 0:
                                print("Please fill in all blanks")
                                continue
                            elif len(admin_passport) < 6 or len(admin_passport) > 11:
                                    print("Invalid Passport Number. Please try again...")
                                    continue
                            else:
                                with open('admin_credentials.txt', 'r') as file:
                                    info = file.read().split(", ")
                                if admin_passport in info:
                                    print("Duplicate Passport Number Found. Please try again...")
                                    continue
                                else:
                                    admin.append(admin_passport)
                                    while True: 
                                        admin_dob = input("Date of Birth (DD/MM/YYYY): ")
                                        if len(admin_dob) == 0:
                                            print("Please fill in all blanks")
                                            continue
                                        else:
                                            tenth_days = int(admin_dob[0]) * 10
                                            one_days = int(admin_dob[1])
                                            tenth_months = int(admin_dob[3]) * 10
                                            one_months = int(admin_dob[4])
                                            month = tenth_months +one_months
                                            days = tenth_days + one_days
                                            if days > 31 or days < 0:
                                                print("Invalid Day input")
                                                continue
                                            elif month > 12 or month < 0:
                                                print("Invalid Month input")
                                                continue
                                            else:
                                                admin.append(admin_dob)
                                            while True:
                                                admin_contact = input("Telephone No.: ")
                                                if len(admin_contact) == 0:
                                                    print("Please fill in all blanks")
                                                    continue
                                                elif len(admin_contact) > 11 or len(admin_contact) < 9:
                                                    print("Invalid Phone Number. Please try again...")
                                                    continue
                                                else:
                                                    admin.append(admin_contact)
                                                    admin_address = input("Address: ")
                                                    admin.append(admin_address)
                                                    with open('admin_credentials.txt', 'r') as file:
                                                        info = file.read().split(", ")
                                                        file.close()
                                                    if len(info) == 0:
                                                        admin_ID = 77775555
                                                    else:               
                                                        acc = info[1]
                                                        while True: 
                                                            if int(acc) < 80000000 and int(acc) > 77775555:
                                                                admin_ID = int(acc) + 16
                                                                if str(admin_ID) in info:
                                                                    acc = admin_ID
                                                                    continue
                                                                else:
                                                                    break
                                                            elif int(acc) > 88889999:
                                                                admin_ID = int(acc) - 13
                                                                if str(admin_ID) in info:
                                                                    acc = admin_ID
                                                                    continue
                                                                else:
                                                                    break
                                                            elif int(acc) > 800000000 and int(acc) < 88889999:
                                                                admin_ID = int(acc) - 19
                                                                if str(admin_ID) in info:
                                                                    acc = admin_ID
                                                                    continue
                                                                else:
                                                                    break
                                                    print(f"Account Number: {admin_ID}")
                                                    idpw_list.append(admin_ID)
                                                    admin.insert(1, admin_ID)
                                                    admin_pw = input("Password: ")
                                                    idpw_list.append(admin_pw)
                                                    break
                                            break
                                    break
                        break
                    #Registration form for Malaysian admins
                    else: 
                        while True: 
                            admin_IC_num = input("IC No.: ")
                            if len(admin_IC_num) == 0:
                                print("Please fill in all blanks")
                                continue
                            elif len(admin_IC_num) != 12:
                                print("Invalid IC number. Please try again")
                                continue
                            else:
                                with open('admin_credentials.txt', 'r') as file:
                                    info = file.read().split(", ")
                                    file.close()
                                if admin_IC_num in info:
                                    print("Duplicate IC Number Found. Please try again...")
                                    continue
                                else:
                                    admin.append(admin_IC_num)
                                    while True: 
                                        admin_dob = input("Date of Birth (DD/MM/YYYY): ")
                                        if len(admin_dob) == 0:
                                            print("Please fill in all blanks")
                                            continue
                                        else:
                                            tenth_days = int(admin_dob[0]) * 10
                                            one_days = int(admin_dob[1])
                                            tenth_months = int(admin_dob[3]) * 10
                                            one_months = int(admin_dob[4])
                                            month = tenth_months + one_months
                                            days = tenth_days + one_days
                                            if days > 31 and days < 0:
                                                print("Invalid Day input")
                                                continue
                                            elif month > 12 and month < 0:
                                                print("Invalid Month input")
                                                continue
                                            else:
                                                admin.append(admin_dob)
                                                while True:
                                                    admin_contact = input("Telephone No.: ")
                                                    if len(admin_contact) == 0:
                                                        print("Please fill in all blanks")
                                                        continue
                                                    elif len(admin_contact) > 11 or len(admin_contact) < 9:
                                                        print("Invalid Phone Number. Please try again...")
                                                        continue
                                                    else:
                                                        admin.append(admin_contact)
                                                        admin_address = input("Address: ")
                                                        admin.append(admin_address)
                                                        with open('admin_credentials.txt', 'r') as file:
                                                            info = file.read().split(", ")
                                                            file.close()   
                                                        if len(info) == 0:
                                                            admin_ID = 77775555
                                                        else:
                                                            acc = info[1]
                                                            while True: 
                                                                if int(acc) < 80000000 and int(acc) > 77775555:
                                                                    admin_ID = int(acc) + 16
                                                                    if str(admin_ID) in info:
                                                                        acc = admin_ID
                                                                        continue
                                                                    else:
                                                                        break
                                                                elif int(acc) > 88889999:
                                                                    admin_ID = int(acc) - 13
                                                                    if str(admin_ID) in info:
                                                                        acc = admin_ID
                                                                        continue
                                                                    else:
                                                                        break
                                                                elif int(acc) > 80000000 and int(acc) < 88889999:
                                                                    admin_ID = int(acc) - 19
                                                                    if str(admin_ID) in info:
                                                                        acc = admin_ID
                                                                        continue
                                                                    else:
                                                                        break
                                                        print(f"Account Number: {admin_ID}")
                                                        idpw_list.append(admin_ID)
                                                        admin.insert(1, admin_ID)
                                                        admin_pw = input("Password: ")
                                                        idpw_list.append(admin_pw)
                                                        break
                                                break
                                    break
                        break
            else: 
                print("Invalid Response. Please try again...")
                continue
        break   
    #open credentials, id & password text file databases to store information on new admin 
    with open('admin_credentials.txt', 'r') as file:
        info = file.read().split(", ")
        file.close()
    admin.reverse()
    for i in admin:
        info.insert(0, i)
    with open('client_credentials.txt', 'w') as file:
        for i in info:
            file.write("%s, " % i)
        file.close()
    for i in idpw_list:
        with open('admin_idpw_list.txt', 'a') as file:
            file.write("%s, " % id)
            file.close()
    print("Admin Account Created Successfully")
    admin_sorting()   
    super_user_menu(user_id)

#This function will only be accessed by the client
#To change password of client's account
def change_client_pw(user_id):
    print("Change Client Password Menu")
    while True:
        #Requests for client's account number, opens data file and search for inputed account number
        with open('client_idpw_list.txt', 'r') as file:
            idpw = file.read().split(", ")
            file.close()
            while True: 
                    print("Type 'cancel' to cancel the process...")
                    pw = input ("New Password: ")
                    if pw == 'cancel':
                        print("Returning to menu...")
                        menu(user_id)
                    else:
                        con = input("Confirm New Password: ")
                        if pw != con:
                            print("Passwords are not identical. Please check again.")
                            continue
                        #Takes number and increment index by 1 to get position and value of password
                        #Requests input for new password and check if new password and old password are the same 
                        elif pw == idpw[idpw.index(user_id) + 1]:
                            print("New password cannot be the same as existing password.")
                            continue
                        else:
                            #Stores whole file as a list in a list, then makes ammendments to list, clears the data file. 
                            #Then rewriting the file with the list that contains the changed password
                            with open('client_idpw_list.txt', 'r') as file:
                                idpw = file.read().split(", ")
                                file.close()
                                ori = idpw.index(user_id) + 1
                                del idpw[ori]
                                idpw.insert(ori, pw)
                                idpw.pop()
                            with open('client_idpw_list.txt', 'w') as file:
                                for i in idpw:
                                    file.write("%s, " % i)
                                file.close()
                            break
            break
    print("Password Changed Successfully\nReturning to menu...\n")
    menu(user_id)

#This function will be only accessed by administrators and staff 
#Used to change Client's Account Password by referencing to Client's Account ID
def change_client_pw_for_staff(user_id):
    print("Change Client Password Menu")
    while True:
        #Requests for client's account number, opens data file and search for inputed account number
        id = input("Please enter client account no.: ")
        with open('client_idpw_list.txt', 'r') as file:
            idpw = file.read().split(", ")
            file.close()
            while True:
                if id in idpw:
                    print("Type 'cancel' to cancel process...")
                    pw = input ("New Password: ")
                    if pw == 'cancel':
                        with open('staff_credentials.txt', 'r') as file:
                            info = file.read().split(", ")
                            file.close()
                        if user_id in info:
                            print("Returning to menu...\n")
                            staff_menu(user_id)
                        else:
                            print("Returning to menu...\n")
                            super_user_menu(user_id)
                    else:
                        con = input("Confirm New Password: ")
                        if pw != con:
                            print("Passwords are not identical. Please check again.")
                            continue
                        #Takes number and increment index by 1 to get position and value of password
                        #Requests input for new password and check if new password and old password are the same 
                        elif pw == idpw[idpw.index(id) + 1]:
                            print("New password cannot be the same as existing password.")
                            continue
                        else:
                            #Stores whole file as a list in a list, then makes ammendments to the list, clears the data file. 
                            #Then rewriting the file with the list that contains the changed password
                            with open('client_idpw_list.txt', 'r') as file:
                                idpw = file.read().split(", ")
                                file.close()
                                ori = idpw.index(id) + 1
                                del idpw[ori]
                                idpw.insert(ori, pw)
                                idpw.pop()
                            with open('client_idpw_list.txt', 'w') as file:
                                for i in idpw:
                                    file.write("%s, " % i)
                                file.close()
                            break
                else:
                    print("Client Account No. not found. Please try again.")
                    continue
        with open('staff_credentials.txt', 'r') as file:
            info = file.read().split(", ")
        print("Password Changed Successfully\n")
        if user_id in info:
            print("Returning to menu...\n")
            staff_menu(user_id)
        else:
            print("Returning to menu...\n")
            super_user_menu(user_id)
        
#This function will be only accessed by administrators and staff 
#Used to change Account Password by referencing to Staff's Account ID
def change_staff_pw(user_id):
    print("Change Staff Password Menu")
    while True:  
        #Requests for staff's account number, opens data file and search for inputed account number
        id = input("Please enter staff account no.: ")
        with open('staff_idpw_list.txt', 'r') as file:
            idpw = file.read().split(", ")
            file.close()
            while True:
                if id in idpw:
                    print("Type 'cancel' to cancel process...")
                    pw = input ("New Password: ")
                    if pw == 'cancel':
                        with open('staff_credentials.txt', 'r') as file:
                            info = file.read().split(", ")
                        if user_id in info:
                            print("Returning to menu...\n")
                            staff_menu(user_id)
                        else:
                            print("Returning to menu...\n")
                            super_user_menu(user_id)
                    else:
                        con = input("Confirm New Password: ")
                        if pw != con:
                            print("Passwords are not identical. Please check again.")
                            continue
                        #Takes number and increment index by 1 to get position and value of password
                        #Requests input for new password and check if new password and old password are the same 
                        elif pw == idpw[idpw.index(id) + 1]:
                            print("New password cannot be the same as old password.")
                            continue
                        else:
                            #Stores whole file as a list in a list, then makes ammendments to the list, clears the data file. 
                            #Then rewriting the file with the list that contains the changed password
                            with open('staff_idpw_list.txt', 'r') as file:
                                idpw = file.read().split(", ")
                                ori = idpw.index(id) + 1
                                del idpw[ori]
                                idpw.insert(ori, pw)
                                idpw.pop()
                                with open('staff_idpw_list.txt', 'w') as file:
                                    for i in idpw:
                                        file.write("%s, " % i)
                                    file.close()
                            break
                else:
                    print("Staff Account not found. Please try again.")
                    continue

        print("Password Changed Successfully\n")
        with open('staff_credentials.txt', 'r') as file:
            info = file.read().split(", ")
        if user_id in info:
            ind = info[info.index(user_id) + 10]
            if ind == 'Clerk':
                print("Returning to menu...\n")
                staff_menu(user_id)
            elif ind == "Manager":
                print("Returning to menu...\n")
                staff_menu(user_id)
            else:
                print("Returning to menu...\n")
                super_user_menu(user_id)

#This function will only be accessed by the administrator
#To change password of administrator account
def change_admin_pw(user_id):
    print("Change Admin Password Menu")
    while True: 
        #Requests for admnistrator's account number, opens data file and search for inputed account number
        id = input("Please enter admin account no.: ")
        with open('admin_idpw_list.txt', 'r') as file:
            idpw = file.read().split(", ")
            file.close()
            while True:
                if id in idpw: 
                    print("Type 'cancel' to cancel process...")
                    pw = input ("New Password: ")
                    if pw == 'cancel':
                        print("Returning to menu...")
                        super_user_menu(user_id)
                    else:
                        con = input("Confirm New Password: ")
                        if pw != con:
                            print("Passwords are not identical. Please check again.")
                            continue
                        #Takes number and increment index by 1 to get position and value of password
                        #Requests input for new password and check if new password and old password are the same 
                        elif pw == idpw[idpw.index(id) + 1]:
                            print("New password cannot be the same as old password.")
                            continue
                        else:
                            #Stores whole file as a list in a list, then makes ammendments to the list, clears the data file. 
                            #Then rewriting the file with the list that contains the changed password
                            with open('admin_idpw_list.txt', 'r') as file:
                                idpw = file.read().split(", ")
                                file.close()
                                ori = idpw.index(id) + 1
                                del idpw[ori]
                                idpw.insert(ori, pw)
                                idpw.pop()        
                            with open('admin_idpw_list.txt', 'w') as file:
                                for i in idpw:
                                    file.write("%s, " % i)
                                file.close()
                            break
                else:
                    print("Admin Account No. not found. Please try again.")
                    continue
        print("Password Changed Successfully\nReturning to menu...\n")
        super_user_menu(user_id)

#changes the age of every user account type
#Accepts three parameters, user's id number, user's account number, and the general object's index in database list
def change_age(user_id, acc_num, obj_ind):
    with open('client_credentials.txt', 'r') as file:
        client = file.read().split(", ")
        file.close()
    with open('staff_credentials.txt', 'r') as file:
        staff = file.read().split(", ")
        file.close()
    #change age for client
    if acc_num in client: 
        with open('client_credentials.txt', 'r') as file:
            info = file.read().split(", ")
            file.close()
        age = info[obj_ind + 4]
        while True:
            new_age = input("New Age: ")
            confirm = input("Age Confirm: ")
            if new_age != confirm:
                print("Ages must match")
                continue
            elif int(new_age) <= 18:
                print("Invalid Age. Please try again...")
                continue
            else:
                info.remove(age)
                info.insert(obj_ind + 4, new_age)
                file.close()
                with open('client_credentials.txt', 'w') as file:
                    for i in info: 
                        file.write("%s, " % i)
                    file.close()
                print("Information Changed Successfully")
                break
        client_details(user_id)
    #change age for staff
    elif acc_num in staff:
        with open('staff_credentials.txt', 'r') as file:
            info = file.read().split(", ")
            file.close()
        age = info[obj_ind + 4]
        while True: 
            new_age = input("New Age: ")
            confirm = input("Age Confirm: ")
            if new_age != confirm:
                print("Ages must match")
                continue
            elif int(new_age) <= 18:
                print("Invalid Age. Please try again...")
                continue
            else:
                info.remove(age)
                info.insert(obj_ind + 4, new_age)
                file.close()
                with open('staff_credentials.txt', 'w') as file:
                    for i in info: 
                        file.write("%s, " % i)
                    file.close()
                print("Information Changed Successfully")
                break
        staff_details(user_id)
    #change age for admin
    else:
        with open('admin_credentials.txt', 'r') as file:
            info = file.read().split(", ")
            file.close()
        age = info[obj_ind + 4]
        while True: 
            new_age = input("New Age: ")
            confirm = input("Please Confirm: ")
            if new_age != confirm:
                print("Ages must match")
                continue
            elif int(new_age) <= 18:
                print("Invalid Age. Please try again...")
                continue
            else:
                info.remove(age)
                info.insert(obj_ind + 4, new_age)
                file.close()
                with open('admin_credentials.txt', 'w') as file:
                    for i in info: 
                        file.write("%s, " % i)
                    file.close()
                print("Information Changed Successfully")
                break
        admin_details(user_id)

#changes the nationality of every user account type
#Accepts three parameters, user's id number, user's account number, and the general object's index in database list
def change_nat(user_id, acc_num, obj_ind):
    with open('client_credentials.txt', 'r') as file:
        client = file.read().split(", ")
        file.close()
    with open('staff_credentials.txt', 'r') as file:
        staff = file.read().split(", ")
        file.close()
    #change nationality for client
    if acc_num in client:
        with open('client_credentials.txt', 'r') as file:
            info = file.read().split(", ")
            file.close()
        nation = info[obj_ind + 5]
        while True:
            new_nat = input("New Nationality: ")
            confirm = input("Nationality Confirm: ")
            if new_nat != confirm:
                print("Nationality must match")
                continue
            else:
                info.remove(nation)
                info.insert(obj_ind + 5, new_nat)
                file.close()
                with open('client_credentials.txt', 'w') as file:
                    for i in info: 
                        file.write("%s, " % i)
                    file.close()
                print("Information Changed Successfully")
                break
        client_details(user_id)
    #change nationality for staff
    elif acc_num in staff:
        with open('staff_credentials.txt', 'r') as file:
            info = file.read().split(", ")
            file.close()
        nation = info[obj_ind + 5]
        while True: 
            new_nat = input("New Nationality: ")
            confirm = input("Nationality Confirm: ")
            if new_nat != confirm:
                print("Nationalities must match")
                continue
            else:
                info.remove(nation)
                info.insert(obj_ind + 5, new_nat)
                file.close()
                with open('staff_credentials.txt', 'w') as file:
                    for i in info: 
                        file.write("%s, " % i)
                    file.close()
                print("Information Changed Successfully")
                break
        staff_details(user_id)
    #change nationality for admin
    else:
        with open('admin_credentials.txt', 'r') as file:
            info = file.read().split(", ")
            file.close()
        nation = info[obj_ind + 5]
        while True: 
            new_nat = input("New Nationality: ")
            confirm = input("Please Confirm: ")
            if new_nat != confirm:
                print("Nationalities must match")
                continue
            else:
                info.remove(nation)
                info.insert(obj_ind + 5, new_nat)
                file.close()
                with open('admin_credentials.txt', 'w') as file:
                    for i in info: 
                        file.write("%s, " % i)
                    file.close()
                print("Information Changed Successfully")
                break
        admin_details(user_id)

#changes the date of birth of every user account type
#Accepts three parameters, user's id number, user's account number, and the general object's index in database list
def change_dob(user_id, acc_num, obj_ind):
    with open('client_credentials.txt', 'r') as file:
        client = file.read().split(", ")
        file.close()
    with open('staff_credentials.txt', 'r') as file:
        staff = file.read().split(", ")
        file.close()
    #change date of birth for client
    if acc_num in client:
        with open('client_credentials.txt', 'r') as file:
            info = file.read().split(", ")
            file.close()
        dob = info[obj_ind + 7]
        while True: 
            new_dob = input("New Date of Birth (DD/MM/YYYY): ")
            confirm = input("Date of Birth Confirm: ")
            tenth_days = int(new_dob(0)) * 10
            one_days = int(new_dob(1))
            tenth_months = int(new_dob(3)) * 10
            one_months = int(new_dob(4))
            month = tenth_months +one_months
            days = tenth_days + one_days
            if new_dob != confirm:
                print("Date of Births must match")
                continue
            elif days > 31 or days < 0:
                print("Invalid Day input")
                continue
            elif month > 12 or month < 0:
                print("Invalid Month input")
                continue
            else:
                info.remove(dob)
                info.insert(obj_ind + 7, new_dob)
                file.close()
                with open('client_credentials.txt', 'w') as file:
                    for i in info: 
                        file.write("%s, " % i)
                    file.close()
                print("Information Changed Successfully")
                break
        client_details(user_id)
    #change date of birth for staff
    elif acc_num in staff:
        with open('staff_credentials.txt', 'r') as file:
            info = file.read().split(", ")
            file.close()
        dob = info[obj_ind + 7]
        while True: 
            new_dob = input("New Date of Birth (DD/MM/YYYY): ")
            confirm = input("Date of Birth Confirm: ")
            tenth_days = int(new_dob(0)) * 10
            one_days = int(new_dob(1))
            tenth_months = int(new_dob(3)) * 10
            one_months = int(new_dob(4))
            month = tenth_months + one_months
            days = tenth_days + one_days
            if new_dob != confirm:
                print("Date of Births must match")
                continue
            elif days > 31 or days < 0:
                print("Invalid Day input")
                continue
            elif month > 12 or month < 0:
                print("Invalid Month input")
                continue
            else:
                info.remove(dob)
                info.insert(obj_ind + 7, new_dob)
                file.close()
                with open('staff_credentials.txt', 'w') as file:
                    for i in info: 
                        file.write("%s, " % i)
                    file.close()
                print("Information Changed Successfully")
                break
        staff_details(user_id)
    #change date of birth for admin
    else:
        with open('admin_credentials.txt', 'r') as file:
            info = file.read().split(", ")
            file.close()
        dob = info[obj_ind + 7]
        while True: 
            new_dob = input("New Date of Birth (DD/MM/YYYY): ")
            confirm = input("Date of Birth Confirm: ")
            tenth_days = int(new_dob(0)) * 10
            one_days = int(new_dob(1))
            tenth_months = int(new_dob(3)) * 10
            one_months = int(new_dob(4))
            month = tenth_months +one_months
            days = tenth_days + one_days
            if new_dob != confirm:
                print("Date of Births must match")
                continue
            elif days > 31 or days < 0:
                print("Invalid Day input")
                continue
            elif month > 12 or month < 0:
                print("Invalid Month input")
                continue
            else:
                info.remove(dob)
                info.insert(obj_ind + 7, new_dob)
                file.close()
                with open('admin_credentials.txt', 'w') as file:
                    for i in info:
                        file.write("%s, " % i)
                    file.close()
                print("Information Changed Successfully")
                break
        admin_details(user_id)

#changes the phone number of every user account type
#Accepts three parameters, user's id number, user's account number, and the general object's index in database list
def change_ph_num(user_id, acc_num, obj_ind):
    with open('client_credentials.txt', 'r') as file:
        client = file.read().split(", ")
        file.close()
    with open('staff_credentials.txt', 'r') as file:
        staff = file.read().split(", ")
        file.close()
    #change phone number for client
    if acc_num in client:
        with open('client_credentials.txt', 'r') as file:
            info = file.read().split(", ")
            file.close()
        ph_num = info[obj_ind + 8]
        while True: 
            new_ph_num = input("New Phone No.: ")
            confirm = input("Phone No. Confirm: ")
            if new_ph_num != confirm:
                print("Phone Numbers must match")
                continue
            elif len(new_ph_num) > 11 or len(new_ph_num) < 9:
                print("Invalid Phone Number. Please try again...")
                continue
            else:
                info.remove(ph_num)
                info.insert(obj_ind + 8, new_ph_num)
                file.close()
                with open('client_credentials.txt', 'w') as file:
                    for i in info: 
                        file.write("%s, " % i)
                    file.close()
                print("Information Changed Successfully")
                break
        client_details(user_id)
    #change phone number for staff
    elif acc_num in staff:
        with open('staff_credentials.txt', 'r') as file:
            info = file.read().split(", ")
            file.close()
        ph_num = info[obj_ind + 8]
        while True: 
            new_ph_num = input("New Phone No.: ")
            confirm = input("Phone No. Confirm: ")
            if new_ph_num != confirm:
                print("Phone Numbers must match")
                continue
            elif len(new_ph_num) > 11 or len(new_ph_num) < 9:
                print("Invalid Phone Number. Please try again...")
                continue
            else:
                info.remove(ph_num)
                info.insert(obj_ind + 8, new_ph_num)
                file.close()
                with open('staff_credentials.txt', 'w') as file:
                    for i in info: 
                        file.write("%s, " % i)
                    file.close()
                print("Information Changed Successfully")
                break
        staff_details(user_id)
    #change phone number for admin
    else: 
        with open('admin_credentials.txt', 'r') as file:
            info = file.read().split(", ")
            file.close()
        ph_num = info[obj_ind + 8]
        while True: 
            new_ph_num = input("New Phone No.: ")
            confirm = input("Phone No. Confirm: ")
            if new_ph_num != confirm:
                print("Phone Numbers must match")
                continue
            elif len(new_ph_num) > 11 or len(new_ph_num) < 9:
                print("Invalid Phone Number. Please try again...")
                continue
            else:
                info.remove(ph_num)
                info.insert(obj_ind + 8, new_ph_num)
                file.close()
                with open('admin_credentials.txt', 'w') as file:
                    for i in info: 
                        file.write("%s, " % i)
                    file.close()
                print("Information Changed Successfully")
                break
        admin_details(user_id)

#changes the address of every user account type
#Accepts three parameters, user's id number, user's account number, and the general object's index in database list
def change_addr(user_id, acc_num, obj_ind):
    with open('client_credentials.txt', 'r') as file:
        client = file.read().split(", ")
        file.close()
    with open('staff_credentials.txt', 'r') as file:
        staff = file.read().split(", ")
        file.close()
    #change address for client
    if acc_num in client:
        with open('client_credentials.txt', 'r') as file:
            info = file.read().split(", ")
            file.close()
        addr = info[obj_ind + 9]
        while True: 
            new_addr = input("New Address: ")
            confirm = input("Please Confirm: ")
            if new_addr != confirm:
                print("Addresses must match")
                continue
            else:
                info.remove(addr)
                info.insert(obj_ind + 9, new_addr)
                file.close()
                with open('client_credentials.txt', 'w') as file:
                    for i in info: 
                        file.write("%s, " % i)
                    file.close()
                print("Information Changed Successfully")
                break
        client_details(user_id)
    #change address for staff
    elif acc_num in staff:
        with open('staff_credentials.txt', 'r') as file:
            info = file.read().split(", ")
            file.close()
        addr = info[obj_ind + 9]
        while True: 
            new_addr = input("New Address: ")
            confirm = input("Please Confirm: ")
            if new_addr != confirm:
                print("Addresses must match")
                continue
            else:
                info.remove(addr)
                info.insert(obj_ind + 9, new_addr)
                file.close()
                with open('staff_credentials.txt', 'w') as file:
                    for i in info: 
                        file.write("%s, " % i)
                    file.close()
                print("Information Changed Successfully")
                break
        staff_details(user_id)
    #change address for admin
    else:
        with open('admin_credentials.txt', 'r') as file:
            info = file.read().split(", ")
            file.close()
        addr = info[obj_ind + 9]
        while True: 
            new_addr = input("New Address: ")
            confirm = input("Please Confirm: ")
            if new_addr != confirm:
                print("Addresses must match")
                continue
            else:
                info.remove(addr)
                info.insert(obj_ind + 9, new_addr)
                file.close()
                with open('admin_credentials.txt', 'w') as file:
                    for i in info: 
                        file.write("%s, " % i)
                    file.close()
                print("Information Changed Successfully")
                break
        admin_details(user_id)

#main function for changing client details
#medium for some built-in services and remote services in other functions
def client_details(user_id):
    print("Change Client Details Menu")
    with open('staff_credentials.txt', 'r') as file:
        info = file.read().split(", ")
        file.close()
    if user_id in info:
        salutation = info[info.index(user_id) + 1] 
        name = info[info.index(user_id) + 2]
        print(f"Welcome, {salutation} {name}\n")
    else:
        with open('admin_credentials.txt', 'r') as file:
            admin = file.read().split(", ")
            file.close()
        salutation = admin[admin.index(user_id) + 1] 
        name = admin[admin.index(user_id) + 2]
        print(f"Welcome, {salutation} {name}\n")

    with open('client_credentials.txt', 'r') as file:
        info = file.read().split(", ")
        file.close()
        while True: 
            acc_num = input("Client Account Number: ")
            if acc_num in info:
                obj_ind = info.index(acc_num)
                service = input("Type 'cancel' to cancel process\nWhat would you like to change?\n1. Age\n2. Nationality\n3. Identification Card No./Passport No.\n4. Birth Date\n5. Phone No.\n6. Address\n7. Occupation\nAnswer: ")
                if service == '1':
                    change_age(user_id, acc_num, obj_ind)
                elif service == '2':
                    change_nat(user_id, acc_num, obj_ind)
                elif service == '3':
                    nat = info[obj_ind + 6]
                    while True: 
                        with open('client_credentials.txt', 'r') as file:
                            read = file.read().split(", ")
                            file.close()
                        if acc_num in read:
                            #change identification card number for Malaysian
                            if read[read.index(acc_num) + 6] == "Malaysian":
                                new_num = input("New Customer ID Card No.: ")
                                confirm = input("ID Card No. Confirm: ")
                                if new_num != confirm:
                                    print("Identification Card numbers must match")
                                    continue
                                elif new_num in read:
                                    print("Duplicate ID Card Number Found. Please try again...")
                                    continue
                                elif len(new_num) != 12  and 'Malaysia' == info[obj_ind + 6]:
                                    print("Invalid ID Card Number. Please Try Again.")
                                    continue
                                else:
                                    info.remove(nat)
                                    info.insert(obj_ind + 6, new_num)
                                    file.close()
                                    with open('client_credentials.txt', 'w') as file:
                                        for i in info: 
                                            file.write("%s, " % i)
                                        file.close()
                                    break
                            #change passport number for Non-Malaysians
                            elif read[read.index(acc_num) + 6] != "Malaysian":
                                new_num = input("New Customer Passport No.: ")
                                confirm = input("Passport No. Confirm: ")
                                if new_num != confirm:
                                    print("Passport Numbers must match")
                                    continue
                                elif new_num in read:
                                    print("Duplicate Paspport Number Found. Please try again...")
                                    continue
                                elif len(new_num) < 11  or len(new_num) > 6:
                                    print("Invalid Passport Number. Please Try Again.")
                                    continue
                                else:
                                    info.remove(nat)
                                    info.insert(obj_ind + 6, new_num)
                                    file.close()
                                    with open('client_credentials.txt', 'w') as file:
                                        for i in info: 
                                            file.write("%s, " % i)
                                        file.close()
                                    print("Information Changed Successfully")
                                    break
                    client_details(user_id)
                elif service == '4':
                    change_dob(user_id, acc_num, obj_ind)
                elif service == '5':
                    change_ph_num(user_id, acc_num, obj_ind)
                elif service == '6':
                    change_addr(user_id, acc_num, obj_ind)
                elif service == '7':
                    #changes customer's occupation
                    occu = info[obj_ind + 9]
                    while True: 
                        new_occu = input("New Customer Occupation: ")
                        confirm = input("Occupation Confirm: ")
                        if new_occu != confirm:
                            print("Occupations must match")
                            continue
                        else:
                            info.remove(occu)
                            info.insert(obj_ind + 9, new_occu)
                            file.close()
                            with open('client_credentials.txt', 'w') as file:
                                for i in info: 
                                    file.write("%s, " % i)
                                file.close()
                            print("Information Changed Successfully")
                            break
                    client_details(user_id)
                elif service == 'cancel':
                    #cancel process and returns user to menu
                    print("Thank you! Returning to menu...\n")
                    with open('staff_credentials.txt', 'r') as file:
                        staff = file.read().split(", ")
                        file.close()
                        if user_id in staff:
                            staff_menu(user_id)
                        else:
                            super_user_menu(user_id)
                else:
                    print("Invalid Response. Please try again...")
                    continue

            else:
                print("Client Account Number not found. Please try again...")
                continue
            break

#main function for changing staff details
#medium for some built-in services and remote services in other functions 
def staff_details(user_id):
    print("Change Staff Details Menu")
    with open('admin_credentials.txt', 'r') as file:
        admin = file.read().split(", ")
        file.close()
    salutation = admin[admin.index(user_id) + 1] 
    name = admin[admin.index(user_id) + 2]
    print(f"Welcome, {salutation} {name}\n")
    
    while True: 
        acc_num = input("Staff Account Number: ")
        with open('staff_credentials.txt', 'r') as file:
            info = file.read().split(", ")
            file.close()
            if acc_num in info:
                obj_ind = info.index(acc_num)
                service = input("Type 'cancel' to cancel process\nWhat would you like to change?\n1. Age\n2. Nationality\n3. Identification Card No./Passport No.\n4. Birth Date\n5. Phone No.\n6. Address\n7. Staff Position\nAnswer: ")
                if service == '1':
                    change_age(user_id, acc_num, obj_ind)
                elif service == '2':
                    change_nat(user_id, acc_num, obj_ind)
                elif service == '3':
                    nat = info[obj_ind + 6]
                    while True: 
                        with open('client_credentials.txt', 'r') as file:
                            read = file.read().split(", ")
                            file.close()
                        if acc_num in read:
                            #change identification card number for Malaysians
                            if read[read.index(acc_num) + 6] == "Malaysian":
                                new_num = input("New Staff ID Card No.: ") 
                                confirm = input("ID Card No. Confirm: ")
                                if new_num != confirm:
                                    print("Identification Card Numbers must match")
                                    continue
                                elif new_num in read:
                                    print("Duplicate ID Card Number Found. Please try again...")
                                    continue
                                elif len(new_num) != 12  and 'Malaysia' == info[obj_ind + 6]:
                                    print("Invalid ID Card Number. Please try again...")
                                    continue
                                else:
                                    info.remove(nat)
                                    info.insert(obj_ind + 6, new_num)
                                    file.close()

                                    with open('staff_credentials.txt', 'w') as file:
                                        for i in info: 
                                            file.write("%s, " % i)
                                        file.close()
                                    print("Information Changed Successfully")
                                    break
                            #change passport number for Non-Malaysians
                            elif read[read.index(acc_num) + 6] != "Malaysian":
                                new_num = input("New Customer Passport No.: ")
                                confirm = input("Passport No. Confirm: ")
                                if new_num != confirm:
                                    print("Passport Numbers must match")
                                    continue
                                elif new_num in read:
                                    print("Duplicate Passport Number Found. Please try again...")
                                    continue
                                elif len(new_num) < 11  or len(new_num) > 6:
                                    print("Invalid Passport Number. Please Try Again.")
                                    continue
                                else:
                                    info.remove(nat)
                                    info.insert(obj_ind + 6, new_num)
                                    file.close()
                                    with open('staff_credentials.txt', 'w') as file:
                                        for i in info: 
                                            file.write("%s, " % i)
                                        file.close()
                                    print("Information Changed Successfully")
                                    break
                    staff_details(user_id)
                elif service == '4':
                    change_dob(user_id, acc_num, obj_ind)
                elif service == '5':
                    change_ph_num(user_id, acc_num, obj_ind)
                elif service == '6':
                    change_addr(user_id, acc_num, obj_ind)
                elif service == '7':
                    #change staff's position based on promotion or demotion
                    posi = info[obj_ind + 10]
                    while True:
                        new_posi = input("New Staff Position: ")
                        confirm = input("Position Confirm: ")
                        if new_posi != confirm:
                            print("Staff Positions must match")
                            continue
                        elif new_posi != "Manager" or new_posi != "Clerk":
                            print("Invalid Staff Position. Please try again...")
                            continue
                        else:
                            info.remove(posi)
                            info.insert(obj_ind + 10, new_posi)
                            file.close()
                            with open('staff_credentials.txt', 'w') as file:
                                for i in info: 
                                    file.write("%s, " % i)
                                file.close()
                            print("Information Changed Successfully")
                            break
                    staff_details(user_id)
                elif service == 'cancel':
                    #cancel process and returns user to menu
                    print("Thank you! Returning to menu...\n")
                    super_user_menu(user_id)
                else:
                    print("Invalid Response. Please try again...")
                    continue
            else:
                print("staff Account Number not found. Please try again...")
                continue
            break

#main function for changing admin details
#medium for some built-in services and remote services in other functions
def admin_details(user_id):
    print("Change Admin Details Menu")
    with open('admin_credentials.txt', 'r') as file:
        admin = file.read().split(", ")
    salutation = admin[admin.index(user_id) + 1] 
    name = admin[admin.index(user_id) + 2]
    print(f"Welcome, {salutation} {name}\n")
    while True: 
        acc_num = input("Admin Account Number: ")
        with open('admin_credentials.txt', 'r') as file:
            info = file.read().split(", ")
            if acc_num in info:
                obj_ind = info.index(acc_num)
                service = input("Type 'cancel' to cancel process\nWhat would you like to change?\n1. Age\n2. Nationality\n3. Identification Card No./Passport No.\n4. Birth Date\n5. Phone No.\n6. Address\nAnswer: ")
                if service == '1':
                    change_age(user_id, acc_num, obj_ind)
                elif service == '2':
                    change_nat(user_id, acc_num, obj_ind)
                elif service == '3':
                    id_num = info[obj_ind + 6]
                    with open('client_credentials.txt', 'r') as file:
                        read = file.read().split(", ")
                    #change identification card for Malaysians
                    if info[obj_ind + 5] == "Malaysian":
                        while True:
                            new_num = input("New Admin ID Card No.: ")
                            confirm = input("Please Confirm: ")
                            if new_num != confirm:
                                print("Identification Card Numbers must match")
                                continue
                            elif new_num in read:
                                print("Duplicate ID Card Number Found. Please try again...")
                                continue
                            elif len(new_num) != 12  and 'Malaysia' == info[obj_ind + 5]:
                                print("Invalid ID Card Number. Please try again...")
                                continue
                            else:
                                info.remove(id_num)
                                info.insert(obj_ind + 6, new_num)
                                file.close()

                                with open('admin_credentials.txt', 'w') as file:
                                    for i in info: 
                                        file.write("%s, " % i)
                                    file.close()
                                print("Information Changed Successfully")
                                break
                    #changes passport number for Non-Malaysians
                    elif read[read.index(acc_num) + 5] != "Malaysian":
                        while True:
                            new_num = input("New Customer Passport No.: ")
                            confirm = input("Please Confirm: ")
                            if new_num != confirm:
                                print("Passport Numbers must match")
                                continue
                            elif new_num in read:
                                print("Duplicate Passport Number Found. Please try again...")
                                continue
                            elif len(new_num) < 11  or len(new_num) > 6:
                                print("Invalid Passport Number. Please Try Again.")
                                continue
                            else:
                                info.remove(id_num)
                                info.insert(obj_ind + 6, new_num)
                                file.close()
                                with open('admin_credentials.txt', 'w') as file:
                                    for i in info: 
                                        file.write("%s, " % i)
                                    file.close()
                                print("Information Changed Successfully")
                                break
                    admin_details(user_id)
                elif service == '4':
                    change_dob(user_id, acc_num, obj_ind)
                elif service == '5':
                    change_ph_num(user_id, acc_num, obj_ind)
                elif service == '6':
                    change_addr(user_id, acc_num, obj_ind)
                elif service == 'cancel':
                    print("Thank you! Returning to menu...\n")
                    super_user_menu(user_id)
                else:
                    print("Invalid Response. Please try again...")
                    continue

            elif acc_num not in info:
                print("staff Account Number not found. Please try again...")
                continue
            break

#Allow clients to transfer money from own account balance into another available user account's balance
def transfer(user_id):
    print("Transfer Menu")
    with open('client_credentials.txt', 'r') as file:
        item = file.read().split(", ")
        file.close()
    salutation = item[item.index(user_id) + 1] 
    name = item[item.index(user_id) + 2]
    
    with open(f'Balance/{user_id}_balance.txt', 'r') as money:
        acc = money.read().split(", ")
        file.close()
        balance = acc[0]
    #show current user his account balance 
    print(f"Hi, {salutation} {name}\nYour Account Balance is: RM {balance}\n")
    while True:
        trans_acc = input("Type 'cancel' to cancel process\nAccount Number to Transfer: ")
        if trans_acc not in item:
            print("Account number not found. Please try again...")
            continue
        elif trans_acc == 'cancel':
            #cancel process and returns user to menu
            print("Thank you! Returning to menu...\n")
            menu(user_id)
        else:
            #request user for confirmation of transfer account number
            confirm = input(f"Account Number to Transfer Confirm: {trans_acc}\nPress 'enter' to confirm...")
            while True:
                trans_amo = input("Type 'cancel' to cancel process\nTransfer Amount: RM ")
                if trans_amo == "cancel":
                    #cancel process 
                    print("Thank you! Returning to menu...\n")
                    menu(user_id)
                else: 
                    #request for confirmation of transfer amount 
                    confirm = input(f"Amount to Transfer Confirm: RM ")
                    if trans_amo != confirm:
                        print("Confirmation values must be the same. Please try again...")
                        continue
                    else:
                        new_bal = float(balance) - float(trans_amo)
                        acc_type = item[item.index(user_id) + 11]
                        #check final balance according to account type 
                        if acc_type == 'Savings' and new_bal < 100.00:
                            print("New Balance below minimum amount of RM 100.00\nPlease key in a suitable amount")
                            continue
                        elif acc_type == 'Current' and new_bal < 500.00:
                            print("New Balance below minimum amount of RM 500.00\nPlease key in a suitable amount")
                            continue
                        elif float(trans_amo) > float(balance):
                            print("Insufficient Account Balance to perform transaction\nPlease input suitable amount...")
                            continue
                        else:
                            with open(f'Balance/{user_id}_balance.txt', 'w') as file:
                                file.write("%s, " % new_bal)
                                file.close()
                                print("Balance Updated...")
                            with open('client_credentials.txt', 'r') as file:
                                id = file.read().split(", ")
                                if trans_acc in id:
                                    with open(f'Balance/{trans_acc}_balance.txt', 'r') as file:
                                        t_bal = file.read().split(", ")
                                        file.close()
                                    trans_bal = t_bal[0]
                                    fin_bal = float(trans_bal) + float(trans_amo)
                                    with open(f'Balance/{trans_acc}_balance.txt', 'w') as file:
                                        file.write("%s, " % fin_bal)
                                        file.close()
                                    with open(f'Balance/{user_id}_balance.txt', 'r') as money:
                                        acc = money.read().split(", ")
                                        file.close()
                                    balance = acc[0]
                                    dt = datetime.datetime.now()
                                    day = dt.strftime("%d")
                                    month = dt.strftime("%m")
                                    year = dt.strftime("%Y")
                                    curr_time = dt.strftime("%X")
                                    dt_now = f"{day}/{month}/{year} {curr_time}"
                                    #append details of transaction to both account Statement of Account 
                                    with open(f'SOA/{user_id}_SOA.txt', 'a') as file:
                                        file.write(f"\n{dt_now}\nTransfer Out:\nAccount No.: {user_id} -----> Account No.: {trans_acc}\n-RM{trans_amo}\n")
                                        file.close()
                                    with open(f'SOA/{trans_acc}_SOA.txt', 'a') as file:
                                        file.write(f"\n{dt_now}Transfer In:\nAccount No.: {user_id} -----> Account No.: {trans_acc}\n+RM {trans_amo}\n")
                                        file.close()
                                    print(f"Your Updated Account Balance is: RM {balance}\n")
                                    menu(user_id)
                                else: 
                                    print("Invalid Account Number. Please Try Again")
                                    continue
            
#allow clients to withdraw money
def withdraw(user_id):
    print("Withdrawal Menu")
    with open('client_credentials.txt', 'r') as file:
        item = file.read().split(", ")
        if user_id in item:
            salutation = item[item.index(user_id) + 1] 
            name = item[item.index(user_id) + 2]
    
    with open(f'Balance/{user_id}_balance.txt', 'r') as money:
        acc = money.read().split(", ")
        file.close()
    balance = acc[0]
    #display account balance 
    print(f"Hi, {salutation} {name}\nYour Account Balance is: RM {balance}\n")
    print("How much would you like to withdraw?")
    while True:
        withd = input("Type 'cancel' to cancel process\nAmount of Withdrawal: RM ")
        if withd == 'cancel':
            print("Thank you! Returning to menu...")
            menu(user_id)
        else:
            confirm = input(f"Amount of Withdrawal Confirm: RM ")
            if withd != confirm:
                print("Withdrawal Values must be same. Please try again...")
                continue
            else:
                with open(f'Balance/{user_id}_balance.txt', 'r') as file:
                    acc = file.read().split(", ")
                    file.close()
                bal = acc[0]
                new_bal = float(bal) - float(withd)
                with open('client_credentials.txt', 'r') as file:
                    check = file.read().split(", ")
                    file.close()
                acc_type = check[check.index(user_id) + 11]
                #check final account balance based on account type
                if acc_type == 'Savings' and new_bal < 100.00:
                    print("New Balance below minimum amount of RM 100.00\nPlease key in a suitable amount")
                    continue
                elif acc_type == 'Current' and new_bal < 500.00:
                    print("New Balance below minimum amount of RM 500.00\nPlease key in a suitable amount")
                    continue
                elif float(withd) > float(bal):
                    print("Insufficient Account Balance to perform withdrawal\nPlease input suitable amount...")
                    continue
                else: 
                    with open(f'Balance/{user_id}_balance.txt', 'w') as file:
                        file.write("%s, " % new_bal)
                        file.close()
                        print("Balance Updated...")
                    dt = datetime.datetime.now()
                    day = dt.strftime("%d")
                    month = dt.strftime("%m")
                    year = dt.strftime("%Y")
                    curr_time = dt.strftime("%X")
                    dt_now = f"{day}/{month}/{year} {curr_time}"
                    #Appending details of withdrawal to statement of account 
                    with open(f'SOA/{user_id}_SOA.txt', 'a') as file:
                        file.write(f"\n{dt_now}\nWithdrawal:\n-RM {withd}\n")
                        file.close()
                    break
    
    print(f"Your New Account Balance is: RM {new_bal}\n")
    menu(user_id)

#allow users to deposit money into account
def deposit(user_id):
    print("Deposit Menu")
    with open('client_credentials.txt', 'r') as file:
        item = file.read().split(", ")
        file.close()
    salutation = item[item.index(user_id) + 1] 
    name = item[item.index(user_id) + 2]
    
    with open(f'Balance/{user_id}_balance.txt', 'r') as money:
        acc = money.read().split(", ")
        file.close()
    balance = acc[0]
    #display account balance 
    print(f"Hi, {salutation} {name}\nYour Account Balance is: RM {balance}\nHow much would you like to deposit?\n")
    with open(f'Balance/{user_id}_balance.txt', 'r') as file:
        acc = file.read().split(", ")
        file.close()
    while True:
        dep = input("Type 'cancel' to cancel process\nAmount of Deposit: RM ")
        if dep == 'cancel':
            print("\nAlright, Thank you!\nReturning to menu...")
            menu(user_id)
        else:
            confirm = input(f"Amount of Deposit Confirm: RM ")
            if dep != confirm:
                print("Deposit amount must be same. Please try again...")
                continue
            else:
                bal = acc[0]
                new_bal = float(dep) + float(bal)
                with open(f'Balance/{user_id}_balance.txt', 'w') as file:
                    file.write("%s, " % new_bal)
                    file.close()
                    print("Balance Updated...")
                with open(f'Balance/{user_id}_balance.txt', 'r') as money:
                    acc = money.read().split(", ")
                    file.close()
                balance = acc[0]
                dt = datetime.datetime.now()
                day = dt.strftime("%d")
                month = dt.strftime("%m")
                year = dt.strftime("%Y")
                curr_time = dt.strftime("%X")
                dt_now = f"{day}/{month}/{year} {curr_time}"
                #append details of deposit to statement of account 
                with open(f'SOA/{user_id}_SOA.txt', 'a') as file:
                    file.write(f"\n{dt_now}\nDeposit:\n+RM {dep}\n")
                    file.close()
                break
    print(f"Your New Account Balance is: RM {balance}\n")
    menu(user_id)
    
#view balance of user 
def view_balance(user_id):
    print("View Balance Menu")
    with open('client_credentials.txt', 'r') as file:
        item = file.read().split(", ")
    salutation = item[item.index(user_id) + 1] 
    name = item[item.index(user_id) + 2]
    with open(f'Balance/{user_id}_balance.txt', 'r') as money:
        acc = money.read().split(", ")
        file.close()
    balance = acc[0]
    
    print(f"Hi, {salutation} {name}\nYour Account Balance is: RM {balance}\n")
    menu(user_id)

#prints client statement of account
def state_of_acc(user_id):
    print("Print Client Statement of Account Menu")
    with open('client_credentials.txt', 'r') as file:
        read = file.read().split(", ")
        file.close()
    while True:
        name = read[read.index(user_id) + 2]
        with open(f'Balance/{user_id}_balance.txt', 'r') as file:
            bal = file.read().split(", ")
            file.close()
        balance = bal[0]
        with open(f'SOA/{user_id}_SOA.txt', 'r') as file:
            soa = file.read().split(", ")
            file.close()
        #request for response of client
        request = input("Would you like to save a copy of your Statemen of Account? (Y/N)\nAnswer: ")
        if request == 'N':
            print("Alright! Have a nice day!")
            menu(user_id)
        elif request == 'Y':
            dt = datetime.datetime.now()
            day = dt.strftime("%d")
            month = dt.strftime("%m")
            sp_month = dt.strftime("%b")
            year = dt.strftime("%Y")
            curr_time = dt.strftime("%X")
            dt_now = f"{day}/{month}/{year} {curr_time}"
            while True:
                #create file for client in the SOA Downloads folder
                if not os.path.isfile(f'SOA Downloads/{user_id}_{sp_month}_SOA.txt'):
                    with open(f'SOA Downloads/{user_id}_{sp_month}_SOA.txt', 'x') as file:
                        pass
                    continue
                else:
                    with open(f'SOA Downloads/{user_id}_{sp_month}_SOA.txt', 'w') as file:
                        for i in soa:
                            file.write(i)
                        file.write(f"\n\nDate of Statement of Account: {dt_now}")
                        file.write("\n-------------------------------------------------------\n")
                        file.write(f"Final Balance:                               |RM{balance}|\n")
                        file.write("-------------------------------------------------------")
                        file.close()
                    while True:
                        #creates file for staff or admin in the SOA Database folder
                        if not os.path.isfile(f'SOA Database/{user_id}_{sp_month}_SOA.txt'):
                            with open(f'SOA Database/{user_id}_{sp_month}_SOA.txt', 'x') as file:
                                pass
                            continue
                        else:
                            with open(f'SOA Database/{user_id}_{sp_month}_SOA.txt', 'w') as file:
                                for i in soa:
                                    file.write(i)
                                file.write(f"\n\nDate of Statement of Account: {dt_now}")
                                file.write("\n-------------------------------------------------------\n")
                                file.write(f"Final Balance:                               |RM{balance}|\n")
                                file.write("-------------------------------------------------------")
                                file.close()
                            with open(f'Balance/{user_id}_balance.txt', 'r') as file:
                                bal_list = file.read().split(", ")
                                file.close()
                            with open('client_credentials.txt', 'r') as file:
                                acc_list = file.read().split(", ")
                                file.close()
                            bal = bal_list[0]
                            user_acc_type = acc_list[acc_list.index(user_id) + 11]
                            with open(f'SOA/{user_id}_SOA.txt', 'w') as file:
                                file.write(f"Client Name: {name}\nAccount No.: {user_id}\nAccount Type: {user_acc_type}\nDate & Time: {dt_now}\n")
                                file.write("\n-------------------------------------------------------\n")
                                file.write(f"Original/Carried Balance:                    |RM{bal}|\n")
                                file.write("-------------------------------------------------------")
                                file.close()
                            print("Statement of Account has been saved to the 'SOA Downloads' folder\nThank you for choosing us!\n")
                            print("Returning to menu...")
                            menu(user_id)
        else:
            print("Invalid Response. Please try again...")
            continue

#Saving client's statement of account for staff or admin
def state_of_acc_for_staff(user_id):
    print("Print Client Statement of Account Menu")
    with open('client_credentials.txt', 'r') as file:
        read = file.read().split(", ")
        file.close()
    while True:
        #request for user account number
        acc_num = input("Type 'cancel' to cancel process\nClient Account Number: ")
        if acc_num == 'cancel':
            print("Returning to menu...")
            with open('staff_credentials.txt', 'r') as file:
                staff = file.read().split(", ")
                file.close()
            if user_id in staff:
                staff_menu()
            else:
                super_user_menu()
        elif acc_num in read:
            while True:
                name = read[read.index(acc_num) + 2]
                with open(f'Balance/{acc_num}_balance.txt', 'r') as file:
                    bal = file.read().split(", ")
                    file.close()
                balance = bal[0]
                with open(f'SOA/{acc_num}_SOA.txt', 'r') as file:
                    soa = file.read().split(", ")
                    file.close()
                #request for response from user for cancellation or process proceed 
                request = input("Would you like to save a copy of your Statemen of Account? (Y/N)\nAnswer: ")
                if request == 'N':
                    print("Alright! Have a nice day!\nReturning to menu...")
                    with open('staff_credentials.txt', 'r') as file:
                        staff = file.read().split(", ")
                        file.close()
                    if user_id in staff:
                        staff_menu()
                    else:
                        super_user_menu()
                elif request == 'Y':
                    dt = datetime.datetime.now()
                    day = dt.strftime("%d")
                    month = dt.strftime("%m")
                    sp_month = dt.strftime("%b")
                    year = dt.strftime("%Y")
                    curr_time = dt.strftime("%X")
                    dt_now = f"{day}/{month}/{year} {curr_time}"
                    while True:
                        #Create file in SOA Database folder for staff or admin
                        if not os.path.isfile(f'SOA Database/{acc_num}_{sp_month}_SOA.txt'):
                            with open(f'SOA Database/{acc_num}_{sp_month}_SOA.txt', 'x') as file:
                                pass
                            continue
                        else:
                            with open(f'SOA Database/{acc_num}_{sp_month}_SOA.txt', 'w') as file:
                                for i in soa:
                                    file.write(i)
                                file.write(f"\n\nDate of Statement of Account: {dt_now}")
                                file.write("\n-------------------------------------------------------\n")
                                file.write(f"Final Balance:                               |RM{balance}|\n")
                                file.write("-------------------------------------------------------")
                                file.close()
                            with open(f'Balance/{acc_num}_balance.txt', 'r') as file:
                                bal_list = file.read().split(", ")
                                file.close()
                            with open('client_credentials.txt', 'r') as file:
                                acc_list = file.read().split(", ")
                                file.close()
                            bal = bal_list[0]
                            user_acc_type = acc_list[acc_list.index(acc_num) + 11]
                            with open(f'SOA/{acc_num}_SOA.txt', 'w') as file:
                                file.write(f"Client Name: {name}\nAccount No.: {acc_num}\nAccount Type: {user_acc_type}\nDate & Time: {dt_now}\n")
                                file.write("\n-------------------------------------------------------\n")
                                file.write(f"Original/Carried Balance:                    |RM{bal}|\n")
                                file.write("-------------------------------------------------------")
                                file.close()
                            print("Statement of Account has been saved to the SOA Database Folder\nThank you for choosing us!\n")
                            print("Returning to menu...")
                            menu(user_id)
                else:
                    print("Invalid Response. Please try again...")
                    continue
        else:
            print("Client Account Number Not Found. Please try again...")
            continue

#will run function every day but only make changes when the date is "01"
def auto_soa(arr):
    dt = datetime.datetime.now()
    day = dt.strftime("%d")
    month = dt.strftime("%m")
    sp_month = dt.strftime("%b")
    year = dt.strftime("%Y")
    curr_time = dt.strftime("%X")
    dt_now = f"{day}/{month}/{year} {curr_time}"
    if day == '01' and len(arr) != 0:
        ind = 0
        acc_num = arr[ind]
        with open(f'SOA/{acc_num}_SOA.txt', 'r') as file:  
            user_soa = file.read().split(", ")
            file.close()
        with open(f'Balance/{acc_num}_balance.txt', 'r') as file:
            bal = file.read().split(", ")
            file.close()
        with open('client_credentials.txt', 'r') as file:
            search = file.read().split(", ")
            file.close()
        balance = bal[0]
        name = search[search.index(acc_num) + 2]
        while True:
            if not os.path.isfile(f'SOA Database/{acc_num}_{sp_month}_SOA.txt'):
                with open(f'SOA Database/{acc_num}_{sp_month}_SOA.txt', 'x') as file:
                    pass
                continue
            else:
                with open(f'SOA Database/{acc_num}_{sp_month}_SOA.txt', 'w') as file:
                    for i in user_soa:
                        file.write(i)
                    file.write(f"\n\nDate of Statement of Account: {dt_now}")
                    file.write("\n-------------------------------------------------------\n")
                    file.write(f"Final Balance:                               |RM{balance}|\n")
                    file.write("-------------------------------------------------------")
                    file.close()
                with open(f'Balance/{acc_num}_balance.txt', 'r') as file:
                    bal_list = file.read().split(", ")
                    file.close()
                with open('client_credentials.txt', 'r') as file:
                    acc_list = file.read().split(", ")
                    file.close()
                bal = bal_list[0]
                user_acc_type = acc_list[acc_list.index(acc_num) + 11]
                with open(f'SOA/{acc_num}_SOA.txt', 'w') as file:
                    file.write(f"Client Name: {name}\nAccount No.: {acc_num}\nAccount Type: {user_acc_type}\nDate & Time: {dt_now}\n")
                    file.write("\n-------------------------------------------------------\n")
                    file.write(f"Original/Carried Balance:                    |RM{bal}|\n")
                    file.write("-------------------------------------------------------")
                    file.close()
                break
        del arr[ind]
        auto_soa(arr)
    else:
        pass

#view details of user account 
def view_details(user_id):
    print("Details Viewing Menu")
    with open('client_credentials.txt', 'r') as file:
        client = file.read().split(", ")
        file.close()
    with open('staff_credentials.txt', 'r') as file:
        staff = file.read().split(", ")
        file.close()
    with open('admin_credentials.txt', 'r') as file:
        admin = file.read().split(", ")
        file.close()
    #view details for client account
    if user_id in client:
        salu = client[client.index(user_id) + 1]
        name = client[client.index(user_id) + 2]
        print(f"Welcome, {salu}{name}")
        print(f"Account Number: {user_id}\nSalutation: {salu}")
        print(f"First Name: {name}\nLast Name: {client[client.index(user_id) + 3]}")
        print(f"Age: {client[client.index(user_id) + 4]}\nNationality: {client[client.index(user_id) + 5]}")
        print(f"ID Card No./Passport No.: {client[client.index(user_id) + 6]}\nDate of Birth: {client[client.index(user_id) + 7]}")
        print(f"Phone Number: {client[client.index(user_id) + 8]}\nAddress: {client[client.index(user_id) + 9]}")
        print(f"Occupation: {client[client.index(user_id) + 10]}\nAccount Type: {client[client.index(user_id) + 11]}\n")
        print("Returning to menu...")
        menu(user_id)
    #view details for staff account
    elif user_id in staff and user_id not in client:
        salu = staff[staff.index(user_id) + 1]
        name = staff[staff.index(user_id) + 2]
        print(f"Welcome, {salu}{name}")
        print(f"Account Number: {user_id}\nSalutation: {salu}")
        print(f"First Name: {name}\nLast Name: {staff[staff.index(user_id) + 3]}")
        print(f"Age: {staff[staff.index(user_id) + 4]}\nNationality: {staff[staff.index(user_id) + 5]}")
        print(f"ID Card No./Passport No.: {staff[staff.index(user_id) + 6]}\nDate of Birth: {staff[staff.index(user_id) + 7]}")
        print(f"Phone Number: {staff[staff.index(user_id) + 8]}\nAddress: {staff[staff.index(user_id) + 9]}")
        print(f"Staff Position: {staff[staff.index(user_id) + 10]}\n")
        print("Returning to menu...")
        staff_menu(user_id)
    #view details for admin account
    elif user_id in admin and user_id not in client and user_id not in staff:
        salu = admin[admin.index(user_id) + 1]
        name = admin[admin.index(user_id) + 2]
        print(f"Welcome, {salu}{name}")
        print(f"Account Number: {user_id}\nSalutation: {salu}")
        print(f"First Name: {name}\nLast Name: {admin[admin.index(user_id) + 3]}")
        print(f"Age: {admin[admin.index(user_id) + 4]}\nNationality: {admin[admin.index(user_id) + 5]}")
        print(f"ID Card No./Passport No.: {admin[admin.index(user_id) + 6]}\nDate of Birth: {admin[admin.index(user_id) + 7]}")
        print(f"Phone Number: {admin[admin.index(user_id) + 8]}\nAddress: {admin[admin.index(user_id) + 9]}")
        print("Returning to menu...")
        super_user_menu(user_id)

#allow staff or admin to unlock a user's account
def acc_lock(user_id):
    print("Unlock User Account Menu")
    with open('client_credentials.txt', 'r') as file:
        client = file.read().split(", ")
        file.close()
    with open('staff_credentials.txt', 'r') as file:
        staff = file.read().split(", ")
        file.close()
    with open('admin_credentials.txt', 'r') as file:
        admin = file.read().split(", ")
        file.close()
    while True:
        acc_num = input("User Account Number: ")
        if acc_num in client:
            client_ind = client.index(acc_num) + 1
            if client[client_ind] != "Account Locked":
                print("Account is not locked")
                break
            else:
                del client[client_ind]
                with open('client_credentials.txt', 'w') as file:
                    for i in client:
                        file.write("%s, " % i)
                    file.close() 
                print("Account Unlocked")
                break
        elif acc_num not in client and acc_num in staff:
            staff_ind = staff.index(acc_num) + 1
            if staff[staff_ind] != "Account Locked":
                print("Account is not locked")
                break
            else:
                del staff[staff_ind]
                with open('staff_credentials.txt', 'w') as file:
                    for i in staff:
                        file.write("%s, " % i)
                    file.close() 
                print("Account Unlocked")
                break
        elif acc_num not in client and acc_num not in staff and acc_num in admin:
            admin_ind = admin.index(acc_num) + 1
            if admin[admin_ind] != "Account Locked":
                print("Account is not locked")
                break
            else:
                del admin[admin_ind]
                with open('admin_credentials.txt', 'w') as file:
                    for i in admin:
                        file.write("%s, " % i)
                    file.close() 
                print("Account Unlocked")
                break
        else:
            print("Invalid Account ID. Please try again...")
            continue
    
    with open('staff_credentials.txt', 'r') as file:
        staff = file.read().split(", ")
        file.close()
    if user_id in staff:
        print("\nReturning to menu...\n")
        staff_menu(user_id)
    else:
        print("\nReturning to menu...\n")
        super_user_menu(user_id)

#This function will only be accessed by client accounts
#It contains a few more subfunctions that will provide the clients with
#the necessary services
#Upon entry, it will display name and salutation of client according to Client ID
def menu(user_id):
    with open('client_credentials.txt', 'r') as file:
        item = file.read().split(", ")
        file.close()
        salutation = item[item.index(user_id) + 1] 
        name = item[item.index(user_id) + 2]
        print(f"Welcome Back, {salutation} {name}\n")
        while True:
            print("What type of service would you require?\n1. Transfer\n2. Withdrawal\n3. Deposit\n4. View Balance")
            print("5. Change your password\n6. Display Statement Of Account\n7. View Your Details\n")
            print("Type 'exit' to exit application.\n")
            ans = input("Request: ")
            if ans == '1':
                print("\n")
                transfer(user_id)
            elif ans == '2':
                print("\n") 
                withdraw(user_id)
            elif ans == '3':
                print("\n")
                deposit(user_id)
            elif ans == '4':
                print("\n")
                view_balance(user_id)
            elif ans == "5":
                print("\n")
                change_client_pw(user_id)
            elif ans == '6':
                print("\n")
                state_of_acc(user_id)
            elif ans == '7':
                print("\n")
                view_details(user_id)
            elif ans == 'exit':
                print("\n\nThank you for choosing us.\nWe hope to see you again soon.\nHave a great day!\n")
                login()
            else:
                print("Invalid Response. Please Try Again.")
                continue
    
#This function will only be accessed by staff accounts
#It contains a few more subfunctions that will facilitate the staff in their work
#Upon entry, it will display name and salutation of staff according to Staff ID
def staff_menu(user_id):
    with open('staff_credentials.txt', 'r') as file:
        item = file.read().split(", ")
        file.close()
        salutation = item[item.index(user_id) + 1] 
        name = item[item.index(user_id) + 2]
        print(f"Welcome Back, {salutation} {name}\n")
    with open('count.txt', 'r') as file:
        count = file.read().split(", ")
        file.close()
    if count[0] == '1':
        pass
    else:
        num = []
        with open('client_credentials.txt', 'r') as file:
            client = file.read().split(", ")
            file.close()
        while True:
            if len(client) != 0:
                num.append(client[1])
                del client[0:13]
                continue
            break
        auto_soa(num)
        with open('count.txt', 'w') as file:
            today = datetime.datetime.now()
            day = today.strftime("%d")
            file.write('1, ')
            file.write(day)
            file.close()
    while True:
        print("What type of service would you require?\n1. Create new client account\n2. Change client account password")
        print("3. Change client details\n4. Create new staff account\n5. View Your Details")
        print("6. Print Client Statement of Account\n7. Unlock Account\n")
        print("Type 'exit' to exit application.\n")
        ans = input("Request: ")
        if ans == '1':
            print("\n")
            new_acc_client(user_id)
        elif ans == '2': 
            print("\n")
            change_client_pw_for_staff(user_id)
        elif ans == '3':
            print("\n")
            client_details(user_id)
        elif ans == '4':
            with open('staff_credentials.txt', 'r') as file:
                lists = file.read().split(", ")
                file.close()
            if "Manager" in lists:
                print("\n")
                new_acc_staff(user_id)
            else:
                print("Access Denied")
                continue
        elif ans == '5':
            print("\n")
            view_details(user_id)
        elif ans == '6':
            print("\n")
            state_of_acc_for_staff(user_id)
        elif ans == '7':
            print("\n")
            acc_lock(user_id)
        elif ans == 'exit':
            print("\n\nThank you for choosing us.\nWe hope to see you again soon.\nHave a great day!\n")
            login()
        else:
            print("Invalid Response. Please Try Again.")
            continue
    
#This function will only be accessed by administrator accounts
#It contains a few more subfunctions that will facilitate the admin in their work
#Upon entry, it will display name and salutation of admin according to Admin ID
def super_user_menu(user_id):
    with open('admin_credentials.txt', 'r') as file:
        item = file.read().split(", ")
        file.close()
        salutation = item[item.index(user_id) + 1] 
        name = item[item.index(user_id) + 2]
        print(f"Welcome Back, {salutation} {name}\n")
    while True:
        print("What type of service would you require?\n1. Create new Client Account\n2. Change Client Account Password")
        print("3. Change Client Details\n4. Create new Staff Account\n5. Change Staff Account password")
        print("6. Change Staff details\n7. Change Admin Password\n8. Creating new Admin Account\n9. Change Admin Details")
        print("10. View Your Details\n11. Unlock Account\n12. Print Client Statement of Account\n")
        print("Type 'exit' to exit application.\n")
        ans = input("Request: ")
        if ans == '1':
            print("\n")
            new_acc_client(user_id)
        elif ans == '2': 
            print("\n")
            change_client_pw_for_staff(user_id)
        elif ans == '3':
            print("\n")
            client_details(user_id)
        elif ans == '4':
            print("\n")
            new_acc_staff(user_id)
        elif ans == '5':
            print("\n")
            change_staff_pw(user_id)
        elif ans == '6':
            print("\n")
            staff_details(user_id)
        elif ans == "7":
            print("\n")
            change_admin_pw(user_id)
        elif ans == "8":
            print("\n")
            new_acc_admin(user_id)
        elif ans == '9':
            print("\n")
            admin_details(user_id)
        elif ans == '10':
            print("\n")
            view_details(user_id)
        elif ans == '11':
            print("\n")
            acc_lock(user_id)
        elif ans == '12':
            print("\n")
            state_of_acc_for_staff(user_id)
        elif ans == 'exit':
            print("\nThank you for choosing us.\nWe hope to see you again soon.\nHave a great day!\n")
            login()
        else:
            print("Invalid Response. Please Try Again.")
            continue

#Upon entry, it will check if user is client, admin, or staff and proceed to ask for credentials
#Credentials will be compared to database in text files for validation
#If credentials are correct, respective menu functions will run
def login():
    while True: 
        print("Welcome Back User!")
        count = 0
        while count < 3: 
            user_id = input("User ID: ")
            user_pw = input("Password: ")
            with open('client_idpw_list.txt', 'r') as file:
                idpw_list = file.read().split(", ")
                file.close()
            with open('staff_idpw_list.txt', 'r') as file:
                staff_list = file.read().split(", ")
                file.close()
            with open('admin_idpw_list.txt', 'r') as file:
                admin_list = file.read().split(", ")
                file.close()
            with open('client_credentials.txt', 'r') as file:
                client_lock = file.read().split(", ")
                file.close()
            with open('staff_credentials.txt', 'r') as file:
                staff_lock = file.read().split(", ")
                file.close()
            with open('admin_credentials.txt', 'r') as file:
                admin_lock = file.read().split(", ")
                file.close()
            if user_id in idpw_list:
                acc_lock = client_lock.index(user_id) + 1
                if client_lock[acc_lock] == "Account Locked":
                    print("Account has been locked, please contact staff for assistance...")
                    exit()
                elif user_pw in idpw_list:
                    file.close()
                    print("Login Succesful\n")
                    menu(user_id)
                else:
                    print("Either your ID or Password is incorrect.\nPlease Try Again\n")
                    count += 1
                    continue
            elif user_id in staff_list:
                acc_staff_lock = staff_lock.index(user_id) + 1
                if staff_lock[acc_staff_lock] == "Account Locked":
                    print("Account has been locked, please contact staff for assistance...")
                    exit()
                elif user_pw in staff_list:
                    file.close()
                    print("Login Successful\n")
                    staff_menu(user_id)
                else:
                    print("Either your ID or Password is incorrect.\nPlease Try Again\n")
                    count += 1
                    continue
                    
            elif user_id in admin_list:
                acc_admin_lock = admin_lock.index(user_id) + 1
                if admin_lock[acc_admin_lock] == "Account Locked":
                    print("Account has been locked, please contact staff for assistance...")
                    exit()
                if user_pw in admin_list:
                    file.close()
                    print("Login Successful\n")
                    super_user_menu(user_id)
                else:
                    print("Either your ID or Password is incorrect.\nPlease Try Again\n")
                    count += 1
                    continue
            else:
                print("Account ID not found. Please try again...")
                continue

        else:
            #Locks user's account by adding "Account Locked" into account details text file database
            print("Account Lcoked. Please contact staff for account retrieval") 
            if user_id in client_lock:
                ind = client_lock.index(user_id) + 1
                client_lock.insert(ind, "Account Locked")
                with open('client_credentials.txt', 'w') as file:
                    for i in client_lock:
                        file.write("%s, " % i)
                    file.close()
            elif user_id in staff_lock:
                ind = staff_lock.index(user_id) + 1
                staff_lock.insert(ind, "Account Locked")
                with open('staff_credentials.txt', 'w') as file:
                    for i in staff_lock:
                        file.write("%s, " % i)
                    file.close()
            elif user_id in admin_lock:
                ind = admin_lock.index(user_id) + 1
                admin_lock.insert(ind, "Account Locked")
                with open('admin_credentials.txt', 'w') as file:
                    for i in admin_lock:
                        file.write("%s, " % i)
                    file.close()
            else:
                pass
            exit()

'''with open('count.txt', 'r') as file:
    new_day = file.read().split(", ")
    file.close()
curr = datetime.datetime.now()
new = curr.strftime("%d")'''
#create "Balance" folder 
if not os.path.exists('Balance'):
    os.makedirs('Balance')
#create "SOA" folder
if not os.path.exists('SOA'):
    os.makedirs('SOA')
#create "SOA Database" folder
if not os.path.exists('SOA Database'):
    os.makedirs('SOA Database')
#create "SOA Downloads" folder
if not os.path.exists('SOA Downloads'):
    os.makedirs('SOA Downloads')
#rewrite 'count.txt' to determine running of auto_soa function
'''if int(new_day[1]) < int(new):
    new_day.pop()
    del new_day[1]
    new_day.append(new)
    with open('count.txt', 'w') as file:
        for i in new_day:
            file.write(i)
        file.close()
else:
    pass'''
login()