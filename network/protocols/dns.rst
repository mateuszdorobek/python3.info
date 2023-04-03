DNS
===

* https://yamakira.github.io/python-network-programming/protocols/dns/index.html


``dnspython``
-------------

Installation
------------
.. code-block:: console

    $ pip install dnspython

Basic DNS queries
-----------------
.. code-block:: python

    import dns.resolver


    name = 'python3.info'

    answer = dns.resolver.query(name, 'MX')
    print(answer.rrset)

.. code-block:: python

    import dns.resolver

    name = 'python3.info'
    answer = dns.resolver.query(name, 'MX')

    print(answer.canonical_name)
    # readthedocs.io.

    print(answer.expiration)
    # 1541631181.7326112

    print(answer.response.answer)
    # [
    #   <DNS python3.info. IN CNAME RRset>,
    #   <DNS readthedocs.io. IN MX RRset>
    # ]

    print(answer.rrset)
    # readthedocs.io. 71 IN MX 10 aspmx3.googlemail.com.
    # readthedocs.io. 71 IN MX 10 aspmx2.googlemail.com.
    # readthedocs.io. 71 IN MX 5 alt1.aspmx.l.google.com.
    # readthedocs.io. 71 IN MX 1 aspmx.l.google.com.
    # readthedocs.io. 71 IN MX 5 alt2.aspmx.l.google.com.

    print(answer.rrset.items)
    # [
    #   <DNS IN MX rdata: 10 aspmx3.googlemail.com.>,
    #   <DNS IN MX rdata: 10 aspmx2.googlemail.com.>,
    #   <DNS IN MX rdata: 5 alt1.aspmx.l.google.com.>,
    #   <DNS IN MX rdata: 1 aspmx.l.google.com.>,
    #   <DNS IN MX rdata: 5 alt2.aspmx.l.google.com.>
    # ]



.. code-block:: python

    import dns.resolver


    name = 'python3.info'
    records = ['A', 'AAAA', 'MX', 'NS', 'TXT', 'SOA']


    for record in records:
        answer = dns.resolver.query(name, record)
        print(answer.rrset)

    # readthedocs.io. 377 IN A 104.18.231.122
    # readthedocs.io. 377 IN A 104.18.229.122
    # ...
    # readthedocs.io. 377 IN AAAA 2606:4700::6812:e57a
    # readthedocs.io. 377 IN AAAA 2606:4700::6812:e37a
    # ...
    # readthedocs.io. 377 IN MX 10 aspmx2.googlemail.com.
    # readthedocs.io. 377 IN MX 1 aspmx.l.google.com.
    # ...
    # readthedocs.io. 377 IN TXT "google-site-verification=..."
    # readthedocs.io. 377 IN TXT "google-site-verification=..."
    # readthedocs.io. 4502 IN SOA ivan.ns.cloudflare.com. dns.cloudflare.com. 2030876750 10000 2400 604800 3600

Zone transfer
-------------
* *DNS Zone transfer* is the process where a *DNS* server passes a copy of part of it's database (which is called a "zone") to another *DNS* server.
* *DNS zone transfer*, also sometimes known by the inducing *DNS* query type *AXFR*, is a type of *DNS* transaction.
* It is one of the many mechanisms to replicate *DNS* databases across a set of *DNS* servers.

.. code-block:: python

    import dns.query
    import dns.zone


    z = dns.zone.from_xfr(dns.query.xfr('nsztm1.digi.ninja', 'zonetransfer.me'))
    names = z.nodes.keys()
    names.sort()

    for n in names:
        print(z[n].to_text(n))

Reverse DNS lookup (PTR record)
-------------------------------
* Reverse *DNS* resolution (*rDNS*)
* Determination of a domain name associated with an *IP* address via querying *DNS*
* Checks *PTR* record

#. Reverse lookup of the *IP* address ``8.8.4.4``
#. *PTR* (record for the domain name ``4.4.8.8.in-addr.arpa``) would be looked up
#. Found to point to ``google-public-dns-b.google.com``

.. code-block:: python

    import dns.reversename


    domain_address = dns.reversename.from_address('8.8.4.4')
    # <DNS name 4.4.8.8.in-addr.arpa.>

    ip_address = dns.reversename.to_address(domain_address)
    # 8.8.4.4

.. code-block:: python

    import dns.resolver
    import dns.reversename


    domain_address = dns.reversename.from_address('8.8.4.4')
    # <DNS name 4.4.8.8.in-addr.arpa.>

    domain_name = str(dns.resolver.query(domain_address, 'PTR')[0])
    # google-public-dns-b.google.com.
