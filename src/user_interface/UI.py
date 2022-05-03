from user_interface.sign_in import SignIn
from user_interface.sign_up import SignUp
from user_interface.sign_in_rules import not_empty
from start import Start
from accounts import Account


class UI:
    def __init__(self, root):
        self.root = root
        self.current = None
        self.account = Account()

    def start(self):
        self.sign_in_view()

    def sign_in_view(self):
        self.destroy_current()
        self.current = SignIn(self.root, self.press_login, self.press_sign_up)

    def sign_up_view(self):
        self.destroy_current()
        self.current = SignUp(self.root, self.press_create, self.press_back)

    def press_login(self):
        correct = not_empty(self.current.username.get(),
                            self.current.password.get())
        if correct:
            correct_2 = self.account.find_account(
                self.current.username.get(), self.current.password.get())
            if correct_2:
                self.root.destroy()
                start = Start()
                start.start()

    def press_sign_up(self):
        self.sign_up_view()

    def press_create(self):
        correct = not_empty(self.current.username.get(),
                            self.current.password.get())
        if correct:
            correct_2 = self.account.new_account(
                self.current.username.get(), self.current.password.get())
            if correct_2:
                self.sign_in_view()

    def press_back(self):
        self.sign_in_view()

    def destroy_current(self):
        if self.current:
            self.current.destroy()
        self.current = None
