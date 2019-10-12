accno=[1001,1002,1003]
cname=["ajay kumar", "vijay kumar", "rajesh kumar"]
bal=[1000,2000,3000]

while True:
    print("""
    select operation to perform
    1. Account Open
    2. Account Deposit
    3. Withdraw Amount
    4. Balance Enquiry
    5. Account Close
    6. List All Accounts
    7. Exit
    """)

    n=int(input("Enter your choice: "))

    if n==1:
       print("Account open module".center(40,"-"))
       new_acno=int(input("Enter account number: "))
       if new_acno in accno:
           print("Account Number Already Exist, Cant Be Allocated...")
       else:
           new_cn=input("Enter customer name: ")
           new_bal=int(input("Enter opening balance: "))
           accno.append(new_acno)
           cname.append(new_cn)
           bal.append(new_bal)
           print("Account Openned Successfully!!!!!")
    elif n==2:
        print("Account Deposit Module".center(40,"-"))
        acno=int(input("Enter Account Number: "))
        if acno in accno:
            amt=int(input("Enter Amount to be deposited: "))
            pos=accno.index(acno)
            bal[pos]=bal[pos]+amt
            print("Amount Deposited Successfully!!!")
        else:
            print("Invalid Account Number")
    elif n==3:
        print("Withdraw Amount Module".center(40, "-"))
        acno = int(input("Enter Account Number: "))
        if acno in accno:
            pos = accno.index(acno)
            amt = int(input("Enter Amount to be withdrawn: "))
            if amt<=bal[pos]:
                bal[pos] = bal[pos] - amt
                print("Amount Withdrawn Successfully!!!")
            else:
                print("Amount is greater than available balance!!!!")
        else:
            print("Invalid Account Number")
    elif n==4:
        print("Balance Check Module".center(40,"-"))
        search_acno=int(input("Enter Account Number: "))
        if search_acno in accno:
            print("Following Account Found...")
            pos=accno.index(search_acno)
            print("Customer Name => ", cname[pos])
            print("Available Balance is Rs. ", bal[pos])
        else:
            print("Invalid Account Number!!!!")
    elif n==5:
        print("Account Close Module".center(40,"-"))
        search_acno=int(input("Enter Account Number: "))
        if search_acno in accno:
            ch=input("Following Account Found... Want to Close it (y/n): ")
            if (ch=='y') or (ch=='Y'):
                pos=accno.index(search_acno)
                del accno[pos]
                del cname[pos]
                del bal[pos]
                print(" Account Closed!! ".center(30,"-"))
            else:
                print("Account Not Closed...")
        else:
            print("ERROR!!!! Account Not Found...")
    elif n==6:
        print("List of Accounts".center(40,"="))
        for pos in range(len(accno)):
            print(f"| {accno[pos]} | {cname[pos]:15} | {bal[pos]}")
        print("End of List".center(40,"="))
    elif n==7:
        print(" Bye Bye ".center(50,"x"))
        break
    else:
        print("Invalid choice")