# Starkour  
2D-tasohyppelypeli, jossa tavoitteena hypätä mahdollisimman monen esteen yli.

## Näin pelaat
- hyppy = välilyöntinäppäin

## Release-linkit
[loppupalautus](https://github.com/sohvip/ot-harjoitustyo/releases/tag/loppupalautus)  
[viikko 6](https://github.com/sohvip/ot-harjoitustyo/releases/tag/viikko6)  
[viikko 5](https://github.com/sohvip/ot-harjoitustyo/releases/tag/viikko5) 

## Dokumentaatio 
[vaatimusmaarittely.md](https://github.com/sohvip/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)  
[tuntikirjanpito.md](https://github.com/sohvip/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)  
[changelog.md](https://github.com/sohvip/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)  
[arkkitehtuuri.md](https://github.com/sohvip/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)  
[kayttoohje.md](https://github.com/sohvip/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)  
[testaus.md](https://github.com/sohvip/ot-harjoitustyo/blob/master/dokumentaatio/testaus.md)  

## Käynnistys
- asenna poetry: `poetry install`
- käynnistä peli: `poetry run invoke start`

## Testaaminen
- testien suorittaminen: `poetry run invoke test`
- testikattavuus: `poetry run invoke coverage`
- testikattavuusraportti: `poetry run invoke coverage-report`
- pylint: `poetry run invoke lint`
