age = int(input("Enter age: "))
gender = input("Enter gender (M/F): ")
membership_type = input("Enter membership type (Monthly/Yearly): ")
if age >= 18 and age < 30:
    if gender == 'M':
        if membership_type == 'Monthly':
            print("Rs50")
        elif membership_type == 'Yearly':
            print("Rs500")
    elif gender == 'F':
        if membership_type == 'Monthly':
            print("Rs45")
        elif membership_type == 'Yearly':
            print("Rs450")
elif age >= 30 and age <= 50:
    if membership_type == 'Monthly':
        print("Rs60")
    elif membership_type == 'Yearly':
        print("Rs600")
elif age > 50:
    if membership_type == 'Monthly':
        print("Rs40")
    elif membership_type == 'Yearly':
        print("Rs400")