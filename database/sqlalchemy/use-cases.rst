SQLAlchemy Use Cases
====================


Use Case - 0x01
---------------
* SQLAlchemy to Pandas

.. code-block:: python

    from sqlalchemy import create_engine
    import pandas as pd


    # DATABASE powinen zaczynać się od sqlite:///
    DATABASE = 'sqlite:///myfile.db'

    SQL = """

        SELECT *
        FROM astronauts;

    """

    # %%timeit -r 1 -n 1
    # with create_engine(DATABASE).connect() as db:
    #    df = pd.read_sql(SQL, db)
    # 2.47 ms ± 0 ns per loop (mean ± std. dev. of 1 run, 1 loop each)
    #
    # %%
    # df.info(memory_usage='deep')

    with create_engine(DATABASE).connect() as db:
        df = pd.read_sql(SQL, db)

    print(df)


Use Case - 0x02
---------------
.. code-block:: python

    from datetime import date

    from sqlalchemy import create_engine, select, func
    from sqlalchemy import Column, String, Integer, Date
    from sqlalchemy.orm import sessionmaker, declarative_base



    DATABASE = 'sqlite:///:memory:'
    engine = create_engine(DATABASE, future=True)
    Session = sessionmaker(engine)
    Model = declarative_base()


    class User(Model):
        __tablename__ = 'users'
        uid = Column(Integer, autoincrement=True, primary_key=True)
        firstname = Column(String, nullable=False, index=True)
        lastname = Column(String, nullable=False)
        born = Column(Date, default=date.today)

        def __repr__(self):
            return f'{self.firstname} {self.lastname}'

    with Session.begin() as db:
        Model.metadata.create_all(engine)
        db.add_all([
            User(firstname='Mark', lastname='Watney'),
            User(firstname='Melissa', lastname='Lewis'),
            User(firstname='Rick', lastname='Martinez'),
            User(firstname='Alex', lastname='Vogel'),
            User(firstname='Beth', lastname='Johanssen'),
            User(firstname='Chris', lastname='Beck'),
        ])


    query_select = (
        select(User.firstname,
               User.lastname,
               User.born).

        where((User.born >= date(1969,7,21))
            & (User.born <= date.today())
            & (User.born.between('2022-01-01', '2022-02-23'))
            & (User.firstname != None)
            & (User.lastname.in_(['Watney', 'Lewis', 'Martinez']))
            & (User.firstname.in_(
                select(User.firstname).
                where(User.firstname.startswith('M')).
                distinct()))
            & (User.firstname.like('Mel__%'))).

        order_by(User.firstname.desc().nulls_first(),
                 User.lastname.asc()).

        group_by(User.firstname).
        having(func.count(User.firstname == 1)).
        limit(10).
        offset(5)
    )

    print(query_select.compile(engine, compile_kwargs={"literal_binds": True}))
    # SELECT users.firstname,
    #        users.lastname,
    #        users.born
    # FROM users
    # WHERE users.born >= '1969-07-21'
    #   AND users.born <= '2022-02-22'
    #   AND users.born BETWEEN '2022-01-01' AND '2022-02-23'
    #   AND users.firstname IS NOT NULL
    #   AND users.lastname IN ('Watney', 'Lewis', 'Martinez')
    #   AND users.firstname IN (
    #       SELECT DISTINCT users.firstname
    #       FROM users
    #       WHERE (users.firstname LIKE 'M' || '%'))
    #   AND users.firstname LIKE 'Mel__%'
    # GROUP BY users.firstname
    # HAVING count(users.firstname = 1)
    # ORDER BY users.firstname DESC NULLS FIRST,
    #          users.lastname ASC
    # LIMIT 10
    # OFFSET 5


    with Session.begin() as db:
        result = db.execute(query_select)
        for row in result.all():
            print(row)

    # (1, 'Mark', 'Watney')
    # (2, 'Melissa', 'Lewis')
    # (3, 'Rick', 'Martinez')
    # (4, 'Alex', 'Vogel')
    # (5, 'Beth', 'Johanssen')
    # (6, 'Chris', 'Beck')
