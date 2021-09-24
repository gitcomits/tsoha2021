# tsoha2021
opetussovellus - tsoha lab work 2021

Opetussovellus

Sovelluksen avulla voidaan järjestää verkkokursseja, joissa on tekstimateriaalia ja automaattisesti tarkastettavia tehtäviä. Jokainen käyttäjä on opettaja tai opiskelija.

Sovelluksen ominaisuuksia:

    Käyttäjä voi kirjautua sisään ja ulos sekä luoda uuden tunnuksen.
      - käyttäjäryhmiä on kaksi, molemmilla omat oikeutensa
      
    Opiskelija näkee listan kursseista ja voi liittyä kurssille.
      - samalle kurssille ei voi olla ilmoitautuneena kuin kerran samanaikaisesti 
      
    Opiskelija voi lukea kurssin tekstimateriaalia sekä ratkoa kurssin tehtäviä.
      - tehtävien ratkaiseminen lasketaan tentti tilaisuudeksi, mahdollisuuksia on vain yksi
    
    Opiskelija pystyy näkemään tilaston, mitkä kurssin tehtävät hän on ratkonut.
    
    Opettaja pystyy luomaan uuden kurssin, muuttamaan olemassa olevaa kurssia ja poistamaan kurssin.
      - jos joku on jo ehtinyt suorittaa kurssin ennen sen poistamista jää siitä merkintä näkyviin
    
    Opettaja pystyy lisäämään kurssille tekstimateriaalia ja tehtäviä. Tehtävä voi olla ainakin monivalinta tai tekstikenttä, johon tulee kirjoittaa oikea vastaus.
    
    Opettaja pystyy näkemään kurssistaan tilaston, keitä opiskelijoita on kurssilla ja mitkä kurssin tehtävät kukin on ratkonut.


-----------------
24.9.2021

Sovellusta on mahdollista testata osoitteessa:


https://onlin3school.herokuapp.com/


Tämän hetkinen versio toimii kirjautumisen osin, sivuilla ei ole vielä muuta sisältöä.

Rekisteröityminen
	- käyttäjä syöttää sähköpostin
			   nimen 
			   valitsee ryhmän johon kuuluu
			   salasanan
			   salasanan varmennuksen
	
	Ohjelma tarkistaa että sähköposti on valiidi, ettei käyttäjätunnus ole jo varattu, ettei sähköposti ole jo varattu sekä salasanan täsmäämisen
	Tämän jälkeen ne tallennetaan tietokantaan ja käyttäjä ohjautuu sisäänkirjautumis sivulle
	Onnistuneen sisäänkirjautumisen jälkeen henkilö pysyy sisään kirjautuneena kunns kirjautuu ulos 'Logout' painikkeella
	Riippuen siitä onko kirjautunut opiskelijana tai opettajana näkyy/ei näy Upload courses linkki (ei toiminnassa vielä)
	Account sivu näyttää kirjautuneen tiedot

 
