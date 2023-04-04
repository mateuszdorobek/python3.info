# Inspiration: https://github.com/jdillard/sphinx-sitemap/blob/master/sphinx_sitemap/__init__.py

from typing import Any
from pathlib import Path
from datetime import datetime, timezone
from sphinx.application import Sphinx
from sphinx.util.logging import getLogger

__version__ = "1.0.0"

logger = getLogger(__name__)


def setup(app: Sphinx) -> dict[str, Any]:
    """
    Sphinx extension setup function.
    It adds config values and connects Sphinx events to the sitemap builder.
    :param app: The Sphinx Application instance
    :return: A dict of Sphinx extension options
    """
    app.connect("build-finished", on_finish)
    try:
        app.add_config_value("html_baseurl", default=None, rebuild="")
    except BaseException:
        pass
    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
        "version": __version__,
    }

def on_finish(app: Sphinx, exception):
    """
    Generates the sitemap.xml from the collected HTML page links.
    :param app: The Sphinx Application instance
    """
    SITEMAP_FILE = f'{app.outdir}/sitemap.xml'
    TEMPLATE_ROW = """
    <url>
        <loc>{url}</loc>
        <lastmod>{lastmod:%Y-%m-%dT%H:%M:%S%z}</lastmod>
        <changefreq>daily</changefreq>
        <priority>{priority}</priority>
    </url>"""
    Path(SITEMAP_FILE).write_text('')
    sitemap = Path(SITEMAP_FILE).open(mode='a')
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
        row = TEMPLATE_ROW.format(
            url=f'{app.builder.config.html_baseurl}/{path}',
            lastmod=datetime.fromtimestamp(file.stat().st_mtime).replace(tzinfo=timezone.utc),
            priority=priority)
        sitemap.write(row)
    sitemap.write('\n</urlset>\n')
    sitemap.close()
    logger.info(f'Sitemap generated: {SITEMAP_FILE}')
