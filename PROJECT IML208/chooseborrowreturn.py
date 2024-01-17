import tkinter as tk
from tkinter import messagebox
import os
from datetime import datetime

class ChooseBookPage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("BONFIRE BOOKSTORE - Choose a Book")
        self.geometry("1000x600")
        self.config(bg='#ccad72')

        self.selected_book = tk.StringVar()
        self.selected_book.set("")

        self.choose_label = tk.Label(self, text="BONFIRE BOOKSTORE CHOOSE BOOK", font=("Playfair Dispair", 16), bg='#ccad72', fg='white')
        self.choose_label.pack()

        self.books = [
            {"Book Name": "The King of Kites", "ISBN": 9780237538804,  "Author Name": "Judith Heneghan"},
            {"Book Name": "History of Malaysia", "ISBN": 9780824824259, "Author Name": "Barbara Watson Andaya"},
            {"Book Name": "A Pale View of Hills", "ISBN": 9780571245659, "Author Name": "Kazuo Ishiguro"},
            {"Book Name": "Langit Petang", "ISBN": 9789670591490, "Author Name": "A. Samad Said"},
            {"Book Name": "The Great Gatsby", "ISBN": 9780333791035,  "Author Name": "F. Scott Fitzerald"},
            {"Book Name": "Math Art: Truth, Beauty, Equations", "ISBN": 9781454930440, "Author Name": "Sthephen Ornes"},
        ]

        #Display available books
        self.book_labels = []
        for book in self.books:
            label_text = f"{book['Book Name']} | ISBN: {book['ISBN']} | Author: {book['Author Name']}"
            book_label = tk.Label(self, text=label_text, font=("Playfair Dispair", 12), bg='#ccad72', fg='white')
            book_label.pack()
            self.book_labels.append(book_label)

        # Add a dropdown menu to select a book
        self.book_selection_label = tk.Label(self, text="Select a Book:", font=("Playfair Dispair", 12), bg='#ccad72', fg='white')
        self.book_selection_label.pack()
        book_titles = [book["Book Name"] for book in self.books]
        self.book_selection_menu = tk.OptionMenu(self, self.selected_book, *book_titles)
        self.book_selection_menu.config(font=("Playfair Dispair", 12), bg='#ccad72', fg='white')
        self.book_selection_menu.pack()

        # Add a button to choose a book
        self.choose_book_button = tk.Button(self, text="Borrow Book", command=self.choose_book, font=("Playfair Dispair", 12))
        self.choose_book_button.pack()

    def choose_book(self):
        selected_book_title = self.selected_book.get()
        if selected_book_title:
            # Create an instance of BorrowPage to get user information
            borrow_page = BorrowPage(selected_book_title, "", "", "")
            borrow_page.mainloop()

            # Retrieve borrower information from the BorrowPage instance
            borrower_name = borrow_page.customer_name
            borrower_id = borrow_page.customer_id
            borrower_phone = borrow_page.phone_number

        # After the BorrowPage is closed, create an instance of ReturnBookPage
        return_book_page = ReturnBookPage(selected_book_title, datetime.now().date().strftime("%Y-%m-%d"))
        return_book_page.mainloop()

        # Add a button to go to the buy/borrow page
        self.borrow_button = tk.Button(self, text="Borrow", command=self.borrow, font=("Playfair Dispair", 12))
        self.borrow_button.pack()

class BorrowPage(tk.Tk):
    def __init__(self, selected_book_title, customer_name, customer_id, phone_number):
        super().__init__()
        self.title("BONFIRE BOOKSTORE - Borrow")
        self.geometry("1000x600")
        self.config(bg='#ccad72')

        self.borrow_label = tk.Label(self, text="BONFIRE BOOKSTORE BORROW BOOK", font=("Playfair Dispair", 16), bg='#ccad72', fg='white')
        self.borrow_label.pack()

        self.selected_book_title = selected_book_title
        self.customer_name = customer_name
        self.customer_id = customer_id
        self.phone_number = phone_number

        # Request user information
        self.name_label = tk.Label(self, text="Your Name:", font=("Playfair Dispair", 16), bg='#ccad72', fg='white')
        self.name_label.pack()
        self.name_entry = tk.Entry(self, font=("Playfair Dispair", 12))
        self.name_entry.insert(0, self.customer_name)
        self.name_entry.pack()

        self.id_label = tk.Label(self, text="Your ID:", font=("Playfair Dispair", 16), bg='#ccad72', fg='white')
        self.id_label.pack()
        self.id_entry = tk.Entry(self, font=("Playfair Dispair", 12))
        self.id_entry.insert(0, self.customer_id)
        self.id_entry.pack()

        self.phone_label = tk.Label(self, text="Your Phone Number:", font=("Playfair Dispair", 16), bg='#ccad72', fg='white')
        self.phone_label.pack()
        self.phone_entry = tk.Entry(self, font=("Playfair Dispair", 12))
        self.phone_entry.insert(0, self.phone_number)
        self.phone_entry.pack()

        self.borrow_button = tk.Button(self, text="Borrow", command=self.borrow, font=("Playfair Dispair", 12))
        self.borrow_button.pack()

    def borrow(self):
        borrowed_book_info = f"Book Title: {self.selected_book_title}\n"
        user_info = f"Your Name: {self.name_entry.get()}\nYour ID: {self.id_entry.get()}\nYour Phone Number: {self.phone_entry.get()}"

        # Combine book information and user information
        full_info = borrowed_book_info + user_info

        # You can save this information to a file, display it in a messagebox, etc.
        messagebox.showinfo("Borrow Confirmation", f"Borrowing Information:\n{full_info}")

class ReturnBookPage(tk.Tk):
    def __init__(self, selected_book_title, borrowing_date):
        super().__init__()
        self.title("BONFIRE BOOKSTORE - Return Book")
        self.geometry("1000x600")
        self.config(bg='#ccad72')

        self.return_label = tk.Label(self, text="BONFIRE BOOKSTORE RETURN BOOK", font=("Playfair Dispair", 16), bg='#ccad72', fg='white')
        self.return_label.pack()

        self.selected_book_title = selected_book_title
        self.borrowing_date = borrowing_date

        # Display book and user information
        self.book_label = tk.Label(self, text=f"Book Title: {self.selected_book_title}", font=("Playfair Dispair", 16), bg='#ccad72', fg='white')
        self.book_label.pack()

        self.return_date_label = tk.Label(self, text=f"Borrowing Date: {self.borrowing_date}", font=("Playfair Dispair", 16), bg='#ccad72', fg='white')
        self.return_date_label.pack()

        self.return_button = tk.Button(self, text="Return", command=self.return_book, font=("Playfair Dispair", 12))
        self.return_button.pack()

    def return_book(self):
        # Calculate the days passed since borrowing
        today_date = datetime.now().date()
        borrowing_date = datetime.strptime(self.borrowing_date, "%Y-%m-%d").date()
        days_passed = (today_date - borrowing_date).days

        # Calculate the late fee (RM1 per day after 7 days)
        late_fee = max(0, days_passed - 7) * 1

        # Display return information
        return_info = f"Book Title: {self.selected_book_title}\n"
        return_date_info = f"Return Date: {today_date}\nBorrowing Date: {borrowing_date}\nDays Passed: {days_passed}\nLate Fee: RM{late_fee:.2f}"

        full_info = return_info + return_date_info

        # Display return information in a messagebox
        messagebox.showinfo("Return Confirmation", f"Return Information:\n{full_info}")

if __name__ == "__main__":
    app = ChooseBookPage()
    app.mainloop() 