HTTP MIME Types
===============
* type/subtype
* ``text`` - Represents any document that contains text and is theoretically human readable
* ``image`` - Represents any kind of images. Videos are not included, though animated images (like animated gif) are described with an image type
* ``audio`` - Represents any kind of audio files
* ``video`` - Represents any kind of video files
* ``application`` - Represents any kind of binary data
* ``multipart``

Multipurpose Internet Mail Extensions (MIME) is an Internet standard that
extends the format of email messages to support text in character sets other
than ASCII, as well as attachments of audio, video, images, and application
programs. Message bodies may consist of multiple parts, and header
information may be specified in non-ASCII character sets. Email messages
with MIME formatting are typically transmitted with standard protocols,
such as the Simple Mail Transfer Protocol (SMTP), the Post Office Protocol
(POP), and the Internet Message Access Protocol (IMAP).

The MIME standard is specified in a series of requests for comments:
RFC 2045, RFC 2046, RFC 2047, RFC 4288, RFC 4289 and RFC 2049. The
integration with SMTP email is specified in RFC 1521 and RFC 1522.

Although the MIME formalism was designed mainly for SMTP, its content types
are also important in other communication protocols. In the HyperText
Transfer Protocol (HTTP) for the World Wide Web, servers insert a MIME
header field at the beginning of any Web transmission. Clients use the
content type or media type header to select an appropriate viewer
application for the type of data indicated. [#WikipediaMIME]_

.. code-block:: text

    MIME-Version: 1.0

.. code-block:: text

    Content-Type: text/plain

.. code-block:: text

    Content-Disposition: attachment; filename=genome.jpeg;
      modification-date="Wed, 12 Feb 1997 16:29:51 -0500";

.. code-block:: text

    MIME-Version: 1.0
    Content-Type: multipart/mixed; boundary=frontier

    This is a message with multiple parts in MIME format.
    --frontier
    Content-Type: text/plain

    This is the body of the message.
    --frontier
    Content-Type: application/octet-stream
    Content-Transfer-Encoding: base64

    PGh0bWw+CiAgPGhlYWQ+CiAgPC9oZWFkPgogIDxib2R5PgogICAgPHA+VGhpcyBpcyB0aGUg
    Ym9keSBvZiB0aGUgbWVzc2FnZS48L3A+CiAgPC9ib2R5Pgo8L2h0bWw+Cg==
    --frontier--


Html, xhtml, xml, html5
-----------------------
* HTML5 = html = living standard

XML has

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8"?>
    <crew>
        <astronaut firstname="Mark" lastname="Watney" />
        <astronaut firstname="Melissa" lastname="Lewis" />
        <astronaut>
            <firstname>Mark</firstname>
            <lastname>Watney</lastname>
        </astronaut>
    </crew>

.. code-block:: xml

    <html>
        <head>
            <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        </head>
        <body>
            <h1>hello</h1>
            <p>hello world</p>
            <p>hello world</p>
            <img src="..." />
            <br />
        </body>
    <html>

.. code-block:: html

    <html>
        <body>
            <h1>hello</h1>
            <p>hello world
            <p>hello world
            <img src="...">
            <br>
        </body>
    </html>

.. code-block:: html

    <html>
        <head>
            <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        </head>
        <body>
        </body>
    </html>

.. code-block:: html

    <!DOCTYPE html>
    <html>
        <head>
            <meta charset="utf-8" />
        </head>
        <body>
        </body>
    </html>


Text Types
----------
* ``text/plain``
* ``text/html``
* ``text/css``


Application Types
-----------------
* ``application/json``
* ``application/javascript``
* ``application/ecmascript``
* ``application/octet-stream`` - As it really means unknown binary
* ``application/pkcs12``
* ``application/vnd.mspowerpoint``
* ``application/xhtml+xml``
* ``application/xml``
* ``application/pdf``
* ``application/ogg`` - An audio or video file using the OGG container format. Theora is the usual video codec used within it; Vorbis is the usual audio code
* ``application/*``


Multipart Types
---------------
* ``multipart/form-data``
* ``multipart/byteranges``


Image Types
-----------
* ``image/gif`` - GIF images (lossless compression, superseded by PNG)
* ``image/jpeg`` - JPEG images
* ``image/png`` - PNG images
* ``image/svg+xml`` - SVG images (vector images)
* ``image/x-icon`` - Windows icons
* ``image/bmp``
* ``image/webp``
* ``image/vnd.microsoft.icon``


Audio Types
-----------
* ``audio/wave``
* ``audio/wav``
* ``audio/x-wav``
* ``audio/x-pn-wav`` - An audio file in the WAVE container format. The PCM audio codec (WAVE codec '1') is often supported, but other codecs have more limited support (if any)
* ``audio/webm`` - An audio file in the WebM container format. Vorbis and Opus are the most common audio codecs
* ``audio/ogg`` - An audio file in the OGG container format. Vorbis is the most common audio codec used in such a container
* ``audio/midi``
* ``audio/mpeg``
* ``audio/*``


Video Types
-----------
* ``video/mp4``
* ``video/webm`` - A video file, possibly with audio, in the WebM container format. VP8 and VP9 are the most common video codecs used within it; Vorbis and Opus the most common audio codecs
* ``video/ogg`` - A video file, possibly with audio, in the OGG container format. Theora is the usual video codec used within it; Vorbis is the usual audio codec


Further Reading
---------------
* ``RFC 1426`` - SMTP Service Extension for 8bit-MIMEtransport. J. Klensin, N. Freed, M. Rose, E. Stefferud, D. Crocker. February 1993.
* ``RFC 1847`` - Security Multiparts for MIME: Multipart/Signed and Multipart/Encrypted
* ``RFC 3156`` - MIME Security with OpenPGP
* ``RFC 2045`` - MIME Part One: Format of Internet Message Bodies
* ``RFC 2046`` - MIME Part Two: Media Types. N. Freed, Nathaniel Borenstein. November 1996.
* ``RFC 2047`` - MIME Part Three: Message Header Extensions for Non-ASCII Text. Keith Moore. November 1996.
* ``RFC 4288`` - MIME Part Four: Media Type Specifications and Registration Procedures.
* ``RFC 4289`` - MIME Part Four: Registration Procedures. N. Freed, J. Klensin. December 2005.
* ``RFC 2049`` - MIME Part Five: Conformance Criteria and Examples. N. Freed, N. Borenstein. November 1996.
* ``RFC 2183`` - Communicating Presentation Information in Internet Messages: The Content-Disposition Header Field. Troost, R., Dorner, S. and K. Moore. August 1997.
* ``RFC 2231`` - MIME Parameter Value and Encoded Word Extensions: Character Sets, Languages, and Continuations. N. Freed, K. Moore. November 1997.
* ``RFC 2387`` - The MIME Multipart/Related Content-type
* ``RFC 1521`` - Mechanisms for Specifying and Describing the Format of Internet Message Bodies


References
----------
.. [#WikipediaMIME] https://en.wikipedia.org/wiki/MIME
