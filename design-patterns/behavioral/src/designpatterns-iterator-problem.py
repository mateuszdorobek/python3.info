from dataclasses import dataclass, field


@dataclass
class BrowseHistory:
    urls: list[str] = field(default_factory=list)

    def push(self, url: str) -> None:
        self.urls.append(url)

    def pop(self) -> str:
        return self.urls.pop()

    def get_urls(self) -> list[str]:
        return self.urls


if __name__ == '__main__':
    history = BrowseHistory()
    history.push(url='https://a.example.com')
    history.push(url='https://b.example.com')
    history.push(url='https://c.example.com')

    for i in range(len(history.get_urls())):
        url = history.get_urls()[i]
        print(i)
