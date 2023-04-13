Dependency Injection
====================

* http://python-dependency-injector.ets-labs.org/introduction/di_in_python.html

Dependency injection, as a software design pattern, has number of advantages that are common for each language (including Python):

    * Dependency Injection decreases coupling between a class and its dependency.
    * Because dependency injection doesn't require any change in code behavior it can be applied to legacy code as a refactoring. The result is clients that are more independent and that are easier to unit test in isolation using stubs or mock objects that simulate other objects not under test. This ease of testing is often the first benefit noticed when using dependency injection.
    * Dependency injection can be used to externalize a system's configuration details into configuration files allowing the system to be reconfigured without recompilation (rebuilding). Separate configurations can be written for different situations that require different implementations of components. This includes, but is not limited to, testing.
    * Reduction of boilerplate code in the application objects since all work to initialize or set up dependencies is handled by a provider component.
    * Dependency injection allows a client to remove all knowledge of a concrete implementation that it needs to use. This helps isolate the client from the impact of design changes and defects. It promotes reusability, testability and maintainability.
    * Dependency injection allows a client the flexibility of being configurable. Only the client's behavior is fixed. The client may act on anything that supports the intrinsic interface the client expects.

Dependency injection:

.. code-block:: python

    from dataclasses import dataclass
    from datetime import timedelta
    from typing import Any


    @dataclass
    class ICache:
        expiration: timedelta = timedelta(days=30)
        location: str | None = None

        def get(self, key: str) -> Any:
            raise NotImplementedError

        def set(self, key: str, value: Any) -> None:
            raise NotImplementedError

        def is_valid(self, key) -> bool:
            raise NotImplementedError


    class CacheFilesystem(ICache):
        """Cache using files"""


    class CacheMemory(ICache):
        """Cache using memory"""


    class CacheDatabase(ICache):
        """Cache using database"""


    @dataclass
    class HTTP:
        _cache: CacheInterface

        def _fetch(self, url):
            return ...

        def get(self, url):
            if self._cache.is_valid(url):
                # Use cached data
                self._cache.get(url)
            else:
                data = self._fetch(url)
                self._cache.set(url, data)


    if __name__ == '__main__':
        database = CacheDatabase(location='sqlite3:///tmp/http-cache.sqlite3')
        filesystem = CacheFilesystem(location='/tmp/')
        memory = CacheMemory(expiration=timedelta(hours=2))

        http1 = HTTP(_cache=database)
        http1.get('https://python3.info')

        http2 = HTTP(_cache=filesystem)
        http2.get('https://python3.info')

        http3 = HTTP(_cache=memory)
        http3.get('https://python3.info')


.. code-block:: python

    import os
    from dataclasses import dataclass, field
    from hashlib import sha1
    from datetime import timedelta, datetime
    from http import HTTPStatus
    import requests


    class CacheInterface:
        def _get_location(self, key: str) -> str:
            raise NotImplementedError

        def get(self, key: str) -> str:
            raise NotImplementedError

        def set(self, key: str, value: str) -> None:
            raise NotImplementedError

        def clear(self, key: str) -> None:
            raise NotImplementedError

        def is_valid(self, key: str) -> bool:
            raise NotImplementedError


    @dataclass
    class CacheMemory(CacheInterface):
        expiration: timedelta = timedelta(seconds=30)
        _data: dict[str, str] = field(default_factory=dict)

        def is_valid(self, key: str) -> bool:
            return key in self._data

        def set(self, key: str, value: str) -> None:
            self._data[key] = value

        def get(self, key: str) -> str:
            return self._data[key]


    @dataclass
    class CacheFilesystem(CacheInterface):
        location: str = "/tmp/cache/"
        expiration: timedelta = timedelta(seconds=30)

        def __post_init__(self):
            if os.path.isfile(self.location):
                os.remove(self.location)
            if not os.path.isdir(self.location):
                os.makedirs(self.location, exist_ok=True)

        def _get_location(self, key: str) -> str:
            filename = sha1(key.encode()).hexdigest()
            return os.path.join(self.location, filename)

        def is_valid(self, key: str) -> bool:
            location = self._get_location(key)
            if not os.path.isfile(location):
                return False
            timestamp = os.path.getmtime(location)
            modification_date = datetime.fromtimestamp(timestamp)
            last_update = datetime.now() - modification_date
            return last_update < self.expiration:

        def get(self, key: str) -> str:
            location = self._get_location(key)
            with open(location) as file:
                return file.read()

        def set(self, key: str, value: str) -> None:
            location = self._get_location(key)
            with open(location, mode="w") as file:
                file.write(value)


    @dataclass
    class HTTPGateway:
        _cache: CacheInterface = CacheMemory

        def get(self, url):
            if self._cache.is_valid(url):
                return self._cache.get(url)
            else:
                data = self._fetch(url)
                self._cache.set(url, data)
                return data

        def _fetch(self, url):
            response = requests.get(url)
            if response.status_code == HTTPStatus.OK:
                return response.text
            else:
                raise ConnectionError()


    @dataclass
    class CacheDatabase(CacheInterface):
        location: str


    if __name__ == '__main__':
        cache = CacheFilesystem(location="/tmp/cache/", expiration=timedelta(seconds=1))
        http = HTTPGateway(cache)

        URL = 'https://python3.info/_static/iris-clean.csv'
        data = http.get(URL)
        print(data)


.. todo:: Assignments
