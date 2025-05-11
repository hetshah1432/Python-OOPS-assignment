class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id

class StudentMember(Member):
    def __init__(self, name, member_id):
        super().__init__(name, member_id)
        self.books_borrowed = 0

    def add_book(self):
        self.books_borrowed += 1
        print(f"Book added. Total borrowed: {self.books_borrowed}")

    def return_book(self):
        if self.books_borrowed > 0:
            self.books_borrowed -= 1
            print(f"Book returned. Total borrowed: {self.books_borrowed}")
        else:
            print("No books to return.")

    def display_status(self):
        print(f"{self.name} (ID: {self.member_id}) has borrowed {self.books_borrowed} book(s).")
