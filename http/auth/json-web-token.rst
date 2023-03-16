Auth JSON Web Token
===================
* https://datatracker.ietf.org/doc/html/rfc7519
* https://jwt.io/
* JWT - JSON Web Token
* ``sub`` - subject - identifies the principal that is the subject of the JWT
* ``iss`` - issuer - claim identifies the principal that issued the JWT
* ``aud`` - Audience - identifies the recipients that the JWT is intended for
* ``exp`` - Expiration Time - identifies the expiration time on or after which the JWT MUST NOT be accepted for processing
* ``nbf`` - Not Before - identifies the time before which the JWT MUST NOT be accepted for processing
* ``iat`` - Issued At - identifies the time at which the JWT was issued
* ``jti`` - JWT ID - provides a unique identifier for the JWT
* ``scopes`` - set of permissions to a JWT token
* ``typ`` - Type - Header Parameter
* ``cty`` - Content Type - Header Parameter

.. code-block:: json

     {"iss":"joe",
      "exp":1300819380,
      "https://example.com/is_root":true}

Base64url encoding the octets of the UTF-8 representation of the JWT
   Claims Set yields this encoded JWS Payload (with line breaks for
   display purposes only):

.. code-block:: text

     eyJpc3MiOiJqb2UiLA0KICJleHAiOjEzMDA4MTkzODAsDQogImh0dHA6Ly9leGFt
     cGxlLmNvbS9pc19yb290Ijp0cnVlfQ

   The encoded JWS Signature is the empty string.

   Concatenating these encoded parts in this order with period ('.')
   characters between the parts yields this complete JWT (with line
   breaks for display purposes only):

.. code-block:: text

     eyJhbGciOiJub25lIn0
     .
     eyJpc3MiOiJqb2UiLA0KICJleHAiOjEzMDA4MTkzODAsDQogImh0dHA6Ly9leGFt
     cGxlLmNvbS9pc19yb290Ijp0cnVlfQ
     .

.. figure:: img/http-oauth2-jwt-sequence.png

    Source: [#Thiyagarajan2021]_

.. figure:: img/http-oauth2-jwt-components.png

    Source: [#Thiyagarajan2021]_

.. figure:: img/http-oauth2-jwt-signature.png

    Source: [#Thiyagarajan2021]_


Registered Claim Names
----------------------
The following Claim Names are registered in the IANA "JSON Web Token
Claims" registry established by Section 10.1.  None of the claims
defined below are intended to be mandatory to use or implement in all
cases, but rather they provide a starting point for a set of useful,
interoperable claims.  Applications using JWTs should define which
specific claims they use and when they are required or optional.  All
the names are short because a core goal of JWTs is for the
representation to be compact. [#rfc7519]_


"iss" (Issuer) Claim
--------------------
The "iss" (issuer) claim identifies the principal that issued the
JWT.  The processing of this claim is generally application specific.
The "iss" value is a case-sensitive string containing a StringOrURI
value.  Use of this claim is OPTIONAL. [#rfc7519]_


"sub" (Subject) Claim
---------------------
The "sub" (subject) claim identifies the principal that is the
subject of the JWT.  The claims in a JWT are normally statements
about the subject.  The subject value MUST either be scoped to be
locally unique in the context of the issuer or be globally unique.
The processing of this claim is generally application specific.  The
"sub" value is a case-sensitive string containing a StringOrURI
value.  Use of this claim is OPTIONAL. [#rfc7519]_

"aud" (Audience) Claim
----------------------
The "aud" (audience) claim identifies the recipients that the JWT is
intended for.  Each principal intended to process the JWT MUST
identify itself with a value in the audience claim.  If the principal
processing the claim does not identify itself with a value in the
"aud" claim when this claim is present, then the JWT MUST be
rejected.  In the general case, the "aud" value is an array of case-
sensitive strings, each containing a StringOrURI value.  In the
special case when the JWT has one audience, the "aud" value MAY be a
single case-sensitive string containing a StringOrURI value.  The
interpretation of audience values is generally application specific.
Use of this claim is OPTIONAL. [#rfc7519]_


"exp" (Expiration Time) Claim
-----------------------------
The "exp" (expiration time) claim identifies the expiration time on
or after which the JWT MUST NOT be accepted for processing.  The
processing of the "exp" claim requires that the current date/time
MUST be before the expiration date/time listed in the "exp" claim.
Implementers MAY provide for some small leeway, usually no more than
a few minutes, to account for clock skew.  Its value MUST be a number
containing a NumericDate value.  Use of this claim is OPTIONAL. [#rfc7519]_


"nbf" (Not Before) Claim
------------------------
The "nbf" (not before) claim identifies the time before which the JWT
MUST NOT be accepted for processing.  The processing of the "nbf"
claim requires that the current date/time MUST be after or equal to
the not-before date/time listed in the "nbf" claim.  Implementers MAY
provide for some small leeway, usually no more than a few minutes, to
account for clock skew.  Its value MUST be a number containing a
NumericDate value.  Use of this claim is OPTIONAL. [#rfc7519]_


"iat" (Issued At) Claim
------------------------
The "iat" (issued at) claim identifies the time at which the JWT was
issued.  This claim can be used to determine the age of the JWT.  Its
value MUST be a number containing a NumericDate value.  Use of this
claim is OPTIONAL. [#rfc7519]_


"jti" (JWT ID) Claim
--------------------
The "jti" (JWT ID) claim provides a unique identifier for the JWT.
The identifier value MUST be assigned in a manner that ensures that
there is a negligible probability that the same value will be
accidentally assigned to a different data object; if the application
uses multiple issuers, collisions MUST be prevented among values
produced by different issuers as well.  The "jti" claim can be used
to prevent the JWT from being replayed.  The "jti" value is a case-
sensitive string.  Use of this claim is OPTIONAL. [#rfc7519]_


JOSE Header
-----------
For a JWT object, the members of the JSON object represented by the
JOSE Header describe the cryptographic operations applied to the JWT
and optionally, additional properties of the JWT.  Depending upon
whether the JWT is a JWS or JWE, the corresponding rules for the JOSE
Header values apply.

This specification further specifies the use of the following Header
Parameters in both the cases where the JWT is a JWS and where it is a
JWE. [#rfc7519]_


"typ" (Type) Header Parameter
-----------------------------
The "typ" (type) Header Parameter defined by [JWS] and [JWE] is used
by JWT applications to declare the media type [IANA.MediaTypes] of
this complete JWT.  This is intended for use by the JWT application
when values that are not JWTs could also be present in an application
data structure that can contain a JWT object; the application can use
this value to disambiguate among the different kinds of objects that
might be present.  It will typically not be used by applications when
it is already known that the object is a JWT.  This parameter is
ignored by JWT implementations; any processing of this parameter is
performed by the JWT application.  If present, it is RECOMMENDED that
its value be "JWT" to indicate that this object is a JWT.  While
media type names are not case sensitive, it is RECOMMENDED that "JWT"
always be spelled using uppercase characters for compatibility with
legacy implementations.  Use of this Header Parameter is OPTIONAL. [#rfc7519]_


"cty" (Content Type) Header Parameter
-------------------------------------
The "cty" (content type) Header Parameter defined by [JWS] and [JWE]
is used by this specification to convey structural information about
the JWT.

In the normal case in which nested signing or encryption operations
are not employed, the use of this Header Parameter is NOT
RECOMMENDED.  In the case that nested signing or encryption is
employed, this Header Parameter MUST be present; in this case, the
value MUST be "JWT", to indicate that a Nested JWT is carried in this
JWT.  While media type names are not case sensitive, it is
RECOMMENDED that "JWT" always be spelled using uppercase characters
for compatibility with legacy implementations.  See Appendix A.2 for
an example of a Nested JWT. [#rfc7519]_


Install
-------
.. code-block:: console

    $ pip install 'python-jose[cryptography]' python-multipart


Further Reading
---------------
OWASP JWT security cheatsheet:

* https://cheatsheetseries.owasp.org/cheatsheets/JSON_Web_Token_for_Java_Cheat_Sheet.html
* https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html

Best practices:

* https://curity.io/resources/learn/jwt-best-practices/
* https://blog.logrocket.com/jwt-authentication-best-practices/

JWT attacker point of view:

* https://owasp.org/www-chapter-vancouver/assets/presentations/2020-01_Attacking_and_Securing_JWT.pdf
* https://owasp.org/www-chapter-belgium/assets/2021/2021-02-18/JWT-Security.pdf


References
----------
.. [#Thiyagarajan2021] Thiyagarajan, S. Python API Development - Comprehensive Course for Beginners. Year: 2021. Retrieved: 2022-03-26. URL: https://www.youtube.com/watch?v=0sOvCWFmrtA

.. [#rfc7519] Jones, M. et al. JSON Web Token (JWT). Year: 2015. Retrieved: 2022-03-28. URL: https://datatracker.ietf.org/doc/html/rfc7519
