
nic = None

print("Enter Your Name: ", end='')
name = input()
names = []

name_1 = name.isdigit()

if len(name) > 0 and name_1 == False:
    name = name.lower()
    print("Hi " + name.title() + " Welcome to M1 School")
    print("Enter Your NIC Number: ", end='')
    nic = input()
    nics = []
    name1 = names.append(name)
    nic1 = nics.append(nic)

else:
    print("Invalid Input")
    exit()

mid_number = None
year = None

if len(nic) == 12 and nic.isdigit():
    year = int(nic[0:4])
    mid_number = int(nic[4:7])

elif len(nic) == 10:
    v = nic[9]
    if v == 'v' or v == 'V':
        year = int(nic[0:2]) + 1900
        mid_number = int(nic[2:5])

else:
    print("Invalid Input")
    exit()

gender = None

if 500 < mid_number <= 866:
    gender = "Miss."
    mid_number = mid_number - 500
elif 0 < mid_number <= 366:
    gender = "Mr."
else:
    print("Invalid Input")
    exit()

month_n = None
day = None
month = None

if year > 1960:
    year_1 = year / 4
    year_2 = type(year_1)
    if year_2 == int:
        month_n = [31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335, 366]
    elif year_2 == float:
        month_n = [31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]
    else:
        print("Invalid Input")
        exit()

else:
    print("Invalid Input")
    exit()

months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June',
          7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}

if mid_number <= month_n[0]:
    month = 1
    day = mid_number
elif mid_number <= month_n[1]:
    month = 2
    day = mid_number - month_n[0]
elif mid_number <= month_n[2]:
    month = 3
    day = mid_number - month_n[1]
elif mid_number <= month_n[3]:
    month = 4
    day = mid_number - month_n[2]
elif mid_number <= month_n[4]:
    month = 5
    day = mid_number - month_n[3]
elif mid_number <= month_n[5]:
    month = 6
    day = mid_number - month_n[4]
elif mid_number <= month_n[6]:
    month = 7
    day = mid_number - month_n[5]
elif mid_number <= month_n[7]:
    month = 8
    day = mid_number - month_n[6]
elif mid_number <= month_n[8]:
    month = 9
    day = mid_number - month_n[7]
elif mid_number <= month_n[9]:
    month = 10
    day = mid_number - month_n[8]
elif mid_number <= month_n[10]:
    month = 11
    day = mid_number - month_n[9]
elif mid_number <= month_n[11]:
    month = 12
    day = mid_number - month_n[10]
else:
    print("Invalid Input")
    exit()

day = day - 1
month = months.get(month)

brith_day = [month, day, year]
brith_days = []
brith_day1 = brith_days.append(brith_day)

print("Hi, " + gender + name.title() + " Your Birthday is " + month + " " + str(day) + ", " + str(year))
