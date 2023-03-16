from urllib.request import urlopen
from dataclasses import dataclass, field


@dataclass
class Browser:
    history: list[str] = field(default_factory=list)

    def open(self, url: str) -> None:
        self.history.append(url)
        # return urlopen(url).read()


if __name__ == '__main__':
    browser = Browser()
    browser.open('https://python.astrotech.io')
    browser.open('https://numpy.astrotech.io')
    browser.open('https://pandas.astrotech.io')
    browser.open('https://design-patterns.astrotech.io')

    for url in browser.history:
        print(url)

# https://python.astrotech.io
# https://numpy.astrotech.io
# https://pandas.astrotech.io
# https://design-patterns.astrotech.io
