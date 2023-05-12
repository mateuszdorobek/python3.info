OOP Class Factory
=================


Class Definition
----------------
>>> class MyClass:
...     pass

>>> MyClass = type('MyClass', (), {})


Static Attributes
-----------------
>>> class MyClass:
...     myattr = 1

>>> MyClass = type('MyClass', (), {'myattr': 1})


Static Methods
--------------
>>> class MyClass:
...     def mymethod():  # noqa
...         pass

>>> def mymethod():
...     pass
>>>
>>> MyClass = type('MyClass', (), {'mymethod': mymethod})


Dynamic Methods
---------------
>>> class MyClass:
...     def mymethod(self):
...         pass

>>> def mymethod(self):
...     pass
>>>
>>> MyClass = type('MyClass', (), {'mymethod': mymethod})


Init Method
-----------
>>> class User:
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
...
...     def hello(self):
...         print('hello')
...

>>> def __init__(self, firstname, lastname):
...     self.firstname = firstname
...     self.lastname = lastname
>>>
>>> def hello(self):
...     print('hello')
>>>
>>> User = type('User', (), {
...     'hello': hello,
...     '__init__': __init__,
... })


Class Inheritance
-----------------
>>> class Parent:
...     pass
>>>
>>>
>>> class MyClass(Parent):
...     pass

>>> MyClass = type('MyClass', (Parent,), {})


Recap
-----
>>> class Parent:
...     pass
>>>
>>>
>>> class MyClass(Parent):
...     myattr = 1
...
...     def mymethod(self):
...         pass

>>> MyClass = type('MyClass', (Parent,), {'myattr': 1, 'mymethod': mymethod})


What is a class?
----------------
>>> def hello_static():
...     print('hello')
>>>
>>> def hello_dynamic(self):
...     print('hello')
>>>
>>> def myinit(self):
...     ...
>>>
>>> def mystr(self):
...     ...
>>>
>>> User = type('User', (), {
...     '__init__': myinit,
...     '__str__': mystr,
...     '__repr__': mystr,
...     'firstname': 'Mark',
...     'lastname': 'Watney',
...     'hello_static': hello_static,
...     'hello_dynamic': hello_dynamic,
... })

>>> hex(id(hello_static))  # doctest: +SKIP
0x1064e3910
>>>
>>> hex(id(hello_dynamic))  # doctest: +SKIP
0x106082830
>>>
>>> hex(id(myinit))  # doctest: +SKIP
0x103fb4540
>>>
>>> hex(id(mystr))  # doctest: +SKIP
0x1064e2e60
>>>
>>> hex(id('Mark'))  # doctest: +SKIP
0x1062527f0
>>>
>>> hex(id('Watney'))  # doctest: +SKIP
0x1063502b0

>>> # doctest: +SKIP
... User = {
...     '__init__': 0x103fb4540,
...     '__str__': 0x1064e2e60,
...     '__repr__': 0x1064e2e60,
...     'firstname': 0x1062527f0,
...     'lastname': 0x1063502b0,
...     'hello_static': 0x1064e3910,
...     'hello_dynamic': 0x106082830,
... }

Mind, how similar this is to C language struct:

>>> class User:
...     firstname: str
...     lastname: str
>>>
>>>
>>> mark = User()
>>>
>>> mark.firstname = 'Mark'
>>> mark.lastname = 'Watney'
>>>
>>> print(mark.firstname)
Mark
>>> print(mark.lastname)
Watney

.. code-block:: c

    struct User {
      char firstname[30];
      char lastname[30];
    };

    mark = (struct User*) malloc(sizeof(struct User));

    mark->firstname = "Mark";
    mark->lastname = "Watney";

    printf(mark->firstname);
    printf(mark->lastname);


Dynamic Class Creation
----------------------
>>> Admin()
Traceback (most recent call last):
NameError: name 'Admin' is not defined
>>>
>>>
>>> for classname in ['Guest', 'User', 'Admin']:
...     globals()[classname] = type(classname, (), {})
>>>
>>>
>>> Admin
<class '__main__.Admin'>
>>> Admin()  # doctest: +ELLIPSIS
<__main__.Admin object at 0x...>


Use Case - 0x01
---------------
* Init

>>> User = type('User', (), {
...     'firstname': 'Mark',
...     'lastname': 'Watney',
...     'hello': lambda: print('hello')})
>>>
>>> User.hello()
hello
>>>
>>> vars(User)  # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
mappingproxy({'firstname': 'Mark',
              'lastname': 'Watney',
              'hello': <function <lambda> at 0x...>,
              '__module__': '__main__',
              '__dict__': <attribute '__dict__' of 'User' objects>,
              '__weakref__': <attribute '__weakref__' of 'User' objects>,
              '__doc__': None})


Use Case - 0x02
---------------
* Dynamic Classes 1

>>> DATA = [
...     ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
...     (5.8, 2.7, 5.1, 1.9, 'virginica'),
...     (5.1, 3.5, 1.4, 0.2, 'setosa'),
...     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
...     (6.3, 2.9, 5.6, 1.8, 'virginica'),
...     (6.4, 3.2, 4.5, 1.5, 'versicolor'),
...     (4.7, 3.2, 1.3, 0.2, 'setosa'),
...     (7.0, 3.2, 4.7, 1.4, 'versicolor'),
...     (7.6, 3.0, 6.6, 2.1, 'virginica')]
>>>
>>>
>>> class Iris:
...     def __init__(self, **kwargs):
...         self.__dict__ = kwargs
...
...     def __repr__(self):
...         clsname = self.__class__.__name__
...         values = tuple(vars(self).values())
...         return f'{clsname}{values}'
>>>
>>>
>>> header, *rows = DATA
>>> header = [x.lower().replace(' ', '_') for x in header]
>>>
>>> result = []
>>>
>>> for *features,species in rows:
...     features = dict(zip(header, features))
...     clsname = species.capitalize()
...     if clsname not in globals():
...         globals()[clsname] = type(clsname, (Iris,), {})
...     cls = globals()[clsname]
...     iris = cls(**features)
...     result.append(iris)
>>>
>>> result  # doctest: +NORMALIZE_WHITESPACE
[Virginica(5.8, 2.7, 5.1, 1.9),
 Setosa(5.1, 3.5, 1.4, 0.2),
 Versicolor(5.7, 2.8, 4.1, 1.3),
 Virginica(6.3, 2.9, 5.6, 1.8),
 Versicolor(6.4, 3.2, 4.5, 1.5),
 Setosa(4.7, 3.2, 1.3, 0.2),
 Versicolor(7.0, 3.2, 4.7, 1.4),
 Virginica(7.6, 3.0, 6.6, 2.1)]
>>>
>>> vars(result[0])  # doctest: +NORMALIZE_WHITESPACE
{'sepal_length': 5.8,
 'sepal_width': 2.7,
 'petal_length': 5.1,
 'petal_width': 1.9}


Use Case - 0x03
---------------
* Dynamic Classes 2

>>> from dataclasses import dataclass
>>> from itertools import zip_longest
>>>
>>>
>>> DATA = [
...     ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
...     (5.8, 2.7, 'virginica'),
...     (5.1, 3.5, 1.4, 0.2, 'setosa'),
...     (5.7, 'versicolor'),
...     (6.3, 2.9, 5.6, 1.8, 'virginica'),
...     (6.4, 3.2, 4.5, 1.5, 'versicolor'),
...     (4.7, 3.2, 1.3, 'setosa'),
...     (7.0, 3.2, 4.7, 1.4, 'versicolor'),
...     (7.6, 3.0,  'virginica')]
>>>
>>>
>>> @dataclass(init=False)
... class Iris:
...     def __init__(self, **kwargs):
...         self.__dict__ = kwargs
>>>
>>>
>>> result = []
>>> header, *rows = DATA
>>> header = [x.lower().replace(' ', '_') for x in header]
>>>
>>> for *features,species in rows:
...     features = dict(zip_longest(header, features, fillvalue=None))
...     clsname = species.capitalize()
...     if clsname not in globals():
...         globals()[clsname] = type(clsname, (Iris,), {})
...     cls = globals()[clsname]
...     iris = cls(**features)
...     result.append(iris)
>>>
>>> result  # doctest: +NORMALIZE_WHITESPACE
[Virginica(5.8, 2.7, None, None, None),
 Setosa(5.1, 3.5, 1.4, 0.2, None),
 Versicolor(5.7, None, None, None, None),
 Virginica(6.3, 2.9, 5.6, 1.8, None),
 Versicolor(6.4, 3.2, 4.5, 1.5, None),
 Setosa(4.7, 3.2, 1.3, None, None),
 Versicolor(7.0, 3.2, 4.7, 1.4, None),
 Virginica(7.6, 3.0, None, None, None)]
>>>
>>> vars(result[0])  # doctest: +NORMALIZE_WHITESPACE
{'sepal_length': 5.8,
 'sepal_width': 2.7,
 'petal_length': None,
 'petal_width': None,
 'species': None}


Use Case - 0x03
---------------
* Factory

>>> DATA = [
...     ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
...     (5.8, 2.7, 5.1, 1.9, 'virginica'),
...     (5.1, 3.5, 1.4, 0.2, 'setosa'),
...     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
...     (6.3, 2.9, 5.6, 1.8, 'virginica'),
...     (6.4, 3.2, 4.5, 1.5, 'versicolor'),
...     (4.7, 3.2, 1.3, 0.2, 'setosa')]
>>>
>>>
>>> class Iris:
...     def __init__(self, sepal_length, sepal_width, petal_length, petal_width):
...         self.sepal_length = sepal_length
...         self.sepal_width = sepal_width
...         self.petal_length = petal_length
...         self.petal_width = petal_width
...
...     def __repr__(self):
...         name = self.__class__.__name__
...         values = tuple(self.__dict__.values())
...         return f'{name}{values}'
>>>
>>>
>>> class Setosa(Iris):
...     pass
>>>
>>> class Virginica(Iris):
...     pass
>>>
>>> class Versicolor(Iris):
...     pass
>>>
>>>
>>> def factory(species: str):
...     if species == 'setosa':
...         return Setosa
...     if species == 'virginica':
...         return Virginica
...     if species == 'versicolor':
...         return Versicolor
>>>
>>>
>>> result = []
>>>
>>> for *features, species in DATA[1:]:
...     iris = factory(species)
...     i = iris(*features)
...     result.append(i)
>>>
>>> result  # doctest: +NORMALIZE_WHITESPACE
[Virginica(5.8, 2.7, 5.1, 1.9),
 Setosa(5.1, 3.5, 1.4, 0.2),
 Versicolor(5.7, 2.8, 4.1, 1.3),
 Virginica(6.3, 2.9, 5.6, 1.8),
 Versicolor(6.4, 3.2, 4.5, 1.5),
 Setosa(4.7, 3.2, 1.3, 0.2)]


Use Case - 0x04
---------------
* Object factory

>>> from dataclasses import dataclass
>>>
>>>
>>> DATA = [
...     ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
...     (5.8, 2.7, 5.1, 1.9, 'virginica'),
...     (5.1, 3.5, 1.4, 0.2, 'setosa'),
...     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
...     (6.3, 2.9, 5.6, 1.8, 'virginica'),
...     (6.4, 3.2, 4.5, 1.5, 'versicolor'),
...     (4.7, 3.2, 1.3, 0.2, 'setosa')]
>>>
>>>
>>> @dataclass
... class Iris:
...     sepal_length: float
...     sepal_width: float
...     petal_length: float
...     petal_width: float
>>>
>>> class Setosa(Iris):
...     pass
>>>
>>> class Virginica(Iris):
...     pass
>>>
>>> class Versicolor(Iris):
...     pass
>>>
>>>
>>> def factory(species: str):
...     clsname = species.capitalize()
...     classes = globals()
...     return classes[clsname]
>>>
>>>
>>> result = [factory(species)(*features)
...           for *features, species in DATA[1:]]
>>>
>>> result  # doctest: +NORMALIZE_WHITESPACE
[Virginica(sepal_length=5.8, sepal_width=2.7, petal_length=5.1, petal_width=1.9),
 Setosa(sepal_length=5.1, sepal_width=3.5, petal_length=1.4, petal_width=0.2),
 Versicolor(sepal_length=5.7, sepal_width=2.8, petal_length=4.1, petal_width=1.3),
 Virginica(sepal_length=6.3, sepal_width=2.9, petal_length=5.6, petal_width=1.8),
 Versicolor(sepal_length=6.4, sepal_width=3.2, petal_length=4.5, petal_width=1.5),
 Setosa(sepal_length=4.7, sepal_width=3.2, petal_length=1.3, petal_width=0.2)]


Use Case - 0x05
---------------
* Class factory

>>> from dataclasses import dataclass
>>>
>>>
>>> DATA = [
...     ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
...     (5.8, 2.7, 5.1, 1.9, 'virginica'),
...     (5.1, 3.5, 1.4, 0.2, 'setosa'),
...     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
...     (6.3, 2.9, 5.6, 1.8, 'virginica'),
...     (6.4, 3.2, 4.5, 1.5, 'versicolor'),
...     (4.7, 3.2, 1.3, 0.2, 'setosa')]
>>>
>>>
>>> @dataclass
... class Iris:
...     sepal_length: float
...     sepal_width: float
...     petal_length: float
...     petal_width: float
>>>
>>>
>>>
>>> def factory(species: str):
...     clsname = species.capitalize()
...     classes = globals()
...     if clsname not in classes:
...         classes[clsname] = type(clsname, (Iris,), {})
...     return classes[clsname]
>>>
>>>
>>> result = [factory(species)(*features)
...           for *features, species in DATA[1:]]
>>>
>>> result  # doctest: +NORMALIZE_WHITESPACE
[Virginica(sepal_length=5.8, sepal_width=2.7, petal_length=5.1, petal_width=1.9),
 Setosa(sepal_length=5.1, sepal_width=3.5, petal_length=1.4, petal_width=0.2),
 Versicolor(sepal_length=5.7, sepal_width=2.8, petal_length=4.1, petal_width=1.3),
 Virginica(sepal_length=6.3, sepal_width=2.9, petal_length=5.6, petal_width=1.8),
 Versicolor(sepal_length=6.4, sepal_width=3.2, petal_length=4.5, petal_width=1.5),
 Setosa(sepal_length=4.7, sepal_width=3.2, petal_length=1.3, petal_width=0.2)]


Use Case - 0x06
---------------
>>> from dataclasses import dataclass
>>>
>>>
>>> DATA = [
...     ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
...     (5.8, 2.7, 5.1, 1.9, 'virginica'),
...     (5.1, 3.5, 1.4, 0.2, 'setosa'),
...     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
...     (6.3, 2.9, 5.6, 1.8, 'virginica'),
...     (6.4, 3.2, 4.5, 1.5, 'versicolor'),
...     (4.7, 3.2, 1.3, 0.2, 'setosa')]
>>>
>>>
>>> @dataclass
... class Iris:
...     sepal_length: float
...     sepal_width: float
...     petal_length: float
...     petal_width: float
>>>
>>>
>>> def factory(row):
...     *features, species = row
...     clsname = species.capitalize()
...     cls = type(clsname, (Iris,), {})
...     return cls(*features)
>>>
>>>
>>> result = map(factory, DATA[1:])
>>>
>>> list(result)  # doctest: +NORMALIZE_WHITESPACE
[Virginica(sepal_length=5.8, sepal_width=2.7, petal_length=5.1, petal_width=1.9),
 Setosa(sepal_length=5.1, sepal_width=3.5, petal_length=1.4, petal_width=0.2),
 Versicolor(sepal_length=5.7, sepal_width=2.8, petal_length=4.1, petal_width=1.3),
 Virginica(sepal_length=6.3, sepal_width=2.9, petal_length=5.6, petal_width=1.8),
 Versicolor(sepal_length=6.4, sepal_width=3.2, petal_length=4.5, petal_width=1.5),
 Setosa(sepal_length=4.7, sepal_width=3.2, petal_length=1.3, petal_width=0.2)]


Use Case - 0x07
---------------
>>> from pprint import pprint
>>>
>>>
>>> DATA = [
...     ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
...     (5.8, 2.7, 5.1, 1.9, 'virginica'),
...     (5.1, 3.5, 1.4, 0.2, 'setosa'),
...     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
...     (6.3, 2.9, 5.6, 1.8, 'virginica'),
...     (6.4, 3.2, 4.5, 1.5, 'versicolor'),
...     (4.7, 3.2, 1.3, 0.2, 'setosa'),
...     (7.0, 3.2, 4.7, 1.4, 'versicolor'),
...     (7.6, 3.0, 6.6, 2.1, 'virginica')]
>>>
>>>
>>> def myinit(self, sl, sw, pl, pw):
...     self.sl = sl
...     self.sw = sw
...     self.pl = pl
...     self.pw = pw
>>>
>>> def myrepr(self):
...     clsname = self.__class__.__name__
...     values = tuple(vars(self).values())
...     return f'{clsname}{values}'
>>>
>>> iris = type('Iris', (), {'__init__': myinit, '__repr__': myrepr})
>>>
>>> result = [cls(*values)
...           for *values, species in DATA[1:]
...           if (clsname := species.capitalize())
...           and (cls := type(clsname, (iris,), {}))]
>>>
>>>
>>> pprint(result)
[Virginica(5.8, 2.7, 5.1, 1.9),
 Setosa(5.1, 3.5, 1.4, 0.2),
 Versicolor(5.7, 2.8, 4.1, 1.3),
 Virginica(6.3, 2.9, 5.6, 1.8),
 Versicolor(6.4, 3.2, 4.5, 1.5),
 Setosa(4.7, 3.2, 1.3, 0.2),
 Versicolor(7.0, 3.2, 4.7, 1.4),
 Virginica(7.6, 3.0, 6.6, 2.1)]


Use Case - 0x08
---------------
>>> DATA = [
...     ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
...     (5.8, 2.7, 5.1, 1.9, 'virginica'),
...     (5.1, 3.5, 1.4, 0.2, 'setosa'),
...     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
...     (6.3, 2.9, 5.6, 1.8, 'virginica'),
...     (6.4, 3.2, 4.5, 1.5, 'versicolor'),
...     (4.7, 3.2, 1.3, 0.2, 'setosa')]

>>> def myinit(self, **kwargs):
...     self.__dict__ = kwargs
>>>
>>> def mystr(self):
...     clsname = self.__class__.__name__
...     values = tuple(vars(self).values())
...     return f'{clsname}{values}'
>>>
>>> Iris = type('Iris', (), {
...     '__init__': myinit,
...     '__str__': mystr,
...     '__repr__': mystr})

>>> result = []
>>> header = [x.lower().replace(' ', '_') for x in DATA[0]]
>>> data = [dict(zip(header,row)) for row in DATA[1:]]
>>>
>>> for row in data:
...     clsname = row.pop('species').capitalize()
...     if clsname not in globals():
...         globals()[clsname] = type(clsname, (Iris,), {})
...     cls = globals()[clsname]
...     iris = cls(**row)
...     result.append(iris)

>>> pprint(result, width=120)
[Virginica(sepal_length=5.8, sepal_width=2.7, petal_length=5.1, petal_width=1.9),
 Setosa(sepal_length=5.1, sepal_width=3.5, petal_length=1.4, petal_width=0.2),
 Versicolor(sepal_length=5.7, sepal_width=2.8, petal_length=4.1, petal_width=1.3),
 Virginica(sepal_length=6.3, sepal_width=2.9, petal_length=5.6, petal_width=1.8),
 Versicolor(sepal_length=6.4, sepal_width=3.2, petal_length=4.5, petal_width=1.5),
 Setosa(sepal_length=4.7, sepal_width=3.2, petal_length=1.3, petal_width=0.2)]


Use Case - 0x09
---------------
>>> from itertools import zip_longest
>>>
>>>
>>> DATA = [
...     ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
...     (5.8, 2.7, 'virginica'),
...     (5.1, 3.5, 1.4, 0.2, 'setosa'),
...     (5.7, 'versicolor'),
...     (6.3, 2.9, 5.6, 1.8, 'virginica'),
...     (6.4, 3.2, 4.5, 1.5, 'versicolor'),
...     (4.7, 3.2, 1.3, 'setosa'),
...     (7.0, 3.2, 4.7, 1.4, 'versicolor'),
...     (7.6, 3.0,  'virginica')]
>>>
>>>
>>> Iris = type('Iris', (), {
...     '__init__': lambda self, **kwargs: self.__dict__.update(kwargs),
...     '__repr__': lambda self: f'{self.__class__.__name__}{tuple(vars(self).values())}'})
>>>
>>> header = [x.lower().replace(' ', '_') for x in DATA[0]]
>>>
>>> result = [cls(**values)
...           for *features,species in DATA[1:]
...           if (values := dict(zip_longest(header, features, fillvalue=None)))
...           and (clsname := species.capitalize())
...           and (cls := type(clsname, (Iris,), {}))]

>>> result  # doctest: +NORMALIZE_WHITESPACE
[Virginica(5.8, 2.7, None, None, None),
 Setosa(5.1, 3.5, 1.4, 0.2, None),
 Versicolor(5.7, None, None, None, None),
 Virginica(6.3, 2.9, 5.6, 1.8, None),
 Versicolor(6.4, 3.2, 4.5, 1.5, None),
 Setosa(4.7, 3.2, 1.3, None, None),
 Versicolor(7.0, 3.2, 4.7, 1.4, None),
 Virginica(7.6, 3.0, None, None, None)]

>>> result[0]
Virginica(5.8, 2.7, None, None, None)

>>> vars(result[0])  # doctest: +NORMALIZE_WHITESPACE
{'sepal_length': 5.8,
 'sepal_width': 2.7,
 'petal_length': None,
 'petal_width': None,
 'species': None}


Use Case - 0x10
---------------
SetUp:

>>> del Iris
>>> del Setosa
>>> del Virginica
>>> del Versicolor
>>> del cls
>>> del values
>>> del species
>>> del iris
>>> del result

Code:

>>> DATA = [
...     ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
...     (5.8, 2.7, 5.1, 1.9, 'virginica'),
...     (5.1, 3.5, 1.4, 0.2, 'setosa'),
...     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
...     (6.3, 2.9, 5.6, 1.8, 'virginica'),
...     (6.4, 3.2, 4.5, 1.5, 'versicolor'),
...     (4.7, 3.2, 1.3, 0.2, 'setosa'),
...     (7.0, 3.2, 4.7, 1.4, 'versicolor'),
...     (7.6, 3.0, 6.6, 2.1, 'virginica'),
...     (4.9, 3.0, 1.4, 0.2, 'setosa'),
...     (4.9, 2.5, 4.5, 1.7, 'virginica'),
...     (7.1, 3.0, 5.9, 2.1, 'virginica'),
...     (4.6, 3.4, 1.4, 0.3, 'setosa'),
...     (5.4, 3.9, 1.7, 0.4, 'setosa'),
...     (5.7, 2.8, 4.5, 1.3, 'versicolor'),
...     (5.7, 2.8, 4.5, 1.3, 'setosa'),
...     (5.0, 3.6, 1.4, 0.3, 'setosa'),
...     (5.5, 2.3, 4.0, 1.3, 'versicolor'),
...     (6.5, 3.0, 5.8, 2.2, 'virginica'),
...     (6.5, 2.8, 4.6, 1.5, 'versicolor'),
...     (6.3, 3.3, 6.0, 2.5, 'virginica'),
...     (6.9, 3.1, 4.9, 1.5, 'versicolor'),
...     (4.6, 3.1, 1.5, 0.2, 'setosa'),
... ]
>>>
>>>
>>> globals()['Iris'] = type('Iris', (), {
...     '__init__': lambda self, *args: setattr(self, 'features', tuple(args)),
...     '__repr__': lambda self: f'{self.__class__.__name__}{self.features}',
... })
>>>
>>>
>>> def iris(row):
...     *values, species = row
...     clsname = species.capitalize()
...     if clsname not in globals():
...         cls = type(clsname, (globals()['Iris'],), {})
...     return cls(*values)
>>>
>>>
>>> result = map(iris, DATA[1:])
>>>
>>> list(result)  # doctest: +NORMALIZE_WHITESPACE
[Virginica(5.8, 2.7, 5.1, 1.9),
 Setosa(5.1, 3.5, 1.4, 0.2),
 Versicolor(5.7, 2.8, 4.1, 1.3),
 Virginica(6.3, 2.9, 5.6, 1.8),
 Versicolor(6.4, 3.2, 4.5, 1.5),
 Setosa(4.7, 3.2, 1.3, 0.2),
 Versicolor(7.0, 3.2, 4.7, 1.4),
 Virginica(7.6, 3.0, 6.6, 2.1),
 Setosa(4.9, 3.0, 1.4, 0.2),
 Virginica(4.9, 2.5, 4.5, 1.7),
 Virginica(7.1, 3.0, 5.9, 2.1),
 Setosa(4.6, 3.4, 1.4, 0.3),
 Setosa(5.4, 3.9, 1.7, 0.4),
 Versicolor(5.7, 2.8, 4.5, 1.3),
 Setosa(5.7, 2.8, 4.5, 1.3),
 Setosa(5.0, 3.6, 1.4, 0.3),
 Versicolor(5.5, 2.3, 4.0, 1.3),
 Virginica(6.5, 3.0, 5.8, 2.2),
 Versicolor(6.5, 2.8, 4.6, 1.5),
 Virginica(6.3, 3.3, 6.0, 2.5),
 Versicolor(6.9, 3.1, 4.9, 1.5),
 Setosa(4.6, 3.1, 1.5, 0.2)]


Use Case - 0x11
---------------
>>> DATA = [
...     ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
...     (5.8, 2.7, 5.1, 1.9, 'virginica'),
...     (5.1, 3.5, 1.4, 0.2, 'setosa'),
...     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
...     (6.3, 2.9, 5.6, 1.8, 'virginica'),
...     (6.4, 3.2, 4.5, 1.5, 'versicolor'),
...     (4.7, 3.2, 1.3, 0.2, 'arctica'),
...     (7.0, 3.2, 4.7, 1.4, 'versicolor'),
...     (7.6, 3.0, 6.6, 2.1, 'virginica')]
...
>>> header, *rows = DATA
...
>>> globals()['Iris'] = type('Iris', (), {
...     '__init__': lambda self, **kwargs: self.__dict__.update(kwargs),
...     '__str__': lambda self: f'{self.__class__.__name__}{tuple(vars(self).values())}',
... })
...
>>> def factory(row):
...     *values, species = row
...     clsname = species.capitalize()
...     if clsname not in globals():
...         globals()[clsname] = type(clsname, (globals()['Iris'],), {})
...     cls = globals()[clsname]
...     kwargs = dict(zip(header, values))
...     return cls(**kwargs)
...
>>> for iris in map(factory, rows):
...     print(iris)
...
Virginica(5.8, 2.7, 5.1, 1.9)
Setosa(5.1, 3.5, 1.4, 0.2)
Versicolor(5.7, 2.8, 4.1, 1.3)
Virginica(6.3, 2.9, 5.6, 1.8)
Versicolor(6.4, 3.2, 4.5, 1.5)
Arctica(4.7, 3.2, 1.3, 0.2)
Versicolor(7.0, 3.2, 4.7, 1.4)
Virginica(7.6, 3.0, 6.6, 2.1)


Assignments
-----------
.. literalinclude:: assignments/oop_class_factory_a.py
    :caption: :download:`Solution <assignments/oop_class_factory_a.py>`
    :end-before: # Solution
