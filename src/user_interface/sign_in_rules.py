from tkinter import messagebox


def not_empty(username, password):
    if username == '' or password == '':
        messagebox.showinfo('', 'Please enter username and password')
        return False
    return True
