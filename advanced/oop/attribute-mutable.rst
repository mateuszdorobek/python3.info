OOP Attribute Mutable/Immutable
===============================
* Function and method arguments should not be mutable

Immutable Types:

* ``int``
* ``float``
* ``complex``
* ``bool``
* ``None``
* ``str``
* ``bytes``
* ``tuple``
* ``frozenset``
* ``mappingproxy``

Mutable Types:

* ``list``
* ``set``
* ``dict``


Problem
-------
Let's define a class:

>>> class User:
...     def __init__(self, firstname, lastname, groups=[]):
...         self.firstname = firstname
...         self.lastname = lastname
...         self.groups = groups

Now, we create an instance of a class:

>>> mark = User('Mark', 'Watney')
>>> melissa = User('Melissa', 'Lewis')

Check groups for both Users:

>>> mark.groups
[]
>>>
>>> melissa.groups
[]

We will assign Mark Watney to three groups: admins, staff, editors:

>>> mark.groups.append('admins')
>>> mark.groups.append('staff')
>>> mark.groups.append('editors')

Now, check the groups once again:

>>> mark.groups
['admins', 'staff', 'editors']
>>>
>>> melissa.groups
['admins', 'staff', 'editors']

This is not a mistake! Both users Mark and Melissa has the same groups
despite the fact, that we set values only for Mark. This is because both
both Mark and Melissa has attribute ``groups`` pointing to the same memory
address:

>>> hex(id(mark.groups))  # doctest: +SKIP
'0x10e732500'
>>>
>>> hex(id(melissa.groups))  # doctest: +SKIP
'0x10e732500'

This is the same object!

>>> from inspect import signature
>>>
>>>
>>> signature(User.__init__)
<Signature (self, firstname, lastname, groups=['admins', 'staff', 'editors'])>
>>>
>>> signature(User.__init__).parameters.get('groups').default
['admins', 'staff', 'editors']
>>>
>>> hex(id(signature(User.__init__).parameters.get('groups').default))  # doctest: +SKIP
'0x10e732500'


Rationale
---------
Note, You should not set mutable objects as a default function argument.
More information in `Argument Mutability`. This is how all dynamically typed
languages work (including JavaScript, PHP, Ruby, Perl etc).

The problem lays in ``__init__()`` method signature. It consist a reference
to the mutable object: ``list``. Python will create a new ``list`` instance
on class creation, not an instance creation! Therefore each user will
reference to the same ``list`` which was created when Python interpreted class.

>>> class User:
...     def __init__(self, firstname, lastname, groups=[]):
...         self.firstname = firstname
...         self.lastname = lastname
...         self.groups = groups

However method body is not interpreted on class creation. This is done in a
runtime. Creating a new ``list`` in method's body will instantiate a new
sequence each time the new instance is created. Consider the following code:

>>> class User:
...     def __init__(self, firstname, lastname, groups=None):
...         self.firstname = firstname
...         self.lastname = lastname
...         self.groups = groups if groups else []

``None`` object is a singleton, which can be reused. Also is not a problematic,
because we will not append or modify anything to the ``None`` itself. As soon
as the new instance is created, the ``__init__()`` body is evaluated and
``self.groups`` is assigned to newly created ``list`` instance.


Solution
--------
>>> class User:
...     def __init__(self, firstname, lastname, groups=None):
...         self.firstname = firstname
...         self.lastname = lastname
...         self.groups = groups if groups else []

Now, we create an instance of a class:

>>> mark = User('Mark', 'Watney')
>>> melissa = User('Melissa', 'Lewis')

Check groups for both Users:

>>> mark.groups
[]
>>>
>>> melissa.groups
[]

We will assign Mark Watney to three groups: admins, staff, editors:

>>> mark.groups.append('admins')
>>> mark.groups.append('staff')
>>> mark.groups.append('editors')

Now, check the groups once again:

>>> mark.groups
['admins', 'staff', 'editors']
>>>
>>> melissa.groups
[]

This time their addresses are differs:

>>> hex(id(mark.groups))  # doctest: +SKIP
'0x108ca7ac0'
>>>
>>> hex(id(melissa.groups))  # doctest: +SKIP
'0x109a88540'

And they are not the same object:

>>> from inspect import signature
>>>
>>>
>>> signature(User.__init__)
<Signature (self, firstname, lastname, groups=None)>
>>>
>>> signature(User.__init__).parameters.get('groups').default
>>>
>>> hex(id(signature(User.__init__).parameters.get('groups').default))  # doctest: +SKIP
'0x106ef4948'

This mechanism works the same, but this time points to the immutable object
which as the name says, cannot be changed, so we are safe now:

>>> hex(id(None))  # doctest: +SKIP
'0x106ef4948'


Assignments
-----------
.. todo:: Assignments
