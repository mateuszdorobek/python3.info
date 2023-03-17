State
=====
* EN: State
* PL: Stan
* Type: object


Pattern
-------
* Changes based on class
* Open/Close principle
* Using polymorphism

.. figure:: img/designpatterns-state-pattern.png

.. literalinclude:: uml/designpatterns-state-pattern.md
    :language: md


Problem
-------
* Canvas object can behave differently depending on selected Tool
* All behaviors are represented by subclass of the tool interface

.. figure:: img/designpatterns-state-problem.png

.. literalinclude:: uml/designpatterns-state-problem.md
    :language: md

.. literalinclude:: src/designpatterns-state-problem.py
    :language: python


Solution
--------
.. figure:: img/designpatterns-state-solution.png

.. literalinclude:: uml/designpatterns-state-solution.md
    :language: md

.. literalinclude:: src/designpatterns-state-solution.py
    :language: python


Use Case - 0x01
---------------
.. figure:: img/designpatterns-state-usecase-01.jpg

    GIMP (GNU Image Manipulation Project) window with tools and canvas [#GIMP]_

>>> class Tool:
...     def on_mouse_over(self): raise NotImplementedError
...     def on_mouse_out(self): raise NotImplementedError
...     def on_mouse_click_leftbutton(self): raise NotImplementedError
...     def on_mouse_unclick_leftbutton(self): raise NotImplementedError
...     def on_mouse_click_rightbutton(self): raise NotImplementedError
...     def on_mouse_unclick_rightbutton(self): raise NotImplementedError
...     def on_key_press(self): raise NotImplementedError
...     def on_key_unpress(self): raise NotImplementedError
>>>
>>>
>>> class Pencil(Tool):
...     def on_mouse_over(self):
...         ...
...
...     def on_mouse_out(self):
...         ...
...
...     def on_mouse_click_leftbutton(self):
...         ...
...
...     def on_mouse_unclick_leftbutton(self):
...         ...
...
...     def on_mouse_click_rightbutton(self):
...         ...
...
...     def on_mouse_unclick_rightbutton(self):
...         ...
...
...     def on_key_press(self):
...         ...
...
...     def on_key_unpress(self):
...         ...
>>>
>>>
>>> class Pen(Tool):
...     def on_mouse_over(self):
...         ...
...
...     def on_mouse_out(self):
...         ...
...
...     def on_mouse_click_leftbutton(self):
...         ...
...
...     def on_mouse_unclick_leftbutton(self):
...         ...
...
...     def on_mouse_click_rightbutton(self):
...         ...
...
...     def on_mouse_unclick_rightbutton(self):
...         ...
...
...     def on_key_press(self):
...         ...
...
...     def on_key_unpress(self):
...         ...


References
----------
.. [#GIMP] Download GIMP. Year: 2022. Retrieved: 2022-08-11. URL: https://anderbot.com/wp-content/uploads/2020/10/GIMP5.jpg


Assignments
-----------
.. literalinclude:: assignments/designpatterns_state_a.py
    :caption: :download:`Solution <assignments/designpatterns_state_a.py>`
    :end-before: # Solution
