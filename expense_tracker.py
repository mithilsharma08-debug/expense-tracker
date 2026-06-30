print("welcome to expense tracker")
expenses=[]
while True:
    print("1 add expense")
    print(("2 view expenses"))
    print("3 total amount")
    print("4 exit")
    print("5 to delete an expense")
    choice=int(input("enter a number"))
    if choice==1:
        date=input("enter date")
        description=input("enter description")
        details=input("enter more details")
        amount=float(input("enter amount"))
        expense={
            "date":date,
            "description":description,
            "details":details,
            "amount":amount}
        expenses.append(expense)

    if choice==2:
        if len(expenses)==0:
            print("no expenses")
        else:
            count=0
            for expense in expenses:
                count+=1
                print(f"{count}.{expense['date']}, {expense['description']},{expense['amount']}")
        
    if choice==3:
        total=0
        for expense in expenses:
            total=total+expense['amount']
            print(total)

    if choice==4:
        print("thanks for using our app")
        break
    if choice==5:
        if len(expenses)==0:
            print("no expenses")
        else:
            number=int(input("enter a number to delete expenses"))
            if number>len(expenses):
                print("invalid")
            else:
                expenses.pop(number-1)
                print(expenses)

    
