print("welcome to atm simulator")
balance=15000
pin='9441'
entered_pin=input("enter a pin...")
if entered_pin!=pin:
    print("invalid pin!please enter correct pin code")
    atm_on=False
else:
    atm_on=True
while atm_on:
    print("main menu:")
    print("1.check balance")
    print("2.deposit money")
    print("3.withdraw money")
    print("4.exit")
    choice=input("enter your choice:")
    if choice=='1':
        print("current balance is",balance)
    elif choice=='2':
        amount=int(input("enter amount to deposit:"))
        balance+=amount
        print("deposited successfully",balance)

    elif choice=='3':
        amount=int(input("enter amount to withdraw:"))
        if amount>balance:
            print("your balance is insufficient")
        else:
            balance-=amount
            print("money withdrawed",balance)
    elif choice=='4':
        print("your exited from the atm machine")
        atm_on=False
    else:
        print("invalid choice")
            
