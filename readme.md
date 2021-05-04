# Farkasnak dokumentáció
Először is.. felkapcsolódsz a robotra. Azt majd elmondom hogy kell.
Aztán, beírod a robot SSH-jára hogy `farkas`. Ez sem túl nehéz.
Na most jön a nehéz rész: programozni.

## Programozás
6 dolgot kell tudnod:
- elore
- hatra
- jobbra
- balra
- modulok
- egyszerre

Ez a 6 függvény létezik, ezeket fogom most itt elmagyarázni.

## Előre

```py
def elore(rots=1, speed=50, adj=2, absWay=None, end=None)
```
Alapból két dolgot adsz meg neki: mennyiséget és sebességet. Például: a `elore(2, 80)` 2 fordulatot megy majd előre, 80as sebességgel. ha ezt írod be: `elore(2, 80, end=True)` akkor a végén meg fog állni.

## Hátra

```py
def hatra(rots=1, speed=50, adj=2, absWay=None, end=None)
```
Alapból két dolgot adsz meg neki: mennyiséget és sebességet. Például: a `hatra(2, 80)` 2 fordulatot megy majd hátra, 80as sebességgel. ha ezt írod be: `hatra(2, 80, end=True)` akkor a végén meg fog állni.

## Jobbra

```py
def jobbra(self, deg=-90, speed=10, prec=1, log=True)
```
Ennek is két dolgot adsz meg: mennyiséget és sebességet. Először a mennyiség (hogy hova akarod hogy elforduljon, abszolút érték a robot elindulásához képest, nem relatív), és hogy milyen sebességet (mennyivel menjen mind a két motor ellentétes irányba). Ha megadod a `prec` értéket is, akkor tudod állítani, hogy mennyire legyen pontos (de ne add meg légyszi).

# Balra

```py
def balra(self, deg=-90, speed=10, prec=1, log=True)
```
Ennek is két dolgot adsz meg: mennyiséget és sebességet. Először a mennyiség (hogy hova akarod hogy elforduljon, abszolút érték a robot elindulásához képest, nem relatív), és hogy milyen sebességet (mennyivel menjen mind a két motor ellentétes irányba). Ha megadod a `prec` értéket is, akkor tudod állítani, hogy mennyire legyen pontos (de ne add meg légyszi).

# Modulok és az egyszerre

```py
def modulok(self, lAmount, lSpeed, rAmount, rSpeed)
def egyszerre(self, speed, amount)
```
Kezdjük a modulokkal. Ezt például így használod: `modulok(1, 20, 2, 30)`. Ennek 4 számot adsz meg, az első hgy mennyit menjen a bal oldali motor (másodpercben), a második hogy milyen sebességgel, a harmadik a jobb motor mennyit menése (szintén másodpercben), a negyedik pedig ennek a sebessége. 

Ha azt szeretnéd, hogy fel emeljen valamit a modul (vagy le), akkor használd az egyszerre függvényt. Ezt így használod: `egyszerre(10, 1)`. Ez tizes sebességgel fogja levinni a modulokat. Az első érték a sebesség, második a mennyiség.

# fullStop
Ez a legegyszerűbb, `fullStop()` egyhelyben megállítja majd a robotot. Ha ezt írod inkább: `fullStop(False)`, akkor a robot még egy kicsit menni fog utána (mert nem lefixeli, csak leveszi a sebességet, ergó momentum). Nem bonyolult.

# Hogy írsz kódokat? 
Látod bal oldalt a fájlokat? Neked azok kellenek, amik run-al kezdődnek. (run1.py, run2.py, ilyenek). A nevei hogy hányadik futásról van szó. Ezek a fájlok így néznek ki: 
```python
from easy import myRobot

def run1def(b: myRobot):
  # b.elore()
  # b.hatra()
  # b.jobbra()
  # b.balra()
  b.modulok(1, -50, 0.5, -100)
  b.egyszerre(20, 5)
  b.egyszerre(-20, 5)
  b.fullStop(False)
  pass

if __name__ == '__main__':
  b = myRobot("outB", "outC", "outD", "in4", None, "in3", None, 1, moduleSensor="in4", modulePort2="outA")
  run1def(b)
```

Neked az a rész kell, ami a run1def után van. Ide írod majd be, hogy minek kell történnie ebben a futásban. A többit ignorálhatod.  Ja, és 