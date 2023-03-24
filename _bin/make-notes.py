import re
from pathlib import Path
from shutil import rmtree
from _config import log, BOOKS, SRC_DIR, OUT_DIR
from _config import get_toc, get_chapters


# TODO: kopiować pliki requirements.txt dla każdego rozdziału do _template/chapter
# TODO: linki do materiałów gdzie można znaleźć dany rozdział, wygenerować na podstawie ścieżki do pliku

def get_headers(file: Path) -> list[str]:
    margin = '(?:\n{0,1})'
    title = r'^.{3,80}\n'
    underline = r'^[*=-]{3,80}\n{0,1}'
    highlights = r'(?:^\*\s.+\n)*'
    exclude_headers = (
        'Assignments',
        'Case Study',
        'Example',
        'References',
        'SetUp',
        'Use Case')
    headers = re.findall(
        pattern=f'{margin}{title}{underline}{highlights}',
        string=file.read_text(),
        flags=re.MULTILINE)
    return [f'\n\n{header.lstrip()}'
            for header in headers
            if not header.lstrip().startswith(exclude_headers)]


if __name__ == '__main__':
    for book in BOOKS:
        outdir = OUT_DIR / book / 'notes'
        rmtree(outdir, ignore_errors=True)
        outdir.mkdir(exist_ok=True, parents=True)
        chapters = get_chapters(book)

        for file in get_toc(book):
            file = Path(file)
            topic = file.stem
            chapter = file.parent.name

            if not chapter:
                log.error(f'No chapter directory: {book}/{file}')
                continue

            i = chapters.index(chapter)
            notes = outdir / f'{i:02}-{chapter}.rst'
            filepath = SRC_DIR / book / file
            if not filepath.exists():
                log.error(f'Stalled entry in index file {book}/{file}')
                exit(1)
            headers = get_headers(filepath)

            with notes.open(mode='a') as fp:
                fp.writelines(headers)
