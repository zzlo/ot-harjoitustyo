# Ohjelmistotekniikka, harjoitustyö || 2048
Sovellus on versio 2048-pelistä, jossa tavoitteena on luoda 2048-laatta.

[RELEASE 1](https://github.com/zzlo/ot-harjoitustyo/releases/tag/viikko5)

[FINAL RELEASE](https://github.com/zzlo/ot-harjoitustyo/releases/tag/loppupalautus)

## Dokumentaatio
[vaatimusmaarittely.md](https://github.com/zzlo/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[tuntikirjanpito.md](https://github.com/zzlo/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

- [Käyttöohje](./dokumentaatio/kayttoohje.md)

- [Arkkitehtuurikuvaus](./dokumentaatio/arkkitehtuuri.md)

- [Testausdokumentti](./dokumentaatio/testausdokumentaatio.md)

## Asennus

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

2. Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```

## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:

```bash
poetry run invoke start
```

### Testaus

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi generoida komennolla:

```bash
poetry run invoke coverage-report
```


### Pylint

Tiedoston [.pylintrc](./.pylintrc) määrittelemät tarkistukset voi suorittaa komennolla:

```bash
poetry run invoke lint
```
