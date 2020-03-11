# ......USER.....

# class User:
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#         self.account_balance = BankAccount(0.01, 0)
        # self.checkingAccount = BankAccount(0, 0)
        # self.savingsAccount = BankAccount(0.1, 0)



#     def make_deposit(self, amount, specified_account):
        # if specified_account == "chackings":
        #     self.checkingAccount.account_balance += amount
        # elif specified_account == "savings":
#     	    self.account.account_balance += amount 
        # else:
        #     print("account does not exist")
        # return self


# 1. make withdrawals.

#     def make_withdrawal(self, amount, specified_account):
#         self.account.account_balance -= amount
#         return self

# 2. display user balance.

#     def display_user_balance(self):
#         print(f"User: {self.name}, Balance: ${self.account.accout_balance}")
#         return self

# 3. show three instances of the User class.

# user1 = User("ben", "benjamin@yahoo.com")
# print(user1)
# user2 = User("chris", "chris@yahoo.com")
# print(user2)
# user3 = User("tom", "tom@yahoo.com")
# print(user3)

# 4. make 3 deposits and 1 withdrawal and then display balance.

# user1.make_deposit(5).make_deposit(10).make_deposit(10).make_withdrawal(5).display_user_balance()


# ......Bank Accounts.....
# class BankAccount:
#     def __init__(self, int_rate, balance):
#         self.interestrate = int_rate
#         self.account_balance = balance


#     def deposit(self, amount):
#         self.account_balance += amount
#         return self

#     def withdraw(self, amount):
#         if self.account_balance > amount:
#             self.account_balance -= amount
#         else:
#             print("insufficient funds, charging the account more money for an overdraft")
#             self.account_balance -= 5
#         return self

#     def display_account_info(self):
#         print(f"Balance: ${self.account_balance}")
#         return self

#     def yield_interest(self):
#         if self.account_balance > 0:
#             self.account_balance += self.account_balance * self .interestrate)
#         return self



# bankaccount1 = BankAccount(0.05, 100)
# bankaccount1.yield_interest().display_account_info()



# .......Users with Bank accounts......
# user1 = User("ben", "benjamin@yahoo.com")
# print(user1.account_balance.interestrate)

# user2 = User("chris", "chris@yahoo.com")
# print(user2.account_balance.account_balance)

# user3 = User("tom", "tom@yahoo.com")
# print(user3.account_deposit(5).display_account_info())

# user1.make_deposit(50, "checkings")
# user1.checkingAccount.display_account_info()
# user1.savingsAccount.display_account_info()










