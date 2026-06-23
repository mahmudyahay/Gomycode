 # this is a class that takes methods like transfer, deposit, withdraw and check balance this class is Banking System
# it has a constructor called balance and every method has x, this x collect amount from user and add it up to
# balance when the deposit method is called, minus x from balance when transfer or withdraw method is called and  also
# return balance when check balance method is called. remember this class must collect balance first
import json


class BankSystem:

    # this is a constructor that help in holding balance
    def __init__(self, balance):
        self.balance = balance

    # this method help in settling out depositing of money
    def deposit(self, x):
        self.balance += x
        print(f'you have successfully deposited {x} your balance if {self.balance}')

    # this method help in withdrawing money
    def withdraw(self, x):
        if x < self.balance:
            self.balance -= x
            print(f'you have successfully withdraw {x} your balance if {self.balance}')
        else:
            print('invalid amount ')

    # this method help in transferring money to another account
    def transfer(self, x):
        if x < self.balance:
            self.balance -= x
            print(f'you have successfully withdraw {x} your balance if {self.balance}')
        else:
            print('invalid amount ')

# this method help in checking balance
    def check_balance(self):
        print(f'your balance is {self.balance}')


# f is a variable name that collect a list from a file and store it on account_details
f = open('data.json', 'r')
account_details = json.load(f)


# this function helps us to login, it is a special function that help us login is not in any class
# because its work is just to check if you have an account_details. if yes it will allow you to_do some work
def login(n, a):
    has_account = False
    # the n and a_variable are to collect name and account_details from the user
    # here I will loop through account_details and check if the same name and account details is in I, then it returns
    # true
    for i in account_details:
        if n == i[0] and a == i[1]:
            has_account = True
    return has_account


# this function helps us to register new user, it is a special function that help in registering, is not in any class
# because its work is just to check if you have an account_details. if you do not it allow you to register
# its check if you have an existing account with the login() function,
# it takes in x and y as name and account number pass it to login() to check if its exist and if it returns true
# it will allow you register and returns the collected name, account number and initial balance to be appended in
# account_details
def register(x, y):
    if login(x, y):
        print('existing account')
    else:
        name = x
        acc = y
        bal = int(input('enter initial bal: '))
        account_details.append([name, acc, bal])
        # the s variable was used to overwrite our data.json file
        s = open('data.json', 'w')
        json.dump(account_details, s)


# this class was crated for admin to add user remove user and see all details in the bank
class Admin:

    @staticmethod
    def bank_details():
        print(account_details)

# this method takes x and y as name and account number and pass it to a register to check if it exist, if not it add to
# account_details
    @staticmethod
    def add_user(x, y):
        register(x, y)

    @staticmethod
    def remove():
        name = input('enter the name: ')
        acc = int(input('enter the acc number: '))
        bal = int(input('enter the initial balance: '))
        account_details.remove([name, acc, bal])
        # as we remove a specific list in our account_details we have to overwrite our file to update records
        s = open('data.json', 'w')
        json.dump(account_details, s)


# I am using while loop because I want to continuously running the system except if user press exist
while True:
    # its start by collecting user data which is data name and data account number then welcome you
    print('hello! welcome to our bank what will you love to do')
    # provides list of task it can handle at initial stage. and have command to collect your reply
    print('1) login 2) register 3) quit 4) Admin')
    # check what you want and run task for you
    command = input('>')
    # check if command has login, if yes iterate through account details check if the first element in I == d_name
    # and if second element in I == d_account then create a user of system then assigns the third element as balance
    # as its required a perimeter for balance
    if 'login' in command:
        d_name = input('enter your name: ')
        d_acc_number = int(input('enter your acc number: '))
        if login(d_name, d_acc_number):
            for k in account_details:
                if d_name == k[0] and d_acc_number == k[1]:
                    user = BankSystem(k[2])
                    # after successfully getting into the object its bring all methods in the BankingSystem for user
                    # to chose and collect reply in CMD also after everything if you deduct anything from your account
                    # it also deduct it from your balance since k[2] is your balance it will deduct and upgrade file
                    print('hello! what will you love to do 1) withdraw 2) AC balance 3) transfer 4) deposit')
                    CMD = input('>')
                    if 'withdraw' in CMD:
                        amount = int(input('enter amount'))
                        user.withdraw(amount)
                        k[2] -= amount
                        file1 = open('data.json', 'w')
                        json.dump(account_details, file1)
                    elif 'AC balance' in CMD:
                        user.check_balance()
                    elif 'transfer' in CMD:
                        # remember every method in our Banking system required amount. in transfer it allow you send to
                        # another account and also confirm the other account and add to it
                        other_acc = int(input('enter acc no: '))
                        for w in account_details:
                            if other_acc in w:
                                print(f' confirm the acc name: {w[0]} yes or no: ')
                                answer = input('>')
                                if 'yes' in answer:
                                    amount = int(input('enter amount to transfer: '))
                                    user.transfer(amount)
                                    if k[2] >= amount:
                                        k[2] -= amount
                                        w[2] += amount
                                    else:
                                        k[2] = k[2]
                                        break
                                    file1 = open('data.json', 'w')
                                    json.dump(account_details, file1)
                                else:
                                    print('no account details in our bank')
                                    break
                        else:
                            print('no account details in our bank')
                            break
                    elif 'deposit' in CMD:
                        amount = int(input('enter amount'))
                        user.deposit(amount)
                        k[2] += amount
                        file1 = open('data.json', 'w')
                        json.dump(account_details, file1)
                    else:
                        print('i do not understand')
                        break
        else:
            print('incorrect login details ')
            break
    elif 'register' in command:
        d_name = input('enter your name: ')
        d_acc_number = int(input('enter your acc number: '))
        register(d_name, d_acc_number)
    elif 'quit' in command:
        break
    elif 'Admin' in command:
        admin_password = 5678
        main_admin = Admin()
        question = input('are you admin: yes or no ')
        if 'yes' in question:
            check_password = int(input('enter your password: '))
            if check_password == admin_password:
                print('hello admin! what will you love to do 1) add user 2)remove user 3)see details')
                reply = input('>')
                if 'add user' in reply:
                    print('add user name and acc number to check if its exist')
                    Admin.add_user(input('enter the name: '), int(input('enter acc number: ')))
                elif 'remove user' in reply:
                    Admin.remove()
                elif 'see details' in reply:
                    Admin.bank_details()
            else:
                print('wrong password')
                break
        else:
            print('wrong perimeter')
            break
