class Error(Exception):
    pass

class Account:
    def __init__(self, name="", accountNo=None, balance=0):
        self.name = name
        self.accountNo = accountNo
        self.balance = balance

    def getBalance(self):
        return self.balance

    def credit(self, amt):
        if amt<=0:
            raise Error("Error: Invalid Amount (should be positive)\n")
        self.balance += amt
        print("Credit Success! New balance is: Rs {}\n".format(self.balance))

    def debit(self, amt):
        if amt>self.balance:
            raise Error("Error: Insufficient balance\n")
        self.balance -= amt
        print("Debit Success! New balance is: Rs {}\n".format(self.balance))

    def __repr__(self):
        return "Name: {}\nAccount Number: {}\nBalance: Rs {}\n".format(self.name, self.accountNo, self.balance)

act = Account("Balram", 12345, 1000)
print(act)
act.credit(3000)
print(act)
act.debit(500)
try:
    act.debit(10000)
except Error as e:
    print(e)

try:
    act.credit(-10000)
except Error as e:
    print(e)

print(act)
