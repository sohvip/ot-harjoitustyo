# Arkkitehtuurikuvaus

## Käyttöliittymä
Sovelluksessa on viisi näkymää:
- sisäänkirjautuminen
- uuden käyttäjän luominen
- pelin aloitusruutu
- pelin pelaaminen
- game over

## Luokkakaavio
```mermaid
  classDiagram
      UI --> SignIn
      UI --> SignUp
      UI --> Account
      UI --> Start
      Start --> Play
      Play --> Spike
      Play --> Background
      Play --> Starie
      Play --> End   
```
## Sekvenssikaavio uuden käyttäjän luomisesta
```mermaid
  sequenceDiagram
    actor User
    participant UI
    participant SignIn
    participant SignUp
    participant Account
    User->>SignIn: click "Sign Up" button
    User->>SignUp: enter username and password
    User->>SignUp: click "Create" button
    SignUp->>UI: press_create()
    UI->>UI: not_empty('ditto', '012')
    UI->>Account: new_account('ditto', '012')
    Account-->>SignIn: ready to sign in
```
## Sekvenssikaavio sisäänkirjautumisesta
```mermaid
  sequenceDiagram
    actor User
    participant UI
    participant SignIn
    participant Account
    participant Start
    User->>SignIn: enter username and password
    User->>SignIn: click "Sign In" button
    UI->>UI: not_empty('ditto', '012')
    UI->>Account: find_account('ditto', '012')
    Account-->>UI: account found and password correct
    UI->>Start: to the games start screen
```
## Sekvenssikaavio pelin kulusta
```mermaid
  sequenceDiagram
    actor User
    participant Start
    participant Play
    participant .End
    User->>Start: click "play" button
    Start->>Play: gameloop()
    User->>Play: press SPACE
    Play->>Play: starie_jump()
    Play->>.End: end_screen() (when player collides with an obstacle)
```
## Tietojen tallentaminen
Käyttäjien kirjautumistiedot tallennetaan pysyvästi `accounts.db`-nimiseen SQLite-tietokantaan `accounts.py`-tiedoston `Account`-luokassa.
