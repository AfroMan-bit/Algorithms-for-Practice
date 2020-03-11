# class User:
#     def __init__(self, name_parameter, email_parameter):
#         self.nameofPerson = name_parameter
#         self.emailofPerson = email_parameter
#         self.account_balance = 0

#     def depositMoney(self, amount);
#         self.account_balance += amount
#         return self

#     def transferMoney(self, otherUser, amount):
#         self.account_balance -= 5
#         otherUser.account_balance += 5
#         return self

# To allow user1, user2 or user3 overdraw their account
    # def withdrawMoney_overdraw(self, amount):
    #     self.account_balance -= amount

# To not allow user1, user2, user3 overdraw their account
#     def withdrawMoney_no_overdraw(self, amount):
#         if self.account_balance > amount:
#             self.account_balance -= amount
#         else:
#             print("insufficient funds")


# user1 = User("Ben", "benjamin@yahoo.com")
# user2 = User("Tom", "tommy@yahoo.com")
# user3 = User("Sarah", "sarah@yahoo.com")

# print(user1.nameofPerson)
# prints the name of the user1

# print(user2.emailfPerson)
# prints the email of the user2

# print(user1.account_balance)
# prints the account balance of the user3 which in this case is 0 by default according to the class User

# user1.depositMoney(50)
# print(user1.account_balance)
# prints the account balance of user1 which by default is 0 and then adds the function depositMoney which is giving an arguemnt of 50 (0 + 50 / account_balance + depositMoney) The output is ($50)

# user1.transferMoney(user 2, 5)
# print(user2.account_balance)
# print(user1.account_balance)
# prints user1 account balance which is now 50 then transfers money to user2 (50 - 5) which is now 5 to be added to the default account balance of 0 (0 + 5 / account_balance + transferMoney from user1)
# Also user1 account_balance (50 - 5) which is now 45 ($45)

# user1.depositMoney(50).depositMoney(30).transferMoney(user2, 5)
# print(user1.account_balance)
# prints user1 account banlace (50 + 30) which is 80 ($80), assuming user1 depositedMoney twice. we use "return self" at the end of the declared functions to add a "chain method" of repeating a chain of function or various types of functions, i.e repeating a particular function for user1 as many times as possible or even adding other functions to modify the final account balance for user 1)
# The final output for account balance user1 will be (80 - 50) which is 75 ($75) because we transfered money 5 (80 - 5) to user2 at the end in the "chain mathod of functions" for user1. This will only work since we added "return self"and this means (updating all the chain methods to the very last function of command in the declared function which in this case we tranfered 5 from user1 to user2)

# user1.withdrawMoney_overdraw(100)
# print(user1.account_balance)
# prints user1 current account balance which is currently 75 and then withdraws 100 which means (75 - 100) which is -25.
# the new user1 account balance is ( -25 which is -$25)
# The above assuming user1 is allowed to overdraw their account

# user1.withdrawMoney_no_overdraw(100)
# print(user1.account_balance)
# prints "insufficient funds" for user1 since user1 current account balance which is currently 75 and then wants to withdraw 100 which means (75 - 100) but is not allowed to because user1 still needs an additional 25 to fulfil the withdrawMoney function of 100. we give a conditional statement in our def withdrawMoney_no_overdraw above saying if user1 account balance is greater than amount allow user1 to withdraw money if not do not allow user1 to redraw money instead give "insuffiecient funds" (if 75 is greater than 100 which in this case is false go to the else statement which is "insufficient funds")
# The above assuming user1 is not allowed to overdraw their account if account balance for user1 is not greater than the withdraw amount and then user1 will get a message "insufficient funds"







