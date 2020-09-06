class User:
    def __init__(self):
        self.name = "Jimmy"
        self.email = "trieujimmy@yahoo.com"
        self.account_balance = 0

guido = User()
monty = User()
print(guido.name)	# output: Jimmy
print(monty.name)	# output: Jimmy

guido.name = "Guido"
monty.name = "Monty"

# -----------------------------------------------------------------------------------
class User:
    def __init__(self, username, email_address):# now our method has 2 parameters!
        self.name = username			# and we use the values passed in to set the name attribute
        self.email = email_address		# and the email attribute
        self.account_balance = 0		# the account balance is set to $0, so no need for a third parameter

jenny = User("Jenny Tree", "tree_jenny@yahoo.com")
johnny = User("Johnny Tree", "tree_johnn@yahoo.com")
print(jenny.name)
print(johnny.email)

# -------------------------------------------------------------------------------------

class User:	# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount	# the specific user's account increases by the amount of the value received

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")

guido.make_deposit(100)
guido.make_deposit(200)
monty.make_deposit(50)
print(guido.account_balance)	# output: 300
print(monty.account_balance)	# output: 50

