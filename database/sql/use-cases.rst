SQL Use Cases
=============


Use Case - 0x01
---------------
.. code-block:: sql

    SELECT category,
           COUNT(category) AS count

    FROM apollo11

    GROUP BY category
    HAVING count > 50

    ORDER BY category DESC
             NULLS FIRST

    LIMIT 0, 5;



Use Case - 0x02
---------------
.. code-block:: sql

    SELECT *
    FROM logs
    WHERE level in (

        SELECT level
        FROM logs
        GROUP BY level
        HAVING COUNT(*) > 5

    );


Use Case - 0x03
---------------
.. code-block:: sql

    SELECT id,
           firstname AS fname,
           lastname AS lname

    FROM astronauts

    WHERE lastname == 'Watney' AND firstname == 'Mark'
       OR lastname == 'Lewis' AND firstname == 'Melissa'
       OR born BETWEEN '1990-01-01' AND '2000-01-01'
       OR lastname IN ('Martinez', 'Vogel')
       OR lastname IN (
          SELECT lastname
          FROM astronauts
          WHERE lastname LIKE 'Wat%'
       )

    ORDER BY lastname DESC,
             firstname ASC
             NULLS FIRST

    LIMIT 0, 3;


Use Case - 0x04
---------------
.. code-block:: sql

    SELECT
        message,
        level,
        COUNT(level) AS count
    FROM logs
    WHERE (datetime <= '1969-07-18' OR datetime >= '1969-07-20')
      AND message LIKE 'Max__%'
      AND level IN (SELECT DISTINCT(level) FROM logs)
    GROUP BY level
    HAVING count > 5
    ORDER BY datetime DESC
    LIMIT 5;


Use Case - 0x05
---------------
.. code-block:: sql

    WITH important_categories AS (
          SELECT DISTINCT(category)
          FROM apollo11
          GROUP BY category
          HAVING COUNT(category) < 50
          ORDER BY category ASC
          LIMIT 5
          OFFSET 0)

    SELECT datetime AS dt,
           category AS lvl,
           event
    FROM apollo11
    WHERE category != 'DEBUG'
      AND date >= '1969-07-16'
      AND date <= '1969-07-24'
      AND (date = '1969-07-20' OR date = '1969-07-21')
      AND datetime BETWEEN '1969-07-20 20:17:41' AND '1969-07-21 15:00'
      AND event LIKE '%CDR%'
      AND category IS NOT NULL
      AND category NOT IN ('DEBUG', 'INFO')
      AND category IN ('CRITICAL', 'ERROR')
      AND category IN (
          SELECT DISTINCT(category)
          FROM apollo11
          GROUP BY category
          HAVING COUNT(category) < 50
          ORDER BY category ASC
          LIMIT 5
          OFFSET 0)
      AND category IN important_categories
    ORDER BY category DESC,
             date ASC NULLS FIRST,
             time ASC NULLS LAST
    LIMIT 30
    OFFSET 0


Use Case - 0x06
---------------
.. code-block:: sql

    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        firstname TEXT,
        lastname TEXT,
        gender TEXT,
        birthday DATE,
        ssn TEXT,
        email TEXT,
        phone TEXT
    );

    CREATE INDEX IF NOT EXISTS idx_users_lastname_firstname
    ON users (lastname, firstname);

    INSERT INTO users (id, firstname, lastname, gender, birthday, ssn, email, phone)
    VALUES
        (1, 'Mark',     'Watney',    'male' ,  '1994-10-12', '94101212345', '+1 (234) 555-0000',  'mwatney@nasa.gov'),
        (2, 'Melissa',  'Lewis',     'female', '1995-07-15', '95071512345', '+1 (234) 555-0001',  'mlewis@nasa.gov'),
        (3, 'Rick',     'Martinez',  'male',   '1996-01-21', '96012112345', '+1 (234) 555-0010',  'rmartinez@nasa.gov'),
        (4, 'Alex',     'Vogel',     'male',   '1994-11-15', '94111512345', '+49 (234) 555-0011', 'avogel@esa.int'),
        (5, 'Beth',     'Johanssen', 'female', '2006-05-09', '06250912345', '+1 (234) 555-0100',  'bjohanssen@nasa.gov'),
        (6, 'Chris',    'Beck',      'male',   '1999-08-02', '99080212345', '+1 (234) 555-0101',  'cbeck@nasa.gov');

.. code-block:: sql

    CREATE TABLE IF NOT EXISTS addresses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        type TEXT,
        street TEXT,
        city TEXT,
        postcode TEXT,
        region TEXT,
        country TEXT
    );

    CREATE INDEX IF NOT EXISTS idx_addresses_country
    ON addresses (country);

    INSERT INTO addresses (id, user_id, type, street, city, postcode, region, country)
    VALUES
        (1, 1, 'billing',  '2101 E NASA Pkwy',                    'Houston',           77058,    'Texas',                  'USA'),
        (2, 1, 'shipment', 'Kennedy Space Center',                'Merritt Island',    32899,    'Florida',                'USA'),
        (3, 2, 'shipment', 'Kamienica Pod św. Janem Kapistranem', 'Cracow',            31008,    'Malopolskie',            'Poland'),
        (4, 3, 'billing',  'Chkalovskoye Shosse',                 'Zvyozdny Gorodok',  141160,   'Moscow Oblast',          'Russia'),
        (5, 3, 'shipment', 'Baikonur Cosmodrome',                 'Baikonur',          468320,   'Kyzylorda Oblast',       'Kazakhstan'),
        (6, 4, 'shipment', 'Linder Hoehe',                        'Cologne',           51147,    'North Rhine-Westphalia', 'Germany'),
        (7, 5, 'shipment', '2825 E Ave P',                        'Palmdale',          93550,    'California',             'USA'),
        (8, 6, 'shipment', '4800 Oak Grove Dr',                   'Pasadena',          91109,    'California',             'USA');

.. code-block:: sql

    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ean13 TEXT,
        name TEXT,
        price REAL
    );

    CREATE INDEX IF NOT EXISTS idx_product_ean13
    ON products (ean13);

    CREATE INDEX IF NOT EXISTS idx_product_name
    ON products (name);

    INSERT INTO products (id, ean13, name, price)
    VALUES
        (1, 5039271113244, 'Alfa',     123.00),
        (2, 5202038482222, 'Bravo',    312.22),
        (3, 5308443764554, 'Charlie',  812.00),
        (4, 5439667086587, 'Delta',    332.18),
        (5, 5527865721147, 'Echo',     114.00),
        (6, 5535686226512, 'Foxtrot',  99.12),
        (7, 5721668602638, 'Golf',     123.00),
        (8, 5776136485596, 'Hotel',    444.40),
        (9, 5863969679442, 'India',    674.21),
        (10, 5908105406923, 'Juliet',   324.00),
        (11, 5957751061635, 'Kilo',     932.20),
        (12, 6190780033092, 'Lima',     128.00),
        (13, 6512625994397, 'Mike',     91.00),
        (14, 6518235371269, 'November', 12.00),
        (15, 6565923118590, 'Oscar',    43.10),
        (16, 6650630136545, 'Papa',     112.00),
        (17, 6692669560199, 'Quebec',   997.10),
        (18, 6711341590108, 'Romeo',    1337.00),
        (19, 6816011714454, 'Sierra',   998.10),
        (20, 7050114819954, 'Tango',    123.00),
        (21, 7251625012784, 'Uniform',  564.99),
        (22, 7251925199277, 'Victor',   990.50),
        (23, 7283004100423, 'Whisky',   881.89),
        (24, 7309682004683, 'X-Ray',    123.63),
        (25, 7324670042560, 'Zulu',     311.00);

.. code-block:: sql

    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date DATE,
        user_id INTEGER,
        product_id INTEGER
    );

    CREATE INDEX IF NOT EXISTS idx_orders_user
    ON orders (user_id);

    INSERT INTO orders (date, user_id, product_id)
    VALUES
        ('2000-01-01', 1, 19),
        ('2000-01-02', 1, 22),
        ('2000-01-03', 5, 4),
        ('2000-01-04', 2, 14),
        ('2000-01-05', 3, 13),
        ('2000-01-01', 1, 2),
        ('2000-01-02', 1, 11),
        ('2000-01-03', 4, 22),
        ('2000-01-04', 5, 18),
        ('2000-01-05', 5, 23),
        ('2000-01-01', 6, 25),
        ('2000-01-02', 1, 18),
        ('2000-01-03', 4, 18),
        ('2000-01-04', 5, 22),
        ('2000-01-05', 5, 23),
        ('2000-02-01', 2, 23),
        ('2000-02-02', 3, 13),
        ('2000-02-03', 1, 14),
        ('2000-02-04', 1, 11),
        ('2000-02-05', 4, 2),
        ('2000-02-01', 5, 24),
        ('2000-02-02', 4, 18),
        ('2000-02-03', 5, 22),
        ('2000-02-04', 5, 9),
        ('2000-02-05', 2, 10),
        ('2000-03-01', 3, 6),
        ('2000-03-02', 4, 22),
        ('2000-03-03', 5, 18),
        ('2000-03-04', 5, 23),
        ('2000-03-05', 6, 25),
        ('2000-03-01', 1, 1),
        ('2000-03-02', 4, 18),
        ('2000-03-03', 5, 17);

.. code-block:: sql

    SELECT *
    FROM users
    INNER JOIN addresses
    ON addresses.user_id == users.id;

.. code-block:: sql

    SELECT
        users.id AS user_id,
        users.firstname AS user_firstname,
        users.lastname AS user_lastname,
        addresses.street AS address_street,
        addresses.city AS address_city,
        addresses.postcode AS address_postcode,
        addresses.region AS address_region,
        addresses.country AS address_country
    FROM users
    INNER JOIN addresses
    ON users.id == addresses.user_id;

.. code-block:: sql

    SELECT
        users.id AS user_id,
        users.firstname AS user_firstname,
        users.lastname AS user_lastname,
        orders.date AS order_date,
        orders.id AS order_id,
        orders.product_id AS product_id
    FROM users
    JOIN orders ON users.id == orders.user_id;

.. code-block:: sql

    SELECT
        users.id AS user_id,
        users.firstname AS user_firstname,
        users.lastname AS user_lastname,
        orders.date AS order_date,
        orders.id AS order_id,
        orders.product_id AS product_id,
        products.ean13 AS product_ean13,
        products.name AS product_name,
        products.price AS product_price
    FROM users
    JOIN orders ON orders.user_id == users.id
    JOIN products ON orders.product_id == products.id;

.. code-block:: sql

    SELECT
        users.id AS user_id,
        users.firstname AS user_firstname,
        users.lastname AS user_lastname,
        orders.date AS order_date,
        orders.id AS order_id,
        SUM(products.price) AS order_total
    FROM users
    JOIN orders ON orders.user_id == users.id
    JOIN products ON orders.product_id == products.id
    GROUP BY user_id;

.. code-block:: sql

    SELECT
        users.id AS user_id,
        users.firstname AS user_firstname,
        users.lastname AS user_lastname,
        orders.date AS order_date,
        orders.id AS order_id,
        SUM(products.price) AS order_total
    FROM users
    JOIN orders ON orders.user_id == users.id
    JOIN products ON orders.product_id == products.id
    GROUP BY user_id
    HAVING order_total >= 2000;
