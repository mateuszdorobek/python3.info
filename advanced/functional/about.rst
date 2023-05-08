Functional About
================
* Programming paradigm
* Programs are constructed by applying and composing functions
* Functions are treated as first-class citizens
* Functional programming avoids side effects
* Functional programming provides referential transparency
* Instead of loop use ``map`` and recurrence
* Functions can be bound to names (including local identifiers), passed as arguments, and returned from other functions, just as any other data type can [#WikipediaFunc]_
* Imperative program will use a loop to traverse and modify a list, while a functional program, would prefer using a higher-order ``map`` function that takes a function and a list, generating and returning a new list by applying the function to each list item [#Spiewak2008]_
* Restricting side effects, can decrease number of bugs, be easier to debug and test, and be more suited to formal verification [#Hughes1984]_ [#Hudak1989]_
* Functional Design Patterns - Scott Wlaschin https://www.youtube.com/watch?v=srQt1NAHYC0
* The Functional Programmer's Toolkit - Scott Wlaschin - https://www.youtube.com/watch?v=Nrp_LZ-XGsY


Advantages
----------
* Comprehensibility: Pure functions don't change states and are entirely dependent on input, and are consequently simple to understand.
* Concurrency: As pure functions avoid changing variables or any data outside it, concurrency implementation is easier.
* Lazy evaluation: Functional programming encourages lazy evaluation, which means that the value is evaluated and stored only when required.
* Easier debugging and testing: Pure functions take arguments once and produce unchangeable output. With immutability and no hidden output, debugging and testing becomes easier.

Source: [#Inouye2022]_


Disadvantages
-------------
* Potentially poorer performance: Immutable values combined with recursion might lead to a reduction in performance.
* Coding difficulties:Though writing pure functions is easy, combining it with the rest of the application and I/O operations can be tough.
* No loops can be challenging:Writing programs in a recursive style instead of loops can be a daunting task.

Source: [#Inouye2022]_


Applications
------------
Generally, functional programming is widely employed in applications
focusing on concurrency or parallelism, and carrying out mathematical
computations.

Functional programming languages are often preferred for academic purposes,
rather than commercial software development. Nevertheless, several prominent
functional languages like Clojure, Erlang, F#, Haskell, and Racket, are used
for developing a variety of commercial and industrial applications.

For example, WhatsApp makes use of Erlang, a programming language following
the functional programming paradigm, to manage data belonging to over
1.5 billion people.

Another important torchbearer of the functional programming style
is Haskell, which is used by Facebook in its anti-spam system. Even
JavaScript, one of the most widely used programming languages, flaunts
the properties of a dynamically typed functional language.

Moreover, the functional style of programming is essential for various
programming languages to lead in distinct domains - like R in statistics
and J, K, and Q in financial analysis. Even used by domain-specific
declarative languages such as Lex/Yacc and SQL for eschewing mutable values.

Source: [#Inouye2022]_


Further Reading
---------------
* Functional Design Patterns - Scott Wlaschin - https://www.youtube.com/watch?v=srQt1NAHYC0
* The Functional Programmer's Toolkit - Scott Wlaschin - https://www.youtube.com/watch?v=Nrp_LZ-XGsY


Example: Procedural
-------------------
* Hard to test

>>> result = []
>>>
>>> with open('/tmp/myfile.log') as file:  # doctest: +SKIP
...     for row in file:
...         d, t, lvl, msg = line.strip().split(', ', maxsplit=3)
...         d = date.fromisoformat(d)
...         t = time.fromisoformat(t)
...         dt = datetime.combine(d,t)
...         result.append({'when':dt, 'level':lvl, 'message':msg})


Example: Functional
-------------------
* Much easier to test
* Function is type annotated
* Function could be reused

>>> def parse(line: str) -> dict:
...     d, t, lvl, msg = line.strip().split(', ', maxsplit=3)
...     d = date.fromisoformat(d)
...     t = time.fromisoformat(t)
...     dt = datetime.combine(d,t)
...     return {'when':dt, 'level':lvl, 'message':msg}
>>>
>>>
>>> with open('/tmp/myfile.log') as file:  # doctest: +SKIP
...     for row in map(parse, file):
...         print(row)


Doctests
--------
>>> def parse(line: str) -> dict:
...     """
...     >>> parse('1969-07-14, 21:00:00, INFO, Terminal countdown started')
...     {'when': datetime.datetime(1969, 7, 14, 21, 0),
...      'level': 'INFO',
...      'message': 'Terminal countdown started'}
...
...     >>> parse('1969-07-24, 17:29, INFO, Crew egress')
...     {'when': datetime.datetime(1969, 7, 24, 17, 29),
...      'level': 'INFO',
...      'message': 'Crew egress'}
...     """
...     d, t, lvl, msg = line.strip().split(', ', maxsplit=3)
...     d = date.fromisoformat(d)
...     t = time.fromisoformat(t)
...     dt = datetime.combine(d,t)
...     return {'when':dt, 'level':lvl, 'message':msg}


References
----------
.. [#WikipediaFunc] Functional programming. Retrieved: 2020-10-09. URL: https://en.wikipedia.org/wiki/Functional_programming
.. [#Hudak1989] Hudak, Paul. "Conception, evolution, and application of functional programming languages". ACM Computing Surveys. 21 (3): 359–411. doi:10.1145/72551.72554. S2CID 207637854. 1989.
.. [#Hughes1984] Hughes, John. "Why Functional Programming Matters". Chalmers University of Technology. 1984.
.. [#Spiewak2008] Spiewak, Daniel. "Implementing Persistent Vectors in Scala". Code Commit. 2008.
.. [#Paulson1996] Paulson, Larry C. "ML for the Working Programmer". Cambridge University Press. ISBN: 978-0-521-56543-1. Retrieved: 2013-02-10. 1996.
.. [#Inouye2022] Inouye, Jenna. "Functional Programming Languages: Concepts & Advantages". Year: 2022. Retrieved: 2022-07-28, URL: https://hackr.io/blog/functional-programming
