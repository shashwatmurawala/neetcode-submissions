class BankAccount: 
    # TODO: Add class and instance attributes at their appropriate places
    acc = 0
    bal = 0
    
    def __init__(self, name: str, bal: int) -> None:
        self.name = name
        self.bal = bal
        BankAccount.acc += 1
        BankAccount.bal += bal


# TODO: Create two accounts
# TODO: Print the information using the mentioned format
Alice = BankAccount("Alice", 1000)
Bob = BankAccount("Bob", 2000)

print(f"Alice's balance: ${Alice.bal}")
print(f"Bob's balance: ${Bob.bal}")
print(f"Total Accounts: {BankAccount.acc}")
print(f"Total Balance: ${BankAccount.bal}")

