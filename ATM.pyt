amount=int(input("enter amount to withdraw"))
availablebalance=int(input("enter available balance"))
if amount>0 and amount%100==0 and amount<availablebalance :
    print(amount)
    balance=( availablebalance - amount)
    print(balance)
else:
    print ( "go out of the atm")
    