.. testsetup::

    # doctest: +SKIP_FILE


Dragon ADR Position Change
==========================
* ADR - Architecture Design Records


Problem
-------
* Move dragon left by 10 and down by 20


Option 1
--------
>>> dragon.shift(left=10, down=20)
>>> dragon.fly(left=10, down=20)

* Good: extensible to 3D
* Good: move by relative shifting (left, right, up, down)
* Good: encapsulation, object knows current position, state and does the move
* Bad: method names are too use-case specific
* Decision: rejected, method names too use-case specific

Problem:

>>> dragon.fly(left=10, down=20)
>>> hero.walk(left=10, down=20)     # code duplication


Option 2
--------
>>> dragon.change_position(left=10, down=20)
>>> dragon.position_change(left=10, down=20)

* Good: extensible to 3D
* Good: move by relative shifting (left, right, up, down)
* Good: encapsulation, object knows current position and moves
* Bad: the method names are a bit too complex for
* Decision: candidate, method names are a bit too complex for now


Option 3
--------
>>> dragon.move(left=10, down=20)
>>> dragon.move(right=10, up=20)
>>> dragon.move(right=10, left=20)

* Good: extensible to 3D
* Good: move by relative shifting (left, right, up, down)
* Good: encapsulation, object knows current position, state and does the move
* Good: hides business logic (inverted y-axis)
* Good: easy ``.move()``
* Good: you can prevent negative shifting (i.e.: ``left=-10``)
* Decision: candidate


Option 4
--------
>>> dragon.move(x=10, y=-20)

* Good: extensible to 3D
* Good: move by relative shifting (left, right, up, down)
* Good: encapsulation, object knows current position, state and does the move
* Good: easy ``.move()``
* Bad: you have to know, which axis is ``left`` and with is ``right``
* Bad: requires knowledge of business logic (inverted y-axis)
* Bad: controller must know other variables, such as speed factor (snail is slower than a dragon), surface on which the dragon is moving (solid is faster than water or ice), injuries (if dragon is not injured with his for example left foot)
* Bad: you cannot prevent negative shifting (i.e.: ``x=-10``)
* Bad: the user must know the internals, how to calculate the position, which way is up or down (positive or negative shifting), note that ``y=-20`` means go up by 20 (we have inverted ``y`` axis)
* Bad: violates abstraction (OOP Principle)
* Bad: violates Tell, Don't Ask (OOP Principle)
* Decision: rejected, it requires to much inside knowledge of API from user


Option 5
--------
>>> dragon.move_to(x=10, y=20)

* Good: extensible to 3D
* Bad: Move by setting absolute position which is similar to ``.set_position()``, but it differs from it where in ``move()`` you can make an animation of movement, and with ``set_position()`` it happens instantly
* Bad: controller must know other variables, such as speed factor (snail is slower than a dragon), surface on which the dragon is moving (solid is faster than water or ice), injuries (if dragon is not injured with his for example left foot)
* Bad: requires knowledge of business logic (inverted y-axis)
* Bad: violates abstraction (OOP Principle)
* Decision: rejected, violates Model-View-Controller (MVC)

.. figure:: img/oop-architecture-mvc.png


Option 6
--------
>>> dragon.move_x(10)
>>> dragon.move_y(-20)

>>> dragon.move_horizontal(10)
>>> dragon.move_vertical(-20)

* Good: extensible to 3D, just add another method
* Bad: require knowledge of an API
* Bad: Move by setting absolute position
* Bad: controller must know other variables, such as speed factor (snail is slower than a dragon), surface on which the dragon is moving (solid is faster than water or ice), injuries (if dragon is not injured with his for example left foot)
* Bad: requires knowledge of business logic (inverted y-axis)
* Bad: the user must know the internals, how to calculate the position, which way is up or down (positive or negative shifting), note that ``y=-20`` means go up by 20 (we have inverted ``y`` axis)
* Bad: violates abstraction (OOP Principle)
* Bad: violates Tell, Don't Ask (OOP Principle)
* Decision: rejected


Option 7
--------
>>> dragon.move_xy(10, -20)

* Bad: Move by setting absolute position
* Bad: controller must know other variables, such as speed factor (snail is slower than a dragon), surface on which the dragon is moving (solid is faster than water or ice), injuries (if dragon is not injured with his for example left foot)
* Bad: the user must know the internals, how to calculate the position, which way is up or down (positive or negative shifting), note that ``y=-20`` means go up by 20 (we have inverted ``y`` axis)
* Bad: requires knowledge of business logic (inverted y-axis)
* Bad: name indicates that this is not extensible to 3D
* Bad: violates abstraction (OOP Principle)
* Bad: violates Tell, Don't Ask (OOP Principle)
* Decision: rejected


Option 8
--------
>>> dragon.move(10, -20)

* Good: extensible to 3D
* Bad: require knowledge of an API
* Bad: Move by setting absolute position
* Bad: controller must know other variables, such as speed factor (snail is slower than a dragon), surface on which the dragon is moving (solid is faster than water or ice), injuries (if dragon is not injured with his for example left foot)
* Bad: requires knowledge of business logic (inverted y-axis)
* Bad: the user must know the internals, how to calculate the position, which way is up or down (positive or negative shifting), note that ``y=-20`` means go up by 20 (we have inverted ``y`` axis)
* Bad: violates abstraction (OOP Principle)
* Bad: violates Tell, Don't Ask (OOP Principle)
* Decision: rejected


Option 9
--------
>>> dragon.move((10, -20))
>>> dragon.move_xy((10, -20))

* Bad: require knowledge of an API
* Bad: Move by setting absolute position
* Bad: controller must know other variables, such as speed factor (snail is slower than a dragon), surface on which the dragon is moving (solid is faster than water or ice), injuries (if dragon is not injured with his for example left foot)
* Bad: the user must know the internals, how to calculate the position, which way is up or down (positive or negative shifting), note that ``y=-20`` means go up by 20 (we have inverted ``y`` axis)
* Bad: requires knowledge of business logic (inverted y-axis)
* Bad: not extensible to 3D
* Bad: violates abstraction (OOP Principle)
* Bad: violates Tell, Don't Ask (OOP Principle)
* Decision: rejected


Option 10
---------
>>> dragon.move(dx=10, dy=-20)
>>> dragon.move(horizontal=10, vertical=-20)

* Good: encapsulation, object knows current position and moves
* Bad: controller computes final offset
* Bad: requires knowledge of business logic (inverted y-axis)
* Bad: the user must know the internals, how to calculate the position, which way is up or down (positive or negative shifting), note that ``y=-20`` means go up by 20 (we have inverted ``y`` axis)
* Bad: violates abstraction (OOP Principle)
* Bad: violates Tell, Don't Ask (OOP Principle)
* Decision: rejected


Option 11
---------
>>> dragon.move(0, 10, 0, 20)

>>> dragon.move((0, 10, 0, 20))

>>> dragon.move([
...     (0, 10, 0, 20),
...     (0, 10, 0, 20)])

* Good: there is only one method ``move()`` responsible for moving
* Bad: Python has keyword arguments, so use it
* Bad: require knowledge of an API
* Bad: not extensible to 3D
* Bad: requires knowledge of business logic (inverted y-axis)
* Bad: the user must know the internals, how to calculate the position, which way is up or down (positive or negative shifting), note that ``y=-20`` means go up by 20 (we have inverted ``y`` axis)
* Bad: violates abstraction (OOP Principle)
* Decision: rejected

Example:

* ``move(left, right, up, down)``

Problem:

* ``check(True, False, None)``

.. code-block:: css

    p {
        margin-top: 25px;
        margin-bottom: 75px;
        margin-right: 50px;
        margin-left: 100px;
    }

.. code-block:: css

    p {
        margin: 25px 50px 75px 100px;
    }

.. code-block:: css

    p {
        margin: 25px 50px 75px;
    }

.. code-block:: css

    p {
        margin: 25px 50px;
    }

.. code-block:: css

    p {
        margin: 25px;
    }

CSS:

* 4 params: top, right, bottom, left
* 3 params: top, right-left, bottom
* 2 params: top-bottom, right-left
* 1 params: top-right-bottom-left


Option 12
---------
>>> dragon.move([
...     (10, -20),
...     (10, -15)])

* Good: move by relative offset
* Bad: require knowledge of an API
* Bad: not extensible to 3D
* Bad: requires knowledge of business logic (inverted y-axis)
* Bad: the user must know the internals, how to calculate the position, which way is up or down (positive or negative shifting), note that ``y=-20`` means go up by 20 (we have inverted ``y`` axis)
* Bad: violates abstraction (OOP Principle)
* Bad: violates Tell, Don't Ask (OOP Principle)
* Decision: rejected

Example:

* ``move(horizontal, vertical)``


Option 13
---------
>>> dragon.move_to([
...     (10, -20),
...     (50, -120),
...     (5)])

* Bad: move by setting absolute position
* Bad: require knowledge of an API
* Bad: not extensible to 3D
* Bad: requires knowledge of business logic (inverted y-axis)
* Bad: the user must know the internals, how to calculate the position, which way is up or down (positive or negative shifting), note that ``y=-20`` means go up by 20 (we have inverted ``y`` axis)
* Bad: violates abstraction (OOP Principle)
* Bad: violates Tell, Don't Ask (OOP Principle)
* Decision: rejected

Example:

* ``move(x, y)``


Option 14
---------
>>> dragon.move_to({'x':50, 'y':-120})

>>> dragon.move_to([
...     {'x':10, 'y':-20},
...     {'x':10, 'y':-15}])

* Bad: require knowledge of an API
* Bad: not extensible to 3D
* Bad: requires knowledge of business logic (inverted y-axis)
* Bad: the user must know the internals, how to calculate the position, which way is up or down (positive or negative shifting), note that ``y=-20`` means go up by 20 (we have inverted ``y`` axis)
* Bad: violates abstraction (OOP Principle)
* Bad: violates Tell, Don't Ask (OOP Principle)
* Decision: rejected


Option 15
---------
>>> dragon.move({'left':50, 'down':120})

>>> dragon.move([
...     {'left':50, 'down':120},
...     {'left':50, 'right':120},
...     {'down':50}])

* Bad: require knowledge of an API
* Bad: not extensible to 3D
* Bad: requires knowledge of business logic (inverted y-axis)
* Bad: violates abstraction (OOP Principle)
* Decision: rejected


Option 16
---------
>>> dragon.move({'dx': 10, 'dy': 20})

>>> dragon.move([
...     {'dx': -10, 'dy': 20},
...     {'dx': -10, 'dy': 0}])

>>> dragon.move([
...     {'dx': -10, 'dy': 20},
...     {'dx': -10, 'dy': 20},
...     {'dx': -10, 'dy': 20}])

* Bad: require knowledge of an API
* Bad: not extensible to 3D
* Bad: requires knowledge of business logic (inverted y-axis)
* Bad: the user must know the internals, how to calculate the position, which way is up or down (positive or negative shifting), note that ``dy=-20`` means go up by 20 (we have inverted ``y`` axis)
* Bad: violates abstraction (OOP Principle)
* Bad: violates Tell, Don't Ask (OOP Principle)
* Decision: rejected


Option 17
---------
>>> dragon.move([
...     Point(x=10, y=20),
...     Point(x=10, y=15)])

>>> path = [
...     Point(x=10, y=20),
...     Point(x=10, y=15),
... ]
>>>
>>> dragon.move(path)

* Good: Move by setting absolute position on a path
* Good: This is how they do it in games
* Good: extensible to 3D
* Bad: requires knowledge of business logic (inverted y-axis)
* Bad: require knowledge of an API
* Decision: possible, common practice in game-dev


Option 18
---------
>>> dragon.move([
...     {'direction': 'left', 'distance': 20},
...     {'direction': 'left', 'distance': 10},
...     {'direction': 'right', 'distance': 20}])

* Good: extensible to 3D
* Bad: require knowledge of an API
* Decision: rejected


Option 19
---------
>>> dragon.move([
...     Left(20),
...     Left(10),
...     Right(20)])

* Good: extensible to 3D
* Bad: require knowledge of an API
* Bad: additional entities
* Decision: rejected


Option 20
---------
>>> dragon.move([
...     Direction('left', 20),
...     Direction('left', 10),
...     Direction('right', 20)])

>>> dragon.move([
...     Direction('left', distance=20),
...     Direction('left', distance=10),
...     Direction('right', distance=20)])

* Good: extensible to 3D
* Bad: require knowledge of an API
* Bad: additional entities
* Decision: rejected


Option 21
---------
>>> x = dragon.x
>>> y = dragon.y
>>> dragon.move(x=x-10, y=y+20)

>>> current = dragon.position
>>> dragon.set_position(x=current.x-10, y=current.y+20)

>>> x = dragon.x - 10
>>> y = dragon.y + 20
>>> dragon.move(x=x, y=y)

>>> dragon.x -= 10
>>> dragon.y += 20

>>> dragon.position_x -= 10
>>> dragon.position_y += 20

* Good: extensible to 3D, just add ``z`` attribute
* Bad: require knowledge of an API
* Bad: the user must know the internals, how to calculate the position, which way is up or down (positive or negative shifting), note that ``y=-20`` means go up by 20 (we have inverted ``y`` axis)
* Bad: violates abstraction (OOP Principle)
* Bad: violates encapsulation (OOP Principle)
* Bad: violates Tell, Don't Ask (OOP Principle)
* Decision: rejected


Option 22
---------
>>> dragon.move(x=-10, y=+20)
>>> dragon.move(dx=-10, dy=+20)
>>> dragon.change_position(left=-10, down=20)

* Good: extensible to 3D
* Bad: business login in controller
* Bad: the user must know the internals, how to calculate the position, which way is up or down (positive or negative shifting), note that ``dy=-20`` means go up by 20 (we have inverted ``y`` axis)
* Bad: violates abstraction (OOP Principle)
* Bad: violates Tell, Don't Ask (OOP Principle)
* Decision: rejected


Option 23
---------
>>> dragon.move('left', 20)
>>> dragon.move('right', 5)

* Good: extensible
* Good: extensible to 3D
* Bad: not possible to do movement in opposite directions in the same time
* Decision: rejected


Option 24
---------
>>> dragon.move('left', distance=20)
>>> dragon.move('right', distance=5)

* Good: extensible
* Good: extensible to 3D
* Bad: not possible to do movement in opposite directions in the same time
* Decision: rejected


Option 25
---------
>>> dragon.move(direction='left', distance=20)
>>> dragon.move(direction='right', distance=5)

* Good: explicit
* Good: verbose
* Good: extensible
* Good: extensible to 3D
* Bad: to complex for now
* Bad: not possible to do movement in opposite directions in the same time
* Decision: rejected


Option 26
---------
>>> LEFT = 61  # keyboard key code
>>> RIGHT = 62
>>> UP = 63
>>> DOWN = 64
>>>
>>> dragon.move(direction=LEFT, distance=20)

* Good: explicit
* Good: verbose
* Good: extensible
* Bad: to chaotic
* Bad: to complex for now
* Bad: there is no easy way to know which are possible directions
* Bad: not possible to do movement in opposite directions in the same time
* Decision: rejected, complex


Option 27
---------
>>> DIRECTION_LEFT = 61  # keyboard key code
>>> DIRECTION_RIGHT = 62
>>> DIRECTION_UP = 63
>>> DIRECTION_DOWN = 64
>>>
>>> dragon.move(direction=DIRECTION_LEFT, distance=20)

* Good: explicit
* Good: verbose
* Good: extensible
* Bad: there is no easy way to know which are possible directions
* Bad: less, but still chaotic
* Bad: to complex for now
* Bad: not possible to do movement in opposite directions in the same time
* Decision: rejected, complex


Option 28
---------
>>> class Direction(Enum):
...     LEFT = 61
...     RIGHT = 62
...     UP = 63
...     DOWN = 64
>>>
>>>
>>> dragon.move(Direction.LEFT, distance=5)
>>> dragon.move(direction=Direction.LEFT, distance=5)

* Good: explicit
* Good: verbose
* Good: extensible
* Good: ordered
* Good: there is a enumeration of possible choices for directions
* Bad: to complex for now
* Bad: not possible to do movement in opposite directions in the same time
* Decision: rejected, complex


Option 29
---------
>>> KEY_BINDING = {
...     'ARROW_UP': dragon.move_up,
...     'ARROW_DOWN': dragon.move_down,
...     'ARROW_LEFT': dragon.move_left,
...     'ARROW_RIGHT': dragon.move_right}
>>>
>>>
>>> def action(key, time):
...     return KEY_BINDING.get(key)(time)
>>>
>>>
>>> action('ARROW_UP', 5)

* Good: explicit
* Good: verbose
* Good: extensible
* Good: there is a enumeration of possible choices for directions
* Bad: to complex for now
* Decision: rejected, complex


Option 30
---------
>>> dragon.move_left(10)
>>> dragon.move_right(10)
>>> dragon.move_upright(10)
>>> dragon.move_downright(10)
>>> dragon.move_downleft(10)
>>> dragon.move_upleft(10)
>>> dragon.move_left_down(10, 20)

Example:

>>> class Key(Enum):
...     LEFT = 61
...     RIGHT = 62
...     UP = 63
...     DOWN = 64
>>>
>>>
>>> game.bind_key(Key.ARROW_LEFT, dragon.move_left)     # good
>>> game.bind_key(Key.ARROW_RIGHT, dragon.move_right)   # good
>>>
>>> game.bind_key(..., dragon.move_downright)           # bad
>>> game.bind_key(..., dragon.move_downleft)            # bad

Use Case 0x01:

>>> db.execute_select(SQL)
>>> db.execute_select_where(SQL)
>>> db.execute_select_order(SQL)
>>> db.execute_select_limit(SQL)
>>> db.execute_select_offset(SQL)
>>> db.execute_select_order_limit(SQL)
>>> db.execute_select_where_order_limit(SQL)
>>> db.execute_select_where_order_limit_offset(SQL)
>>> db.execute_insert(SQL)
>>> db.execute_insert_values(SQL)
>>> db.execute_alter(SQL)
>>> db.execute_alter_table(SQL)
>>> db.execute_alter_index(SQL)
>>> db.execute_create(SQL)
>>> db.execute_create_table(SQL)
>>> db.execute_create_index(SQL)
>>> db.execute_create_database(SQL)

Why not?:

>>> db.execute(SQL)

Use Case 0x02:

>>> read_csv('iris.csv', ';', 'utf-8', True)
>>> read_csv('iris.csv', delimiter=';', encoding='utf-8', verbose=True)

>>> read_csv_with_encoding('iris.csv', 'utf-8')
>>> read_csv_with_delimiter('iris.csv', ';')
>>> read_csv_with_delimiter_encoding('iris.csv', ';', 'utf-8')
>>> read_csv_with_delimiter_encoding_verbose('iris.csv', ';', 'utf-8', True)

>>> file = ReadCSV('iris.csv')  # encapsulation?!
>>> file.set_delimiter(';')
>>> file.set_encoding('utf-8')
>>> file.set_verbose(True)

>>> file = ReadCSV('iris.csv') \
...               .withDelimiter(';') \
...               .withEncoding('utf-8') \
...               .withVerbose(True)

>>> file = read_csv('iris.csv',
...                 delimiter=';',
...                 encoding='utf-8',
...                 verbose=True)

* Bad: not extensible
* Bad: to complex for now
* Bad: not possible to do movement in opposite directions in the same time
* Decision: rejected, complex


Decision
--------
>>> dragon.move(left=10, down=20)

* Good: easy
* Good: verbose
* Good: extensible (easy to convert to 3D)
* Good: encapsulation

Alternative, maybe in future:

>>> dragon.change_position(left=10, down=20)

* Good: consistent with ``set_position()`` and ``get_position()``
* Good: verbose
* Good: extensible
* Bad: a bit too complex for now
