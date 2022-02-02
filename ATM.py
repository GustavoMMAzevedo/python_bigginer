def withdraw_money(current_balance, amount):
    if (current_balance >= amount):
        current_balance = current_balance - amount
        return current_balance

def add_money(current_balance, transfer):
    current_balance= current_balance + transfer
    return current_balance
    

current_balance = 1000
print("Your balance is", current_balance)
question = input("would you like to withdraw (w) or deposit (d) ?")


if (question == "w"):
    amount = int(input("What is the amount to remove?"))
    lower_balance = withdraw_money(current_balance, amount)
    print("Your balance is", lower_balance)

    if (lower_balance <= 100):
        print("Your balance is too low, it is better to make a deposit")
        question_1 = input("would you like to add money to your account? (y/n)")
        if (question_1 == "y"):
            transfer = int(input("What is the amount you want to deposit?"))
            high_balance = add_money(current_balance, transfer)
            print("Your new balance is", high_balance)
        else:
            print("OK, no problem, have a nice day!")
            print("Your final balance is:", lower_balance)


if (question == "d"):
    transfer = int(input("What is the amount you want to deposit?"))
    high_balance = add_money(current_balance, transfer)
    print("Your balance is", high_balance)






