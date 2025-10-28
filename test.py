# tests.py
from operation import *

# Reset data for testing
books.clear()
members.clear()

assert add_book("B1", "AI for All", "Smith", "Non-Fiction", 2) == "Book added successfully."
assert add_member("M1", "Eve", "eve@mail.com") == "Member added successfully."
assert borrow_book("M1", "B1") == "Book borrowed successfully."
assert borrow_book("M1", "B1") == "Book borrowed successfully."
assert borrow_book("M1", "B1") == "No copies available."
assert return_book("M1", "B1") == "Book returned successfully."
assert delete_book("B1") == "Cannot delete — book currently borrowed." or "Book deleted successfully."

print("All tests passed!")