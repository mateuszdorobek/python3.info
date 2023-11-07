Dragon About
============
.. figure:: img/dragon.gif

    Firkraag dragon from game Baldur's Gate II: Shadows of Amn


**The task is a simulation of the software development process.**
The Dragon motive is just a narration for demonstration of the object-oriented
programming paradigm and good programming practices. We will not write
a game and we will not discuss game-dev specifics! However we will mention
a few issues related to the specificity of the games (e.g. that the dragon
breathes fire, etc.), but besides that the whole discussion will apply to
any type of IT projects and software engineering problems in virtually each
business domain.

**You - programmer, Trainer - Product Owner.**
In this task you will play the role of a software engineer (programmer),
and the Trainer will act as a Product Owner with little technical knowledge
- 10 years ago he was a programmer, and now he spends most of his time
in a spreadsheet and in meetings. Remember that Product Owner's technical
background influences on the way how he writes the acceptance criteria.
His software engineering career may cause that requirements will include
not only feature specification, but also suggestions on how to solve problems
or implement them. You have to filter it out from the content of the task.
Unfortunately, this is a very common scenario in the IT industry.

**A task is a specification of business requirements.**
It is not a technical documentation. The assignment describes "what should be",
not "how to do it". Mind that, because it's an important difference!

**The method of implementation is up to you.**
You can add additional fields, methods, functions, variables, constants,
classes, objects, unittest or doctest, type annotation - whatever
you want, but `don't use modules outside the standard library`.
The exceptions are test frameworks (``pytest``, ``hypothesis``, etc).

**The solution must meet the acceptance criteria.**
Remember that this is version `1.0` so do not add additional
unspecified functionalities (e.g. additional characters, game board
boundary checks, etc.). For this reason, you don't have to hold on
the order of points and sub-points in the assignment. You can also
solve problems in the different way from what's written.
You have full freedom.

**Product Owner will not advise you on architectural decisions.**
He won't tell you if it's better to do it in a certain way, or what will
be the impact on future if you apply certain solution. You have to make
decisions and bear their consequences, i.e. easy possibility to introduce
changes in future versions. You need to find a balance between fast
implementation functionality, ease of understanding and maintaining the code,
and no blocking yourself from making changes in the future. Remember about
TDD, YAGNI, DRY, KISS, SOLID, emerging architecture and over-engineering.

**Do not search for solutions or the content of the next parts.**
If you look ahead, you will spoil your fun and learning. This assignment
has incredible educational potential. Don't destroy it.

Good luck, have fun!

PS. There are no errors in the assignment (tested on more than 300 trainings)

Non-functional requirements:

    1. Commit and push your current state of repository
    2. In your directory create an empty directory ``dragon``
    3. In ``dragon`` directory create an empty file ``README.rst``
    4. Add file to the version control system (should be automatic)
    5. Commit with message: "Dragon: NAME", where ``NAME`` is your first name
    6. Push changes to the repository
    7. Write a solution to the assignment in ``dragon`` directory
    8. Upon completing add all files in ``dragon`` to repository
    9. Commit and push changes to the central repository (Github)
