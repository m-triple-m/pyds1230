class Account:

    count = 0

    def __init__(self, name, num, age, amt):
        self.holder_name = name
        self.acc_number = num
        self.age = age
        self.balance = amt

    def debit(self, amount):
        self.balance -= amount
        print(f"{amount} debited from {self.holder_name}'s account, current balance : {self.balance} ")

    
    def credit(self, amount):
        self.balance += amount
        print(f"{amount} credited to {self.holder_name}'s account, current balance : {self.balance} ")



acc001 = Account('Leon Kennedy', 12345, 34, 3000)
# Account.count+=1

print(acc001.balance)

acc001.debit(1500)

a = [1, 2, 4]
b = list([6, 7, 8])
b.append(10)
a.append(5)

acc002 = Account('Ada Wong', 12345, 34, 3000)
# Account.count+=1

print(Account.count, acc001.count, acc002.count)

