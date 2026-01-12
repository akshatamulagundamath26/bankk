from datetime import datetime

class BankAccount:
    def __init__(self, account_number, opening_balance):
        self.account_number = account_number
        self.balance = opening_balance
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Invalid deposit amount")
        self.balance += amount
        self._add_transaction("DEPOSIT", amount)

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Invalid withdrawal amount")
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount
        self._add_transaction("WITHDRAW", amount)

    def _add_transaction(self, ttype, amount):
        self.transactions.append({
            "type": ttype,
            "amount": amount,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "balance": self.balance
        })

    def mini_statement(self):
        return self.transactions[-5:]


def main():
    acc = BankAccount("ACC101", 5000)
    acc.deposit(2000)
    acc.withdraw(1000)

    print("Mini Statement:")
    for txn in acc.mini_statement():
        print(txn)


if __name__ == "__main__":
    main()
