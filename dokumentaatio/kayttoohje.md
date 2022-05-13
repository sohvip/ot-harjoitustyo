# Käyttöohje
Lataa sovelluksen lähdekoodi viimeisimmästä releasesta. Löydät sen GitHub-repositorion kohdasta **Releases**.
## Sovelluksen käynnistäminen
Ennen käynnistämistä asenna poetry: `poetry install`  
Käynnistä sovellus : `poetry run invoke start`
## Uuden käyttäjän luominen
Sovellus on avautuessaan *Sign In* -näkymässä. Uuden käyttäjän pääsee luomaan painamalla näytöllä näkyvää **`Sign Up`**-nappia. 
Napin painaminen vaihtaa näkymän *Sign Up* -näkymään, jossa käyttäjä voi asettaa valitsemansa käyttäjänimen ja salasanan niille tarkoitettuihin tekstikenttiin. 
Käyttäjänimen tulee olla vähintään yhden merkin pituinen ja saman nimistä käyttäjää ei saa olla ennestään olemassa. Salasanan pituuden on oltava vähintään yksi merkki. Viimeinen askel uuden käyttäjän luomiseen on painaa **`Create`**-nappia, joka luo uuden käyttäjän ja tallentaa sen tietokantaan. Sovellus ilmoittaa mikäli käyttäjänimi tai salasana ei ole sopiva.
## Sisäänkirjautuminen
Sovellus avautuu *Sign In* -näkymään, jossa käyttäjä voi asettaa olemassa olevan käyttäjätunnuksen ja salasanan niille osoitettuihin tekstikenttiin. 
Tämän jälkeen painamalla **`Sign In`**-nappia käyttäjä pääsee pelin aloitusnäkymään. Jos käyttäjätiliä ei löydy tai salasana on väärin, ilmestyy ruudulle virheilmoitus.
## Pelin pelaaminen
Pelin aloitusnäkymästä pääsee peliin painamalla keltaista nappia ruudun keskellä. Pelin tarkoituksena on yrittää hypätä mahdollisimman monen piikin yli. 
Pelihahmon saa hyppäämään painamalla välilyöntinäppäintä. Jokainen onnistunut hyppy piikin yli tuo pelaajalle yhden pisteen. Hahmon liikkumisnopeus kasvaa joka viidennen pisteen kohdalla eli kun pistemäärä on 5, 10, 15 jne. Kun pelihahmo osuu piikkiin, peli loppuu ja näkyviin tulee *Game Over* -näkymä. 
Pelaajan keräämät pisteet näkyvät ruudulla ja pisteiden alla on kaksi keltaista nappia. Vasemmalla olevasta napista painamalla pääsee uuteen peliin ja oikeanpuoleisesta takaisin pelin aloitusnäkymään.
## Uloskirjautuminen
Uloskirjautuminen onnistuu painamalla violettia nappia, jossa on ovi ja nuoli. Tällainen nappi löytyy sekä pelin aloitusnäkymän oikeasta alakulmasta että *Game Over* -näkymästä. Napin painaminen vie pelaajan takaisin *Sign In* -näkymään.
## Sovelluksesta poistuminen
Sovelluksesta voi poistua koska tahansa painamalla oikeassa yläkulmassa olevaa punaista raksia.
