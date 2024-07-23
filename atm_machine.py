class Atm:

    def __init__(self):

        self.pin = ''
        self.balance = 0

        self.menu()

    def menu(self):

        option = int(input('''
        Hi, How you want to proceed? Please select the action below!

            1. Generate pin
            2. Deposit money
            3. Withdraw money
            4. Check balance
            5. Exit
        '''))

        if option == 1:
            self.create_pin()
        elif option == 2:
            self.deposit()
        elif option == 3:
            self.withdraw()
        elif option == 4:
            self.check_balance()
        else:
            exit()
            print('Thanks for visiting! Have a nice day!!')

    def create_pin(self):
        pin = int(input('Please enter a four digit number to set a pin successfully: '))
        if 1000 <= pin <= 9999:
            self.pin = pin
            print('Pin created successfully!')
        else:
            print('Invalid pin! Please enter a four digit number.')
        self.menu()

    def deposit(self):
        pin = int(input("Please enter your pin!"))
        if pin == self.pin:
            amount = float(input('Enter the amount you want to deposit!'))
            self.balance += amount
            print('Deposit Successful!')
        else:
            print('Invalid pin!')
        self.menu()

    def withdraw(self):
        pin = int(input("Please enter your pin!"))
        if pin == self.pin:
            amount = float(input('Enter the amount you want to withdraw!'))
            if amount < self.balance:
                self.balance -= amount 
                print('Withdraw Successful!')
            else:
                print('Insufficient Balance!!')
        else:
            print('Invalid pin!')
        self.menu()

    def check_balance(self):
        pin = int(input("Please enter your pin!"))
        if pin == self.pin:
            print(f'Your available balance is {self.balance}')
        else:
            print('Invalid pin!')
        self.menu()