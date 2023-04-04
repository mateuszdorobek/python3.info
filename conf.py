project = 'Python: From None to Machine Learning'
html_baseurl = 'https://python3.info'
author = 'Matt Harasymczuk'
email = 'matt@astrotech.io'

needs_sphinx = '6.1'
project_language = 'en'
html_theme = 'sphinx_rtd_theme'
pygments_style = 'stata-dark'

todo_emit_warnings = False
todo_include_todos = False
html_menu_autohide = True

html_static_path = [
    '_static',
    '_data/csv',
    '_data/json',
    '_data/html',
    '_data/sas',
    '_data/sqlite3',
    '_data/xml',
    '_data/xlsx',
    'sitemap.xml',
    'robots.txt',
]

bibtex_bibfiles = [
    'network/references.bib',
    'numpy/references.bib',
    'intermediate/references.bib',]

# -- Standard book config -----------------------------------------------------
import os
import re
import subprocess
import sys
from datetime import date


# https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-suppress_warnings
suppress_warnings = [
    # 'app.add_node',
    # 'app.add_directive',
    # 'app.add_role',
    # 'app.add_generic_role',
    # 'app.add_source_parser',
    # 'autosectionlabel.*',
    # 'download.not_readable',
    # 'epub.unknown_project_files',
    # 'epub.duplicated_toc_entry',
    # 'i18n.inconsistent_references',
    # 'image.not_readable',
    # 'ref.term',
    # 'ref.ref',
    # 'ref.numref',
    # 'ref.keyword',
    # 'ref.option',
    'ref.citation',
    'ref.footnote',
    # 'ref.doc',
    # 'ref.python',
    # 'misc.highlighting_failure',
    # 'toc.circular',
    # 'toc.excluded',
    # 'toc.not_readable',
    'toc.secnum',
]

sys.path.insert(0, os.path.abspath('_extensions'))
extensions = [
    # 'sphinx.ext.autosectionlabel',
    # 'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.extlinks',
    # 'sphinx.ext.graphviz',
    'sphinx.ext.mathjax',
    'sphinx.ext.todo',
    # 'sphinx.ext.viewcode',
    'sphinxcontrib.bibtex',
    # 'recommonmark',
    # 'nbsphinx',
]

source_suffix = {
    '.rst': 'restructuredtext',
}

if 'recommonmark' in extensions:
    source_suffix['.md'] = 'markdown'
    def setup(app):
        from recommonmark.transform import AutoStructify
        app.add_config_value('recommonmark_config', {
                'enable_eval_rst': True,
        }, True)
        app.add_transform(AutoStructify)


if 'sphinx.ext.mathjax' in extensions:
    imgmath_image_format = 'png'
    imgmath_latex = 'latex'
    # mathjax_path = '_static/mathjax.js'
    mathjax_path = 'https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js'
    mathjax3_config = {
        'extensions': ['tex2jax.js'],
        'jax': ['input/TeX', 'output/HTML-CSS']}


if 'nbsphinx' in extensions:
    # https://nbsphinx.readthedocs.io/en/latest/usage.html
    nbsphinx_input_prompt = 'In [%s]:'
    nbsphinx_output_prompt = 'Out [%s]:'
    nbsphinx_execute = 'always'
    nbsphinx_allow_errors = True
    nbsphinx_timeout = 5
    nbsphinx_execute_arguments = [
        "--InlineBackend.figure_formats={'svg'}",  # 'pdf'
        "--InlineBackend.rc={'figure.dpi': 96}"]
    suppress_warnings += ['nbsphinx',
                          'nbsphinx.localfile',
                          'nbsphinx.gallery',
                          'nbsphinx.thumbnail',
                          'nbsphinx.notebooktitle',
                          'nbsphinx.ipywidgets']

if 'sphinxcontrib.bibtex' in extensions:
    bibtex_bibliography_header = ".. rubric:: References"
    bibtex_footbibliography_header = bibtex_bibliography_header
    bibtex_default_style = 'alpha'


if 'sphinx.ext.extlinks' in extensions:
    extlinks = {'isbn': ('https://e-isbn.pl/IsbnWeb/start/search.html?szukaj_fraza=%s', 'ISBN: ')}


if 'sphinx.ext.doctest' in extensions:
    import doctest
    trim_doctest_flags = True
    # doctest_global_cleanup = """"""
    # doctest_default_flags = doctest.ELLIPSIS | doctest.IGNORE_EXCEPTION_DETAIL | doctest.NORMALIZE_WHITESPACE
    # doctest_default_flags = doctest.FAIL_FAST | doctest.IGNORE_EXCEPTION_DETAIL


# article - For articles in scientific journals, presentations, short reports,
#           Program documentation, invitations, etc
# proc    - A class for proceedings based on the article class.
# minimal - Is as small as it can get. It only sets a page size and a base font.
#           It is mainly used for debugging purposes.
# report  - For longer reports containing several chapters, small books, thesis, etc
# book    - For real books
# slides  - For slides. The class uses big sans serif letters.
# memoir  - For changing sensibly the output of the document.
#           It is based on the book class, but you can create
#           any kind of document with it (1)
# letter  - For writing letters.
# beamer  - For writing presentations (see LaTeX/Presentations).
latex_documentclass = 'report'

# 0 - sequence number of image in whole document
# 1 - sequence number of image in header level 1 (only if :numbered: option is present at toctree directive)
# 2 - sequence number of image in header level 2
#       will use x.1, x.2, ... if located directly under a header level 1,
#       will use 1, 2, ... if at the document level
# etc...
numfig_secnum_depth = 1
numfig = True
smartquotes = False
numfig_format = {
    'section': 'Section %s.',
    'figure': 'Figure %s.',
    'table': 'Table %s.',
    'code-block': 'Code %s.'}

master_doc = 'index'
templates_path = ['_templates']
highlight_language = 'python3'
autodoc_typehints = 'description'
autosectionlabel_maxdepth = 4
autosectionlabel_prefix_document = True

project_slug = re.sub(r'[\W]+', '', project)
sha1 = subprocess.run('git log -1 --format="%h"', stdout=subprocess.PIPE, shell=True, encoding='utf-8').stdout.strip()
year = date.today().year
today = date.today().strftime('%Y-%m-%d')
version = f'#{sha1}, {today}'
release = f'#{sha1}, {today}'
copyright = f'{year}, CC-BY-SA-4.0, {author} <{email}>, last update: {today}'

exclude_patterns = [
    '.github',                    '*/.github',
    '.idea',                      '*/.idea',
    '.run',                       '*/.run',
    '_bin',                       '*/_bin',
    '_build',                     '*/_build',
    '_contrib',                   '*/_contrib',
    '_extensions',                '*/_extensions',
    '_i18n',                      '*/_i18n',
    '_img',                       '*/_img',
    '_slides',                    '*/_slides',
    '_static',                    '*/_static',
    '_themes',                    '*/_themes',
    '_tmp',                       '*/_tmp',
    '__TODO',                     '*/__TODO',
    '.*',                         '*/.*',
    'venv*',                      '*/venv*',
    'virtualenv*',                '*/virtualenv*',
    '.virtualenv*',               '*/.virtualenv*',
    '.venv*',                     '*/.venv*',
    'README.rst',                 '*/README.rst',
    'TODO.rst',                   '*/TODO.rst',
    'Thumbs.db',                  '*/Thumbs.db',
    '.DS_Store',                  '*/.DS_Store',
    'assignments',                '*/assignments',
    '_template.rst',              '*/_template.rst',
    '*.ipynb_checkpoints',        '*/*.ipynb_checkpoints',
    '_about/donation-failed.rst', '_about/donation-success.rst',
]

html_show_sphinx = False
html_use_smartypants = False
html_search_language = project_language
html_permalinks = True
html_permalinks_icon = '¶'
html_theme_path = ['_themes']
html_secnumber_suffix = '. '
html_title = project
html_copy_source = False

html_context = globals().get('html_context', {})
html_static_path = globals().get('html_static_path', [])

if os.path.isfile('_static/img/favicon.png'):
    html_favicon = '_static/img/favicon.png'
elif os.path.isfile('../_static/img/favicon.png'):
    html_favicon = '../_static/img/favicon.png'

if os.path.isdir('_static'):
    html_static_path += ['_static']
elif os.path.isdir('../_static'):
    html_static_path += ['../_static']

if html_theme == 'sphinx_rtd_theme':
    html_context.update({
        'css_files': [
            '_static/css/dark.css',
            '_static/css/print.css'],
        'script_files': [
            '_static/js/jquery.min.js',
            '_static/js/admonition-important.js',
            '_static/js/assignment-numbers.js',
            '_static/js/menu-search.js',
            '_static/js/menu-autonumber.js',
            '_static/js/menu-cite.js',
            '_static/js/menu-donatebutton.js',
            '_static/js/menu-futherreading.js',
            '_static/js/copybutton.js',
            '_static/js/code-editable.js',
            mathjax_path]})

if 'script_files' not in html_context:
    html_context['script_files'] = []

if 'html_menu_autohide' in globals() and html_menu_autohide is True:
    html_context['script_files'].append('_static/js/menu-autohide.js')

if html_theme == 'thesis':
    html_context.update({
        'css_files': ['_static/theme-overrides.css'],
        'script_files': [mathjax_path]})

latex_documents = [('index', f'{project_slug}.tex', project, author, latex_documentclass)]
latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '10pt',
    'figure_align': 'H',  # 'htbp',

    # Fix for: LaTeX Backend Fails with Citations In Figure Captions
    'preamble': r"""
        \usepackage{float}
        \usepackage{etoolbox}
        \AtBeginEnvironment{figure}{\renewcommand{\phantomsection}{}}
    """}

epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright
epub_exclude_files = ['search.html']

man_pages = [
    (master_doc, project_slug, project, [author], 1)]

texinfo_documents = [
    (master_doc, project_slug, project, author, project, '', 'Miscellaneous')]

#%%
# https://github.com/sphinx-doc/sphinx/blob/cc314f13e8a98393ab018d83d8957a724a6f338a/doc/extdev/appapi.rst

# def on_missing_reference(app, env, node, contnode):
#     if node['reftype'] == 'any':
#         return contnode
#     else:
#         return None
#
# def on_duplicate_term(app, env, node, contnode):
#         return None
#
#
# def setup(app):
#     app.connect('missing-reference', on_missing_reference)
#     app.connect('duplicate-term', on_duplicate_term)
