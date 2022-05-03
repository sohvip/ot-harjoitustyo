from tkinter import ttk


class SignUp:
    '''Rakentaa rekisteröitymisnäkymän.'''

    def __init__(self, root, create, back):
        '''Luokan konstruktori. Rakentaa rekisteröitymisnäkymän.

        Args:
            root: Tkinter-elementti, johon näkymä alustetaan.
            create: Funktio, jota kutsutaan, kun create-nappia painetaan.
            back: Funktio, jota kutsutaan, kun back-nappia painetaan.
        '''
        self.root = root
        self.frame = None
        self.create = create
        self.back = back
        self.username = None
        self.password = None
        self.set_up()

    def set_up(self):
        '''Asettelee rekisteröintinäkymän elementit paikoilleen'''
        self.frame = ttk.Frame(master=self.root)
        sign_up = ttk.Label(master=self.frame, text='Sign Up',
                            font=('calibre', 13, 'bold'))
        text = ttk.Label(master=self.frame, text='Username')
        text_2 = ttk.Label(master=self.frame, text='Password')
        self.username = ttk.Entry(master=self.frame)
        self.password = ttk.Entry(master=self.frame, show='*')
        create = ttk.Button(master=self.frame,
                            text='Create', command=self.create)
        back = ttk.Button(master=self.frame, text='Back', command=self.back)
        sign_up.pack()
        text.pack()
        self.username.pack()
        text_2.pack()
        self.password.pack()
        create.pack()
        back.pack()
        self.frame.pack()

    def destroy(self):
        '''Tuhoaa näkymän.'''
        self.frame.destroy()
