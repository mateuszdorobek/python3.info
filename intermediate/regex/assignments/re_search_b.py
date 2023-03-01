"""
* Assignment: RE Search Moon Speech
* Complexity: easy
* Lines of code: 5 lines
* Time: 8 min

English:
    1. Use `re.search()` to find in text [1]
    2. Define `result: str` containing paragraph starting with 'We choose to go to the moon'
    3. Run doctests - all must succeed

Polish:
    1. Użyj `re.search()` do znalezienia w tekscie [1]
    2. Zdefiniuj `result: str` zawierający tekst paragrafu zaczynający się od słów "We choose to go to the moon"
    3. Uruchom doctesty - wszystkie muszą się powieść

References:
    [1] Kennedy, J.F. Moon Speech - Rice Stadium,
        URL: http://er.jsc.nasa.gov/seh/ricetalk.htm
        Year: 2019
        Retrieved: 2019-12-14

Hints:
    * All HTML paragraphs starts with `<p>` and ends with `</p>`
    * In real life paragraphs parsing is more complex

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert type(result) is str, 'result must be a str'
    >>> assert not result.startswith('<p>'), 'result cannot start with <p>'
    >>> assert not result.endswith('</p>'), 'result cannot end with </p>'

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    'We choose to go to the moon. We choose to go to the moon in this decade
     and do the other things, not because they are easy, but because they are
     hard, because that goal will serve to organize and measure the best of our
     energies and skills,because that challenge is one that we are willing to
     accept, one we are unwilling to postpone, and one which we intend to win,
     and the others, too.'
"""

import re


TEXT = ("<h1>TEXT OF PRESIDENT JOHN KENNEDY'S RICE STADIUM MOON SPEECH</h1>\n"
        "<p>President Pitzer, Mr. Vice President, Governor, "
        "CongressmanThomas, Senator Wiley, and Congressman Miller, Mr. Webb, "
        "Mr.Bell, scientists, distinguished guests, and ladies and "
        "gentlemen:</p><p>We choose to go to the moon. We choose to go to "
        "the moon in this decade and do the other things, not because they "
        "are easy, but because they are hard, because that goal will serve "
        "to organize and measure the best of our energies and skills,because "
        "that challenge is one that we are willing to accept, one we are "
        "unwilling to postpone, and one which we intend to win, and the "
        "others, too.</p><p>It is for these reasons that I regard the "
        "decision last year to shift our efforts in space from low to high "
        "gear as among the most important decisions that will be made during "
        "my incumbency in the office of the Presidency.</p><p>In the last 24 "
        "hours we have seen facilities now being created for the greatest "
        "and most complex exploration in man's history.We have felt the "
        "ground shake and the air shattered by the testing of a Saturn C-1 "
        "booster rocket, many times as powerful as the Atlas which launched "
        "John Glenn, generating power equivalent to 10,000 automobiles with "
        "their accelerators on the floor.We have seen the site where the F-1 "
        "rocket engines, each one as powerful as all eight engines of the "
        "Saturn combined, will be clustered together to make the advanced "
        "Saturn missile, assembled in a new building to be built at Cape "
        "Canaveral as tall as a48 story structure, as wide as a city block, "
        "and as long as two lengths of this field.</p>")


# use re.search() to get paragraph starting with "We choose..."
# use .group(1) to get the value from re.Match object
# type: str
result = ...


# Solution
pattern = r'<p>(We choose [a-zA-Z,. ]+)</p>'
result = re.search(pattern, TEXT).group(1)
