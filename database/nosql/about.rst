NoSQL About
===========
* List of NoSQL databases [#Stevens2022]_
* Key–value Store (Redis)
* Key-Value Cache (Redis, Memcached)
* Column-Oriented Store (Cassandra)
* Document Store (MongoDB)
* Graph Database (Neo4j)
* Time Series Database (InfluxDB, Prometheus)
* Object Database
* Tuple Store
* Triplestore (RDF store)
* Relational Database
* Multi Model
* Multi Value

.. figure:: img/nosql-vs-sql.png

A NoSQL (originally referring to "non-SQL" or "non-relational") database
provides a mechanism for storage and retrieval of data that is modeled in
means other than the tabular relations used in relational databases. Such
databases have existed since the late 1960s, but the name "NoSQL" was only
coined in the early 21st century, triggered by the needs of Web 2.0
companies. NoSQL databases are increasingly used in big data and real-time
web applications. NoSQL systems are also sometimes called Not only SQL to
emphasize that they may support SQL-like query languages or sit alongside
SQL databases in polyglot-persistent architectures [#wikiNoSQL]_.

Motivations for this approach include simplicity of design, simpler
"horizontal" scaling to clusters of machines (which is a problem for
relational databases), finer control over availability and limiting the
object-relational impedance mismatch. The data structures used by NoSQL
databases (e.g. key–value pair, wide column, graph, or document) are
different from those used by default in relational databases, making some
operations faster in NoSQL. The particular suitability of a given NoSQL
database depends on the problem it must solve. Sometimes the data
structures used by NoSQL databases are also viewed as "more flexible" than
relational database tables [#wikiNoSQL]_.


Performance
-----------
.. csv-table:: Performance. Source [#wikiNoSQL]_
    :header: Data model, Performance, Scalability, Flexibility, Complexity, Functionality

    Key–value,         high,     high,     high,     none,     none
    Column-oriented,   high,     high,     moderate, low,      minimal
    Document-oriented, high,     high,     high,     low,      low
    Graph,             variable, variable, high,     high,     graph theory
    Relational,        variable, variable, low,      moderate, relational algebra


Document Store
--------------
* ArangoDB
* Azure Cosmos DB
* BaseX
* Clusterpoint
* CouchDB
* Couchbase
* DocumentDB
* Elasticsearch
* IBM Domino
* MarkLogic
* MongoDB
* OrientDB
* Qizx
* RethinkDB
* eXist-db


Key–Value Store
---------------
* Aerospike
* Amazon DynamoDB
* ArangoDB
* Azure Cosmos DB
* BigTable
* Couchbase
* FoundationDB
* InfinityDB
* LMDB
* LocalStorage (web browser + JS)
* MemcacheDB
* Oracle NoSQL Database
* Project Voldemort
* Redis
* Riak
* SessionStorage (web browser + JS)
* Voldemort


Key-Value Cache
---------------
* Apache Ignite
* Coherence
* Couchbase
* Hazelcast
* Infinispan
* Memcached
* Oracle Coherence
* Redis
* Velocity
* eXtreme Scale


Tuple Store
-----------
* Apache River
* GigaSpaces
* OpenLink Virtuoso
* TIBCO ActiveSpaces
* Tarantool


Triplestore (RDF)
-----------------
* AllegroGraph
* MarkLogic
* Ontotext-OWLIM
* Oracle NoSQL database
* Profium Sense
* Virtuoso Universal Server


Graph Database
--------------
* AllegroGraph
* Apache Giraph
* ArangoDB
* Azure Cosmos DB
* InfiniteGraph
* MarkLogic
* Neo4j
* OrientDB
* RedisGraph
* Virtuoso


Time Series Database
--------------------
* InfluxDB
* Prometheus
* TSDB


Column-Oriented Store
---------------------
* Amazon DynamoDB
* Apache Accumulo
* Azure Cosmos DB
* Bigtable
* Cassandra
* Druid
* Google Cloud Datastore
* HBase
* Hypertable
* ScyllaDB


Object Database
---------------
* GemStone/S
* InterSystems Caché
* JADE
* NeoDB
* Ninja Database Pro
* ODABA
* ObjectDB
* ObjectDatabase++
* ObjectStore
* Objectivity/DB
* OpenLink Virtuoso
* Perst
* Realm
* Versant Object Database
* ZODB
* ZopeDB
* db4o


Multi Model
-----------
* Apache Ignite
* ArangoDB
* Azure Cosmos DB
* Couchbase
* FoundationDB
* MarkLogic
* MarkLogic
* Oracle Database
* OrientDB


Multi Value
-----------
* D3 Pick database
* Extensible Storage Engine (ESE/NT)
* InfinityDB
* InterSystems Caché
* Northgate Information Solutions Reality (the original Pick/MV Database)
* OpenQM
* Revelation Software's OpenInsight (Windows) and Advanced Revelation (DOS)
* UniData Rocket U2
* UniVerse Rocket U2
* jBASE Pick database
* mvBase Rocket Software
* mvEnterprise Rocket Software


Further Reading
---------------
* `List of NoSQL database management systems <https://hostingdata.co.uk/nosql-database/>`_


References
----------
.. [#wikiNoSQL] Wikipedia. NoSQL. Year: 2022. Retrieved: 2022-03-17. URL: https://en.wikipedia.org/wiki/NoSQL

.. [#Stevens2022] Stevens, G. List of NoSQL database management systems. Year: 2022. Retrieved: 2022-03-17. URL: https://hostingdata.co.uk/nosql-database/
