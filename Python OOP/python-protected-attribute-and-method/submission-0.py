class Account:
    def __init__(self, name: str, bal: int):
        self.name = name
        self._bal = bal
    
    def display_balance(self) -> None:
        print(f"Balance: ${self._bal}")


# Do not modify the code below this line
account = Account("John", 1000)
account.display_balance()
