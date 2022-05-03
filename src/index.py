from tkinter import Tk
from user_interface.UI import UI


def main():
    window = Tk()
    window.title('Starkour')
    window.geometry('640x480')
    sign_in = UI(window)
    sign_in.start()
    window.mainloop()


if __name__ == "__main__":
    main()
