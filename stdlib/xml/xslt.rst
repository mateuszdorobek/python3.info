XSLT
====
* Using ``lxml`` module


Use Case - 0x01
---------------
.. code-block:: python

    from io import StringIO
    from lxml.etree import XML, XSLT, parse


    TEMPLATE = """
        <xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
            <xsl:template match="/">

                <my_tag>
                    <xsl:value-of select="/outer/inner/text()" />
                </my_tag>

            </xsl:template>
        </xsl:stylesheet>
    """

    DATA = """
        <outer>
            <inner>Hello World</inner>
        </outer>
    """

    transform = XSLT(XML(TEMPLATE))
    data = parse(StringIO(DATA))
    result = transform(data)

    print(result)
    # <?xml version="1.0"?>
    # <my_tag>Hello World</my_tag>


Use Case - 0x02
---------------
.. code-block:: python

    from io import StringIO
    from lxml.etree import XML, XSLT, parse


    DATA = """
        <users>
            <user>
                <firstname>Mark</firstname>
                <lastname>Watney</lastname>
            </user>
            <user>
                <firstname>Melissa</firstname>
                <lastname>Lewis</lastname>
            </user>
        </users>
    """

    TEMPLATE = """
        <html xsl:version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
            <table>
                <thead>
                    <tr>
                        <th>First Name</th>
                        <th>Last Name</th>
                    </tr>
                </thead>
                <tbody>

                    <xsl:for-each select="users/user">
                        <tr>
                            <td><xsl:value-of select="firstname"/></td>
                            <td><xsl:value-of select="lastname"/></td>
                        </tr>
                    </xsl:for-each>

                </tbody>
            </table>
        </html>
    """

    transform = XSLT(XML(TEMPLATE))
    data = parse(StringIO(DATA))
    result = transform(data)

    print(result)
    # <html><table>
    # <thead><tr>
    # <th>First Name</th>
    # <th>Last Name</th>
    # </tr></thead>
    # <tbody>
    # <tr>
    # <td>Mark</td>
    # <td>Watney</td>
    # </tr>
    # <tr>
    # <td>Melissa</td>
    # <td>Lewis</td>
    # </tr>
    # </tbody>
    # </table></html>


Use Case - 0x03
---------------
.. code-block:: python

    from io import StringIO
    from lxml.etree import XML, XSLT, parse


    DATA = """
        <CATALOG>
            <PLANT>
                <COMMON>Bloodroot</COMMON>
                <BOTANICAL>Sanguinaria canadensis</BOTANICAL>
                <ZONE>4</ZONE>
                <LIGHT>Mostly Shady</LIGHT>
                <PRICE>$2.44</PRICE>
                <AVAILABILITY>031599</AVAILABILITY>
            </PLANT>
            <PLANT>
                <COMMON>Columbine</COMMON>
                <BOTANICAL>Aquilegia canadensis</BOTANICAL>
                <ZONE>3</ZONE>
                <LIGHT>Mostly Shady</LIGHT>
                <PRICE>$9.37</PRICE>
                <AVAILABILITY>030699</AVAILABILITY>
            </PLANT>
        </CATALOG>
    """

    TEMPLATE = """
        <html xsl:version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

        <style>
            body {font-family: Arial; font-size: 1em; background-color: #EEEEEE}
            div.title {background-color: teal; color: white; padding: 4px}
            div.description {margin-left:20px;margin-bottom:1em;font-size:10pt}
            span {font-weight: bold}
        </style>

        <body>

        <xsl:for-each select="CATALOG/PLANT">

            <div class="title">
                <span><xsl:value-of select="BOTANICAL"/></span>
                <xsl:value-of select="PRICE"/>
            </div>

            <div class="description">
                    <xsl:value-of select="description"/>
                    <span> (<xsl:value-of select="AVAILABILITY"/> will be available)</span>
            </div>

        </xsl:for-each>
        </body>
        </html>
    """

    transform = XSLT(XML(TEMPLATE))
    data = parse(StringIO(DATA))
    result = transform(data)

    print(result)
    # <html>
    # <style>
    #     body {font-family: Arial; font-size: 1em; background-color: #EEEEEE}
    #     div.title {background-color: teal; color: white; padding: 4px}
    #     div.description {margin-left:20px;margin-bottom:1em;font-size:10pt}
    #     span {font-weight: bold}
    # </style>
    # <body>
    # <div class="title">
    # <span>Sanguinaria canadensis</span>$2.44</div>
    # <div class="description"><span> (031599 will be available)</span></div>
    # <div class="title">
    # <span>Aquilegia canadensis</span>$9.37</div>
    # <div class="description"><span> (030699 will be available)</span></div>
    # </body>
    # </html>


Assignments
===========
.. literalinclude:: assignments/serialization_xml_a.py
    :caption: :download:`Solution <assignments/serialization_xml_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/serialization_xml_b.py
    :caption: :download:`Solution <assignments/serialization_xml_b.py>`
    :end-before: # Solution
