# Arkkitehtuurikuvaus

## Rakenne

Ohjelman rakenne on melko alkeellinen, jossa sovelluslogiikka ja käyttöliittymä on pääsääntöisesti eriytetty niistä vastaaviin Level- ja Ui-luokkiin.

## Käyttöliittymä

Käyttöliittymä muodostuu sovelluksessa vain pelinäkymästä. Näkymän näyttäminen on pääosin Ui-luokan tehtävä, mutta laattojen numerot luodaan sovelluslogiikan muodostavassa Level-luokassa.

## Sovelluslogiikka

Sovelluslogiikasta vastaa Level-luokka. Luokka alustaa pelilaudan, ja luo sille uusia laattoja reagoiden annetun syötteen perusteella.

## Tietojen tallennus

Level-luokan metodi _save_score() vastaa tiedon tallettamisesta, ja _read_score() lukemisesta. Metodit käyttävät tiedostoa highscore.txt-tiedostoa, joka luodaan jos juuresta ei löydy ko. nimistä tiedostoa entuudestaan.
