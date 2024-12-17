
import pandas as pd

stu_df = pd.read_csv("students.csv") #s student
book_df = pd.read_csv("booking.csv") #b booking

list_lecture = ['IT301', 'IT302', 'IT303', 'IT304']
list_lab = ['LAB103', 'LAB104', 'LAB105', 'LAB106']

def welcome():
    print('MUICT Student Room Booking System first name')
    print(' 1. print a list of students')
    print(' 2. submit a booking request')
    print(' 3. check the current booking via room number')
    print(' 4. check the available rooms via date')
    print(' 5. check booking with student ID')
    print(' 6. check booking with student first name')
    print(' 7. print booking summary')
    print(' 0. exit')
    n = input('Option: ')
    return n


def check(item,type,room_type='None'):
    if type == 'id':
        if item in stu_df['id'].values:
            return True
    
    if type == 'date':
        if len(item) == 10 and item[2] == '-' and item[5] == '-': #format
            date = item.split('-')
            if date[0] > '00' and date[1] > '00' and date[1] <= '12' and date[2] > '0000': #not zero
                if date[1] == '02' and (date[0] < '29' or (date[0] == '29' and int(date[2])%4 == 0)): #FEB
                    return True
                elif date[1] in ['04','06','09','11'] and date[0]<='30': #30 days
                    return True
                elif date[1] not in ['04','06','09','11','02'] and date[0]<='31': #31 days
                    return True
                
    if type == 'room':
        if (item in list_lecture and room_type == 'Lecture') or (item in list_lab and room_type == 'Lab'):
            return True
        elif room_type == 'None' and (item in list_lecture or item in list_lab):
            return True

# print(check(input(),input()))

def print_a_list_of_students(): #1
    print(stu_df)

def submit_a_booking_request(): #2
    uid = int(input('ID: '))
    while check(uid,'id') is not True:
        print('Invalid ID')
        uid = int(input('ID: '))

    room_type = input('Room types (Lecture/Lab): ')
    if room_type == 'Lecture':
        print(f'Room: {list_lecture}')
    elif room_type == 'Lab':
        print(f'Room: {list_lab}')
    Room = input('Please choose one room above: ')
    while check(Room,'room',room_type) is not True:
        print('Room not found')
        Room = input('Please select another room: ')

    book_date = input('Booking date (DD-MM-YYYY): ')
    while check(book_date,'date') is not True:
        print('Invalid date')
        book_date = input('Booking date (DD-MM-YYYY): ')

    if len(book_df[(book_df['Date'].isin([book_date]))&(book_df['Room'].isin([Room]))]['Date'].to_dict()) != 0:
        print(f"{Room} is not available on {book_date}")
    else:
        book_df.loc[len(book_df.index)] = [Room,book_date,uid]
        book_df.to_csv('booking.csv',index = False)

# submit_a_booking_request()

def check_the_current_booking_via_room_number(): #3
    Room = input('Room number: ')
    while check(Room,'room') is not True:
        print('Room not found')
        Room = input('Please select another room: ')
    print('Current booking:')
    booked = book_df[book_df['Room'].isin([Room])]
    if len(booked['Room'].to_list()) == 0:
        print(' No booking')
    else:
        for i in range(len(booked['Room'].to_list())):
            print(f" Date: {(booked['Date'].to_list())[i]} Student ID: {(booked['ID'].to_list())[i]}")


# check_the_current_booking_via_room_number()

def check_the_available_rooms_via_date(): #4
    lst1 = ['IT301', 'IT302', 'IT303', 'IT304']
    lst2 = ['LAB103', 'LAB104', 'LAB105', 'LAB106']
    Date = input('Checking date (DD-MM-YYYY): ')
    print('Available rooms:')
    for i in book_df[book_df['Date'].isin([Date])]['Room'].to_list():
        if i in lst1:
            lst1.remove(i)
        elif i in lst2:
            lst2.remove(i)
    print(f' Lecture: {lst1}')
    print(f' Lab: {lst2}')


def check_booking_with_student_ID(): #5
    uid = int(input('ID: '))
    while check(uid,'id') is not True:
        print('Invalid ID')
        uid = int(input('ID: '))
    print('Current bookings:')
    room_booked = book_df[book_df['ID'].isin([uid])]
    if len(room_booked['ID'].to_list()) == 0:
        print('  No booking')
    else:
        room = room_booked['Room'].to_list()
        date = room_booked['Date'].to_list()
        for i in range(len(room)):
            print(f"  Room: {room[i]} Date: {date[i]}")


def check_booking_with_student_first_name(): #6
    fn = input('Firstname: ')
    fn_l = fn.lower()
    fn_c = fn.capitalize()
    found = stu_df[stu_df['fname'].str.contains(fn) | stu_df['fname'].str.contains(fn_c) | stu_df['fname'].str.contains(fn_l)]
    if len(found['id'].to_list()) == 0:
        print('There is no student found.')
    else:
        name = found['fname'].to_list()
        uid = found['id'].to_list()
        for i in range(len(uid)):
            print(uid[i], name[i])
            booking = book_df[book_df['ID'].isin([uid[i]])]
            if len(booking['ID'].to_list()) == 0:
                print('  No booking')
            else:
                print('  Current bookings:')
                for i in range(len(booking['ID'].to_list())):
                    print(f"    Room: {(booking['Room'].to_list())[i]} Date: {(booking['Date'].to_list())[i]}")

def print_booking_summary(): #7
    #Lecture
    print('Lecture:')
    for i in range(len(list_lecture)):
        print(f'  {list_lecture[i]}:')
        booked = book_df[book_df['Room'].isin([list_lecture[i]])]
        if len(booked['Room'].to_list()) == 0:
            print('    No booking')
        else:
            for i in range(len(booked['Room'].to_list())):
                print(f"    Date: {(booked['Date'].to_list())[i]} Student ID: {(booked['ID'].to_list())[i]}")

    #Lab
    print('Lab:')
    for i in range(len(list_lab)):
        print(f'  {list_lab[i]}:')
        booked = book_df[book_df['Room'].isin([list_lab[i]])]
        if len(booked['Room'].to_list()) == 0:
            print('    No booking')
        else:
            for i in range(len(booked['Room'].to_list())):
                print(f"    Date: {(booked['Date'].to_list())[i]} Student ID: {(booked['ID'].to_list())[i]}")


# print_booking_summary()

option = welcome()
while option != '0':
  if option == '1':
    print_a_list_of_students()
  elif option == '2':
    submit_a_booking_request()
  elif option == '3':
    check_the_current_booking_via_room_number()
  elif option == '4':
    check_the_available_rooms_via_date()
  elif option == '5':
    check_booking_with_student_ID()
  elif option == '6':
    check_booking_with_student_first_name()
  elif option == '7':
    print_booking_summary()
  print('===================')
  option = welcome() 
else:
  print('Program close')