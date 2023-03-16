from dataclasses import dataclass, field


class Iterator:
    def has_next(self) -> bool:
        raise NotImplementedError

    def current(self) -> str:
        raise NotImplementedError

    def next(self) -> None:
        raise NotImplementedError


@dataclass
class BrowseHistory:
    urls: list[str] = field(default_factory=list)

    def push(self, url: str) -> None:
        self.urls.append(url)

    def pop(self) -> str:
        return self.urls.pop()

    def get_urls(self) -> list[str]:
        return self.urls

    def create_iterator(self) -> Iterator:
        return self.ListIterator(self)

    @dataclass
    class ListIterator(Iterator):
        history: 'BrowseHistory'
        index: int = 0

        def has_next(self) -> bool:
            return self.index < len(history.urls)

        def current(self) -> str:
            return history.urls[self.index]

        def next(self) -> None:
            self.index += 1


if __name__ == '__main__':
    history = BrowseHistory()
    history.push(url='https://a.example.com')
    history.push(url='https://b.example.com')
    history.push(url='https://c.example.com')

    iterator = history.create_iterator()
    while iterator.has_next():
        url = iterator.current()
        print(url)
        iterator.next()

    # https://a.example.com
    # https://b.example.com
    # https://c.example.com
