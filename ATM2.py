







import random





database = {
    3372291257: ["Seyi","Onifade","seyi@zuri.team","password", 200]
}


def init():
    print("Welcome to SterlingBank")

    have_account = int(input("Do you have account with us?: 1(yes) 2 (no) \n"))

    if have_account == 1:

        login()

    elif have_account == 2:

        register()

    else:
        print("you have sselected invalid option")

        init()

def login():
    print("********* Login *********")

    account_number_from_user = int(input("What is your account number? \n"))
    password = input("What is your password? \n")

    for accountNumber, userDetails in database.items():
        if(accountNumber == accountNumberFromUser):
            if(userdetails[3] == password):
                bankOperation(userDetails)

    print("Invalid account or password")
    login()

def register():
    print("********* Login *********")


    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = input("Create a password for yourself \n")

    accountNumber = generationAccountNumber()

    database[accountNumber] = [first_name, lastname, email, password]

    print("Your account has been created")
    print("== === ===== ===== ===")
    print("Your account number is: %d" % account_number)
    print("Make sure you keep it safe")
    print("== === ===== ===== ===")

    login


def bank_operation(user):
    print("Welcome %s %s " % (user[0], user[1]))

    selected_option = int(input("What would you like to do? (1) deposit (2) widrawal (3) logout "))

    if selected_option == 1:

        deposit_operation()
    elif selected_option == 2:

        widrawal_operation
    elif selected_option == 3:

        logout()
    elif selected_option == 4:

        exit()
    else:

        print("Invalid option selected")
        bank_operation(user)


def widrawal_operation():
    print("widrawal")


def deposit_operation():
    print("Deposit operations")


def generation_account_number():
    return random.randrange(1111111111, 9999999999)


def get_current_balance(user_details, balance):
    user_details[4] = balance


def get_current_balance(user_details):
    return user_details[4]


def logout():
    login()

