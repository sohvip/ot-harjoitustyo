from tkinter import ttk


class SignIn:
    '''Rakentaa kirjautumisnäkymän.'''

    def __init__(self, root, login, sign_up):
        '''Luokan konstruktori. Rakentaa kirjautumisnäkymän.

        Args:
            root: Tkinter-elementti, johon näkymä alustetaan.
            login: Funktio, jota kutsutaan, kun login-nappia painetaan.
            sign_up: Funktio, jota kutsutaan, kun sign up -nappia painetaan.
        '''
        self.root = root
        self.frame = None
        self.username = None
        self.login = login
        self.password = None
        self.sign_up = sign_up
        self.set_up()

    def set_up(self):
        '''Asettelee kirjautumisnäkymän elementit paikoilleen'''
        self.frame = ttk.Frame(master=self.root)
        heading = ttk.Label(master=self.frame, text='Sign In',
                            font=('calibre', 13, 'bold'))
        text_1 = ttk.Label(master=self.frame, text='Username')
        text_2 = ttk.Label(master=self.frame, text='Password')
        self.username = ttk.Entry(master=self.frame)
        self.password = ttk.Entry(master=self.frame, show='*')
        login = ttk.Button(master=self.frame, text='Login', command=self.login)
        sign_up = ttk.Button(
            master=self.frame, text='Sign Up', command=self.sign_up)
        heading.pack()
        text_1.pack()
        self.username.pack()
        text_2.pack()
        self.password.pack()
        login.pack()
        sign_up.pack()
        self.frame.pack()

    def destroy(self):
        '''Tuhoaa näkymän.'''
        self.frame.destroy()
