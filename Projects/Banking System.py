import math as m

accounts = {}

while True:
    print(
        "Select an operation:\n"
        "1. Create account\n2. Deposit\n3. Withdraw\n4. Balance\n"
        "5. Transfer\n6. Interest\n7. History\n8. Close account\n9. Exit"
    )

    num = int(input("Enter your choice: "))

    if num == 9:
        print("Exiting system...")
        break

    # 1. Create Account
    elif num == 1:
        accId = input("Enter Account ID: ")
        amount = int(input("Enter initial balance: "))

        if accId in accounts:
            print(f"Account {accId} already exists")
        else:
            accounts[accId] = {
                "balance":amount,
                "history":["CREATE"]
            }
            print(f"Account {accId} created")

    # 2. Deposit
    elif num == 2:
        accId = input("Enter Account ID: ")
        amount = int(input("Enter deposit amount: "))

        if accId not in accounts:
            print(f"Account {accId} does not exist")
        else:
            accounts[accId]["balance"] += amount
            accounts[accId]["history"].append(f"DEPOSIT {amount}")
            print(f"Deposited {amount} to {accId}")

    # 3. Withdraw
    elif num == 3:
        accId = input("Enter Account ID: ")
        amount = int(input("Enter withdrawal amount: "))

        if accId not in accounts:
            print(f"Account {accId} does not exist")
        else:    
            if accounts[accId]["balance"] < amount:
                print("Insufficient funds")
            else:
                accounts[accId]["balance"] -= amount
                accounts[accId]["history"].append(f"WITHDRAW {amount}")

                print(f"Withdrew {amount} from {accId}")

    # 4. Balance
    elif num == 4:
        accId = input("Enter Account ID: ")

        if accId not in accounts:
            print(f"Account {accId} does not exist")
        else:
            print(f"Balance of {accId}: {accounts[accId]["balance"]}")

    # 5. Transfer
    elif num == 5:
        src = input("Enter source Account ID: ")
        dest = input("Enter destination Account ID: ")
        amount = int(input("Enter amount: "))

        if src not in accounts:
            print(f"Account {src} does not exist")
        elif dest not in accounts:
            print(f"Account {dest} does not exist")
        else:    
            if accounts[src]["balance"] < amount:
                print("Insufficient funds")
            else:
                accounts[src]["balance"] -= amount
                accounts[dest]["balance"] += amount

                accounts[src]["history"].append(f"TRANSFER {src}→{dest} {amount}")
                accounts[dest]["history"].append(f"TRANSFER {src}→{dest} {amount}")
                print(f"Transferred {amount} from {src} to {dest}")

    # 6. Interest
    elif num == 6:
        accId = input("Enter Account ID: ")
        rate = float(input("Enter rate (%): "))

        if accId not in accounts:
            print(f"Account {accId} does not exist")
        else:
            new_balance = m.floor(accounts[accId]["balance"] * (1 + rate / 100))
            accounts[accId]["balance"] = new_balance
            accounts[accId]["history"].append("INTEREST")
            print(f"Interest applied to {accId}")

    elif num == 7:   # History
        accId = input("Enter Account ID: ")

        if accId not in accounts:
            print(f"Account {accId} does not exist")
        elif not accounts[accId]["history"]:
            print("No transactions")
        else:
            for entry in accounts[accId]["history"]:
                print(entry)

    # 8. Close Account
    elif num == 8:
        accId = input("Enter Account ID: ")

        if accId not in accounts:
            print(f"Account {accId} does not exist")
        elif accounts[accId]["balance"] != 0:
            print("Cannot close account – balance must be zero")
        else:
            del accounts[accId]
            print(f"Account {accId} closed")

    else:
        print("Invalid choice")
