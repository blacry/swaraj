#heloo 

import misc
import room_perks
import Bill
import rooms


def room_booking():
    try:
        n = int(input('How many rooms do you want to book? : '))
    except ValueError:
        misc.correct(room_booking)
    
    for i in range(n):
        print('What kind of room do you want to book?')
        print('1.Single Room')
        print('2.Double Room')
        print('3.Twin Room')
        print('4.Family Room')
        print('5.Luxuary Room')
        print('if you want to know the perks of all the rooms, PRESS ENTER <==')    
        room_choice=input('Enter your choice:')
        if room_choice:
            price,roomno = priceDetails(int(room_choice))
        else:
            room_perks.perks()
            room_booking()
        customer_name, customer_email, customer_phone, customer_check_in, customer_check_out = customerDetails()
        cid = c_id()
            
        import mysql.connector as sqlcon
        con = sqlcon.connect( host="sql12.freesqldatabase.com",user="sql12753911",passwd="vXHHHP8jFP",database='sql12753911',auth_plugin="mysql_native_password" )
        cursor=con.cursor()

        query="insert into customerinfo values({},'{}','{}',{},'{}','{}')".format( cid , customer_name, customer_email, customer_phone, customer_check_in, customer_check_out)
        cursor.execute(query)
        con.commit()

        rooms.roomassigner(roomno,cid,customer_check_out)
        Bill.bill(cid,customer_name,customer_email,customer_phone,customer_check_in,customer_check_out,price,roomno)

    print('Thank you for booking with SWARAJ! Your booking has been successfully completed')

def priceDetails(choice):
    if choice==1:
        a = input('Your room will be of ₹ 1000 , Press 1 to confirm & Press 2 to cancel')
        if a == "1":
            room_no=rooms.roomfinder(choice)
            return 1000,room_no
        
        elif a == '2':
            print('Request cancelled')
            room_booking()
        else:
            priceDetails(choice)

    if choice==2:
        a = input('Your room will be of ₹ 2000 , Press 1 to confirm & Press 2 to cancel ')
        if a == "1":
            room_no=rooms.roomfinder(choice)
            return 2000,room_no
        elif a == "2":
            print('Request cancelled')
            room_booking()
        else:
            priceDetails(choice)

    if choice==3:
        a = input('Your room will be of ₹ 4000 , Press 1 to confirm & Press 2 to cancel ')  
        if a == "1":
            room_no=rooms.roomfinder(choice)
            return 4000,room_no
        elif a == "2":
            print('Request cancelled')
            room_booking()
        else:
            priceDetails(choice)

    if choice==4:
        a = input('Your room will be of ₹ 6000 , Press 1 to confirm & Press 2 to cancel ')
        if a == "1":
            room_no=rooms.roomfinder(choice)
            return 6000,room_no
        elif a == "2":
            print('Request cancelled')
            room_booking()
        else:
            priceDetails(choice)
    if choice==5:
        a = input('Your room will be of ₹ 10000 , Press 1 to confirm & Press 2 to cancel ')
        if a == "1":
            room_no=rooms.roomfinder(choice)
            return 10000,room_no
        elif a == "2":
            print('Request cancelled')
            room_booking()
        else:
            priceDetails(choice)
    else:
        misc.correct(room_booking)
   
def customerDetails():
    while True:
        print('Enter your details')

        # Name
        name = input('Enter your name: ').strip()
        if not name:
            print("Name cannot be empty. Please try again.")
            continue

        # Email
        email = input('Enter your email address: ').strip()
        if not ("@gmail.com" in email):
            print("Please enter a valid Gmail address.")
            continue

        # Phone
        phone = input('Enter your phone number (10 digits): ').strip()
        if not (phone.isdigit() and len(phone) == 10 and int(phone) != 0):
            print("Invalid phone number! Please enter a correct number.")
            continue
        
        phone = int(phone)

        # Check-in and Check-out Dates
        check_in = input('Enter the check-in date (YYYY-MM-DD): ').strip()
        if not check_in:
            print("Check-in date cannot be empty. Please try again.")
            continue

        check_out = input('Enter the check-out date (YYYY-MM-DD): ').strip()
        if not check_out:
            print("Check-out date cannot be empty. Please try again.")
            continue

        # Confirmation of data
        print("\nPlease confirm your details:")
        print("Name: {}".format(name))
        print("Email: {}".format(email))
        print("Phone: {}".format(phone))
        print("Check-in Date: {}".format(check_in))
        print("Check-out Date: {}".format(check_out))

        confirmation = input("Is this information correct? (yes/no): ").strip().lower()
        if confirmation == 'yes':
            break
        else:
            print("Let's re-enter your details.\n")

    return name, email, phone, check_in, check_out

def c_id():
    import random
    import mysql.connector as sqlcon
    
    cid=random.randint(10000000,99999999)

    con = sqlcon.connect( host="sql12.freesqldatabase.com",user="sql12753911",passwd="vXHHHP8jFP",database='sql12753911',auth_plugin="mysql_native_password" )
    cursor=con.cursor()

    check = "select c_id from customerinfo where c_id ={}".format(cid)
    cursor.execute(check)
    check = cursor.fetchall()

    if check:
         cid = c_id()
    return cid

def cancelBooking():
    print('Enter your customer id:')
    try:
        cid = int(input())
    except ValueError:
        misc.correct(cancelBooking)
    
    import mysql.connector as sqlcon
    con = sqlcon.connect( host="sql12.freesqldatabase.com",user="sql12753911",passwd="vXHHHP8jFP",database='sql12753911',auth_plugin="mysql_native_password" )
    cursor=con.cursor()
    query="DELETE FROM customerinfo WHERE c_id = {}".format(cid)
    cursor.execute(query)
    print('cursor , fetched => ', cursor , cursor.fetchall())
    print('Booking Cancelled')
    con.commit()
    cursor.close()
    con.close()

def viewCustomers():
    
    import mysql.connector as sqlcon
    con = sqlcon.connect( host="sql12.freesqldatabase.com",user="sql12753911",passwd="vXHHHP8jFP",database='sql12753911',auth_plugin="mysql_native_password" )
    cursor=con.cursor()
    cursor.execute('select * from customerinfo')
    for i in cursor.fetchall(): 
        print(i)
