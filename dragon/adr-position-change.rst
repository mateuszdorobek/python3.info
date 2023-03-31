.. testsetup:: # doctest: +SKIP_FILE


Dragon ADR Position Change
==========================
* Move dragon left by 10 and down by 20
* Move dragon left by 10 and right by 15
* Move dragon right by 15 and up by 5
* Move dragon down by 5



Option 1
--------
>>> dragon.position_x += int
>>> dragon.position_y += int

Example:

>>> # left by 10 and down by 20
>>> dragon.position_x -= 10
>>> dragon.position_y += 20
>>>
>>> # left by 10 and right by 15
>>> dragon.position_x += 5
>>>
>>> # right by 15 and up by 5
>>> dragon.position_x += 15
>>> dragon.position_y -= 5
>>>
>>> # down by 5
>>> dragon.position_y += 5

Pros and Cons:

* Good: extensible to 3D, just add ``z`` attribute
* Bad: require knowledge of an API
* Bad: the user must know the internals, how to calculate the position, which way is up or down (positive or negative shifting), note that ``y=-20`` means go up by 20 (we have inverted ``y`` axis)
* Bad: violates abstraction (OOP Principle)
* Bad: violates encapsulation (OOP Principle)
* Bad: violates Tell, Don't Ask (OOP Principle)
* Decision: rejected

Consequences:

>>> current_x = dragon.position_x
>>> current_y = dragon.position_y
>>> dragon.set_position(x=current_x-10, y=current_y+20)

>>> new_x = dragon.position_x - 10
>>> new_y = dragon.position_y + 20
>>> dragon.set_position(x=new_x, y=new_y)


Option 2
--------
>>> dragon.move(int, int)

Example:

>>> dragon.move(-10, 20)  # left by 10 and down by 20
>>> dragon.move(5, 0)     # left by 10 and right by 15
>>> dragon.move(15, -5)   # right by 15 and up by 5
>>> dragon.move(0, 5)     # down by 5

Pros and Cons:

* Good: move by relative offset
* Bad: requires knowledge of business logic (inverted y-axis)
* Bad: require knowledge of an API
* Bad: not extensible to 3D
* Bad: the user must know the internals, how to calculate the position, which way is up or down (positive or negative shifting), note that ``y=-20`` means go up by 20 (we have inverted ``y`` axis)
* Bad: violates abstraction (OOP Principle)
* Bad: violates Tell, Don't Ask (OOP Principle)
* Decision: rejected

Consequences:

>>> dragon.move(10, -20)  # 2D
>>> dragon.move(10, -20, 30)  # 3D

Use Case:

>>> run('ls', True, False)  # bad
>>> read_csv('iris.csv', ';', 'utf-8', True)  # bad

.. code-block:: css
    :caption: CSS: top-bottom, right-left;

    p {
        margin: 25px 50px;
    }

.. code-block:: css
    :caption: CSS: top, right-left, bottom

    p {
        margin: 25px 50px 75px;
    }


Option 3
--------
>>> dragon.move(tuple[int,int])

Example:

>>> dragon.move((-10, 20))  # left by 10 and down by 20
>>> dragon.move((5, 0))     # left by 10 and right by 15
>>> dragon.move((15, -5))   # right by 15 and up by 5
>>> dragon.move((0, 5))     # down by 5

Pros and Cons:

* Bad: require knowledge of an API
* Bad: Move by setting absolute position
* Bad: controller must know other variables, such as speed factor (snail is slower than a dragon), surface on which the dragon is moving (solid is faster than water or ice), injuries (if dragon is not injured with his for example left foot)
* Bad: the user must know the internals, how to calculate the position, which way is up or down (positive or negative shifting), note that ``y=-20`` means go up by 20 (we have inverted ``y`` axis)
* Bad: requires knowledge of business logic (inverted y-axis)
* Bad: not extensible to 3D
* Bad: violates abstraction (OOP Principle)
* Bad: violates Tell, Don't Ask (OOP Principle)
* Decision: rejected

Consequences:

>>> dragon.move((10, -20))
>>> dragon.move((10, -20, 30))

Use Case:

>>> run(('ls', True, False, None))

.. code-block:: css
    :caption: CSS: top-right-bottom-left

    p {
        margin: 25px;
    }


Option 4
--------
>>> dragon.move(list[tuple[int,int]])

Example:

>>> dragon.move([
...     (-10, 20),  # left by 10 and down by 20
...     (5, 0),     # left by 10 and right by 15
...     (15, -5),   # right by 15 and up by 5
...     (0, 5),     # down by 5
... ])

Pros and Cons:

* Good: extensible to 3D
* Bad: requires knowledge of business logic (inverted y-axis)
* Bad: require knowledge of an API
* Bad: Move by setting absolute position
* Bad: controller must know other variables, such as speed factor (snail is slower than a dragon), surface on which the dragon is moving (solid is faster than water or ice), injuries (if dragon is not injured with his for example left foot)
* Bad: requires knowledge of business logic (inverted y-axis)
* Bad: the user must know the internals, how to calculate the position, which way is up or down (positive or negative shifting), note that ``y=-20`` means go up by 20 (we have inverted ``y`` axis)
* Bad: violates abstraction (OOP Principle)
* Bad: violates Tell, Don't Ask (OOP Principle)
* Decision: rejected

Consequences:

>>> dragon.move([
...     (-10, 20),
...     (5, 0, -5),
...     (0, 10, 20),
...     (0, -5),
... ])


Option 5
--------
>>> dragon.move(int, int, int int)
>>> dragon.move(tuple[int, int, int int])
>>> dragon.move(list[tuple[int, int, int int])

Example:

>>> dragon.move(0, 0, 20, 10)    # left by 10 and down by 20
>>> dragon.move(0, 15, 0, 10)    # left by 10 and right by 15
>>> dragon.move(5, 15, 0, 0)     # right by 15 and up by 5
>>> dragon.move(0, 0, 5, 0)      # down by 5

>>> dragon.move((0, 0, 20, 10))  # left by 10 and down by 20
>>> dragon.move((0, 15, 0, 10))  # left by 10 and right by 15
>>> dragon.move((5, 15, 0, 0))   # right by 15 and up by 5
>>> dragon.move((0, 0, 5, 0))    # down by 5

>>> dragon.move([
...     (0, 0, 20, 10)),        # left by 10 and down by 20
...     (0, 15, 0, 10)),        # left by 10 and right by 15
...     (5, 15, 0, 0)),         # right by 15 and up by 5
...     (0, 0, 5, 0)),          # down by 5
... ]

Pros and Cons:

* Good: there is only one method ``move()`` responsible for moving
* Bad: Python has keyword arguments, so use it
* Bad: require knowledge of an API
* Bad: not extensible to 3D
* Bad: requires knowledge of business logic (inverted y-axis)
* Bad: the user must know the internals, how to calculate the position, which way is up or down (positive or negative shifting), note that ``y=-20`` means go up by 20 (we have inverted ``y`` axis)
* Bad: violates abstraction (OOP Principle)
* Decision: rejected

Consequences:

>>> dragon.move(0, 10, 0, -20)  # bad
>>> dragon.move(0, 10, 0, -20, 0, 30)  # bad

>>> dragon.move([
...     (0, 10, 0, -20),
...     (0, 10, 0, -20, 0, 30),
...     (0, 10, 0, -20),
...     (0, 10, 0, -20, 0, 30),
... ])

Use Case:

>>> run(True, False, None)  # doctest: +SKIP

.. code-block:: css
    :caption: CSS: top, right, bottom, left

    p {
        margin: 25px 50px 75px 100px;
    }


Option 6
--------
>>> dragon.move_xy(int, int)

Example:

>>> dragon.move_xy(-10, 20)  # left by 10 and down by 20
>>> dragon.move_xy(5, 0)     # left by 10 and right by 15
>>> dragon.move_xy(15, -5)   # right by 15 and up by 5
>>> dragon.move_xy(0, 5)     # down by 5

Pros and Cons:

* Bad: Move by setting absolute position
* Bad: controller must know other variables, such as speed factor (snail is slower than a dragon), surface on which the dragon is moving (solid is faster than water or ice), injuries (if dragon is not injured with his for example left foot)
* Bad: the user must know the internals, how to calculate the position, which way is up or down (positive or negative shifting), note that ``y=-20`` means go up by 20 (we have inverted ``y`` axis)
* Bad: requires knowledge of business logic (inverted y-axis)
* Bad: name indicates that this is not extensible to 3D
* Bad: violates abstraction (OOP Principle)
* Bad: violates Tell, Don't Ask (OOP Principle)
* Decision: rejected

Consequences:

>>> dragon.move_xy(10, -20)  # 2D
>>> dragon.move_xyz(10, -20, 0)  # 3D


Option 7
--------
>>> dragon.move_x(int)
>>> dragon.move_y(int)

Example:

>>> # left by 10 and down by 20
>>> dragon.move_x(10)
>>> dragon.move_y(-20)
>>>
>>> # left by 10 and right by 15
>>> dragon.move_x(5)
>>>
>>> # right by 15 and up by 5
>>> dragon.move_x(15)
>>> dragon.move_y(-5)
>>>
>>> # down by 5
>>> dragon.move_y(5)

Pros and Cons:

* Good: extensible to 3D, just add another method
* Bad: require knowledge of an API
* Bad: Move by setting absolute position
* Bad: controller must know other variables, such as speed factor (snail is slower than a dragon), surface on which the dragon is moving (solid is faster than water or ice), injuries (if dragon is not injured with his for example left foot)
* Bad: requires knowledge of business logic (inverted y-axis)
* Bad: the user must know the internals, how to calculate the position, which way is up or down (positive or negative shifting), note that ``y=-20`` means go up by 20 (we have inverted ``y`` axis)
* Bad: violates abstraction (OOP Principle)
* Bad: violates Tell, Don't Ask (OOP Principle)
* Decision: rejected

Consequences:

>>> dragon.move_x(10)  # ok
>>> dragon.move_y(-20)  # ok
>>> dragon.move_z(0)  # ok


Option 8
--------
>>> dragon.move_horizontal(int)
>>> dragon.move_vertical(int)

Example:

>>> # left by 10 and down by 20
>>> dragon.move_horizontal(10)
>>> dragon.move_vertical(-20)
>>>
>>> # left by 10 and right by 15
>>> dragon.move_horizontal(5)
>>>
>>> # right by 15 and up by 5
>>> dragon.move_horizontal(15)
>>> dragon.move_vertical(-5)
>>>
>>> # down by 5
>>> dragon.move_vertical(5)

Pros and Cons:

* Good: extensible to 3D, just add another method
* Bad: require knowledge of an API
* Bad: Move by setting absolute position
* Bad: controller must know other variables, such as speed factor (snail is slower than a dragon), surface on which the dragon is moving (solid is faster than water or ice), injuries (if dragon is not injured with his for example left foot)
* Bad: requires knowledge of business logic (inverted y-axis)
* Bad: the user must know the internals, how to calculate the position, which way is up or down (positive or negative shifting), note that ``y=-20`` means go up by 20 (we have inverted ``y`` axis)
* Bad: violates abstraction (OOP Principle)
* Bad: violates Tell, Don't Ask (OOP Principle)
* Decision: rejected

Consequences:

>>> dragon.move_horizontal(10)  # ok
>>> dragon.move_vertical(-20)  # ok
>>> dragon.move_depth(0)  # bad, depth or altitude?
>>> dragon.move_altitude(0)  # bad, depth or altitude?


Option 9
--------
>>> dragon.move_left(int)
>>> dragon.move_right(int)
>>> dragon.move_up(int)
>>> dragon.move_down(int)

Example:

>>> # left by 10 and down by 20
>>> dragon.move_left(10)
>>> dragon.move_down(20)
>>>
>>> # left by 10 and right by 15
>>> dragon.move_left(10)
>>> dragon.move_right(15)
>>>
>>> # right by 15 and up by 5
>>> dragon.move_right(15)
>>> dragon.move_up(5)
>>>
>>> # down by 5
>>> dragon.move_down(5)

Pros and Cons:

* Bad: not extensible
* Bad: to complex for now
* Bad: not possible to do movement in opposite directions in the same time
* Decision: rejected, complex

Consequences:

>>> dragon.move_upright(10)
>>> dragon.move_upleft(10)
>>> dragon.move_downright(10)
>>> dragon.move_downleft(10)

>>> dragon.move_up_right(10)
>>> dragon.move_up_left(10)
>>> dragon.move_down_right(10)
>>> dragon.move_down_left(10)

Use Case:

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
>>>
>>> db.execute(SQL)

>>> read_csv_with_encoding('iris.csv', 'utf-8')
>>> read_csv_with_delimiter('iris.csv', ';')
>>> read_csv_with_delimiter_encoding('iris.csv', ';', 'utf-8')
>>> read_csv_with_delimiter_encoding_verbose('iris.csv', ';', 'utf-8', True)


Option 10
---------
>>> dragon.move(x=int, y=int)
>>> dragon.move(dx=int, dy=int)
>>> dragon.move(horizontal=int, vertical=int)

Example:

>>> dragon.move(x=-10, y=20)    # left by 10 and down by 20
>>> dragon.move(x=5, y=0)       # left by 10 and right by 15
>>> dragon.move(x=15, y=-5)     # right by 15 and up by 5
>>> dragon.move(x=0, y=5)       # down by 5

>>> dragon.move(dx=-10, dy=20)  # left by 10 and down by 20
>>> dragon.move(dx=5, dy=0)     # left by 10 and right by 15
>>> dragon.move(dx=15, dy=-5)   # right by 15 and up by 5
>>> dragon.move(dx=0, dy=5)     # down by 5

>>> dragon.move(horizontal=-10, vertical=20)  # left by 10 and down by 20
>>> dragon.move(horizontal=5, vertical=0)     # left by 10 and right by 15
>>> dragon.move(horizontal=15, vertical=-5)   # right by 15 and up by 5
>>> dragon.move(horizontal=0, vertical=5)     # down by 5

Pros and Cons:

* Good: extensible to 3D
* Good: move by relative shifting (left, right, up, down)
* Good: encapsulation, object knows current position, state and does the move
* Good: easy ``.move()``
* Bad: you have to know, which axis is ``left`` and with is ``right``
* Bad: requires knowledge of business logic (inverted y-axis)
* Bad: the user must know the internals, how to calculate the position, which way is up or down (positive or negative shifting), note that ``y=-20`` means go up by 20 (we have inverted ``y`` axis)
* Bad: controller must know other variables, such as speed factor (snail is slower than a dragon), surface on which the dragon is moving (solid is faster than water or ice), injuries (if dragon is not injured with his for example left foot)
* Bad: you cannot prevent negative shifting (i.e.: ``x=-10``)
* Bad: violates abstraction (OOP Principle)
* Bad: violates Tell, Don't Ask (OOP Principle)
* Decision: rejected, it requires to much inside knowledge of API from user

Consequences:

>>> dragon.move(x=10, y=-20)  # 2D, ok
>>> dragon.move(x=10, y=-20, z=30)  # 3D, ok

>>> dragon.move(dx=10, dy=-20)  # 2D, ok
>>> dragon.move(dx=10, dy=-20, dz=30)  # 3D, ok

>>> dragon.move(horizontal=10, vertical=-20)  # 2D, ok
>>> dragon.move(horizontal=10, vertical=-20, depth=30)  # 3D, bad, depth or altitude
>>> dragon.move(horizontal=10, vertical=-20, altitude=30)  # 3D, bad, depth or altitude


Option 11
---------
>>> dragon.move(left=int, right=int, up=int, down=int)

Example:

>>> dragon.move(left=10, down=20)    # left by 10 and down by 20
>>> dragon.move(left=10, right=15)   # left by 10 and right by 15
>>> dragon.move(right=15, up=5)      # right by 15 and up by 5
>>> dragon.move(down=5)              # down by 5

Pros and Cons:

* Good: extensible to 3D
* Good: move by relative shifting (left, right, up, down)
* Good: encapsulation, object knows current position, state and does the move
* Good: hides business logic (inverted y-axis)
* Good: easy ``.move()``
* Good: you can prevent negative shifting (i.e.: ``left=-10``)
* Good: encapsulation, object knows current position and moves
* Decision: candidate

Use Case:

>>> read_csv('iris.csv', delimiter=';', encoding='utf-8', verbose=True)

.. code-block:: css
    :caption: CSS: self explanatory

    p {
        margin-top: 25px;
        margin-right: 50px;
        margin-bottom: 75px;
        margin-left: 100px;
    }


Option 12
---------
>>> dragon.shift(left=int, down=int)
>>> dragon.fly(left=int, down=int)

Example:

>>> dragon.shift(left=10, down=20)    # left by 10 and down by 20
>>> dragon.shift(left=10, right=15)   # left by 10 and right by 15
>>> dragon.shift(right=15, up=5)      # right by 15 and up by 5
>>> dragon.shift(down=5)              # down by 5

>>> dragon.fly(left=10, down=20)    # left by 10 and down by 20
>>> dragon.fly(left=10, right=15)   # left by 10 and right by 15
>>> dragon.fly(right=15, up=5)      # right by 15 and up by 5
>>> dragon.fly(down=5)              # down by 5

Pros and Cons:

* Good: extensible to 3D
* Good: move by relative shifting (left, right, up, down)
* Good: encapsulation, object knows current position, state and does the move
* Bad: method names are too use-case specific
* Decision: rejected, method names too use-case specific

Consequences:

>>> dragon.fly(left=10, down=20)     # does the same, but different name
>>> hero.walk(left=10, down=20)      # does the same, but different name
>>> snake.slide(left=10, down=20)    # does the same, but different name

Use Case:

>>> locmem.store(key='...', value='..')
>>> locmem.retrieve(key='...')
>>> database.insert(column='...', value='...')
>>> database.select(column='...')
>>> filesystem.write(filename='...', content='...')
>>> filesystem.read(filename='...')


Option 13
---------
>>> dragon.change_position(left=int, down=int)
>>> dragon.position_change(left=int, down=int)

Example:

>>> dragon.change_position(left=10, down=20)    # left by 10 and down by 20
>>> dragon.change_position(left=10, right=15)   # left by 10 and right by 15
>>> dragon.change_position(right=15, up=5)      # right by 15 and up by 5
>>> dragon.change_position(down=5)              # down by 5

>>> dragon.position_change(left=10, down=20)    # left by 10 and down by 20
>>> dragon.position_change(left=10, right=15)   # left by 10 and right by 15
>>> dragon.position_change(right=15, up=5)      # right by 15 and up by 5
>>> dragon.position_change(down=5)              # down by 5

Pros and Cons:

* Good: extensible to 3D
* Good: move by relative shifting (left, right, up, down)
* Good: encapsulation, object knows current position and moves
* Bad: the method names are a bit too complex for
* Decision: candidate, method names are a bit too complex for now


Option 14
---------
* Move by setting absolute position along path

>>> dragon.move_to(int, int)
>>> dragon.move_to(tuple[int,int])
>>> dragon.move_to(list[tuple[int,int]])

Example:

>>> dragon.move_to(10, -20)
>>> dragon.move_to(50, -120)
>>> dragon.move_to(5, 0)

>>> dragon.move_to((10, -20))
>>> dragon.move_to((50, -120))
>>> dragon.move_to((5, 0))

>>> dragon.move_to([
...     (10, -20),
...     (50, -120),
...     (5, 0)])

Pros and Cons:

* Bad: move by setting absolute position
* Bad: similar to ``.set_position()``
* Bad: require knowledge of an API
* Bad: not extensible to 3D
* Bad: requires knowledge of business logic (inverted y-axis)
* Bad: the user must know the internals, how to calculate the position, which way is up or down (positive or negative shifting), note that ``y=-20`` means go up by 20 (we have inverted ``y`` axis)
* Bad: controller must know other variables, such as speed factor (snail is slower than a dragon), surface on which the dragon is moving (solid is faster than water or ice), injuries (if dragon is not injured with his for example left foot)
* Bad: violates abstraction (OOP Principle)
* Bad: violates Tell, Don't Ask (OOP Principle)
* Decision: rejected, violates Model-View-Controller (MVC)

Rationale:

* ``move()`` make an animation of movement (step by step)
* ``set_position()`` movement instantly (instant set)

Example:

>>> dragon.move_to([
...     (10, -20),
...     (50, -120),
...     (5)])

>>> dragon.move_to([
...     (10, -20, 0),
...     (50, -120, 0),
...     (5, 0, 0)])


Option 15
---------
* Move by setting absolute position along path

>>> dragon.move_to(dict[str,int])
>>> dragon.move_to(list[dict[str,int]])

Example:

>>> dragon.move_to({'x':-10, 'y':20})
>>> dragon.move_to({'x':10, 'y':-120})
>>> dragon.move_to({'x':50, 'y':-120})

>>> dragon.move_to([
...     {'x':10, 'y':-20},
...     {'x':10, 'y':-15}])

Pros and Cons:

* Bad: require knowledge of an API
* Bad: not extensible to 3D
* Bad: requires knowledge of business logic (inverted y-axis)
* Bad: the user must know the internals, how to calculate the position, which way is up or down (positive or negative shifting), note that ``y=-20`` means go up by 20 (we have inverted ``y`` axis)
* Bad: violates abstraction (OOP Principle)
* Bad: violates Tell, Don't Ask (OOP Principle)
* Decision: rejected


Option 16
---------
Example:

>>> dragon.move(Point(x=10, y=20))
>>> dragon.move(Point(x=10, y=20))
>>> dragon.move(Point(x=10, y=20))

>>> dragon.move([
...     Point(x=10, y=20),
...     Point(x=10, y=15),
...     Point(x=10, y=15),
... ])

Pros and Cons:

* Good: Move by setting absolute position on a path
* Good: This is how they do it in games
* Good: extensible to 3D
* Bad: requires knowledge of business logic (inverted y-axis)
* Bad: require knowledge of an API
* Decision: possible, common practice in game-dev

Example:

>>> path = [
...     Point(x=10, y=20),
...     Point(x=10, y=15),
...     Point(x=10, y=15),
... ]
>>>
>>> dragon.move(path)

Use Case:

>>> path: list[Point] = get_path(from_x, from_y, to_x, to_y)
>>> dragon.move(path)


Option 17
---------
* Move by relative shifting in axis

>>> dragon.move_to(dict[str,int])
>>> dragon.move_to(list[dict[str,int]])

Example:

>>> dragon.move({'dx': 10, 'dy': 20})
>>> dragon.move({'dx': 10, 'dy': 20})
>>> dragon.move({'dx': 10, 'dy': 20})

>>> dragon.move([
...     {'dx': -10, 'dy': 20},
...     {'dx': -10, 'dy': 0}])

Pros and Cons:

* Bad: require knowledge of an API
* Bad: not extensible to 3D
* Bad: requires knowledge of business logic (inverted y-axis)
* Bad: the user must know the internals, how to calculate the position, which way is up or down (positive or negative shifting), note that ``dy=-20`` means go up by 20 (we have inverted ``y`` axis)
* Bad: violates abstraction (OOP Principle)
* Bad: violates Tell, Don't Ask (OOP Principle)
* Decision: rejected


Option 18
---------
* Move by relative shifting to the sides

>>> dragon.move_to(dict[str,int])
>>> dragon.move_to(list[dict[str,int]])

Example:

>>> dragon.move({'left':50, 'down':120})
>>> dragon.move({'left':50, 'down':120})
>>> dragon.move({'left':50, 'down':120})

>>> dragon.move([
...     {'left':50, 'down':120},
...     {'left':50, 'right':120},
...     {'down':50}])

Pros and Cons:

* Bad: require knowledge of an API
* Bad: not extensible to 3D
* Bad: requires knowledge of business logic (inverted y-axis)
* Bad: violates abstraction (OOP Principle)
* Bad: **kwargs can convert to keyword arguments
* Decision: rejected


Option 19
---------
* Move by relative shifting to the sides

>>> dragon.move_to(dict[str,int])
>>> dragon.move_to(list[dict[str,int]])

Example:

>>> dragon.move({'direction': 'left', 'distance': 20})
>>> dragon.move({'direction': 'left', 'distance': 10})
>>> dragon.move({'direction': 'right', 'distance': 20})

>>> dragon.move([
...     {'direction': 'left', 'distance': 20},
...     {'direction': 'left', 'distance': 10},
...     {'direction': 'right', 'distance': 20}])

Pros and Cons:

* Good: extensible to 3D
* Bad: require knowledge of an API
* Decision: rejected


Option 20
---------
* Move by relative shifting to the sides

>>> dragon.move(Direction)
>>> dragon.move(list[Direction])

Example:

>>> dragon.move(Direction('left', distance=20))
>>> dragon.move(Direction('left', distance=10))
>>> dragon.move(Direction('right', distance=20))

>>> dragon.move([
...     Direction('left', distance=20),
...     Direction('left', distance=10),
...     Direction('right', distance=20)])

Pros and Cons:

* Good: extensible to 3D
* Bad: require knowledge of an API
* Bad: additional entities
* Decision: rejected


Option 21
---------
* Move by relative shifting to the sides

>>> dragon.move(str, int)
>>> dragon.move(str, distance=int)
>>> dragon.move(direction=str, distance=int)

Example:

>>> dragon.move('left', 20)
>>> dragon.move('right', 5)
>>> dragon.move('left', distance=20)
>>> dragon.move('right', distance=5)
>>> dragon.move(direction='left', distance=20)
>>> dragon.move(direction='right', distance=5)

Pros and Cons:

* Good: extensible
* Good: extensible to 3D
* Bad: not possible to do movement in opposite directions in the same time
* Decision: rejected

Consequences:

>>> dragon.move('l', 20)
>>> dragon.move('r', 5)
>>> dragon.move('l', distance=20)
>>> dragon.move('r', distance=5)
>>> dragon.move(direction='l', distance=20)
>>> dragon.move(direction='r', distance=5)

Use Case:

>>> plt.plot(x, y, color='cyan')
>>> plt.plot(x, y, color='c')

>>> df.plot(kind='line')
>>> df.interpolate('polynomial')
>>> plt.plot(x, y, color='red')


Option 22
---------
* Move by relative shifting to the sides

>>> dragon.move(Left | Right | Up | Down)
>>> dragon.move(list[Left | Right | Up | Down])

Example:

>>> dragon.move(Left(20))
>>> dragon.move(Left(10))
>>> dragon.move(Right(20))

>>> dragon.move([
...     Left(20),
...     Left(10),
...     Right(20)])

Pros and Cons:

* Good: extensible to 3D
* Bad: require knowledge of an API
* Bad: additional entities
* Decision: rejected


Option 23
---------
* Move by relative shifting to the sides
* Bind to keyboard key codes

>>> dragon.move(int, int)
>>> dragon.move(int, distance=int)
>>> dragon.move(direction=int, distance=int)

Example:

>>> # keyboard key codes
>>> LEFT = 0x61
>>> DOWN = 0x62
>>> RIGHT = 0x63
>>> UP = 0x64
>>>
>>> # movement
>>> dragon.move(LEFT, 20)
>>> dragon.move(LEFT, distance=20)
>>> dragon.move(direction=LEFT, distance=20)

>>> # keyboard key codes
>>> DIRECTION_LEFT = 0x61
>>> DIRECTION_DOWN = 0x62
>>> DIRECTION_UP = 0x64
>>> DIRECTION_RIGHT = 0x63
>>>
>>> # movement
>>> dragon.move(DIRECTION_LEFT, 20)
>>> dragon.move(DIRECTION_LEFT, distance=20)
>>> dragon.move(direction=DIRECTION_LEFT, distance=20)

>>> # keyboard key codes
>>> class Direction(IntEnum):
...     LEFT = 0x61
...     DOWN = 0x62
...     RIGHT = 0x63
...     UP = 0x64
>>>
>>>
>>> # movement
>>> dragon.move(Direction.LEFT, 5)
>>> dragon.move(Direction.LEFT, distance=5)
>>> dragon.move(direction=Direction.LEFT, distance=5)

Pros and Cons:

* Good: explicit
* Good: verbose
* Good: extensible
* Bad: to chaotic
* Bad: to complex for now
* Bad: there is no easy way to know which are possible directions
* Bad: not possible to do movement in opposite directions in the same time
* Decision: rejected, complex

.. figure:: img/keyboard-keycodes-us.png


Option 24
---------
* Move by relative shifting to the sides
* Bind to keyboard key codes

>>> dragon.move(int, int)
>>> dragon.move(int, distance=int)
>>> dragon.move(direction=int, distance=int)

Example:

>>> # keyboard key codes
>>> ARROW_LEFT = 0x61
>>> ARROW_DOWN = 0x62
>>> ARROW_RIGHT = 0x63
>>> ARROW_UP = 0x64
>>>
>>>
>>> def move(key, time):
...     if key == ARROW_LEFT:
...         dragon.move_left(time)
...     elif key == ARROW_DOWN:
...         dragon.move_down(time)
...     elif key == ARROW_RIGHT:
...         dragon.move_right(time)
...     elif key == ARROW_UP:
...         dragon.move_up(time)
>>>
>>>
>>> move(ARROW_UP, 5)

>>> # keyboard key codes
>>> class Key(IntEnum):
...     ARROW_LEFT = 0x61
...     ARROW_DOWN = 0x62
...     ARROW_RIGHT = 0x63
...     ARROW_UP = 0x64
>>>
>>>
>>> def move(key, time):
...     match key:
...         case Key.ARROW_LEFT: dragon.move_left(time)
...         case Key.ARROW_DOWN: dragon.move_down(time)
...         case Key.ARROW_RIGHT: dragon.move_right(time)
...         case Key.ARROW_UP: dragon.move_up(time)
...         case _: raise NotImplementedError
>>>
>>>
>>> move(Key.ARROW_UP, 5)

Pros and Cons:

* Good: explicit
* Good: verbose
* Good: extensible
* Good: there is a enumeration of possible choices for directions
* Bad: to complex for now
* Decision: rejected, complex


Option 25
---------
>>> # keyboard key codes
>>> class Key(IntEnum):
...     ARROW_LEFT = 0x61
...     ARROW_DOWN = 0x62
...     ARROW_RIGHT = 0x63
...     ARROW_UP = 0x64
>>>
>>>
>>> game.bind(Key.ARROW_LEFT, dragon.move_left)     # good
>>> game.bind(Key.ARROW_DOWN, dragon.move_down)     # good
>>> game.bind(Key.ARROW_RIGHT, dragon.move_right)   # good
>>> game.bind(Key.ARROW_UP, dragon.move_up)         # good

Pros and Cons:

* Bad: not extensible
* Bad: to complex for now
* Bad: not possible to do movement in opposite directions in the same time
* Decision: rejected, complex


Decision
--------
>>> class Dragon:
...     def move(self, *,
...              left: int = 0, right: int = 0,
...              down: int = 0, up: int = 0,
...              ) -> None: ...
>>>
>>> dragon.move(left=10, down=20)

Pros and Cons:

* Good: easy
* Good: verbose
* Good: extensible (easy to convert to 3D)
* Good: encapsulation


Future
------
>>> class Dragon:
...     def change_position(self, *,
...                         left: int = 0, right: int = 0,
...                         down: int = 0, up: int = 0,
...                         ) -> None: ...
>>>
>>> dragon.change_position(left=10, down=20)

Pros and Cons:

* Good: consistent with ``set_position()`` and ``get_position()``
* Good: verbose
* Good: extensible
* Bad: a bit too complex for now
