#!/usr/bin/env python
"""
usage: run.py OPTION [DIRS|FILES|CHAPTERS]

options:
  --help                show this help message and exit
  --build [CHAPTER]     build documentation in html format
  --doctest [CHAPTER]   doctest ReST and Python files
  --install [CHAPTER]   install requirements
  --gather              gather chapter requirements to main requirements

example:
    run.py --install
    run.py --install basics
    run.py --doctest *
    run.py --doctest basics
    run.py --doctest basics/types
    run.py --doctest basics/types/numeric-int.rst

Hint:
    You can pass more than one directory and/or file.
    Separate them using space.
"""

from datetime import datetime, timezone
import logging
import sys
from pathlib import Path
from argparse import ArgumentParser, Action
from shutil import rmtree
from subprocess import Popen, PIPE, TimeoutExpired
from conf import html_baseurl

sys.tracebacklimit = 8
logging.basicConfig(level='INFO', format='%(message)s')
log = logging.getLogger(__name__)

BASE_DIR = Path(__file__).parent


def run(cmd, timeout=None):
    process = Popen(cmd, stdout=PIPE, shell=True)
    while process.poll() is None:
        try:
            stdout, stderr = process.communicate(timeout=timeout)
        except TimeoutExpired:
            process.kill()
            raise TimeoutError from None
        if stdout:
            print(stdout.decode())
    return process.returncode


class Gather(Action):
    def __call__(self, parser, namespace, chapter, *args, **kwargs):
        run(r'clear && printf "\e[3J"')  # noqa
        run(f'cat */requirements.txt |sort |uniq > requirements.txt')
        log.info('Requirements Gathered in requirements.txt')
        exit(0)


class Install(Action):
    def __call__(self, parser, namespace, chapter, *args, **kwargs):
        if chapter is None:
            chapter = '.'
        run(r'clear && printf "\e[3J"')  # noqa
        run(f'pip install -r {chapter}/requirements.txt')
        log.info('Requirements installed')
        exit(0)


class Build(Action):
    def __call__(self, parser, namespace, chapter, *args, **kwargs):
        if chapter is None:
            src = BASE_DIR
            dst = Path('/tmp') / 'pybook'
        else:
            src = BASE_DIR / chapter
            dst = Path('/tmp') / chapter
        rmtree(dst, ignore_errors=True)
        run(r'clear && printf "\e[3J"')  # noqa
        run(f'sphinx-build -a -E -j auto --color -b html {src} {dst}')
        exit(0)


class GPT(Action):
    def __call__(self, parser, namespace, paths, *args, **kwargs):
        run(r'clear && printf "\e[3J"')  # noqa
        files = sorted(self.get_files(paths))
        for file in files:
            if file.name == 'run.py':
                continue
            if '/gpt' in file.read_text():
                log.critical(f'/gpt found in \t{file}')
                exit(1)
        log.info('No /gpt found in files')
        exit(0)

    @staticmethod
    def get_files(paths: str):
        for path in map(Path, paths):
            if path == Path(''):
                continue
            elif not path.exists():
                continue
            elif path.suffix in ('.rst', '.py'):
                yield path
            else:
                yield from Path(path).rglob('*.rst')
                yield from Path(path).rglob('*.py')


class Doctest(Action):
    def __call__(self, parser, namespace, paths, *args, **kwargs):
        run(r'clear && printf "\e[3J"')  # noqa
        all_tests = 0
        files = sorted(self.get_files(paths))
        for file in files:
            if self.is_ignored(file): continue
            if self.is_venv(file): continue
            if self.is_skipped(file): continue
            if count := self.count_doctests(file):
                self.run_doctest(file)
                all_tests += count
            else:
                log.error(f'NOTESTS\t{file}')
        logging.warning(f'\nAll tests {all_tests}')
        exit(0)

    @staticmethod
    def is_ignored(file: Path):
        doctestignore = Path(file.parts[0]) / '.doctestignore'
        if doctestignore.exists():
            log.warning(f'IGNORED\t{file}')
            return True
        else:
            return False

    @staticmethod
    def is_skipped(file: Path):
        if '# doctest: +SKIP_FILE' in file.read_text():
            log.warning(f'SKIPPED\t{file}')
            return True
        else:
            return False

    @staticmethod
    def is_venv(file: Path):
        log.debug(f'VENV\t{file}')
        return str(file).startswith('.venv-py')

    @staticmethod
    def count_doctests(file: Path):
        return file.read_text().count('>>> ')

    @staticmethod
    def get_files(paths: str):
        for path in map(Path, paths):
            if path == Path(''):
                continue
            elif not path.exists():
                continue
            elif path.suffix in ('.rst', '.py'):
                yield path
            else:
                yield from Path(path).rglob('*.rst')
                yield from Path(path).rglob('*.py')

    @staticmethod
    def run_doctest(file: Path):
        log.debug(f'RUN\t {file}')
        try:
            exitcode = run(f'python -m doctest {file}', timeout=45)
        except TimeoutError:
            log.error(f'TIMEOUT\t{file}')
            exit(1)
        if exitcode == 0:
            log.info(f'PASSED\t{file}')
        else:
            log.critical(f'FAILED\t{file}')
            exit(1)


class Sitemap(Action):
    TEMPLATE_ROW = """
    <url>
        <loc>{url}</loc>
        <lastmod>{lastmod:%Y-%m-%d}</lastmod>
        <changefreq>daily</changefreq>
        <priority>{priority}</priority>
    </url>"""

    def __call__(self, parser, namespace, chapter, *args, **kwargs):
        Path('sitemap.xml').write_text('')
        sitemap = Path('sitemap.xml').open(mode='a')
        sitemap.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        sitemap.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for file in Path().rglob('*.rst'):
            path = str(file).replace('.rst', '.html')
            if path == 'index.html':
                priority = '1.0'
            elif 'index.html' in path:
                priority = '0.8'
            else:
                priority = '0.5'
            row = self.TEMPLATE_ROW.format(
                url=f'{html_baseurl}/{path}',
                lastmod=datetime.fromtimestamp(file.stat().st_mtime),
                priority=priority)
            sitemap.write(row)
        sitemap.write('</urlset>\n')
        sitemap.close()
        exit(0)


if __name__ == '__main__':
    parser = ArgumentParser()

    parser.add_argument('--build',
                        nargs='?', metavar='CHAPTER', action=Build,
                        help='build documentation in html format')

    parser.add_argument('--doctest',
                        nargs='+', metavar='CHAPTER', action=Doctest,
                        help='doctest *.rst and *.py files')

    parser.add_argument('--gpt',
                        nargs='+', metavar='CHAPTER', action=GPT,
                        help='Scan for /gpt')

    parser.add_argument('--install',
                        nargs='?', metavar='CHAPTER', action=Install,
                        help='install requirements')

    parser.add_argument('--sitemap',
                        nargs=0, action=Sitemap,
                        help='generate sitemap.xml')

    parser.add_argument('--gather',
                        nargs=0, action=Gather,
                        help='gather chapter requirements to one file')

    parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help()
        exit(1)
