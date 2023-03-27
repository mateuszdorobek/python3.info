Regex Syntax Use Cases
======================


National Identification Numbers
-------------------------------
* Worldwide
* https://github.com/arthurdejong/python-stdnum/tree/master/stdnum/pl

>>> def pesel_check_digit(self):
...     weights = (1, 3, 7, 9, 1, 3, 7, 9, 1, 3)
...     check = sum(w * int(n) for w, n in zip(weights, self.pesel))
...     return str((10 - check) % 10)

.. figure:: img/regex-dowodosobisty-new-1.jpg

.. figure:: img/regex-dowodosobisty-prl-1.jpg
.. figure:: img/regex-dowodosobisty-prl-2.jpg
.. figure:: img/regex-dowodosobisty-prl-3.jpg

.. figure:: img/regex-dowodosobisty-old-1.jpg
.. figure:: img/regex-dowodosobisty-old-2.jpg
.. figure:: img/regex-dowodosobisty-old-3.jpg


Dates
-----
ISO Date:

>>> pattern = r'^\d{4}-\d{2}-\d{2}$'

US Long Date:

>>> pattern = r'^\w+ \d{2}, \d{4}$'

US Short Date:

>>> pattern = r'^\d{2}/\d{2}/\d{2}$'


Email
-----
* [#rfc3696]_

>>> pattern = r'^[a-zA-Z0-9][\w.+-]*@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]{2,20}$'

W3C HTML5 Standard [#w3cemailregex]_ regexp for email field

>>> pattern = r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$"


URL
---
W3C standard for URL understanding

.. code-block:: text

    ^(?=[^&])(?:(?<scheme>[^:/?#]+):)?(?://(?<authority>[^/?#]*))?
    (?<path>[^?#]*)(?:\?(?<query>[^#]*))?(?:#(?<fragment>.*))?

>>> scheme = r'(?:(?<scheme>[^:/?#]+):)?'
>>> authority = r'(?://(?<authority>[^/?#]*))?'
>>> path = r'(?<path>[^?#]*)'
>>> query = r'(?:\?(?<query>[^#]*))?'
>>> fragment = r'(?:#(?<fragment>.*))?'
>>>
>>> pattern = f'^(?=[^&]){scheme}{authority}{path}{query}{fragment}'
>>>
>>> print(pattern)
^(?=[^&])(?:(?<scheme>[^:/?#]+):)?(?://(?<authority>[^/?#]*))?(?<path>[^?#]*)(?:\?(?<query>[^#]*))?(?:#(?<fragment>.*))?

W3C standard for URL parsing

.. code-block:: text

    /^\s*[a-z](?:[-a-z0-9\+\.])*:(?:\/\/(?:(?:%[0-9a-f][0-9a-f]|[-a-z0-9\._~
    \uA0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF\u10000-\u1FFFD\u20000-\u2FFFD\u30000-
    \u3FFFD\u40000-\u4FFFD\u50000-\u5FFFD\u60000-\u6FFFD\u70000-\u7FFFD\u80000-
    \u8FFFD\u90000-\u9FFFD\uA0000-\uAFFFD\uB0000-\uBFFFD\uC0000-\uCFFFD\uD0000-
    \uDFFFD\uE1000-\uEFFFD!\$&\'\(\)\*\+,;=:])*@)?(?:\[(?:(?:(?:[0-9a-f]{1,4}:)
    {6}(?:[0-9a-f]{1,4}:[0-9a-f]{1,4}|(?:[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4]
    [0-9]|25[0-5])(?:\.(?:[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])){3}
    )|::(?:[0-9a-f]{1,4}:){5}(?:[0-9a-f]{1,4}:[0-9a-f]{1,4}|(?:[0-9]|[1-9][0-9]
    |1[0-9][0-9]|2[0-4][0-9]|25[0-5])(?:\.(?:[0-9]|[1-9][0-9]|1[0-9][0-9]|2
    [0-4][0-9]|25[0-5])){3})|(?:[0-9a-f]{1,4})?::(?:[0-9a-f]{1,4}:){4}
    (?:[0-9a-f]{1,4}:[0-9a-f]{1,4}|(?:[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]
    |25[0-5])(?:\.(?:[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])){3})|
    (?:[0-9a-f]{1,4}:[0-9a-f]{1,4})?::(?:[0-9a-f]{1,4}:){3}(?:[0-9a-f]{1,4}:
    [0-9a-f]{1,4}|(?:[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(?:\.
    (?:[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])){3})|(?:(?:[0-9a-f]
    {1,4}:){0,2}[0-9a-f]{1,4})?::(?:[0-9a-f]{1,4}:){2}(?:[0-9a-f]{1,4}:[0-9a-f]
    {1,4}|(?:[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(?:\.(?:[0-9]|
    [1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])){3})|(?:(?:[0-9a-f]{1,4}:){0,3}
    [0-9a-f]{1,4})?::[0-9a-f]{1,4}:(?:[0-9a-f]{1,4}:[0-9a-f]{1,4}|(?:[0-9]|
    [1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(?:\.(?:[0-9]|[1-9][0-9]|1[0-9]
    [0-9]|2[0-4][0-9]|25[0-5])){3})|(?:(?:[0-9a-f]{1,4}:){0,4}[0-9a-f]{1,4})?::
    (?:[0-9a-f]{1,4}:[0-9a-f]{1,4}|(?:[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|
    25[0-5])(?:\.(?:[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])){3})|
    (?:(?:[0-9a-f]{1,4}:){0,5}[0-9a-f]{1,4})?::[0-9a-f]{1,4}|(?:(?:[0-9a-f]
    {1,4}:){0,6}[0-9a-f]{1,4})?::)|v[0-9a-f]+[-a-z0-9\._~!\$&\'\(\)\*\+,;
    =:]+)\]|(?:[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(?:\.
    (?:[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])){3}|
    (?:%[0-9a-f][0-9a-f]|[-a-z0-9\
    ._~\uA0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF\u10000-\u1FFFD\u20000-\u2FFFD
    \u30000-\u3FFFD\u40000-\u4FFFD\u50000-\u5FFFD\u60000-\u6FFFD\u70000-\u7FFFD
    \u80000-\u8FFFD\u90000-\u9FFFD\uA0000-\uAFFFD\uB0000-\uBFFFD\uC0000-\uCFFFD
    \uD0000-\uDFFFD\uE1000-\uEFFFD!\$&\'\(\)\*\+,;=@])*)(?::[0-9]*)?(?:\/(?:
    (?:%[0-9a-f][0-9a-f]|[-a-z0-9\
    ._~\uA0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF\u10000-\u1FFFD\u20000-\u2FFFD
    \u30000-\u3FFFD\u40000-\u4FFFD\u50000-\u5FFFD\u60000-\u6FFFD\u70000-\u7FFFD
    \u80000-\u8FFFD\u90000-\u9FFFD\uA0000-\uAFFFD\uB0000-\uBFFFD\uC0000-\uCFFFD
    \uD0000-\uDFFFD\uE1000-\uEFFFD!\$&\'\(\)\*\+,;=:@]))*)*|\/(?:(?:(?:
    (?:%[0-9a-f][0-9a-f]|[-a-z0-9\
    ._~\uA0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF\u10000-\u1FFFD\u20000-\u2FFFD
    \u30000-\u3FFFD\u40000-\u4FFFD\u50000-\u5FFFD\u60000-\u6FFFD\u70000-\u7FFFD
    \u80000-\u8FFFD\u90000-\u9FFFD\uA0000-\uAFFFD\uB0000-\uBFFFD\uC0000-\uCFFFD
    \uD0000-\uDFFFD\uE1000-\uEFFFD!\$&\'\(\)\*\+,;=:@]))+)(?:\/(?:
    (?:%[0-9a-f][0-9a-f]|[-a-z0-9\
    ._~\uA0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF\u10000-\u1FFFD\u20000-\u2FFFD
    \u30000-\u3FFFD\u40000-\u4FFFD\u50000-\u5FFFD\u60000-\u6FFFD\u70000-\u7FFFD
    \u80000-\u8FFFD\u90000-\u9FFFD\uA0000-\uAFFFD\uB0000-\uBFFFD\uC0000-\uCFFFD
    \uD0000-\uDFFFD\uE1000-\uEFFFD!\$&\'\(\)\*\+,;=:@]))*)*)?|(?:(?:
    (?:%[0-9a-f][0-9a-f]|[-a-z0-9\
    ._~\uA0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF\u10000-\u1FFFD\u20000-\u2FFFD
    \u30000-\u3FFFD\u40000-\u4FFFD\u50000-\u5FFFD\u60000-\u6FFFD\u70000-\u7FFFD
    \u80000-\u8FFFD\u90000-\u9FFFD\uA0000-\uAFFFD\uB0000-\uBFFFD\uC0000-\uCFFFD
    \uD0000-\uDFFFD\uE1000-\uEFFFD!\$&\'\(\)\*\+,;=:@]))+)(?:\/(?:
    (?:%[0-9a-f][0-9a-f]|[-a-z0-9\
    ._~\uA0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF\u10000-\u1FFFD\u20000-\u2FFFD
    \u30000-\u3FFFD\u40000-\u4FFFD\u50000-\u5FFFD\u60000-\u6FFFD\u70000-\u7FFFD
    \u80000-\u8FFFD\u90000-\u9FFFD\uA0000-\uAFFFD\uB0000-\uBFFFD\uC0000-\uCFFFD
    \uD0000-\uDFFFD\uE1000-\uEFFFD!\$&\'\(\)\*\+,;=:@]))*)*|(?!
    (?:%[0-9a-f][0-9a-f]|[-a-z0-9\
    ._~\uA0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF\u10000-\u1FFFD\u20000-\u2FFFD
    \u30000-\u3FFFD\u40000-\u4FFFD\u50000-\u5FFFD\u60000-\u6FFFD\u70000-\u7FFFD
    \u80000-\u8FFFD\u90000-\u9FFFD\uA0000-\uAFFFD\uB0000-\uBFFFD\uC0000-\uCFFFD
    \uD0000-\uDFFFD\uE1000-\uEFFFD!\$&\'\(\)\*\+,;=:@])))(?:\?(?:
    (?:%[0-9a-f][0-9a-f]|[-a-z0-9\
    ._~\uA0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF\u10000-\u1FFFD\u20000-\u2FFFD
    \u30000-\u3FFFD\u40000-\u4FFFD\u50000-\u5FFFD\u60000-\u6FFFD\u70000-\u7FFFD
    \u80000-\u8FFFD\u90000-\u9FFFD\uA0000-\uAFFFD\uB0000-\uBFFFD\uC0000-\uCFFFD
    \uD0000-\uDFFFD\uE1000-\uEFFFD!\$&\'\(\)\*\+,;=:@])
    |[\uE000-\uF8FF\uF0000-\uFFFFD|\u100000-\u10FFFD\/\?])*)?(?:\#(?:
    (?:%[0-9a-f][0-9a-f]|[-a-z0-9\
    ._~\uA0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF\u10000-\u1FFFD\u20000-\u2FFFD
    \u30000-\u3FFFD\u40000-\u4FFFD\u50000-\u5FFFD\u60000-\u6FFFD\u70000-\u7FFFD
    \u80000-\u8FFFD\u90000-\u9FFFD\uA0000-\uAFFFD\uB0000-\uBFFFD\uC0000-\uCFFFD
    \uD0000-\uDFFFD\uE1000-\uEFFFD!\$&\'\(\)\*\+,;=:@])|[\/\?])*)?\s*$/i


Parsing URLs
------------
* Source [#W3CParsingURLs]_

To parse a *URL* url into its component parts, the user agent must use the
following steps:

#. Strip leading and trailing space characters from url.
#. Parse url in the manner defined by :RFC:`3986`, with the following
   exceptions:

    * Add all characters with code points less than or equal to
      ``U+0020`` or greater than or equal to ``U+007F`` to the
      ``<unreserved>`` production.

    * Add the characters ``U+0022``, ``U+003C``, ``U+003E``, ``U+005B`` ...
      ``U+005E``, ``U+0060``, and ``U+007B`` ... ``U+007D`` to the
      ``<unreserved>`` production

    * Add a single ``U+0025`` *PERCENT SIGN* character as a second
      alternative way of matching the ``<pct-encoded>`` production, except
      when the ``<pct-encoded>`` is used in the ``<reg-name>`` production.

    * Add the ``U+0023`` *NUMBER SIGN* character to the characters allowed
      in the ``<fragment>`` production.

#. If url doesn't match the ``<URI-reference>`` production, even after the
   above changes are made to the *ABNF* definitions, then parsing the *URL*
   fails with an error. [:RFC:`3986`] Otherwise, parsing url was successful;
   the components of the *URL* are substrings of url defined as follows:

.. glossary::

    scheme
        The substring matched by the ``<scheme>`` production, if any.

    host
        The substring matched by the ``<host>`` production, if any.

    port
        The substring matched by the ``<port>`` production, if any.

    hostport
        If there is a ``<scheme>`` component and a ``<port>`` component and
        the port given by the ``<port>`` component is different than the
        default port defined for the protocol given by the ``<scheme>``
        component, then ``<hostport>`` is the substring that starts with the
        substring matched by the ``<host>`` production and ends with the
        substring matched by the ``<port>`` production, and includes the
        colon in between the two. Otherwise, it is the same as the
        ``<host>`` component.

    path
        The substring matched by one of the following productions, if one of
        them was matched:

    path-abempty
    path-absolute
    path-noscheme
    path-rootless
    path-empty
    query
        The substring matched by the ``<query>`` production, if any.

    fragment
        The substring matched by the ``<fragment>`` production, if any.

    host-specific
        The substring that follows the substring matched by the <authority>
        production, or the whole string if the ``<authority>`` production
        wasn't matched.


References
----------
.. [#rfc3696] RFC 3696. Year: 2019. Retrieved: 2019-03-13. URL: https://datatracker.ietf.org/doc/html/rfc3696#section-3
.. [#w3cemailregex] W3C. Parsing Email. Year: 2019. Retrieved: 2019-03-13. URL: https://html.spec.whatwg.org/multipage/input.html#valid-e-mail-address
.. [#W3CParsingURLs] W3C. Parsing URLs. Year: 2019. Retrieved: 2019-03-13. URL: https://dev.w3.org/html5/spec-LC/urls.html#parsing-urls


Assignments
-----------
.. literalinclude:: assignments/re_standards_a.py
    :caption: :download:`Solution <assignments/re_standards_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/re_standards_b.py
    :caption: :download:`Solution <assignments/re_standards_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/re_standards_c.py
    :caption: :download:`Solution <assignments/re_standards_c.py>`
    :end-before: # Solution
