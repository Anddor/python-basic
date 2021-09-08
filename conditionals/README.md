# Betingelser (If og sånt)

Programmene våre kan ikke få til så mye hvis det samme skjer hver gang. Derfor bruker vi "conditionals", eller betingelser, for å styre hva som skal skje i ulike tilfeller.

Vi kan skrive dette som en `if`. Som navnet antyder betyr dette bare "hvis noe er sant". Så i Python kan vi si:

```python
if True:
    print("Dette er alltid sant!")
```

`if` aktiverer altså koden inne i blokken om verdien etterpå er Boolean-verdien `True`. Det er med andre ord helt likt å skrive:
```python
sant = True

if sant:
    print("Dette er alltid sant!")
```


Ofte vil vi gjøre enten én ting eller en annen, da bruker vi `if` og `else`, altså hvis-ellers.

```python
sulten = True

if sulten:
    print("Spis mat!")
else:
    print("ikke spis mat!")
```

På samme måte som vi kan plusse sammen med tall, har vi noen egne operasjoner vi kan gjøre med datatypen `Boolean`. Vi sjekke om både en ting og en annen er sant med `and`:
```python
>>> True and True
True
>>> True and False
False
```
Og vi sjekker om den ene ting eller den andre er sant med `or`:
```python
>>> True or False
True
>>> False or False
False
```

Noen operasjoner vi gjør med tall som `int` og `decimal`, gir en bool som resultat. Gjerne de som sammenligner to tall. `>` tegnet sjekker om det til venstre er større enn det til høyre (husk at krokodillemunnen vil spise det største tallet):

```python
>>> 5 > 6
False
```

Vi kan sjekke sjekke om en person er gamle nok til å ta lappen med `>=`, "større eller lik"-tegnet:

```python
if alder >= 18:
    print("Du kan ta lappen!")
else:
    print("Du er for ung for lappen.")
```

(Hvorfor ville det blitt feil å bruke `>` ?)

Hvis vi vil legge til støtte for moped også kan vi sjekke flere ting etter hverandre med `elif` som er kort for "else if", altså ellers hvis. Vi sjekker kun alternativ nummer 2 om alternativ nummer 1 ikke er sant.

```python
if alder >= 18: 
    print("Du kan ta lappen for bil og moped")
elif alder >= 16:
    print("Du kan ta bare ta lappen for moped")
else:
    print("Du kan i det minste sykle")
```
