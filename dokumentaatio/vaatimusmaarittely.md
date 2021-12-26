# Vaatimusmäärittely
## Sovelluksen tarkoitus
Sovellus on versio 2048-pelistä, jossa tavoite on luoda 2048-arvoinen laatta yhdistelemällä samanarvoisia laattoja. Peli loppuu, kun pelattavia siirtoja ei enää ole (pelaaja häviää, ellei ole luonut 2048-laattaa).
## Käyttäjät
Sovelluksessa on vain yksi käyttäjätyyppi, *pelaaja*.
## Keskeinen toiminallisuus
* Pelaaja voi aloittaa uuden pelin, jolloin generoidaan 4x4 pelikenttä, jossa on alussa muutama 2- tai 4-arvoinen laatta.
* Pelaaja voi liikuttaa laattoja joko ylös, alas, oikealle tai vasemmalle. Liikuttaminen tapahtuu nuolinäppäimillä. Liikuttaessa laatat siirtyvät nuolen suuntaan niin pitkälle kuin mahdollista. Jos tiellä on samanarvoinen laatta, yhdistyvät nämä laatat muodostaakseen uuden 2x-arvoisen laatan. Laattojen liikkumisen jälkeen generoidaan  yksi uusi 2- tai 4-arvoinen laatta johonkin tyhjään ruutuun.
* Mahdollisten siirtojen loppuessa pelaaja häviää pelin, ja peli on aloitettava uudestaan "new game"-nappia painamalla. Jos pelaaja saa luotua 2048-arvoisen laatan, onnittelee peli pelaajaa voitosta, mutta peliä voi silti jatkaa eteenpäin.
* Peli seuraa myös pelaajan pistesaldoa, johon saa jokaisesta laattojen yhdistyksestä uuden laatan verran pisteitä lisää. Lisäksi ruudulla näkyy myös ennätystulos, joka muuttuu reaaliaikaisesti, jos nykyinen tulos on uusi ennätys.
## Jatkokehitysideoita
* Highscore-lista. Pelaajan hävitessä pelaaja voi syöttää nimen (tai käyttäjätunnuksen?), joka annetaan pistetuloksen kanssa highscoret sisältävään tauluun. Lista voisi mahdollisesti hyödyntää esimerkiksi Google Docsia, johon sovellus voisi päivittää tuloksia ja myös näyttää ne itse sovelluksessa.
* Kustomoitavat kuvakkeet eri arvoisille laatoille.
