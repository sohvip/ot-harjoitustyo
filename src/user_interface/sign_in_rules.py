from tkinter import messagebox


def not_empty(username, password):
    '''Tarkistaa onko annetut merkkijonot vähintään yhden merkin pituisia.

    Args:
        username: Käyttäjän syöttämä käyttäjätunnus.
        password: Käyttäjän syöttämä salasana.

    Returns:
        False, jos käyttäjätunnus tai salasana on tyhjä. Muulloin True.
    '''
    if username == '' or password == '':
        messagebox.showinfo('', 'Please enter username and password')
        return False
    return True
