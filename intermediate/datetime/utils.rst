Datetime Time Utils
===================


Sleep
-----
Time sleep function:

>>> from time import sleep
>>>
>>> sleep(0.1)

>>> from time import sleep
>>>
>>>
>>> for i in range(3):
...     # do something
...     sleep(0.1)

>>> # doctest: +SKIP
... from time import sleep
... from random import randint
... import requests
...
...
... for i in range(0, 2):
...     resp = requests.get('https://python3.info')
...     delay = randint(0,3)
...     sleep(delay)


``calendar``
------------
* HTML Calendar

>>> from calendar import HTMLCalendar
>>>
>>>
>>> html = HTMLCalendar().formatmonth(1969, 7)
>>> print(html)  # doctest: +NORMALIZE_WHITESPACE
<table border="0" cellpadding="0" cellspacing="0" class="month">
<tr><th colspan="7" class="month">July 1969</th></tr>
<tr><th class="mon">Mon</th><th class="tue">Tue</th><th class="wed">Wed</th><th class="thu">Thu</th><th class="fri">Fri</th><th class="sat">Sat</th><th class="sun">Sun</th></tr>
<tr><td class="noday">&nbsp;</td><td class="tue">1</td><td class="wed">2</td><td class="thu">3</td><td class="fri">4</td><td class="sat">5</td><td class="sun">6</td></tr>
<tr><td class="mon">7</td><td class="tue">8</td><td class="wed">9</td><td class="thu">10</td><td class="fri">11</td><td class="sat">12</td><td class="sun">13</td></tr>
<tr><td class="mon">14</td><td class="tue">15</td><td class="wed">16</td><td class="thu">17</td><td class="fri">18</td><td class="sat">19</td><td class="sun">20</td></tr>
<tr><td class="mon">21</td><td class="tue">22</td><td class="wed">23</td><td class="thu">24</td><td class="fri">25</td><td class="sat">26</td><td class="sun">27</td></tr>
<tr><td class="mon">28</td><td class="tue">29</td><td class="wed">30</td><td class="thu">31</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td></tr>
</table>


Use Case - 0x01
---------------
>>> #doctest: +SKIP
... from time import sleep
...
...
... def progressbar(percent):
...     filled = '=' * percent
...     empty = ' ' * (100-percent)
...     clear = '\b' * 110
...     bar = f'{clear}{percent:4}% |{filled}{empty}|'
...     print(bar, end='')
...
...
... for i in range(0,101):
...     progressbar(i)
...     sleep(0.2)
