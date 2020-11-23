# IKT105 - Sammendrag

All teksten er hentet fra hallvard sine slides.
Har skrevet alt inn her for det som jeg mener er viktigt å huske samt, ting som er markert med rød tekst og som **GENERELT** er viktig å huske :)

# Forelesninger
## K01_Generelt_om_databaser
* En  samling av data
* En samling av relatert informasjon
### Hva består en database av ? 
* Selve databasen med lagrede data.
* Data Dictionary (systemkataloger)
    * Med alle nødvendige opplysninger om databasens struktur
* DBMS - Database Management System
    * Database Software til operasjoner på databasen

### DBMS
* Software system for håndtering av informasjon i en database.
* Software system for å organisere data som modellerer informasjon fra den virkelige verden.
* DBMS har 4 hoved-oppgaver
    * Akseptere data og instruksjoner fra bruker
    * Gjenfinne informasjon fra databasen
    * oppdatere databasen
    * Sikre dataen i databasen

### Ulike typer databaser
* Hierakiske databaser
* Nettverks-databaser
* Invertert liste database
* Relasjons-database

![](https://i.imgur.com/zdoWDPG.png)

## K02_Relasjonsdatabaser
### Tabeller
* Dataene i en relasjonsdatabse er plasser i to-dimensjonale tabeller
* En Relasjons-database består av tabeller

### Hva er en relasjons-database
* En relasjons-database er en database hvor alle dateene er samlet i to-dimensjonale tabeller og hvor tabellene eventuelt står i en 1:1 eller 1:n relasjon til hverandre
* Tabellene er inndelt i rader (records) og kolonner(felter)

### Viktige fortrinn ved relasjons-database
* Reduserer laglring av redundante data.
* Data kan kan lett omorganiseres og kombineres i nye relasjoner, de er ikke låst til faste relasjoner pga måten de er lagret på.
* Data kan lett oppdateres i det disse vil bli oppdatert på et minimum antall steder.
* Reduserer behovet for disk-plass

### 3 Sentrale gjenfinnings-operasjoner i Codd's relasjons-algebra
* Selection
    * Ekstraherer alle rader fra en tabell, hvor radene oppfyller gitte kriterier
* Projection
    * Ekstraherer en eller flere kolonner fra en tabell
* Join
    * Ekstraherer kolonner fra flere relaterte tabeller
![](https://i.imgur.com/vxvqbs0.png)


### Normal-Former
* [TL;DR Normal-Former](https://www.youtube.com/watch?v=UDFRhj_K508)
![](https://i.imgur.com/bcjY11E.png)
* SNr
    * Selger-nummer
* Navn
    * Selger-navn
* PNr
    * Post-nummer
* Sted
    * Post-Sted
* VNr
    * Vare-nummer
* Pris
    * Vare-Pris
* Mg
    * Vare-mengde

### 1NF - Første Normalform
* Hver tabell skal ha en fast postlengde
* Det skal være kun en post-type pr. tabell
* Hver post skal ha et eget identifikasjons-felt ( ID )
* Før 1NF
    * ![](https://i.imgur.com/gR1CIvR.png)
* Etter 1NF 
    * ![](https://i.imgur.com/VDeNVJO.png)

Ved første normalform så har man da satt opp slik at det bare er
SNr, Navn, PNr, Sted, VNr, Pris og Mg i den nye tabellen, for da når man skal legge inn flere varer så slipper man å måtte utvide tabellen med flere felter

### 2NF - Andre Normalform
* Databasen må være på 1.normalform
* Deler av ID skal ikke kune være determinantfelt for andre felt, dvs deler av ID skal ikke entydig kunne bestemme verdier i et annet felt.
* Før 2NF
    * ![](https://i.imgur.com/EBRwaqS.png)
* Etter 2NF
    * ![](https://i.imgur.com/nu0jzQP.png)

Etter andre normalform, så separerer man ting enda mer så man da kan ha en egen tabell for selgere og kan da enkelt oppdatere selgere uten å måtte oppdatere hele tabelle med varer.
Og samme med vare, man trenger ikke å oppdatere alt når man får inn en ny vare, men heller bare oppdatere vare nummer og pris
og til slutt ha en Tabell som inneholder en identifikator til Selger og vare og da ha en egen tabell for Selger id og vare id og hvor mye mengde de skal ha :)

### 3NF - Tredje Normalform
* Databasen må være på 2.normalform
* Det må ikke eksistere noen funksjonellel avhengigheter mellomegenskapsfeltene (felter utenom ID-feltene)
* Før 3NF
    * ![](https://i.imgur.com/LwOx8wP.png)
* Etter 3NF
    * ![](https://i.imgur.com/PAQcP3r.png)
* Hvordan ting er koblet sammen
    * ![](https://i.imgur.com/HagHNzG.png)

### Modellator - Notasjon
* Kråkefot
    * Uten attributter
        * ![](https://i.imgur.com/saCquFo.png)
    * Med attributter
        * ![](https://i.imgur.com/GebdCDG.png)

### Modellator
* Kråkefot
    * ![](https://i.imgur.com/gKQ9V35.png)
* Gaffel
    * ![](https://i.imgur.com/H7wCSuM.png)
* Pil
    * ![](https://i.imgur.com/4c9op7w.png)
* Pil/Dobbeltpil
    * ![](https://i.imgur.com/ovOE7hO.png)
* Antall
    * ![](https://i.imgur.com/d0HLnFB.png)
* Niam-basert
    * ![](https://i.imgur.com/WBlfuiR.png)
* Kan/ Må
    * ![](https://i.imgur.com/ogCvOCV.png)

### 1:n ( 0...m - 1...1 )
* Kråkefot
    * ![](https://i.imgur.com/qv0EiUv.png)
* Niam-basert
    * ![](https://i.imgur.com/n5VNxBP.png)
* Pil 
    * ![](https://i.imgur.com/Wm7xDxg.png)

### 1:1 ( 0...1 - 1..1 )
* Kråkefot
    * ![](https://i.imgur.com/bS9cOXL.png)
* Niam-basert
    * ![](https://i.imgur.com/a6AObsI.png)
* Pil
    * ![](https://i.imgur.com/D2enHKP.png)

### Generellt metode for tilordning av 3NF-tabeller (0)
* Vi går tilbake til vår opprinnelige Selger-tabell på 1NF form
* Følgende felter er med i denne 1NF-tabellen 
    * ID er markerkt med *

```
* SNr       Selger-nummer
Navn      Selger-Navn
PNr       Post-nummer
Sted      Post-sted
* VNr       Vare-nummer
Pris      Vare-pris
Mg        Vare-mengde
```

### Generell metode for tilordning av 3NF-tabeller (1)
1. Vi tegner inn relasjoner  (piler) fra de feltene som entydig bestemmer verdiene i andre felter til disse andre feltene.
* Total (1NF)
    * ![](https://i.imgur.com/zkxu8WL.png)

----

2. Lag en ny tabell ved å plukke ut alle *-feltene som er funksjonelt avhengig av alle disse *-feltene. Denne nye tabellen vil være på 2NF
![](https://i.imgur.com/Pc1jjkh.png)

----

3. Hvis det u 1NF-tabellen finnes felt som er avhengig av en ekte delmengde av *-feltene, plukkes disse ut sammen med tilhørende *-felt  i egne tabeller. Disse nye tabeellene vil være på 2NF.
* Selger (2NF)
    * ![](https://i.imgur.com/YM8HhRL.png)
* Vare (2NF)
    * ![](https://i.imgur.com/doOi1tq.png)

----

4. Hvis det i noen av våre 2NF-tabeller (Salg, Selger, Vare) finnes ikke-*-felter (ikke ID-felter) som entydig bestemmer verdier i andre ikke-*-felter, plukkes disse nevnte feltene ut i egne tabeller. I vårt eksempel gjelder dette tabellen Selger (PNr bestemmer Sted). Tabellen Selger splitter i to:
* Tabellene Selger og Adr(Adresse)
* Selgeer-tabellen beholder informasjon om PNr.
* ID i disse nye tabellene vil være de feltene som entydig bestemme andre felt-verdier.
* Alle tabellene vil nå være på 3NF
* Selger (3NF)
    * ![](https://i.imgur.com/dO85aCN.png)
* Adr (3NF)
    * ![](https://i.imgur.com/cOAHAUx.png)

----

5. Alle våre 4 tabeller (Selger, Adr, Vare, Salg) vil nå oppfylle 3NF.
* Selger (3NF)
    * ![](https://i.imgur.com/7O4Dvui.png)
* Adr (3NF)
    *  ![](https://i.imgur.com/pFZEXb2.png)
* Salg (3NF)
    * ![](https://i.imgur.com/fnSlyfi.png)
* Vare (3NF)
    * ![](https://i.imgur.com/4vDyHaj.png)

----

6. Følgende relasjoner gjelder mellom våre 4 tabeller ( Selger, Adr, Vare, Salg ) Vil nå oppfylle 3NF
![](https://i.imgur.com/Ban1VhZ.png)
### Select Statement
* SELECT 
    * kolonner
* FROM
    * Tabeller
* WHERE
    * rader

## K04_Datamodellering_Ny_Kråkefot
### Datamodellering
* Et språk for å analysere og beskrive virkeligheten.
* En metode for å beskrive naturlige sammenhenger i data som skal benyttes i et informasjons-system

### Objekt
* Et Objekt er en gjenstand eller et begrep som er entydig identifiserbar.
* En bil er et objekt
    * Denne bilen kan vi identifisere eller gjenkjenne ved identifikasjonen bilnummer siden biler har ulikt bilnummer
    * ID = bilnummer
* En person er et objekt
    * Personen kan vi identifisere ved hjelp av navn hvis den gruppa personer vi betrakter er slik at ingen har samme navn.
    * ID = fødselsnummer
* Et tidspunkt kan vi betrakte som et objekt.
    * ID = Dato + Klokkeslett

### Attributt
* Attributt (egenskaper)
    * Med attributt mener vi en egenskap knuttet til et objekt
* Attributter knyttet til en bil kan være
    * Farge
    * Vekt
    * Pris
    * Årsmodell
* Attributter knyttet til en person kan være
    * Alder
    * Høyde
    * Vekt
    * Yrkee

### Verdi
* Verdi
    * Verdiene en attributt kan anta
* Attributtet Farge kan ha verdiene
    * Rød
    * Blå
    * Grønn
* Attributtet Yrke kan ha verdiene
    * Fisker
    * Lege
    * Snekker


### Entitet
* Med en entitet mener vi et objekt tilknyttet dets attributter og verdier

### Objekt / Attributt / Verdi / Entitet
![](https://i.imgur.com/hwYS0JC.png)

### Relasjoner (Sammenhenger)
![](https://i.imgur.com/ya90Adw.png)

* Objekter
    * ![](https://i.imgur.com/ELRYSqM.png)
* Entiteter
    * ![](https://i.imgur.com/m3q6Dc9.png)
* En-til-en (1:1)
    * ![](https://i.imgur.com/mcDC0bG.png)
* En-til-mange (1:n)
    * ![](https://i.imgur.com/LSWVPrd.png)
* Mange-til-mange (n:m)
    * ![](https://i.imgur.com/7KJHiLO.png)

### n:m relasjon eksempel
![](https://i.imgur.com/zle1l2z.png)

### Objektering av relasjoner
* En n:m relasjon mellom Firma og Vare gir opphav til et nytt objekt FV
![](https://i.imgur.com/S2kJF4r.png)


### Objektering av relasjoner
![](https://i.imgur.com/65eNTln.png)

### Entiteter - Tabeller
![](https://i.imgur.com/uTjc9jd.png)

1. Grupper sammen objekter til entiteter
2. Overfør entiteten og relasjonene mellom disse til tabeller.

### Entiteter - Tabeller
![](https://i.imgur.com/7boNnNQ.png)


## DB-concurrency
### DB Transaksjoner - ACID
* **A**tomic - Udelbar
    * Transaction cannot be subdivided
* **C**onsistent - fra en konsistent tilstand til annen
    * Contraints don't change from before transaction to after transaction
* **I**solated - Ulike T påvirker ikke hverandre
    * Database changes not revealed to users (other transactions) until after transaction has completed
* **D**urable - Varige Endringer
    * Database changes are permanent

### ACID - Isolation implementation
* Locking of resources in the database
* Conflicting goals
    * Correct results vs. Transaction speed
* Strategy, assure correctness and minimise:
    * The number of resources locked
    * The restriction imposed, e.g. allow read
    * The duration of locks held
...
...
...
FAEN SÅ LEI DATABASER ! 

-----

# Sammendrag Databasesystemer Boka 
* [kopimi.datapor.no/trilambda/DAT202/book/](http://kopimi.datapor.no/trilambda/DAT202/book/)

# Tidligere Eksamensoppgaver
* [kopimi.datapor.no/trilambda/DAT202/exam/](http://kopimi.datapor.no/trilambda/DAT202/exam/)

# Scripting Eksempler
* [kopimi.datapor.no/trilambda/DAT202/mysql/](http://kopimi.datapor.no/trilambda/DAT202/mysql/)

# DATABASE QUIZ
## INTRODUKSJON
Q: Livsløpet til et databasesystem er Forstudie, analyse, ? , implementasjon, ?  og produksjon.
A: Design, Testig

Q: Relasjonsdatabaser har en fordel når det kommer til Utviklings- og velikeholds-kostnader 
A: Utviklings- og velikeholds-kostnader

Q: Hvorfor trenger vi Ascii/unicode? 
A: For å kunne tolke binær data på rett måte

Q: En database-utvikler kan ikke være DBA (Database administrator)? 
A: False

Q: Metadata blir lagret i systemkatalogen (DD)? 
A: True

Q: Hva består en database av? 
A: Databasen, Data Dictionary, DBMS

Q: Parsering, optimalisering og eksekveringsplan er begreper som blir brukt av?
A: DBHS(databasehåndteringssystem)

Q: Hva blir minne(RAM) brukt til i en database? 
A: Data blir lest inn i minne for å utføre spørringer siden det er mye raskere

Q: Hva er en DBHS(databasehåndteringssystem)/DBMS(Databasemanagementsystem)? 
A: Det er DBHS som behandler og utfører SQL

Q: Hva kan man lese ut av system-katalogen (DD)?
A: Navn på tabellen, kolonnen, og hva slags type data som er lagret i hver enkelt kolonne, brukere og hvilke rettigheter disse har

Q: Hva er en transaksjon?
A: Operasjoner som brukere utfører mot en database kalles transaksjoner

Q: Forskjell på data og informasjon?
A: Data er definert som enhver fysisk representasjon av opplysninger, og informasjon er meningsinnholdet

Q: [Svar] har 4 hoved-oppgaver: 
- Akseptere data og instruksjoner fra brukeren
- Gjennfinne informasjon fra databasen
- Oppdatere databasen
- Sikre dataene i databasen
A:
- DBHS
- Databasemanagementsystem
- Databasehåndteringssystem
- DBMS

Q: Hva kan man lese ut av system-katalogen (DD)? 
A: Navn på tabellen, kolonnen, og hva slags type data som er lagret i hver enkelt kolonne, brukere og hvilke rettigheter disse har

Q: Hva avgjør man under databasedesign? 
A: Begrepsmessig, logisk og fysisk design

## Databasedesign

Q: Hva mener vi med en verdi?
A: Verdi er noe som en attributt kan ha (eks. tall, tekst).

Q: Hvis vi har tabellene personer og biler (og antar det ikke finnes medeiere), hvilken type relasjon vil være mest passende for å beskrive relasjonen mellom dem? I den gitte rekkefølgen. 
A: En til mange.

Q: Hva er en attributt?
A: Egenskap knyttet til et objekt.

Q: Hva menes med enitet?
A: Et objekt med tilknyttede attributter og verdier.

Q: Naturlige identifikatorer, løpenummer og entiteter som blir representert ved hjelp av forhold til andre entiteter er eksempler på en 
A: Identifikator

Q: Hva er forskjellen på “assosiativ entitet” og “koblingsentitet” ? 
A: Assosiativ entitet er entiteten som knytter et mange til mange forhold sammen, og koblingsentitet brukes ikke i database sammenheng.

Q: Hvilket forhold har person og bil?
![](https://i.imgur.com/ONNhyQr.png)
A: En bil kan eies av 0 eller 1 person. En person kan eie 0 eller mange biler

Q: Er dette lov?
![](https://i.imgur.com/7S0UzOP.png)
A: True

Q: Anta at man startet med en tabell "Student" og en tabell "Kurs". Disse to tabellene har en mange til mange kobling, og man løser dette ved å lage en hjelpetabell som kobler "Student" og "Kurs" sammen (Bildet under). Hva er rett utsagn?
![](https://i.imgur.com/yA9YP6E.png)
A: Modellen er riktig, noe som gjør at mange studenter og kurs kan ha eksamen.

Q: Hvor mange eksamener kan en student ta?
![](https://i.imgur.com/WPhExKt.png)
A: Må ta 1

Q: Hva er et ER-diagram (Entity Relationship Diagram)? 
A: En grafisk fremstilling av strukturen til en database, men beskrivelse er abstrakt i den forstand at vi ikke tar stilling til hvordan data er representert fysisk.

Q: Hvorfor brukes entitisering? 
A: Når man har et mange til mange forhold som man splitter opp.

Q: Hva pleier å egne seg godt som identifikator(er) i en modell?
A: Alle svarene er riktig

Q: Er dette lov?
A: True

Q: Hvor mange eksamener kan en student ta?
A: Må ta 1

Q: Hva er datamodellering?
A: En metode for å beskrive naturlige sammenhenger i data som skal benyttes i et informasjonssystem.

Q: Hva er forskjellen på “assosiativ entitet” og “koblingsentitet” ?
A: Det er ikke noe forskjell, de betyr det samme.

Q: Eksempler på “Naturlige Identifikatorer” er:
A: Personnummer, skilt nummer, osv.

Q: Naturlige identifikatorer, løpenummer og entiteter som blir representert ved hjelp av forhold til andre entiteter er eksempler på en [svar].
A: Identifikator

Q: Når man utvikler et nytt database system erstatter man ofte papirskjemaer med en digital database. Papirskjemaer er ofte laget på “Hode/linje-mønsteret”. Tenk deg at du skal lage entiteter for vitnemål som er skrevet på papir og bruker “Hode/linje-mønsteret”. Hva ville vært “hode”, og hva ville vært “linje”?
A: Hode: Tittel, Studentnummer, Navn Linje: Kurskode, Semester, Karakter

Q: Hva menes med enitet? 
A: Et objekt med tilknyttede attributter og verdier.

## SQL & MySQL 
Q: Tabellene du ser under er alle tabellene og dataen i databasen.
A: select Navn from Selger where Navn = "Hansen" or Navn = "Nilsen";

Q: Ved bruk av SQL, hvordan kan man finne antallet rader i tabellen “Persons”? 
A: SELECT COUNT(\*) FROM Persons

Q: Hvilket SQL nøkkelord brukes for å sortere resultat-settet? 
A: ORDER BY

Q: Hva vil denne spørringen gi ut? (WHERE Navn LIKE '%er%')
A: Alle navn som har ‘er’ inni seg, uavhengig hvor

Q: Hva vil denne spørringen gi ut? (WHERE Navn LIKE '%a')
A: Alle navn som slutter på ‘a’

Q: Tabellene du ser under er alle tabellene og dataen i databasen.
A: select Selger.Navn, count(Salg.Mg) from Selger, Salg where Selger.SNr = Salg.SNr group by Selger.Navn;

Q: Ved bruk av SQL, hvordan henter man alle kolonnene fra en tabell med navn “Persons”? 
A: SELECT * FROM Persons

Q: Tabellene du ser under er alle tabellene og dataen i databasen.
A: select Selger.Navn, Adr.Sted from Selger, Adr where Selger.PNr = Adr.PNr;

Q: Ved bruk av SQL, hvordan velger man alle radene fra en tabell med navn “Persons” hvor verdien til “LastName” ligger alfabetisk mellom (inklusiv) “Hansen” og “Pettersen”? 
A: SELECT * FROM Persons WHERE LastName BETWEEN 'Hansen' AND 'Pettersen'

Q: Ved bruk av SQL, hvordan velger man alle radene fra en tabell med navn “Persons” hvor verdien til kolonnen “FirstName” starter med en “a”? 
A: SELECT * FROM Persons WHERE FirstName LIKE 'a%'

Q: Tabellene du ser under er alle tabellene og dataen i databasen. 
(Hvilke spørringer kan du gjøre for å få ut dette resultatet?)

| SNr | Navn | PNr |
|-----|------|-----|
|  2  |Olsen | 6400|

A: Alle alternativene vil gi resultatet

Q: Ved bruk av SQL, hvordan velger man alle radene fra en tabell med navn “Persons” hvor verdien til kolonnen “FirstName” er lik “Ola”? 
A: SELECT * FROM Persons WHERE FirstName='Ola’

## Filer, Indekser, Transaksjoner og Databaseadministrasjon
Q: I [Svar] blir data lest inn i minne for å utføre beregninger. 
A:  Harddisk, Magnetbånd, Primærminne

Q: Vi sier at minne er [svar] og ssd(hardisk) er [svar]
A1: Flyktig, Volatile
A2: Ikke flyktig, Ikke-flyktig, Non volatile, Non-volatile

Q: Hva er fordelen med usortert data? 
A: Raskt å sette inn ny data.

Q: Hvilken påstand er rett om SSD? 
A: En SSD er et elektronisk lagrinsmedium basert på flash-teknologi av typen NAND.

Q: Hva er en transaksjonslogg? 
A: En fil på harddisken som inneholder data om alle operasjoner som er utført mot databasen

Q: Kan man bare ved hjelp av transaksjonsloggen gjenoppbygge dataene i databasen ved mediefeil?
A: False

Q: Hva er riktig om to-faselåsing? 
A: En transaksjon kan bare ta nye låser i voksefase og forblir i den helt til den låser opp en lås, da begynner minkefasen hvor den bare kan låse opp låser.

Q: Hvordan kan man forhindre vranglås(deadlock) 
A: Tidsstempler

Q: Hva menes med replikering? 
A: En tabell, eller deler av en tabell, blir lagret på flere noder (flere kopier).

Q: Kommunikasjonen foregår ved at klienten sender en forespørsel til tjeneren. Hvilken systemarkitektur er dette? 
A: Klient/tjener databasesystem

Q: Man kan si at en harddisk er bygget opp av:
A: Man kan si at en harddisk er bygget opp av: 

Q: Hva er ulempen med sortert data? 
A: Tar lang tid å sette inn ny data.

Q: I [svar] sikkerhetskopieres dataen til harddisker, optisk medier og/eller magnetbånd. 
A: Sekundærminne, Primærminne, Tertiærminne

Q: Hvilket lagringsmedie støtter ikke “direkteaksess”? 
A: Magnetbånd

Q: En SSD er organisert i blokker som er telt opp i sider. Hva er riktig om skriving og sletting? 
A: Det er lov å skrive til en side, men bare sletting av blokker.

Q: Vi har en tabell:
![](https://i.imgur.com/BtEUOrf.png)
En INTEGER bruker 4 byte på disken. Hvor mange byte på disken bruker hele tabellen?
A: 70

Q: Hva er en transaksjon? 
A: En transaksjon er en logisk operasjon mot en database og består av en eller fler SQL spørringer.

Q: Når man leser transaksjonsloggen baklengs og erstatter nye verdier med gamle kalles dette:
A: Undo

Q: Hvilke låsetyper brukes i en flerbrukerdatabase? 
A: Leselås og skrivelås.

Q: Hva er et eksempel på “instansfeil”? 
A: Strømbrudd

Q: Hvorfor ønsker man å bruke caching?
A: For å øke hastigheten på hele eller deler av databasen som blir mye etterspurt.

Q: Hva menes med minnedatabaser? 
A: Hele databasen holdes i minne.

Q: Hva er “RAID” systemer, og hvorfor bruker man det? 
A: Et RAID system er en sammenkobling av disker som til sammen danner en logisk disk. Dette brukes for å sikre at data ikke går tapt siden harddisker ikke varer evig.

Q: Hvilken er feil utsagn om indekser? 
A: Indekser trenger ikke være sortert med hensyn til søkenøkkelen.

Q: Hva er ulempen med sortert data? 
A: Tar lang tid å sette inn ny data.

Q: Hvilket lagringsmedie støtter ikke “direkteaksess”? 
A: Magnetbånd

Q: Hva er en transaksjonslogg? 
A: En fil på harddisken som inneholder data om alle operasjoner som er utført mot databasen.

Q: Hva står ACID for? 
A: Atomicity, Consistency, Isolation, Durability

Q: Når man leser forlengs i transaksjonsloggen kan avbrutte transaksjoner gjennomføres på nytt, fra starten av. Her vil gamle verdier overskrives på nytt. Dette kalles:
A: Redo

Q: Hva er et eksempel på “instansfeil”? 
A: Strømbrudd

Q: Brukerne jobber ut ifra enkle terminaler som kan være et tastatur og mus. Hvilken systemarkitektur er dette? 
A: Sentralisert databasesystem

Q: Kommunikasjonen foregår ved at klienten sender en forespørsel til tjeneren. Hvilken systemarkitektur er dette? 
A: Klient/tjener databasesystem

Q: Hvilken påstand er rett om SSD?
A: En SSD er et elektronisk lagrinsmedium basert på flash-teknologi av typen NAND.

Q: Man kan si at en harddisk er bygget opp av: 
A: Skiver, sektorer og blokker.

Q: Hva er aksesstiden til en harddisk? 
A: Tiden det tar å flytte lesearmen, rotasjonstiden og overføringstiden.

Q: Hvis en transaksjon har leselås, hvilke rettigheter har den?
A: Den kan bare lese cellen.

Q: Kan man bare ved hjelp av transaksjonsloggen gjenoppbygge dataene i databasen ved mediefeil? 
A: False

Q: Hva menes med replikering? 
A: En tabell, eller deler av en tabell, blir lagret på flere noder (flere kopier).

Q: Hva skjer under en kald sikkerhetskopiering? 
A: Alle brukerne må logge av systemet før det tas ned for å kjøre en sikkerhetskopiering.
