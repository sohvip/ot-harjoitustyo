```mermaid
  classDiagram
      Nopat -- Pelinappula
      Pelinappula -- Ruutu
      Pelinappula "1" -- "1" Pelaaja
      Ruutu --> Seuraava_Ruutu
      Ruutu -- Aloitusruutu
      Ruutu -- Vankila
      Ruutu -- Sattuma_ja_Yhteismaa
      Sattuma_ja_Yhteismaa -- Kortit
      Kortit --> Toiminto
      Aloitusruutu --> Toiminto
      Vankila --> Toiminto
      Ruutu -- Asemat_ja_Laitokset
      Ruutu -- Normaalit_Kadut
      Asemat_ja_Laitokset --> Toiminto
      Normaalit_Kadut --> Toiminto
      Normaalit_Kadut "1" -- "1" Nimi
      Normaalit_Kadut -- Rakentaminen
      Rakentaminen --> Pelaaja
      Pelaaja --> Raha
      Ruutu "40" -- "1" Pelilauta
      
```

