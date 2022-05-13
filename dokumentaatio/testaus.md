# Testausdokumentti
Sovellusta on testattu automatisoiduin testein unittestilla.
## Testaus
Testit löytyvät *src*-kansion alta *tests*-kansiosta. Testiluokat on nimetty kaikki samalla periaatteella testattavien luokkien tiedostojen nimien mukaan.  
Esimerkiksi `Start`-luokka on tiedostossa *start.py*, joten sitä vastaava testiluokka on nimeltään `TestStart`.
## Testikattavuus
Sovelluksen testikattavuus on 71%, kun mukaan ei oteta puhtaasti käyttöliittymästä vastaavia luokkia.
![testikattavuus](https://user-images.githubusercontent.com/95978191/168306836-817579b2-6d98-422a-ba3d-03a4116e53a2.png)  
`Start`-, `Play`-, ja `End`-luokissa olevat *get_events()*-funktiot on jätetty testauksen ulkopuolelle, sillä ne kuuluvat käyttöliittymään ja laskivat siksi testaamattomina testikattavuusprosenttia alemmaksi kuin se oikeasti on.
Muutenkin edellä mainituissa luokissa on sekaisin käyttöliittymää ja sovelluslogiikkaa, joten testikattavuus jää niissä 50% paikkeille. Kaikki testattavan arvoinen on pyritty testaamaan.
## Huomio
Testit ajaessa näytölle ilmestyy ilmoituksia (5 kpl), jotka pitää kaikki sulkea yksi kerrallaan painamalla `OK` tai yläkulman punaista raksia, jotta testit saadaan suoritettua loppuun.
