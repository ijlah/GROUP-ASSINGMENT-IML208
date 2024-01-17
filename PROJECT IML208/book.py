import sqlite3
from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as mb
import tkinter.simpledialog as sd

# Connecting to Database
connector = sqlite3.connect('bookstore.db')
cursor = connector.cursor()

connector.execute(
    'CREATE TABLE IF NOT EXISTS Bookstore (BK_NAME TEXT, ISBN TEXT PRIMARY KEY NOT NULL, AUTHOR_NAME TEXT, BK_STATUS TEXT)'
)


def issuer_card():
    return 'N/A'

def display_records():
    global connector, cursor
    global tree

    tree.delete(*tree.get_children())

    curr = connector.execute('SELECT * FROM Bookstore')
    data = curr.fetchall()

    for records in data:
        tree.insert('', END, values=records)


def clear_fields():
    global bk_status, ISBN , bk_name, author_name

    bk_status.set('Available')
    for i in ['ISBN', 'bk_name', 'author_name']:
        exec(f"{i}.set('')")
    ISBN_entry.config(state='normal')
    try:
        tree.selection_remove(tree.selection()[0])
    except:
        pass

def display_customer_list():
    mb.showinfo('Customer List', 'Displaying Customer List') 

def buy_borrow():
    mb.showinfo('Buy/Borrow', 'Processing Buy/Borrow')  

def clear_and_display():
    clear_fields()
    display_records()


def view_record():
    global bk_name, ISBN, bk_status, author_name
    global tree

    if not tree.focus():
        mb.showerror('Select a row!', 'To view a record, you must select it in the table. Please do so before continuing.')
        return

    current_item_selected = tree.focus()
    values_in_selected_item = tree.item(current_item_selected)
    selection = values_in_selected_item['values']

    bk_name.set(selection[0])
    ISBN.set(selection[1])
    bk_status.set(selection[3])
    author_name.set(selection[2])


def add_record():
    global connector
    global bk_name, ISBN , author_name, bk_status

    surety = mb.askyesno('Are you sure?',
                         'Are you sure this is the data you want to enter?\nPlease note that Book ID cannot be changed in the future')

    if surety:
        try:
            connector.execute(
                'INSERT INTO Bookstore (BK_NAME, ISBN, AUTHOR_NAME, BK_STATUS) VALUES (?, ?, ?, ?)',
                (bk_name.get(), ISBN.get(), author_name.get(), bk_status.get()))
            connector.commit()

            clear_and_display()

            mb.showinfo('Record added', 'The new record was successfully added to your database')
        except sqlite3.IntegrityError:
            mb.showerror('ISBN already in use!',
                         'The ISBN you are trying to enter is already in the database, please alter that book\'s record or check any discrepancies on your side')


def update_record():
    def update():
        global bk_status, bk_name, ISBN , author_name
        global connector, tree

        cursor.execute(
            'UPDATE Bookstore SET BK_NAME=?, BK_STATUS=?, AUTHOR_NAME=? WHERE ISBN=?',
            (bk_name.get(), bk_status.get(), author_name.get(), ISBN.get())
        )
        connector.commit()

        clear_and_display()

        edit.destroy()
        ISBN_entry.config(state='normal')
        clear.config(state='normal')

    view_record()

    ISBN_entry.config(state='disable')
    clear.config(state='disable')

    edit = Button(left_frame, text='Update Record', font=btn_font, bg=btn_hlb_bg, width=20, command=update)
    edit.place(x=50, y=375)


def remove_record():
    if not tree.selection():
        mb.showerror('Error!', 'Please select an item from the database')
        return

    current_item = tree.focus()
    values = tree.item(current_item)
    selection = values["values"]

    cursor.execute('DELETE FROM Bookstore WHERE ISBN=?', (selection[1],))
    connector.commit()

    tree.delete(current_item)

    mb.showinfo('Done', 'The record you wanted deleted was successfully deleted.')

    clear_and_display()


def delete_inventory():
    if mb.askyesno('Are you sure?',
                   'Are you sure you want to delete the entire inventory?\n\nThis command cannot be reversed'):
        tree.delete(*tree.get_children())

        cursor.execute('DELETE FROM Bookstore')
        connector.commit()
    else:
        return


def change_availability():
    global tree, connector

    if not tree.selection():
        mb.showerror('Error!', 'Please select a book from the database')
        return

    current_item = tree.focus()
    values = tree.item(current_item)
    ISBN = values['values'][1]
    BK_status = values["values"][3]

    if BK_status == 'Issued':
        surety = mb.askyesno('Is return confirmed?', 'Has the book been returned to you?')
        if surety:
            cursor.execute('UPDATE Bookstore SET bk_status=?, WHERE ISBN=?', ('Available', ISBN))
            connector.commit()
    else:
        mb.showinfo(
            'Cannot be returned', 'The book status cannot be set to Available unless it has been returned')

   
        cursor.execute('UPDATE Bookstore SET bk_status=?, where ISBN=?', ('Issued', ISBN))
        connector.commit()

    clear_and_display()


# Variables
lf_bg = '#FFE4C4'  # Light Goldenrod Yellow
rtf_bg = '#FFD700'  # Gold
rbf_bg = '#DAA520'  # Goldenrod
btn_hlb_bg = '#B8860B'  # Dark Goldenrod  

lbl_font = ('Georgia', 13)  # Font for all labels
entry_font = ('Times New Roman', 12)  # Font for all Entry widgets
btn_font = ('Gill Sans MT', 13)

# Initializing the main GUI window
root = Tk()
root.title('BONFIRE BOOKSTORE')
root.geometry('1110x700')
root.resizable(0, 0)

Label(root, text='BONFIRE BOOKSTORE', font=("Noto Sans CJK TC", 15, 'bold'), bg=btn_hlb_bg,
      fg='White').pack(side=TOP, fill=X)

# StringVars
bk_status = StringVar()
bk_name = StringVar()
ISBN = StringVar()
author_name = StringVar()

# Frames
left_frame = Frame(root, bg=lf_bg)
left_frame.place(x=0, y=30, relwidth=0.3, relheight=0.96)

RT_frame = Frame(root, bg=rtf_bg)
RT_frame.place(relx=0.3, y=30, relheight=0.2, relwidth=0.7)

RB_frame = Frame(root)
RB_frame.place(relx=0.3, rely=0.24, relheight=0.785, relwidth=0.7)

# Left Frame
Label(left_frame, text='Book Name', bg=lf_bg, font=lbl_font).place(x=98, y=25)
Entry(left_frame, width=25, font=entry_font, text=bk_name).place(x=45, y=55)

Label(left_frame, text='ISBN', bg=lf_bg, font=lbl_font).place(x=110, y=105)
ISBN_entry = Entry(left_frame, width=25, font=entry_font, text=ISBN)
ISBN_entry.place(x=45, y=135)

Label(left_frame, text='Author Name', bg=lf_bg, font=lbl_font).place(x=90, y=185)
Entry(left_frame, width=25, font=entry_font, text=author_name).place(x=45, y=215)

Label(left_frame, text='Status of the Book', bg=lf_bg, font=lbl_font).place(x=75, y=265)
dd = OptionMenu(left_frame, bk_status, *['Available', 'Issued'])
dd.configure(font=entry_font, width=12)
dd.place(x=75, y=300)

submit = Button(left_frame, text='Add new record', font=btn_font, bg=btn_hlb_bg, width=20, command=add_record)
submit.place(x=50, y=375)

clear = Button(left_frame, text='Clear fields', font=btn_font, bg=btn_hlb_bg, width=20, command=clear_fields)
clear.place(x=50, y=435)


# Button to display Customer List
display_customer_button = Button(left_frame, text='Display Customer List', font=btn_font, bg=btn_hlb_bg, width=20, command=display_customer_list)
display_customer_button.place(x=50, y=500)

# Button for Buy/Borrow
buy_borrow_button = Button(left_frame, text='Buy/Borrow', font=btn_font, bg=btn_hlb_bg, width=20, command=buy_borrow)
buy_borrow_button.place(x=50, y=556)

# Right Top Frame
Button(RT_frame, text='Delete book record', font=btn_font, bg=btn_hlb_bg, width=17, command=remove_record).place(
    x=8, y=30)
Button(RT_frame, text='Delete full inventory', font=btn_font, bg=btn_hlb_bg, width=17,
       command=delete_inventory).place(x=178, y=30)
Button(RT_frame, text='Update book details', font=btn_font, bg=btn_hlb_bg, width=17,
       command=update_record).place(x=348, y=30)
Button(RT_frame, text='Change Book Availability', font=btn_font, bg=btn_hlb_bg, width=19,
       command=change_availability).place(x=518, y=30)

# Right Bottom Frame
Label(RB_frame, text='BOOK INVENTORY', bg=rbf_bg, font=("Noto Sans CJK TC", 15, 'bold')).pack(side=TOP, fill=X)

tree = ttk.Treeview(RB_frame, selectmode=BROWSE,
                    columns=('Book Name', 'ISBN', 'Author', 'Status'))

XScrollbar = Scrollbar(tree, orient=HORIZONTAL, command=tree.xview)
YScrollbar = Scrollbar(tree, orient=VERTICAL, command=tree.yview)
XScrollbar.pack(side=BOTTOM, fill=X)
YScrollbar.pack(side=RIGHT, fill=Y)

tree.config(xscrollcommand=XScrollbar.set, yscrollcommand=YScrollbar.set)

tree.heading('Book Name', text='Book Name', anchor=CENTER)
tree.heading('ISBN', text='ISBN', anchor=CENTER)
tree.heading('Author', text='Author', anchor=CENTER)
tree.heading('Status', text='Status of the Book', anchor=CENTER)

tree.column('#0', width=0, stretch=NO)
tree.column('#1', width=225, stretch=NO)
tree.column('#2', width=70, stretch=NO)
tree.column('#3', width=150, stretch=NO)



tree.place(y=30, x=0, relheight=0.9, relwidth=1)

clear_and_display()

# Finalizing the window
root.update()
root.mainloop()
