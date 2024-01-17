import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from datetime import datetime


class RegisterLoginApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("BONFIRE BOOKSTORE")
        self.geometry("700x400")
        self.config(bg="#ccad72")

        # Load the image using Pillow
        image = Image.open("C:\\Users\\ijlah\\OneDrive - Universiti Teknologi MARA\\IML208\\new logo.jpg")  # Update with your image path
        resized_image = image.resize((280, 160))

        # Convert the image to a PhotoImage object
        pattern_image = ImageTk.PhotoImage(resized_image)

        # Create a label in the window and set the image
        label = tk.Label(self, image=pattern_image)
        label.image = pattern_image  # Keep a reference to the image to prevent garbage collection
        label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

        # Dictionary to store staff and customer information
        self.staff_info = {
            "2022491592": {"password": "icecramel1308", "name": "JEEHA"},
            "2022465764": {"password": "rocketpuncher00", "name": "FATIN"},
            "2022865806": {"password": "040303", "name": "ALYA"},
            "2022495162": {"password": "aamanna", "name": "AISHA"},
        }

        self.customer_info = {}

        # Initialize user_type_var
        self.user_type_var = tk.StringVar(value="staff")

        self.create_widgets()

    def create_widgets(self):
        # Staff and Customer Radiobuttons
        self.staff_radio = tk.Radiobutton(self, text="Staff", variable=self.user_type_var, value="staff")
        self.customer_radio = tk.Radiobutton(self, text="Customer", variable=self.user_type_var, value="customer")

        self.staff_radio.place(relx=0.45, rely=0.4, anchor=tk.CENTER)
        self.customer_radio.place(relx=0.55, rely=0.4, anchor=tk.CENTER)

        # Login frame
        login_frame = tk.Frame(self, bg="#ccad72")
        login_frame.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

        # Login labels and entries
        tk.Label(login_frame, text="ID:", bg="#ccad72", fg='white', font=("Playfair Dispair", 12)).grid(row=0, column=0, pady=5, sticky='e')
        self.entry_ID = tk.Entry(login_frame, font=("Playfair Dispair", 18))
        self.entry_ID.grid(row=0, column=1, pady=5, padx=10, sticky='w')

        tk.Label(login_frame, text="PASSWORD:", bg="#ccad72", fg='white', font=("Playfair Dispair", 12)).grid(row=1, column=0, pady=5, sticky='e')
        self.entry_password = tk.Entry(login_frame, show="*", font=("Playfair Dispair", 18))
        self.entry_password.grid(row=1, column=1, pady=5, padx=10, sticky='w')

        # Login button
        tk.Button(login_frame, text="LOGIN", command=self.login, font=("Playfair Dispair", 13)).grid(row=2, column=0, columnspan=2, pady=10)

        # Register button
        tk.Button(login_frame, text="REGISTER", command=self.register_customer, font=("Playfair Dispair", 13)).grid(row=3, column=0, columnspan=2, pady=10)

    def login(self):
        ID = self.entry_ID.get()
        password = self.entry_password.get()
        user_type = self.user_type_var.get()

        if user_type == "staff":
            staff_ID = self.entry_ID.get()

            if staff_ID in self.staff_info and password == self.staff_info[staff_ID]["password"]:
                staff_name = self.staff_info[staff_ID]["name"]
                messagebox.showinfo("Login successful", f"Welcome, {staff_name}!")
                self.entry_ID.delete(0, tk.END)
                self.entry_password.delete(0, tk.END)
            else:
                messagebox.showerror("Login failed", "Incorrect staff ID or password. Please try again.")
                self.entry_ID.delete(0, tk.END)
                self.entry_password.delete(0, tk.END)

        elif user_type == "customer":
            customer_ID = self.entry_ID.get()
            messagebox.showinfo("Login", "User login successful")

            # Create an instance of the ChooseBookPage class and start its mainloop
            choose_book_page = ChooseBookPage()
            choose_book_page.mainloop()

        else:
            messagebox.showwarning("Login", "Invalid user type")

    def register_customer(self):
        handler = RegistrationHandler(self)
        handler.mainloop()


class RegistrationHandler(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Register - BONFIRE BOOKSTORE")
        self.geometry("1000x600")
        self.config(bg='#ccad72')

        # Register labels and entries
        self.register_label = tk.Label(self, text="BONFIRE BOOKSTORE REGISTRATION", font=("Playfair Dispair", 16), bg='#ccad72', fg='white')
        self.register_label.pack()

        self.name_label = tk.Label(self, text="Name", font=("Playfair Dispair", 16), bg='#ccad72', fg='white')
        self.name_label.pack()
        self.name_entry = tk.Entry(self, font=("Playfair Dispair", 12))
        self.name_entry.pack()

        self.identification_label = tk.Label(self, text="Identification", font=("Playfair Dispair", 16), bg='#ccad72', fg='white')
        self.identification_label.pack()
        self.identification_entry = tk.Entry(self, font=("Playfair Dispair", 12))
        self.identification_entry.pack()

        self.address_label = tk.Label(self, text="Address", font=("Playfair Dispair", 16), bg='#ccad72', fg='white')
        self.address_label.pack()
        self.address_entry = tk.Entry(self, font=("Playfair Dispair", 12))
        self.address_entry.pack()

        self.phone_label = tk.Label(self, text="Phone Number", font=("Playfair Dispair", 16), bg='#ccad72', fg='white')
        self.phone_label.pack()
        self.phone_entry = tk.Entry(self, font=("Playfair Dispair", 12))
        self.phone_entry.pack()

        self.email_label = tk.Label(self, text="Email", font=("Playfair Dispair", 16), bg='#ccad72', fg='white')
        self.email_label.pack()
        self.email_entry = tk.Entry(self, font=("Playfair Dispair", 12))
        self.email_entry.pack()

        self.password_label = tk.Label(self, text="Password", font=("Playfair Dispair", 16), bg='#ccad72', fg='white')
        self.password_label.pack()
        self.password_entry = tk.Entry(self, font=("Playfair Dispair", 12))
        self.password_entry.pack()

        # Gender Dropdown
        self.gender_label = tk.Label(self, text="Gender", font=("Playfair Dispair", 16), bg='#ccad72', fg='white')
        self.gender_label.pack()
        genders = ["Male", "Female"]
        self.gender_var = tk.StringVar()
        self.gender_var.set(genders[0])  # Default selection
        self.gender_menu = tk.OptionMenu(self, self.gender_var, *genders)
        self.gender_menu.config(font=("Playfair Dispair", 12), bg='#ccad72', fg='white')
        self.gender_menu.pack()

        # Category Dropdown
        self.category_label = tk.Label(self, text="Category", font=("Playfair Dispair", 16), bg='#ccad72', fg='white')
        self.category_label.pack()
        categories = ["Student", "OKU", "Child", "Adult"]
        self.category_var = tk.StringVar()
        self.category_var.set(categories[0])  # Default selection
        self.category_menu = tk.OptionMenu(self, self.category_var, *categories)
        self.category_menu.config(font=("Playfair Dispair", 12), bg='#ccad72', fg='white')
        self.category_menu.pack()

        self.register_button = tk.Button(self, text="Register", command=self.register, font=("Playfair Dispair", 12))
        self.register_button.pack()


    def register(self):
        name = self.name_entry.get()
        identification = self.identification_entry.get()
        name = self.name_entry.get()
        identification = self.identification_entry.get()
        address = self.address_entry.get()
        phone_number = self.phone_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        gender = self.gender_var.get()
        category = self.category_var.get()

       
        registration_data = f"Name: {name}\nIdentification: {identification}\nAddress: {address}\nPhone Number: {phone_number}\nEmail: {email}\nPassword: {password}\nGender: {gender}\nCategory: {category}\n"


        # Write the data to a text file
        file_path = 'customer_data.txt'
        with open(file_path, 'a') as file:
            file.write(registration_data + '\n')

        messagebox.showinfo("Registration", "Registration successful!")
        self.destroy()  # Close the register page

        # Close the registration window
        self.destroy()

        # Open the login window
        self.parent.deiconify()

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

        # Calculate the maximum width needed for the dropdown based on the longest book name
        max_book_name_length = max(len(book["Book Name"]) for book in self.books)
        dropdown_width = max(20, max_book_name_length)  # Ensure a minimum width of 20 characters

        book_titles = [book["Book Name"] for book in self.books]
        self.book_selection_menu = tk.OptionMenu(self, self.selected_book, *book_titles)
        self.book_selection_menu.config(font=("Playfair Dispair", 12), bg='#ccad72', fg='white', width=dropdown_width)
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
    app = RegisterLoginApp()
    app.mainloop()
