#railway ticket
print("-----------------Railway Ticket-------------------")
while True:
    def railway():
        ticket=1000
        gender=input("enter the gender")
        age=int(input("enter the age"))
        if gender=="m":
            if age>=60:
                print("senior citizen")
                ticket=ticket-30/100*ticket
                print(ticket)
            elif age<60:
                print("normal citizen")
                print(ticket)
        elif gender=="f":
            if age>=60:
                print("senior citizen")
                ticket=ticket-50/100*ticket
                print(ticket)
            elif age<60:
                print("normal citizen")
                ticket=ticket-30/100*ticket
                print(ticket)
    railway()
