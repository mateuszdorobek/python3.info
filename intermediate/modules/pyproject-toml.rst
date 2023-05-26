TOML pyproject.toml
===================
* https://packaging.python.org/en/latest/tutorials/packaging-projects/
* https://peps.python.org/pep-0517/
* https://peps.python.org/pep-0518/
* https://peps.python.org/pep-0621/
* https://peps.python.org/pep-0639/#add-license-files-key
* https://peps.python.org/pep-0660/
* https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html

Modern Python packages can contain a pyproject.toml file, first introduced
in PEP 518 and later expanded in PEP 517, PEP 621 and PEP 660. This file
contains build system requirements and information, which are used by pip
to build the package. [#pyproject]_


Metadata
--------
There are two kinds of metadata: static and dynamic. Static metadata is
specified in the pyproject.toml file directly and cannot be specified or
changed by a tool. Dynamic metadata is listed via the dynamic key (defined
later in this specification) and represents metadata that a tool will later
provide [#packageMetadata]_.

The keys defined in this specification MUST be in a table named ``[project]``
in ``pyproject.toml``. No tools may add keys to this table which are not
defined by this specification. For tools wishing to store their own settings
in ``pyproject.toml``, they may use the ``[tool]`` table as defined in the
build dependency declaration specification. The lack of a ``[project]`` table
implicitly means the build back-end will dynamically provide all keys.

.. csv-table:: Project Metadata [#packaging]_
    :header: "Configuration", "Description"
    :widths: 20, 80

    "name",              "is the distribution name of your package. This can be any name as long as it only contains letters, numbers, ., _ , and -. It also must not already be taken on PyPI. Be sure to update this with your username for this tutorial, as this ensures you won't try to upload a package with the same name as one which already exists."
    "version",           "is the package version. See the version specifier specification for more details on versions. Some build backends allow it to be specified another way, such as from a file or a git tag."
    "authors",           "is used to identify the author of the package; you specify a name and an email for each author. You can also list maintainers in the same format."
    "description",       "is a short, one-sentence summary of the package."
    "readme",            "is a path to a file containing a detailed description of the package. This is shown on the package detail page on PyPI. In this case, the description is loaded from README.md (which is a common pattern). There also is a more advanced table form described in the project metadata specification."
    "requires-python",   "gives the versions of Python supported by your project. Installers like pip will look back through older versions of packages until it finds one that has a matching Python version."
    "classifiers",       "gives the index and pip some additional metadata about your package. In this case, the package is only compatible with Python 3, is licensed under the MIT license, and is OS-independent. You should always include at least which version(s) of Python your package works on, which license your package is available under, and which operating systems your package will work on. For a complete list of classifiers, see https://pypi.org/classifiers/."
    "urls",              "lets you list any number of extra links to show on PyPI. Generally this could be to the source, documentation, issue trackers, etc."

More information in here [#packageMetadata]_


Example
-------
.. literalinclude:: src/pyproject.toml
    :language: toml


Verify
------
* To verify use: ``pip install .``

.. code-block:: console

    $ pip install .


Build
-----
.. code-block:: console

    $ python3 -m pip install --upgrade build
    $ python3 -m build

Result:

.. code-block:: text

    dist/
    ├── myproject-1.0.0-py3-none-any.whl
    └── myproject-1.0.0.tar.gz


Upload
------
The first thing you'll need to do is register an account on TestPyPI, which
is a separate instance of the package index intended for testing and
experimentation. It's great for things like this tutorial where we don't
necessarily want to upload to the real index. To register an account, go
to https://test.pypi.org/account/register/ and complete the steps on that
page. You will also need to verify your email address before you're able
to upload any packages. For more details, see Using TestPyPI [#pypiUpload]_.

To securely upload your project, you'll need a PyPI API token.
Create one at https://test.pypi.org/manage/account/#api-tokens,
setting the "Scope" to "Entire account". Don't close the page until
you have copied and saved the token — you won't see that token again
[#pypiUpload]_.

Now that you are registered, you can use twine to upload the distribution
packages [#pypiUpload]_.

You will be prompted for a username and password. For the username,
use ``__token__``. For the password, use the token value, including
the ``pypi-`` prefix [#pypiUpload]_.

.. code-block:: console

    $ python3 -m pip install --upgrade twine
    $ python3 -m twine upload --repository testpypi dist/*
    Uploading distributions to https://test.pypi.org/legacy/
    Enter your username: __token__
    Uploading myproject-1.0.0-py3-none-any.whl
    100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 8.2/8.2 kB • 00:01 • ?
    Uploading myproject-1.0.0.tar.gz
    100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.8/6.8 kB • 00:00 • ?

Once uploaded, your package should be viewable on TestPyPI;
for example: https://test.pypi.org/project/myproject


Install
-------
.. code-block:: console

    $ python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps myproject
    Collecting myproject
      Downloading https://test-files.pythonhosted.org/packages/.../myproject_1.0.0-py3-none-any.whl
    Installing collected packages: myproject
    Successfully installed myproject-1.0.0

This example uses ``--index-url`` flag to specify TestPyPI instead of live
PyPI. Additionally, it specifies ``--no-deps``. Since TestPyPI doesn't have
the same packages as the live PyPI, it's possible that attempting to install
dependencies may fail or install something unexpected. While our example
package doesn't have any dependencies, it's a good practice to avoid
installing dependencies when using TestPyPI [#pypiUpload]_.


Usage
-----
>>> from myproject import mymodule  # doctest: +SKIP
>>> mymodule.run()  # doctest: +SKIP


Further Reading
---------------
* https://packaging.python.org/en/latest/specifications/declaring-project-metadata/#example


References
----------
.. [#pyproject] Pip developers. "pyproject.toml". Year: 2022. Retrieved: 2022-12-01. URL: https://pip.pypa.io/en/stable/reference/build-system/pyproject-toml/
.. [#packaging] Python Packaging Authority (PyPA). Packaging Python Projects. Year: 2023. Retrieved: 2023-01-29. URL: https://packaging.python.org/en/latest/tutorials/packaging-projects/#configuring-metadata
.. [#packageMetadata] Python Packaging Authority (PyPA). Declaring project metadata. Year: 2023. Retrieved: 2023-01-29. URL: https://packaging.python.org/en/latest/specifications/declaring-project-metadata/#declaring-project-metadata
.. [#pypiUpload] Python Packaging Authority (PyPA). Packaging Python Projects. Uploading the distribution archives. https://packaging.python.org/en/latest/tutorials/packaging-projects/#uploading-the-distribution-archives
