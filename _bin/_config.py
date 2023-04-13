import logging
import re
from pathlib import Path



SRC_DIR = Path('/Users/matt/Developer/book-python')
OUT_DIR = Path('/Users/matt/Developer/_template')

BOOKS = [
    'advanced',
    'basics',
    'data-science',
    'database',
    'design-patterns',
    'devops',
    'django',
    'fastapi',
    'intermediate',
    'machine-learning',
    'matplotlib',
    'network',
    'numpy',
    'OOP',
    'pandas',
]

VERBOSE = False

logging.basicConfig(
    level='ERROR',
    datefmt='%Y-%m-%d %H:%M:%S',
    format='{asctime} {filename} {levelname:<7} {message}',
    style='{'
)

log = logging.getLogger('pybook')


def get_toc(book: str) -> list[str]:
    path = SRC_DIR / book / 'index.rst'
    filename = '([-\w/]*\.rst)'
    return re.findall(
        pattern=f'^\s+{filename}$',
        string=path.read_text(),
        flags=re.MULTILINE)


def get_chapters(book: str) -> list[str]:
    chapters = []
    for file in get_toc(book):
        chapter = file.split('/')[0]
        if chapter not in chapters:
            chapters.append(chapter)
    return chapters
