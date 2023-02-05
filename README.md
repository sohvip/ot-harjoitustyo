# Starkour  
2D-tasohyppelypeli, jossa tavoitteena hypätä mahdollisimman monen esteen yli.  
  
![Screenshot from 2023-02-05 19-00-48](https://user-images.githubusercontent.com/95978191/216833384-bb9cdd3c-d351-4d6f-b035-c37c8b196163.png)
![Screenshot from 2023-02-05 19-02-09](https://user-images.githubusercontent.com/95978191/216833386-03bbf8dc-9b6e-4552-8db8-7d9c901ae563.png)
![Screenshot from 2023-02-05 19-02-21](https://user-images.githubusercontent.com/95978191/216833394-08f8b154-3aaa-41ed-9e88-5a58f9c26e82.png)

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
