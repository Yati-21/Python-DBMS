# -*- coding: utf-8 -*-
"""SQL PROJ BHAVIK-YATI

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mvWylZ_AjFoDThzZYTSPoxclOnHdCP6E
"""

import sqlite3
#CREATE DATABSE
conn = sqlite3.connect('Library.db')
c=conn.cursor()

# CREATE TABLE
CreateCommand =('''CREATE TABLE IF NOT EXISTS BOOKS
                      (Book_ID char(4) PRIMARY KEY,
                      Name varchar(50),
                      Author  varchar(30),
                      Price int(8),
                      Type varchar(20),
                      Quantity int(3));''' )
conn.execute(CreateCommand)
conn.commit()
conn.close()

# INSERTING VALUES

conn = sqlite3.connect('Library.db')
c = conn.cursor()
many_records = [('A006','The Hobbit', 'J.R.R. Tolkien',350, "fantasy ",10),
                ('A007','The Alchemist', 'Paulo Coelho',300, "fantasy",5 ),
                ('B005','Think like a monk', 'Jay Shetty',250, "Self help",8),
                ('A009','The Lord of Rings','J.R.R. Tolkien',350, "fantasy ",6)]

c.executemany("INSERT INTO Books VALUES(?,?,?,?,?,?);",many_records )

conn.commit()
conn.close()

# INSERTING VALUES

def add_record():
  id  = input("Enter the Book ID : ")
  name = input("Enter the book name : ")
  author = input("Enter the author name : ")
  price = input("Enter price of book: ")
  TYPE = input("Enter Book type: ")
  quantity = input("Enter number of books: ")
  conn = sqlite3.connect('Library.db')
  c = conn.cursor()
  Record=(id,name,author,price,TYPE,quantity)
  c.execute("insert into Books values(?,?,?,?,?,?);",Record)

  conn.commit()
  conn.close()
  print('Data added successfully!')

#DELETING RECORD

def delete_rec():
  conn = sqlite3.connect('Library.db')
  c = conn.cursor()
  delete = input("Enter Book ID to be deleted : ")
  c.execute("DELETE FROM Books WHERE Book_ID = '"+delete+"' ;")
  conn.commit()
  conn.close()
  print("Record deleted successfully!")

def displayall():
  conn = sqlite3.connect('Library.db')
  c = conn.cursor()
  c.execute("SELECT * FROM Books")
  items = c.fetchall()
  for row in items:
    print(row)
  conn.commit()
  conn.close()

def Q_Mmodify() :
  conn = sqlite3.connect('Library.db')
  c = conn.cursor()
  modify = input("Enter Book ID to be Modified : ")
  quantity = input("Enter no. of books: ")
  c.execute("UPDATE BOOKS SET Quantity = '" + quantity +"' WHERE Book_ID = '"+ modify +"' ;")
  conn.commit()
  conn.close()

def P_Modify() :
  conn = sqlite3.connect('Library.db')
  c = conn.cursor()
  modify = input("Enter Book ID to be Modified : ")
  price = input("Enter new price: ")
  c.execute("UPDATE BOOKS SET Price = '" + price +"' WHERE Book_ID = '"+ modify +"' ;")
  conn.commit()
  conn.close()



def menu():
    print()
    print("1. Add")
    print("2. Modify")
    print("3. Delete")
    print("4. Display")
    print("5. Exit")
    print()

print("-" * 150)

topic = str.format("{0:^100}", "LIBRARY DATABASE")
print(topic)
print("-" * 150)
print()

while True:

    menu()
    while True:
      choice = input("Enter a choice(1-5): ")


      if choice not in "12345" :          #Validity
        if choice not in "1234"or len(choice) != 1:
          print("Invalid choice!")
        else:
          break
      else:
        break
    print()

    if choice =="5"or choice =="":
      break

    elif choice =="1":
      add_record()

    elif choice =="2":
      print("What do you want to modify?")
      print("1.Quantity of books")
      print("2. Price of book")
      while True:
        CH = input("Enter a choice(1-2): ")
        if CH not in "12" :
          if CH not in "12"or len(CH) != 1:
            print("Invalid choice!")
          else:
            break
        else:
          break
      if CH == "1":
        Q_Mmodify()
      elif CH == "2":
        P_Modify()

    elif choice =="3":
      delete_rec()

    elif choice =="4":
      displayall()

"""# OUTPUT

```
------------------------------------------------------------------------------------------------------------------------------------------------------
                                          LIBRARY DATABASE                                          
------------------------------------------------------------------------------------------------------------------------------------------------------


1. Add
2. Modify
3. Delete
4. Display
5. Exit

Enter a choice(1-5): 4

('A006', 'The Hobbit', 'J.R.R. Tolkien', 350, 'fantasy ', 10)
('A007', 'The Alchemist', 'Paulo Coelho', 300, 'fantasy', 5)
('B005', 'Think like a monk', 'Jay Shetty', 250, 'Self help', 8)
('A009', 'The Lord of Rings', 'J.R.R. Tolkien', 350, 'fantasy ', 6)

1. Add
2. Modify
3. Delete
4. Display
5. Exit

Enter a choice(1-5): 1

Enter the Book ID : B123
Enter the book name : abcd
Enter the author name : aaa
Enter price of book: 1234
Enter Book type: xyz
Enter number of books: 10
Data added successfully!

1. Add
2. Modify
3. Delete
4. Display
5. Exit

Enter a choice(1-5): 4

('A006', 'The Hobbit', 'J.R.R. Tolkien', 350, 'fantasy ', 10)
('A007', 'The Alchemist', 'Paulo Coelho', 300, 'fantasy', 5)
('B005', 'Think like a monk', 'Jay Shetty', 250, 'Self help', 8)
('A009', 'The Lord of Rings', 'J.R.R. Tolkien', 350, 'fantasy ', 6)
('B123', 'abcd', 'aaa', 1234, 'xyz', 10)

1. Add
2. Modify
3. Delete
4. Display
5. Exit

Enter a choice(1-5): 2

What do you want to modify?
1.Quantity of books
2. Price of book
Enter a choice(1-2): 2
Enter Book ID to be Modified : B123
Enter new price: 2345

1. Add
2. Modify
3. Delete
4. Display
5. Exit

Enter a choice(1-5): 3

Enter Book ID to be deleted : B123
Record deleted successfully!

1. Add
2. Modify
3. Delete
4. Display
5. Exit

Enter a choice(1-5): 4

('A006', 'The Hobbit', 'J.R.R. Tolkien', 350, 'fantasy ', 10)
('A007', 'The Alchemist', 'Paulo Coelho', 300, 'fantasy', 5)
('B005', 'Think like a monk', 'Jay Shetty', 250, 'Self help', 8)
('A009', 'The Lord of Rings', 'J.R.R. Tolkien', 350, 'fantasy ', 6)

1. Add
2. Modify
3. Delete
4. Display
5. Exit

Enter a choice(1-5): 5

```

```

```
"""