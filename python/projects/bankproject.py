import random

print("****wlecome to ATM!*****\n")

acc = int(input("Please !!!, Enter a account number : "))
pas = int(input("Enter a Password : "))

if(acc==8506965463):
    if(pas==8273):
      print("\nAccount Number Verified : ")
      print("Password Is Verified : ")
    else:
      print("Password Is Not Verified : ")
else:
    print("Account Number Is Not Verified : ")

if(acc!=8506965463 and pas!=8273):
    print("\nDetails Is Invalid : ")
    print("Now Card Is Rejected")    
    
      
print("\nNow Choice The OPtion To Continue The Process :\n")


# choice = ["Withdrow","Check Balance"]
print("1. Withdrew Money ")
print("2. deposit money ")
print("3. Check Balance ")
print("4. Exit ")

current_balance = 2000
amount = 0
deposit_amount = 0
while True:

  choice = input("Enter a choice (1 to 4) : ")

  if choice == '1':
    amount = int(input("Enter a amount to Withdrew : "))
    if current_balance == amount:
     
     print("Withdrew ",amount," rupess successfully",amount)

  elif choice == '2':
    deposit_amount = int(input("Enter Amount to Deposit : "))
    result = deposit_amount + amount
    print(result)
  
  elif choice == '3':
    result = current_balance - amount 
    print("Total Amount is remaining : ",result)
  
  elif choice == '4':
    print("Exiting the program.")
    break

  else:
    print("Invaid choice , please try again !!!")
     









# class Bank:
#     def __init__(self):
#         self.accounts = {}
 
#     def create_account(self, account_number, account_holder, initial_balance):
#         if account_number in self.accounts:
#             return "Account already exists"
#         if initial_balance < 0:
#             return "Initial balance must be non-negative"
 
#         self.accounts[account_number] = {
#             'account_holder': account_holder,
#             'balance': initial_balance
#         }
#         return "Account created successfully"
 
#     def deposit(self, account_number, amount):
#         if account_number not in self.accounts:
#             return "Account does not exist"
#         if amount <= 0:
#             return "Amount to deposit must be positive"
 
#         self.accounts[account_number]['balance'] += amount
#         return "Deposited " + str(amount) + " successfully. New balance : " + str(self.accounts[account_number]['balance'])
 
#     def withdraw(self, account_number, amount):
#         if account_number not in self.accounts:
#             return "Account does not exist"
#         if amount <= 0:
#             return "Amount to withdraw must be positive"
 
#         if self.accounts[account_number]['balance'] < amount:
#             return "Insufficient balance."
 
#         self.accounts[account_number]['balance'] -= amount
#         return "Withdrew " + str(amount) + " successfully. New balance : " + str(self.accounts[account_number]['balance'])
 
#     def check_balance(self, account_number):
#         if account_number not in self.accounts:
#             return "Account does not exist"
 
#         return "Account Holder : " + self.accounts[account_number]['account_holder'] + "\nBalance : " + str(self.accounts[account_number]['balance'])
 
# bank = Bank()	# Create a Bank object
 
# print("\n****** Bank Management System ******")
# print("\n1. Create Account")
# print("2. Deposit Money")
# print("3. Withdraw Money")
# print("4. Check Balance")
# print("5. Exit")
 
# while True:
 
#     choice = input("\nEnter your Choice (1 to 5): ")
 
#     if choice == '1':
#         account_number = input("Enter Account Number : ")
#         account_holder = input("Enter Account Holder's Name : ")
#         initial_balance = float(input("Enter Initial Balance : "))
#         result = bank.create_account(account_number, account_holder, initial_balance)
#         print(result)
 
#     elif choice == '2':
#         account_number = input("Enter Account Number : ")
#         amount = float(input("Enter Amount to Deposit : "))
#         result = bank.deposit(account_number, amount)
#         print(result)
 
#     elif choice == '3':
#         account_number = input("Enter Account Number : ")
#         amount = float(input("Enter Amount to Withdraw : "))
#         result = bank.withdraw(account_number, amount)
#         print(result)
 
#     elif choice == '4':
#         account_number = input("Enter Account Number : ")
#         result = bank.check_balance(account_number)
#         print(result)
 
#     elif choice == '5':
#         print("Exiting the program.")
#         break
 
#     else:
#         print("Invalid Choice. Please Try Again !!!")
 