HTTP Status
===========
* ``1XX`` - Informational
* ``2XX`` - Successful
* ``3XX`` - Redirection
* ``4XX`` - Client Error
* ``5XX`` - Server Error


``1xx`` Informational response
------------------------------
* ``100`` - Continue
* ``101`` - Switching Protocols
* ``102`` - Processing (WebDAV)
* ``103`` - Early Hints


``2xx`` Success
---------------
* ``200`` - OK
* ``201`` - Created
* ``202`` - Accepted
* ``203`` - Non-Authoritative Information
* ``204`` - No Content
* ``205`` - Reset Content
* ``206`` - Partial Content
* ``207`` - Multi-Status (WebDAV)
* ``208`` - Already Reported (WebDAV)
* ``209`` - IM Used


``3xx`` Redirection
-------------------
* ``300`` - Multiple Choices
* ``301`` - Moved Permanently
* ``302`` - Found (Previously 'Moved temporarily')
* ``303`` - See Other
* ``304`` - Not Modified
* ``305`` - Use Proxy
* ``306`` - Switch Proxy
* ``307`` - Temporary Redirect
* ``308`` - Permanent Redirect


``4xx`` Client errors
---------------------
* ``400`` - Bad Request
* ``401`` - Unauthorized
* ``402`` - Payment Required
* ``403`` - Forbidden
* ``404`` - Not Found
* ``405`` - Method Not Allowed
* ``406`` - Not Acceptable
* ``407`` - Proxy Authentication Required
* ``408`` - Request Timeout
* ``409`` - Conflict
* ``410`` - Gone
* ``411`` - Length Required
* ``412`` - Precondition Failed
* ``413`` - Payload Too Large
* ``414`` - URI Too Long
* ``415`` - Unsupported Media Type
* ``416`` - Range Not Satisfiable
* ``417`` - Expectation Failed
* ``418`` - I'm a teapot - This code was defined in 1998 as one of the traditional IETF April Fools' jokes, in RFC 2324
* ``421`` - Misdirected Request
* ``422`` - Unprocessable Entity (WebDAV)
* ``423`` - Locked (WebDAV)
* ``424`` - Failed Dependency (WebDAV)
* ``426`` - Upgrade Required
* ``428`` - Precondition Required
* ``429`` - Too Many Requests
* ``431`` - Request Header Fields Too Large
* ``451`` - Unavailable For Legal Reasons


``5xx`` Server errors
---------------------
* ``500`` - Internal Server Error
* ``501`` - Not Implemented
* ``502`` - Bad Gateway
* ``503`` - Service Unavailable
* ``504`` - Gateway Timeout
* ``505`` - HTTP Version Not Supported
* ``506`` - Variant Also Negotiates
* ``507`` - Insufficient Storage (WebDAV)
* ``508`` - Loop Detected (WebDAV)
* ``510`` - Not Extended
* ``511`` - Network Authentication Required


Built-in Match
--------------
* HTTP Status

>>> status = 404
>>>
>>> match status:
...     case 400:             reason = 'Bad request'
...     case 401 | 403 | 405: reason = 'Not allowed'
...     case 404:             reason = 'Not found'
...     case 418:             reason = "I'm a teapot"
...     case _:               reason = 'Unexpected status'
>>>
>>>
>>> print(reason)
Not found


Custom Enum
-----------
* ``from enum import Enum``

>>> from enum import Enum
>>>
>>>
>>> class HTTPStatus(Enum):
...     OK = 200
...     CREATED = 201
...     BAD_REQUEST = 400
...     NOT_FOUND = 404
...     INTERNAL_ERROR = 500
>>>
>>>
>>> status = 404
>>>
>>> match HTTPStatus(status):
...     case HTTPStatus.BAD_REQUEST:    response = 'Bad request'
...     case HTTPStatus.NOT_FOUND:      response = 'Not found'
...     case HTTPStatus.INTERNAL_ERROR: response = 'Internal Server Error'
...     case _:                         response = 'Unexpected status'
>>>
>>>
>>> print(response)
Not found


Built-in Enum
-------------
* ``from http import HTTPStatus``

>>> from http import HTTPStatus
>>>
>>>
>>> HTTPStatus(200).name
'OK'
>>>
>>> HTTPStatus(404).name
'NOT_FOUND'
>>>
>>> HTTPStatus(500).name
'INTERNAL_SERVER_ERROR'
>>>
>>> HTTPStatus(418).name
'IM_A_TEAPOT'

Using statuses:

.. code-block:: python

    from http import HTTPStatus

    HTTPStatus.OK
    HTTPStatus.OK == 200

    HTTPStatus.OK.value
    HTTPStatus.OK.phrase
    HTTPStatus.OK.description

    list(HTTPStatus)

Most common statuses:

.. code-block:: python

    from http import HTTPStatus


    HTTPStatus.OK                       # 200
    HTTPStatus.CREATED                  # 201
    HTTPStatus.MOVED_PERMANENTLY        # 301
    HTTPStatus.FOUND                    # 302
    HTTPStatus.BAD_REQUEST              # 400
    HTTPStatus.UNAUTHORIZED             # 401
    HTTPStatus.FORBIDDEN                # 403
    HTTPStatus.METHOD_NOT_ALLOWED       # 405
    HTTPStatus.NOT_FOUND                # 404
    HTTPStatus.INTERNAL_SERVER_ERROR    # 500
