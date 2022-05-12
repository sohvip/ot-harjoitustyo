from tkinter import Tk
from user_interface.user_interface import UI


def main():
    '''Alustaa kirjautumisikkunan ja kutsuu sen näkyviin.'''
    window = Tk()
    window.title('Starkour')
    window.geometry('640x480')
    window.configure(bg='#8B5499')
    sign_in = UI(window)
    sign_in.start()
    window.mainloop()


if __name__ == "__main__":
    main()
