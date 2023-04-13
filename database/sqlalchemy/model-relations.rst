.. testsetup::

    # doctest: +SKIP_FILE


Model Relations
===============
* ForeignKey vs PrimaryKey
* ForeignKey vs CompositeForeignKey
* Relation 1 to 1
* Relation 1 to Many
* Relation Many to Many
* ``lazy loading``
* ``joined loading``
* ``subquery loading``
* ``select IN loading``
* ``raise loading``
* ``no loading``


About
-----
The primary forms of relationship loading are [#saDocsLoadingRelationships]_:

``lazy loading`` - Lazy Loading
    available via ``lazy='select'`` or the ``lazyload()`` option, this is
    the form of loading that emits a ``SELECT`` statement at attribute access
    time to lazily load a related reference on a single object at a time.

``joined loading`` - Joined Eager Loading
    available via ``lazy='joined'`` or the ``joinedload()`` option, this
    form of loading applies a ``JOIN`` to the given ``SELECT`` statement so
    that related rows are loaded in the same result set.

``subquery loading`` - Subquery Eager Loading
    available via ``lazy='subquery'`` or the ``subqueryload()`` option,
    this form of loading emits a second ``SELECT`` statement which re-states
    the original query embedded inside of a subquery, then ``JOIN``s that
    subquery to the related table to be loaded to load all members of
    related collections / scalar references at once.

``select IN loading`` - Select ``IN`` loading
    available via ``lazy='selectin'`` or the ``selectinload()`` option,
    this form of loading emits a second (or more) ``SELECT`` statement
    which assembles the primary key identifiers of the parent objects
    into an ``IN`` clause, so that all members of related collections
    or scalar references are loaded at once by primary key.

``raise loading``
    available via ``lazy='raise'``, ``lazy='raise_on_sql'``, or the
    ``raiseload()`` option, this form of loading is triggered at the same
    time a lazy load would normally occur, except it raises an ORM exception
    in order to guard against the application making unwanted lazy loads.
    An introduction to raise loading is at Preventing unwanted lazy loads
    using ``raiseload``.

``no loading``
    available via ``lazy='noload'``, or the ``noload()`` option; this loading
    style turns the attribute into an empty attribute (``None`` or ``[]``)
    that will never load or have any loading effect. This seldom-used
    strategy behaves somewhat like an eager loader when objects are loaded
    in that an empty attribute or collection is placed, but for expired
    objects relies upon the default value of the attribute being returned on
    access; the net effect is the same except for whether or not the
    attribute name appears in the ``InstanceState.unloaded`` collection.
    ``noload`` may be useful for implementing a 'write-only' attribute but
    this usage is not currently tested or formally supported.

Configuring Loader Strategies at Mapping Time:

>>> class Parent(Base):
...     __tablename__ = 'parent'
...     id = Column(Integer, primary_key=True)
...     name = Column(String(30))
...     children = relationship('Child', lazy='joined')

Relationship Loading with Loader Options:

>>> stmt = select(Parent).options(
...       lazyload(Parent.children).
...       subqueryload(Child.subelements))
>>>
>>> result = session.execute(stmt)


PrimaryKey
----------


ForeignKey
----------


Composite ForeignKey
--------------------


One To One Relation
-------------------
* Note ``uselist=False``

>>> class Parent(Base):
...     __tablename__ = 'parent'
...     id = Column(Integer, primary_key=True)
...     name = Column(String(30))
...     children = relationship('Child', backref='parent', uselist=False)

>>> class Child(Base):
...     __tablename__ = 'parent'
...     id = Column(Integer, primary_key=True)
...     name = Column(String(30))
...     parent_id = Column(Integer, ForeignKey('parent.id'))


One to Many Relation
--------------------
* There is no ``uselist=False``

>>> class Parent(Base):
...     __tablename__ = 'parent'
...     id = Column(Integer, primary_key=True)
...     name = Column(String(30))
...     children = relationship('Child', backref='parent')

>>> class Child(Base):
...     __tablename__ = 'parent'
...     id = Column(Integer, primary_key=True)
...     name = Column(String(30))
...     parent_id = Column(Integer, ForeignKey('parent.id'))


Many to Many Relation
---------------------
>>> class ParentsChildren(Base):
...     __tablename__ = 'parents_children'
...     parent_id = Column(Integer, ForeignKey('parent.id'))
...     child_id = Column(Integer, ForeignKey('child.id'))

>>> class Parent(Base):
...     __tablename__ = 'parent'
...     id = Column(Integer, primary_key=True)
...     name = Column(String(30))
...     children = relationship('Child', secondary='ParentsChildren', backref='parents')

>>> class Child(Base):
...     __tablename__ = 'parent'
...     id = Column(Integer, primary_key=True)
...     name = Column(String(30))
...     parents = relationship('Parent', secondary='ParentsChildren', backref='children')


Use Case - 0x01
---------------
>>> class Astronaut(Model):
...     __tablename__ = 'astronauts'
...     id = Column(Integer, primary_key=True, index=True)
...     firstname = Column(String)
...     lastname = Column(String)
...     active = Column(Boolean, nullable=True)
...     creator_id = Column(Integer, ForeignKey('users.id'))
...     creator = relationship('User', back_populates='created')
>>>
>>>
>>> class User(Model):
...     __tablename__ = 'users'
...     id = Column(Integer, primary_key=True, index=True)
...     username = Column(String)
...     email = Column(String)
...     password = Column(String)
...     created = relationship('Astronaut', back_populates='creator')


Further Reading
---------------
* https://docs.sqlalchemy.org/en/14/orm/loading_relationships.html


References
----------
.. [#saDocsLoadingRelationships] https://docs.sqlalchemy.org/en/14/orm/loading_relationships.html
