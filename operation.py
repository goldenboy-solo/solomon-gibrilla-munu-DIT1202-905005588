genres = ("Fiction", "Non-Fiction", "Sci-Fi", "Mystery", "Romance")
books = {}
members = []


#CRUD FUNCTIONS

def add_book(isbn, title, author, genre, total_copies):
    if isbn in books:
        return "Book already exists."
    if genre not in genres:
        return "Invalid genre."
    books[isbn] = {
        "title": title,
        "author": author,
        "genre": genre,
        "total_copies": total_copies,
        "available_copies": total_copies
    }
    return "Book added successfully."


def add_member(member_id, name, email):
    for m in members:
        if m["member_id"] == member_id:
            return "Member already exists."
    members.append({
        "member_id": member_id,
        "name": name,
        "email": email,
        "borrowed_books": []
    })
    return "Member added successfully."


def search_books(keyword):
    results = []
    for isbn, details in books.items():
        if keyword.lower() in details["title"].lower() or keyword.lower() in details["author"].lower():
            results.append((isbn, details))
    return results


def update_book(isbn, title=None, author=None, genre=None, total_copies=None):
    if isbn not in books:
        return "Book not found."
    if genre and genre not in genres:
        return "Invalid genre."
    if title: books[isbn]["title"] = title
    if author: books[isbn]["author"] = author
    if genre: books[isbn]["genre"] = genre
    if total_copies:
        diff = total_copies - books[isbn]["total_copies"]
        books[isbn]["total_copies"] = total_copies
        books[isbn]["available_copies"] += diff
    return "Book updated successfully."


def delete_book(isbn):
    if isbn not in books:
        return "Book not found."
    for m in members:
        if isbn in m["borrowed_books"]:
            return "Cannot delete — book currently borrowed."
    del books[isbn]
    return "Book deleted successfully."


def update_member(member_id, name=None, email=None):
    for m in members:
        if m["member_id"] == member_id:
            if name: m["name"] = name
            if email: m["email"] = email
            return "Member updated successfully."
    return "Member not found."


def delete_member(member_id):
    for m in members:
        if m["member_id"] == member_id:
            if m["borrowed_books"]:
                return "Cannot delete — member has borrowed books."
            members.remove(m)
            return "Member deleted successfully."
    return "Member not found."


#BORROW/RETURN FUNCTIONS

def borrow_book(member_id, isbn):
    if isbn not in books:
        return "Book not found."
    for m in members:
        if m["member_id"] == member_id:
            if len(m["borrowed_books"]) >= 3:
                return "Limit reached (3 books)."
            if books[isbn]["available_copies"] == 0:
                return "No copies available."
            m["borrowed_books"].append(isbn)
            books[isbn]["available_copies"] -= 1
            return "Book borrowed successfully."
    return "Member not found."


def return_book(member_id, isbn):
    for m in members:
        if m["member_id"] == member_id:
            if isbn not in m["borrowed_books"]:
                return "Book not borrowed by this member."
            m["borrowed_books"].remove(isbn)
            books[isbn]["available_copies"] += 1
            return "Book returned successfully."
    return "Member not found."
