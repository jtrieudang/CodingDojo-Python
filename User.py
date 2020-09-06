class User: 
    def __init__(self, name,):
        self.name = name
        self.u_balance = 0

    def make_deposit(self, amount):
        self.u_balance += amount

    def make_withdrawal(self, amount):
        if amount <= self.u_balance:
            self.u_balance -= amount

    def display_user_balance(self):
        return self.u_balance
    
    # transfer money
    def transfer_money(self, other_user, amount):
        if amount <= self.u_balance:
            self.make_withdrawal(amount)
            other_user.make_deposit(amount) # have other_user instead of self because self is you.
            return self

user1 = User('Jimmy')
user2 = User('John')
user3 = User('Jenny')

user1.make_deposit(100)
user1.make_deposit(250)
user1.make_deposit(300)
user1.make_withdrawal(147)
user1.display_user_balance()

user2.make_deposit(500)
user2.make_deposit(200)
user2.make_withdrawal(600)
user2.make_withdrawal(50)


user3.make_deposit(603)
user3.make_withdrawal(402)
user3.make_withdrawal(102)
user3.make_withdrawal(22)
user3.transfer_money(user2, 20) 
# above is to transfer money^ change the amount to see both user 2 and user 3 change
print(user1.u_balance)
print(user2.u_balance)
print(user3.u_balance)