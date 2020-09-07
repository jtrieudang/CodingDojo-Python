class User: 
    def __init__(self, name):
        self.name = name
        self.user_balance = 0

    def make_deposit(self, amount):
        self.user_balance += amount
        return self

    def make_withdrawal(self, amount):
        if amount <= self.user_balance:
            self.user_balance -= amount
            return self

    def display_user_balance(self):
        return self.user_balance
    
    # transfer money
    def transfer_money(self, other_user, amount):
        if amount <= self.user_balance:
            self.make_withdrawal(amount)
            other_user.make_deposit(amount) # have other_user instead of self because self is you.
            return self

user1 = User('Jimmy')
user2 = User('John')
user3 = User('Jenny')

user1.make_deposit(100).make_deposit(250).make_deposit(300).make_withdrawal(147).display_user_balance()

user2.make_deposit(500).make_deposit(200).make_withdrawal(600).make_withdrawal(50)

user3.make_deposit(603).make_withdrawal(402).make_withdrawal(102).make_withdrawal(22).transfer_money(user2, 20) 
# above is to transfer money^ change the amount to see both user 2 and user 3 change
print(user1.user_balance)
print(user2.user_balance)
print(user3.user_balance)