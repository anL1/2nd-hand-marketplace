# Tietokantakaavio

<img src="https://github.com/anL1/2nd-hand-marketplace/blob/master/documentation/images/tietokantakaavio2.png?raw=true" 
width=250 />

# Create Table -lauseet

```
CREATE TABLE account (
        id INTEGER NOT NULL, 
        date_created DATETIME, 
        date_modified DATETIME, 
        name VARCHAR(144) NOT NULL, 
        username VARCHAR(144) NOT NULL, 
        password VARCHAR(144) NOT NULL, 
        PRIMARY KEY (id)
);
```

```
CREATE TABLE category (
        id INTEGER NOT NULL, 
        date_created DATETIME, 
        date_modified DATETIME, 
        name VARCHAR(144) NOT NULL, 
        PRIMARY KEY (id)
);
```

```
CREATE TABLE product (
        id INTEGER NOT NULL, 
        date_created DATETIME, 
        date_modified DATETIME, 
        name VARCHAR(200) NOT NULL, 
        content VARCHAR(300) NOT NULL, 
        price INTEGER NOT NULL, 
        account_id INTEGER NOT NULL, 
        PRIMARY KEY (id), 
        FOREIGN KEY(account_id) REFERENCES account (id)
);
```

```
CREATE TABLE product_category (
        product_id INTEGER NOT NULL, 
        category_id INTEGER NOT NULL, 
        PRIMARY KEY (product_id, category_id), 
        FOREIGN KEY(product_id) REFERENCES product (id), 
        FOREIGN KEY(category_id) REFERENCES category (id)
);
```

```
CREATE TABLE comment (
        id INTEGER NOT NULL, 
        date_created DATETIME, 
        date_modified DATETIME, 
        content VARCHAR(300) NOT NULL, 
        account_id INTEGER NOT NULL, 
        product_id INTEGER NOT NULL, 
        PRIMARY KEY (id), 
        FOREIGN KEY(account_id) REFERENCES account (id), 
        FOREIGN KEY(product_id) REFERENCES product (id)
);
```
