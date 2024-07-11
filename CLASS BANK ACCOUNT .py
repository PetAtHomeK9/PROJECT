"""3. Write a Python class BankAccount with attributes like account_number,
 balance, date_of_opening and customer_name, and methods like deposit, withdraw,
   and check_balance"""


class BankAccount:

    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name
        

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self,amount):
        if amount > self.balance:
            raise "Insuficient Fund"
        self.balance -= amount


    def check_balance(self):
        return self.balance
    
Customer1 = BankAccount("0033900242", 2750, "01/02/2004", "Harry Merrill")
print(Customer1.check_balance())