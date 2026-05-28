expenses = []
while True:

 print("1. Add Expense")
 print("2. view Expense")
 print("3. Show Expense") 
 print("4, delete expense")
 print("5. Exit\n")

 a =  int(input("Enter your choice: "))
 if a == 1:     
       print("You selected Add Expense")
       name = input("Enter expense name: ")
       amount = int(input("Enter expense amount: "))
       expense = {"name": name, "amount": amount}
       expenses.append(expense)
       file = open("expenses.txt", "a")
       file.write(name + " - " + str(amount) + "\n")
       file.close()
       print("Expense added successfully")
 elif a == 2:
       print("you selected view expense")
       file = open("expenses.txt", "r")
       data = file.read()
       print(data)
       file.close()
       for expense in expenses:
          print("Expense Name: ", expense["name"])
          print("Expense Amount", expense['amount'])
 elif a == 3:
         total = 0
         for expense in expenses:
               total = total + expense["amount"]
         print("Total  expense: ", total)
 elif a == 4:
        if len(expenses) == 0:
            print("NO expense to delete")
        else:
                 for index, expense in enumerate(expenses):
                  print(index + 1, expense["name"], "-",expense["amount"])
                 delete_index = int(input("Enter the expense number to delete: "))
                 expenses.pop(delete_index - 1)
                 print("Expense Deleted Successfully")
                
 elif a == 5:
   print("Exiting Program....")
   break  
 else:
      print("Invalid choice")
         
            
             
                 