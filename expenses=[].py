expenses=[]
print("welcome to expense tracker")
while True:
 print("1.add expense"
      "2.view expenses"
      "3.total expenses"
      "4.exit")



 choice=int(input("choose a option"))
    
 if choice==1:
        date=input("enter date")
        description=input("enter descrription")
        amount=float(input("enter amount"))
        expense={
            "date":date,
            "description":description,
            "amount":amount}
        expenses.append(expense)

 if choice==2:
        if len(expenses)==0:
            print("no expense recorded")
        else:
            count=0
            for expense in expenses:
                print(f"{count}.{expense['date']}, {expense['description']}: ${expense['amount']}")

 if choice==3:
        total=0
        for expense in expenses:
         total=total+expense['amount']
        print(total)
    
 if choice==4:
        print("thanks for using our app")
        break