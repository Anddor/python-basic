# Datatyper og Variabler

## Datatyper

Alt vi arbeider med i Python og andre programmeringsspråk har en "type".

For eksempel er noe en streng hvis vi skriver det med `"`:
```python
"hei"
```
(Vi kaller det en streng fordi det er en "streng" av bokstaver.)
git@github.com:Anddor/python-basic.gitgit@github.com:Anddor/python-basic.git
Hvis vi skriver et heltall rett frem er det et bare et heltall, kalt en `Integer` eller `int`:
```python
1
```
En tredje viktig datatype sier om noe er sant eller usant, det heter `Boolean` eller `bool`. Merk at teksten under får en egen farge fordi den har spesiell betydning.
```python
True
False
ikke_en_bool
```


Hvilken datatype noe har tilsier hva vi kan gjøre med en verdi. For eksempel vil Python fungere som en kalkulator hvis du bruker pluss `+`, minus `-`, gange `*`, eller dele `/`, med tall:
```python
>>> 1 + 1
2
```
Men gjøre noe annet om du plusser sammen tekst:
```python
>>> "1" + "1"
'11'
```
Noen operasjoner gir mening:
```python
>>> "1" * 4
'1111'
```
Mens noen gjør ikke det:
```
>>> "1" * "4"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'str'
```
Her forteller python oss at programmet har en type-feil, altså en `TypeError`. Vi kan ikke gange med noe som er "non-int", altså et ikke-heltall.

Hvis du er usikker på hvilken type noe er kan du bruke funksjonen type():
```
>>> type("1")
<class 'str'>
```
```
>>> type(1)
<class 'int'>
```
```
>>> type(1.4)
<class 'float'>
```
```
>>> type(True)
<class 'bool'>
```

Prøv deg frem med ulike datatyper i Python med en interaktiv sesjon. Hva skjer hvis du ganger `*` en `string` med en `bool`? Hva skjer hvis du tar en streng minus en streng? Hva er den rareste operasjonen som du får til?

## Variabler

Ofte trenger vi resultatet av en operasjon til senere, da lagrer vi det i en variabel. Vi lagrer en verdi i Python ved å skrive en "navnelapp" og verdien den skal inneholde med `=` mellom:

```python
navn = "Andreas"
```
Vi bruker `=`, men det kan være bedre å tenke på det som et eget "putt inn i"-tegn (ofte kalt "assignment operator"). Det er _ikke_ det samme som `=` i matematikken. For eksempel kan vi bruke variabelen til å sette ny verdi på seg selv:
```python
navn = navn + " Dørum"
```

Merk at til forskjell fra JavaScript og en del andre programmeringsspråk må vi ikke bruke et spesielt ord for å opprette en ny variabel. Sånn ville det sett ut i js: 
```javascript
let navn = "Andreas"
navn = navn + " Dørum"
```

Variablen kan nå brukes akkurat som om vi skrev verdien, og den har naturlig nok samme datatype:
```
>>> type(navn)
<class 'str'>
```

## Oppgaver

Gjør de tre oppgavene i denne mappen som handler om variabler og datatyper. Når du er ferdig kan du jobbe videre med codewars: TODO: lenke til collection 