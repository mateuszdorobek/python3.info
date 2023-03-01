"""
* Assignment: RE Find Dates
* Complexity: easy
* Lines of code: 2 lines
* Time: 5 min

English:
    1. Using regular expressions find dates in:
       US long format, i.e. "April 12, 1961"
    2. Run doctests - all must succeed

Polish:
    1. Używając wyrażeń regularnych wyszukaj dat w:
       formacie amerykańskim długim np. "April 12, 1961"
    2. Uruchom doctesty - wszystkie muszą się powieść

References:
    [1] Wikipedia Apollo 11,
        URL: https://en.wikipedia.org/wiki/Apollo_11
        Year: 2019
        Retrieved: 2019-12-14

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    ['October 4, 1957',
     'April 12, 1961',
     'May 5, 1961',
     'May 25, 1961',
     'September 12, 1962',
     'September 12, 1962']
"""

import re


TEXT = ("In the late 1950s and early 1960s, the United States was engaged in "
        "the Cold War, a geopolitical rivalry with the Soviet Union. On "
        "October 4, 1957, the Soviet Union launched Sputnik 1, the first "
        "artificial satellite. This surprise success fired fears and "
        "imaginations around the world. It demonstrated that the Soviet Union "
        "had the capability to deliver nuclear weapons over intercontinental "
        "distances, and challenged American claims of military, economic and "
        "technological superiority. This precipitated the Sputnik crisis, "
        "and triggered the Space Race. President Dwight D. Eisenhower "
        "responded to the Sputnik challenge by creating the National "
        "Aeronautics and Space Administration (NASA), and initiating Project "
        "Mercury, which aimed to launch a man into Earth orbit. But on April "
        "12, 1961, Soviet cosmonaut Yuri Gagarin became the first person in "
        "space, and the first to orbit the Earth. Nearly a month later, "
        "on May 5, 1961, Alan Shepard became the first American in space, "
        "completing a 15-minute suborbital journey. After being recovered "
        "from the Atlantic Ocean, he received a congratulatory telephone call "
        "from Eisenhower's successor, John F. Kennedy. Since the Soviet Union "
        "had higher lift capacity launch vehicles, Kennedy chose, from among "
        "options presented by NASA, a challenge beyond the capacity of the "
        "existing generation of rocketry, so that the US and Soviet Union "
        "would be starting from a position of equality. A crewed mission to "
        "the Moon would serve this purpose. On May 25, 1961, Kennedy "
        "addressed the United States Congress on \"Urgent National Needs\" "
        "and declared: I believe that this nation should commit itself to "
        "achieving the goal, before this decade [1960s] is out, of landing a "
        "man on the Moon and returning him safely to the Earth. No single "
        "space project in this period will be more impressive to mankind, "
        "or more important for the long-range exploration of space; and none "
        "will be so difficult or expensive to accomplish. We propose to "
        "accelerate the development of the appropriate lunar space craft. We "
        "propose to develop alternate liquid and solid fuel boosters, "
        "much larger than any now being developed, until certain which is "
        "superior. We propose additional funds for other engine development "
        "and for unmanned explorations—explorations which are particularly "
        "important for one purpose which this nation will never overlook: the "
        "survival of the man who first makes this daring flight. But in a "
        "very real sense, it will not be one man going to the Moon—if we make "
        "this judgment affirmatively, it will be an entire nation. For all of "
        "us must work to put him there. — Kennedy's speech to Congress On "
        "September 12, 1962, Kennedy delivered another speech before a crowd "
        "of about 40,000 people in the Rice University football stadium in "
        "Houston, Texas. A widely quoted refrain from the middle portion of "
        "the speech reads as follows: Kennedy, in a blue suit and tie, "
        "speaks at a wooden podium bearing the seal of the President of the "
        "United States. Vice President Lyndon Johnson and other dignitaries "
        "stand behind him. President John F. Kennedy speaking at Rice "
        "University on September 12, 1962 There is no strife, no prejudice, "
        "no national conflict in outer space as yet. Its hazards are hostile "
        "to us all. Its conquest deserves the best of all mankind, and its "
        "opportunity for peaceful cooperation may never come again. But why, "
        "some say, the Moon? Why choose this as our goal? And they may well "
        "ask, why climb the highest mountain? Why, 35 years ago, fly the "
        "Atlantic? Why does Rice play Texas? We choose to go to the Moon! We "
        "choose to go to the Moon ... We choose to go to the Moon in this "
        "decade and do the other things, not because they are easy, "
        "but because they are hard; because that goal will serve to organize "
        "and measure the best of our energies and skills, because that "
        "challenge is one that we are willing to accept, one we are unwilling "
        "to postpone, and one we intend to win, and the others, too.")


# Use re.findall() to get dates in US format, i.e. "April 12, 1961"
# type: list[str]
result = ...


# Solution
pattern = r'[A-Z][a-z]+ [0-9]{1,2}, [0-9]{4}'
result = re.findall(pattern, TEXT)
