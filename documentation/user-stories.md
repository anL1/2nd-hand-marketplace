# User Storyt

## Toteutetut
* Käyttäjä voi rekisteröityä järjestelmään. Jokaisella käyttäjällä tulee olla uniikki käyttäjänimi.
* Käyttäjä voi muokata tietojaan (nimi, salasana) käyttäjäsivun kautta. Käyttäjänimi on pysyvä.
* Käyttäjä voi luoda uuden ilmoituksen myynnissä olevasta tuotteestaan
   * Ilmoitukselle voi asettaa otsikon, kuvauksen ja hinnan
   * Ilmoituksen voi asettaa yhteen tai useampaan kategoriaan
* Käyttäjä voi muokata luomaansa ilmoitusta tai poistaa sen
* Käyttäjät voivat tarkastella palvelussa olevia ilmoituksia (ei vaadi kirjautumista)
  * Ilmoituksia voi tarkastella kategorioittain
  * Rekisteröitynyt käyttäjä voi lisätä sovellukseen uuden kategorian
* Rekisteröitynyt käyttäjä voi jättää myynti-ilmoitukseen kommentin
* Käyttäjät näkevät ilmoitukseen jätetyt kommentit ilmoituksen sivulla
* Käyttäjä voi poistaa omia kommenttejaan

## Jatkokehitysideoita / ominaisuudet joita ei ehtinyt toteuttamaan
* Ilmoituksia voi tarkastella luomispäivämäärän mukaan
* Käyttäjä voi muokata kommenttiaan
* Käyttäjän voi poistaa
* Kategorian voi poistaa (esim. Admin-rooli voisi olla hyvä tähän). 

## Käyttötapauksiin liittyvät tietokantakyselyt
* Käyttäjä voi rekisteröityä järjestelmään. Jokaisella käyttäjällä tulee olla uniikki käyttäjänimi.
```
INSERT INTO Account (name, username, password) VALUES ('name', 'username', 'pw_hash');
```
* Käyttäjä voi luoda uuden ilmoituksen myynnissä olevasta tuotteestaan
```
INSERT INTO Product (name, content, price) VALUES ('name', 'product description here', 123);
```
* Jos tuote lisätään yhteen tai useampaan kategoriaan niin myös seuraava kysely suoritetaan
```
INSERT INTO Product_Category (product_id, category_id) VALUES (product_id, category_id);
```
* Käyttäjä voi muokata luomaansa ilmoitusta
```
UPDATE Product SET content = 'updated content', name = 'updated name', price = updated price WHERE id = product_id;
```
* Käyttäjä voi poistaa ilmoituksen
```
DELETE FROM Product WHERE id = product_id;
```
* Käyttäjät voivat tarkastella palvelussa olevia ilmoituksia
```
SELECT * FROM Product;
```
* Ilmoituksia voi tarkastella kategorioittain
```
"SELECT product.id, product.name FROM Product_category, Product WHERE product_category.category_id = category_id
AND product_category.product_id = product.id GROUP BY product.id
```
* Rekisteröitynyt käyttäjä voi lisätä sovellukseen uuden kategorian
```
INSERT INTO Category (name) VALUES ('category_name');
```
* Rekisteröitynyt käyttäjä voi jättää myynti-ilmoitukseen kommentin
```
INSERT INTO Comment (content, account_id, product_id) VALUES ('comment content', account_id, product_id);
```
* Käyttäjät näkevät ilmoitukseen jätetyt kommentit (sisältö ja kommentin jättänyt käyttäjä) ilmoituksen sivulla
```
SELECT account.id, account.username, comment.content, comment.id FROM Account, Comment WHERE product_id = ?
AND account_id=account.id
```
* Käyttäjä voi poistaa omia kommenttejaan
```
DELETE FROM Comment WHERE id = ? AND account_id = ?;
```
