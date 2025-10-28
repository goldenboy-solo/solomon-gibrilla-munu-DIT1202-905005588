# demo.py
from operation import*

print("Mini Library Management System")

print(add_book("001", "Python Basics", "John Doe", "Non-Fiction", 5))
print(add_book("002", "Space Odyssey", "Arthur Clarke", "Sci-Fi", 3))
print(add_member("M001", "Solomon", "alice@mail.com"))
print(add_member("M002", "Bob", "bob@mail.com"))

print(borrow_book("M001", "001"))
print(borrow_book("M001", "002"))
print(return_book("M001", "001"))

print(search_books("Python"))
print(delete_book("001"))
print(delete_member("M002"))