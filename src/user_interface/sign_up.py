from tkinter import ttk


class SignUp:
    def __init__(self, root, create, back):
        self.root = root
        self.frame = None
        self.create = create
        self.back = back
        self.username = None
        self.password = None
        self.set_up()

    def set_up(self):
        self.frame = ttk.Frame(master=self.root)
        heading = ttk.Label(master=self.frame, text='Sign Up',
                            font=('calibre', 13, 'bold'))
        text_1 = ttk.Label(master=self.frame, text='Username')
        text_2 = ttk.Label(master=self.frame, text='Password')
        self.username = ttk.Entry(master=self.frame)
        self.password = ttk.Entry(master=self.frame, show='*')
        create = ttk.Button(master=self.frame,
                            text='Create', command=self.create)
        back = ttk.Button(master=self.frame, text='Back', command=self.back)
        heading.pack()
        text_1.pack()
        self.username.pack()
        text_2.pack()
        self.password.pack()
        create.pack()
        back.pack()
        self.frame.pack()

    def destroy(self):
        self.frame.destroy()
