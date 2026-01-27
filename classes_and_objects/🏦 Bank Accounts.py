class BankAccount:
  def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
    self.first_name = first_name
    self.last_name = last_name
    self.account_id = account_id
    self.pin = pin
    self.balance = balance

  def deposit(self, amount):
    self.balance = self.balance + amount
    return self.balance

  def withdraw(self, amount):
    self.balance = self.balance - amount
    return self.balance

  def display_balance(self):
    print(f'Your current account balance is {self.balance}$.')

user1 = BankAccount('Mike', 'Lee', 1279, 'Personal account', 1234, 4)

user1.deposit(96)
user1.withdraw(25)
user1.display_balance()
