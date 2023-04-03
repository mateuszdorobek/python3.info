``scapy``
=========


* ``scapy`` is a Python framework for crafting and transmitting arbitrary packets
* http://www.secdev.org/projects/scapy/
* http://packetlife.net/blog/2011/may/23/introduction-scapy/


Installation
------------
.. code-block:: console

    $ pip install scapy


Running
-------
.. code-block:: console

    $ sudo scapy


Basic usage
-----------

Displays all available protocols
--------------------------------
Displays all available protocols:

.. code-block:: python

    ls()
    # ARP        : ARP
    # ASN1_Packet : None
    # BOOTP      : BOOTP
    # CookedLinux : cooked linux
    # DHCP       : DHCP options
    # DHCP6      : DHCPv6 Generic Message)
    # ...

Lists all command functions
---------------------------
Lists all command functions:

.. code-block:: console

    $ lsc()

.. csv-table:: Scapy functions
    :header: "Function", "Description"
    :widths: 30, 70

    "``IPID_count``", "Identify IP id values classes in a list of packets"
    "``arpcachepoison``", "Poison target's cache with (your MAC,victim's IP) couple"
    "``arping``", "Send ARP who-has requests to determine which hosts are up"
    "``arpleak``", "Exploit ARP leak flaws, like NetBSD-SA2017-002."
    "``bind_layers``", "Bind 2 layers on some specific fields' values. It makes the packet being built"
    "``bridge_and_sniff``", "Forward traffic between interfaces if1 and if2, sniff and return"
    "``chexdump``", "Build a per byte hexadecimal representation"
    "``computeNIGroupAddr``", "Compute the NI group Address. Can take a FQDN as input parameter"
    "``corrupt_bits``", "Flip a given percentage or number of bits from a string"
    "``corrupt_bytes``", "Corrupt a given percentage or number of bytes from a string"
    "``defrag``", "defrag(plist) -> ([not fragmented], [defragmented],"
    "``defragment``", "defragment(plist) -> plist defragmented as much as possible"
    "``dhcp_request``", "Send a DHCP discover request and return the answer"
    "``dyndns_add``", "Send a DNS add message to a nameserver for 'name' to have a new 'rdata'"
    "``dyndns_del``", "Send a DNS delete message to a nameserver for 'name'"
    "``etherleak``", "Exploit Etherleak flaw"
    "``explore``", "Function used to discover the Scapy layers and protocols."
    "``fletcher16_checkbytes``", "Calculates the Fletcher-16 checkbytes returned as 2 byte binary-string."
    "``fletcher16_checksum``", "Calculates Fletcher-16 checksum of the given buffer."
    "``fragleak``", "--"
    "``fragleak2``", "--"
    "``fragment``", "Fragment a big IP datagram"
    "``fuzz``", "Transform a layer into a fuzzy layer by replacing some default values by random objects"
    "``getmacbyip``", "Return MAC address corresponding to a given IP address"
    "``getmacbyip6``", "Returns the MAC address corresponding to an IPv6 address"
    "``hexdiff``", "Show differences between 2 binary strings"
    "``hexdump``", "Build a tcpdump like hexadecimal view"
    "``hexedit``", "Run hexedit on a list of packets, then return the edited packets."
    "``hexstr``", "Build a fancy tcpdump like hex from bytes."
    "``import_hexcap``", "Imports a tcpdump like hexadecimal view"
    "``is_promisc``", "Try to guess if target is in Promisc mode. The target is provided by its ip."
    "``linehexdump``", "Build an equivalent view of hexdump() on a single line"
    "``ls``", "List  available layers, or infos on a given layer class or name."
    "``neighsol``", "Sends and receive an ICMPv6 Neighbor Solicitation message"
    "``overlap_frag``", "Build overlapping fragments to bypass NIPS"
    "``promiscping``", "Send ARP who-has requests to determine which hosts are in promiscuous mode"
    "``rdpcap``", "Read a pcap or pcapng file and return a packet list"
    "``report_ports``", "portscan a target and output a LaTeX table"
    "``restart``", "Restarts scapy"
    "``send``", "Send packets at layer 3"
    "``sendp``", "Send packets at layer 2"
    "``sendpfast``", "Send packets at layer 2 using tcpreplay for performance"
    "``sniff``", "Sniff packets and return a list of packets."
    "``split_layers``", "Split 2 layers previously bound."
    "``sr``", "Send and receive packets at layer 3"
    "``sr1``", "Send packets at layer 3 and return only the first answer"
    "``sr1flood``", "Flood and receive packets at layer 3 and return only the first answer"
    "``srbt``", "send and receive using a bluetooth socket"
    "``srbt1``", "send and receive 1 packet using a bluetooth socket"
    "``srflood``", "Flood and receive packets at layer 3"
    "``srloop``", "Send a packet at layer 3 in loop and print the answer each time"
    "``srp``", "Send and receive packets at layer 2"
    "``srp1``", "Send and receive packets at layer 2 and return only the first answer"
    "``srp1flood``", "Flood and receive packets at layer 2 and return only the first answer"
    "``srpflood``", "Flood and receive packets at layer 2"
    "``srploop``", "Send a packet at layer 2 in loop and print the answer each time"
    "``tcpdump``", "Run tcpdump or tshark on a list of packets"
    "``traceroute``", "Instant TCP traceroute"
    "``traceroute6``", "Instant TCP traceroute using IPv6"
    "``traceroute_map``", "Util function to call traceroute on multiple targets, then"
    "``tshark``", "Sniff packets and print them calling pkt.summary(), a bit like text wireshark"
    "``wireshark``", "Run wireshark on a list of packets"
    "``wrpcap``", "Write a list of packets to a pcap file"

Reading PCAP files
------------------
* Read packets from a *pcap* file
* Write packets to a *pcap* file.

.. code-block:: python

    data = rdpcap("/spare/captures/isakmp.cap")
    # <isakmp.cap: UDP:721 TCP:0 ICMP:0 Other:0>

Graphical dumps (PDF, PS)
-------------------------
.. csv-table:: Graphical dumps (PDF, PS)
    :header: "Command", "Effect"
    :widths: 30, 70

    "``raw(pkt)``", "assemble the packet"
    "``hexdump(pkt)``", "have a hexadecimal dump"
    "``ls(pkt)``", "have the list of fields values"
    "``pkt.summary()``", "for a one-line summary"
    "``pkt.show()``", "for a developed view of the packet"
    "``pkt.show2()``", "same as show but on the assembled packet (checksum is calculated, for instance)"
    "``pkt.sprintf()``", "fills a format string with fields values of the packet"
    "``pkt.decode_payload_as()``", "changes the way the payload is decoded"
    "``pkt.psdump()``", "draws a PostScript diagram with explained dissection"
    "``pkt.pdfdump()``", "draws a PDF with explained dissection"
    "``pkt.command()``", "return a Scapy command that can generate the packet"

Generating sets of packets
--------------------------
.. csv-table:: Generating sets of packets
    :header: "Command", "Effect"
    :widths: 30, 70

    "``summary()``", "displays a list of summaries of each packet"
    "``nsummary()``", "same as previous, with the packet number"
    "``conversations()``", "displays a graph of conversations"
    "``show()``", "displays the preferred representation (usually nsummary())"
    "``filter()``", "returns a packet list filtered with a lambda function"
    "``hexdump()``", "returns a hexdump of all packets"
    "``hexraw()``", "returns a hexdump of the Raw layer of all packets"
    "``padding()``", "returns a hexdump of packets with padding"
    "``nzpadding()``", "returns a hexdump of packets with non-zero padding"
    "``plot()``", "plots a lambda function applied to the packet list"
    "``make table()``", "displays a table according to a lambda function"

List of possible fields
-----------------------
.. code-block:: python

    dir(IP)

.. code-block:: python

    dir(TCP)

.. code-block:: python

    dir(ICMP)

.. code-block:: python

    dir(Ether)

IP packages
-----------
* Packets are constructed as layers of protocols, loosely analogous to the *OSI* model, which can be manipulated independently or glued together.
* ``IP()`` object represents an *IPv4* header.

Create package
--------------
Create package:

.. code-block:: python

    ip = IP(src="192.168.0.1")
    # <IP  src=192.168.0.1 |>

Create package:

.. code-block:: python

    ip = IP(src="192.168.0.1", dst="192.168.0.2")
    # <IP  src=192.168.0.1 dst=192.168.0.2 |>

Modify package
--------------
Modify package:

.. code-block:: python

    ip = IP(src="192.168.0.1")
    ip.dst = "192.168.0.2"
    # <IP  src=192.168.0.1 dst=192.168.0.2 |>

Show package
------------
 Use the ``show()`` method of an object to display all of its fields:

.. code-block:: python

    ip = IP(src="192.168.0.1")
    ip.show()
    # ###[ IP ]###
    #   version= 4
    #   ihl= None
    #   tos= 0x0
    #   len= None
    #   id= 1
    #   flags=
    #   frag= 0
    #   ttl= 64
    #   proto= ip
    #   chksum= None
    #   src= 192.168.0.1
    #   dst= 127.0.0.1
    #   \options\


TCP Package
-----------

Add TCP layer to IP package
---------------------------
* Add a layer for protocol by using the division operator

Add a layer for protocol by using the division operator:

.. code-block:: python

    ip = IP(src="192.168.0.1", dst="192.168.0.2")
    tcp = TCP(sport=1025, dport=80)

    ip / tcp
    # <IP  frag=0 proto=tcp src=192.168.0.1 dst=192.168.0.2 |<TCP  sport=blackjack dport=http |>>

Manipulate the TCP header fields just as IP header:

.. code-block:: python

    ip = IP(src="192.168.0.1", dst="192.168.0.2")
    tcp = TCP(sport=1025, dport=80)

    (tcp/ip).show()
    # ###[ TCP ]###
    #   sport= blackjack
    #   dport= http
    #   seq= 0
    #   ack= 0
    #   dataofs= None
    #   reserved= 0
    #   flags= S
    #   window= 8192
    #   chksum= None
    #   urgptr= 0
    #   options= []
    # ###[ IP ]###
    #      version= 4
    #      ihl= None
    #      tos= 0x0
    #      len= None
    #      id= 1
    #      flags=
    #      frag= 0
    #      ttl= 64
    #      proto= ip
    #      chksum= None
    #      src= 192.168.0.1
    #      dst= 192.168.0.2
    #      \options\


Ethernet frames
---------------
``scapy`` also supports Ethernet and IEEE 802.11 at layer two:

.. code-block:: python

    Ether() / Dot1Q() / IP()
    # <Ether  type=0x8100 |<Dot1Q  type=0x800 |<IP  |>>>

``scapy`` also supports Ethernet and IEEE 802.11 at layer two:

.. code-block:: python

    Dot11() / IP()
    # <Dot11  |<IP  |>>


Sending packets
---------------

OSI layer three
---------------
* ``send()`` function if transmitting at layer three (i.e. without a layer two header)

.. code-block:: python

    ip = IP(src="192.168.0.1", dst="192.168.0.2")
    tcp = TCP(sport=1025, dport=80)

    send(ip/tcp)
    # .
    # Sent 1 packets.

OSI layer two
-------------
* ``sendp()`` function if transmitting at layer two
* Values for blank fields, such as the source and destination addresses in the Ethernet header, are populated automatically by ``scapy`` where possible.

.. code-block:: python

    ip = IP(src="192.168.0.1", dst="192.168.0.2")
    tcp = TCP(sport=1025, dport=80)

    sendp(Ether()/ip/tcp)
    # .
    # Sent 1 packets.


Send and Receive
----------------
* ``scapy`` has the ability to listen for responses to packets it sends, such as *ICMP* echo requests (pings).

One packet
----------
* Build an *IP* packet carrying an *ICMP* header
* Use the ``sr()`` (send/receive) function to transmit the packet and record any response

.. code-block:: python

    ip = IP(dst='python3.info')
    packet = ip / ICMP()

    sr(packet)
    # Begin emission:
    # Finished sending 1 packets.
    #
    # Received 4 packets, got 1 answers, remaining 0 packets
    # (<Results: TCP:0 UDP:0 ICMP:1 Other:0>,
    #  <Unanswered: TCP:0 UDP:0 ICMP:0 Other:0>)

Many packets
------------
* Send and listen for responses to multiple copies of the same packet
* Use the ``srloop()`` function and specify a count of packets to send

.. code-block:: python

    ip = IP(dst="python3.info")
    packet = ip / ICMP()

    srloop(packet, count=3)
    # RECV 1: IP / ICMP 104.18.227.122 > 172.20.10.2 echo-reply 0 / Padding
    # RECV 1: IP / ICMP 104.18.227.122 > 172.20.10.2 echo-reply 0 / Padding
    # RECV 1: IP / ICMP 104.18.227.122 > 172.20.10.2 echo-reply 0 / Padding
    #
    # Sent 3 packets, received 3 packets. 100.0% hits.
    # (<Results: TCP:0 UDP:0 ICMP:3 Other:0>,
    #  <PacketList: TCP:0 UDP:0 ICMP:0 Other:0>)


SYN Scans
---------
* ``SA`` or ``SYN-ACK`` flags indicating an open port.

Scan one port
-------------
Scan one port:

.. code-block:: python

    ip = IP(dst="python3.info")
    tcp = TCP(dport=80, flags="S")

    sr1(ip/tcp)
    # Begin emission:
    # Finished sending 1 packets.
    #
    # Received 4 packets, got 1 answers, remaining 0 packets
    # <IP  version=4 ihl=5 tos=0x0 len=44 id=0 flags= frag=0 ttl=58 proto=tcp chksum=0x7e29 src=104.18.228.122 dst=172.20.10.2 |<TCP  sport=http dport=ftp_data seq=19296319 ack=1 dataofs=6 reserved=0 flags=SA window=29200 chksum=0xb1cc urgptr=0 options=[('MSS', 1408)] |<Padding  load='z*\xc2f\x87\xad\x93\xc5' |>>>

Scan one port:

.. code-block:: python

    ip = IP(dst='35.158.227.45')
    tcp = TCP(dport=21, flags="S")

    sr(ip/tcp)
    # Begin emission:
    # Finished sending 1 packets.
    #
    # Received 4 packets, got 1 answers, remaining 0 packets
    # (<Results: TCP:1 UDP:0 ICMP:0 Other:0>,
    #  <Unanswered: TCP:0 UDP:0 ICMP:0 Other:0>)

    sr1(ip/tcp)
    # Begin emission:
    # Finished sending 1 packets.
    #
    # Received 2 packets, got 1 answers, remaining 0 packets
    # <IP  version=4 ihl=5 tos=0x0 len=44 id=0 flags= frag=0 ttl=64 proto=tcp chksum=0xbdea src=35.158.227.45 dst=172.20.10.2 |<TCP  sport=ftp dport=ftp_data seq=952757507 ack=1 dataofs=6 reserved=0 flags=SA window=65535 chksum=0xb56f urgptr=0 options=[('MSS', 1410)] |<Padding  load='\x16\xd2e\xaf\xa16\xd2\x1b' |>>>

Scan port range
---------------
Scan port range:

.. code-block:: python

    ip = IP(dst="python3.info")
    tcp = TCP(sport=666, dport=(440,443), flags="S")

    sr(ip/tcp)


Advanced examples
-----------------
* https://scapy.readthedocs.io/en/latest/usage.html
