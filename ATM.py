def withdraw_money(current_balance, amount):
    current_balance = current_balance - amount
    return current_balance

def add_money(current_balance, transfer):
    current_balance= current_balance + transfer
    return current_balance


#Variables 
costumer_1_account = 1234
costumer_2_account = 5678
count_1 = 0
count_2 = 0

# Ask if you are the next custumer and if Yes goes into the account number question
while True:
    Next_Costumer = input ("Next Customer Y or N?")
    
  # set the correct current balance variable 
  # if this is the first interaction the initial balance is 0
  # if this is not the fisrt interaction count > 0 the initial balance is the new_balance from the calculation below
  # with this we can always have the latest balance in the account
    if count_1 == 0:
        current_balance_1 = 0
    else:
        current_balance_1 = new_current_balance_1
    if count_2 == 0:
        current_balance_2 = 0
    else:
        current_balance_2 = new_current_balance_2

    if Next_Costumer == "Y":

        #Ask what is the number of the account and check against the variables and proceed with calculation of the balance
        while True:
            
            which_account = input ("What is the number of your account?")

            #Depending on the account selected it shows the account current balance and prompts the user for questions regarding withdraw and deposit
            if int(which_account) == costumer_1_account:
                
                Operation = input ("What transaction would you like to do? Withdraw (W) or Deposit (D)")
                if Operation == "W":
                    try:
                        Deduct_Amount = float (input ("what is the amount that you would like to Withdraw?"))
                        print(Deduct_Amount)
                    except:
                        print ("wrong input")
                        continue
                    new_current_balance_1 = withdraw_money(current_balance_1,Deduct_Amount)
                    #adds 1 to count so that a new value can be stored in the current_balance_1 and always saves the latest value
                    count_1 = count_1 + 1
                    print ("Your New Account Balance is: £ %.2F" % new_current_balance_1)
                    break
                elif Operation == "D":
                    try:
                        Add_Amount = float (input ("what is the amount that you would like to Add?"))
                        print(Add_Amount)
                    except:
                        print ("wrong input")
                        continue
                    new_current_balance_1 = add_money (current_balance_1,Add_Amount)
                    count_1 = count_1 + 1
                    print ("Your New Account Balance is: £ %.2F" % new_current_balance_1)
                    break

            elif int(which_account) == costumer_2_account:

                Operation = input ("What transaction would you like to do? Withdraw (W) or Deposit (D)")
                if Operation == "W":
                    try:
                        Deduct_Amount = float (input ("what is the amount that you would like to Withdraw?"))
                        print(Deduct_Amount)
                    except:
                        print ("wrong input")
                        continue
                    new_current_balance_2 = withdraw_money(current_balance_2,Deduct_Amount)
                    count_2 = count_2 + 1
                    print ("Your New Account Balance is: £ %.2F" % new_current_balance_2)
                    break
                elif Operation == "D":
                    try:
                        Add_Amount = float (input ("what is the amount that you would like to Add?"))
                        print(Add_Amount)
                    except:
                        print ("wrong input")
                        continue
                    new_current_balance_2 = add_money (current_balance_2,Add_Amount)
                    count_2 = count_2 + 1
                    print ("Your New Account Balance is: £ %.2F" % new_current_balance_2)
                    break
    else:
        continue
