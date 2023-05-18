.. testsetup::

    # doctest: +SKIP_FILE


ORM Update
==========
>>> mark = Person.objects.get(firstname='Mark', lastname='Watney')
>>> mark.age = 42
>>> mark.save()

>>> mark = Person.objects.get(firstname='Mark', lastname='Watney').update(age=42)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
AttributeError: 'Person' object has no attribute 'update'

>>> Person.objects.filter(firstname='Mark', lastname='Watney').update(age=42)
1

>>> Person.objects.filter(firstname='Mark').update(age=42)
2


>>> Person.objects.update_or_create(firstname='Mark', lastname='Watney')
(<Person: Mark Watney>, False)

>>> Person.objects.update_or_create(firstname='Mark', lastname='WatneyXXX')
(<Person: Mark WatneyXXX>, True)

>>> c, status = Person.objects.update_or_create(firstname='Mark', lastname='Watney')
>>>
>>> if status is True:
...     print('Created')
... else:
...     print('Updated')
Updated
c
<Person: Mark Watney>

>>> c, status = Person.objects.update_or_create(firstname='Mark', lastname='Watney', defaults={'age': 42})
>>> c
<Person: Mark Watney>
status
False


Update
------


Update or Create
----------------


Bulk Update
-----------


Select for Update
-----------------
