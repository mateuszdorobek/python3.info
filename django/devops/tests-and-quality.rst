Tests and quality
=================


Tests
-----
* https://docs.djangoproject.com/en/dev/topics/testing/overview/

.. code-block:: python

    from django.test import TestCase
    from myapp.models import Animal


    class AnimalTestCase(TestCase):
        def setUp(self):
            Animal.objects.create(name="lion", sound="roar")
            Animal.objects.create(name="cat", sound="meow")

        def test_animals_can_speak(self):
            """Animals that can speak are correctly identified"""
            lion = Animal.objects.get(name="lion")
            cat = Animal.objects.get(name="cat")
            self.assertEqual(lion.speak(), 'The lion says "roar"')
            self.assertEqual(cat.speak(), 'The cat says "meow"')

.. code-block:: console

    # By default, this will discover tests in any file named "test*.py" under the current working directory.
    $ python manage.py test --parallel

    # Run all the tests in the animals.tests module
    $ ./manage.py test animals.tests

    # Run all the tests found within the 'animals' package
    $ ./manage.py test animals

    # Run just one test case
    $ ./manage.py test animals.tests.AnimalTestCase

    # Run just one test method
    $ ./manage.py test animals.tests.AnimalTestCase.test_animals_can_speak

Test URLs
---------
.. code-block:: python

    import logging
    from django.contrib.auth.models import User
    from django.test import TestCase
    from django.test.client import Client


    class Test(TestCase):
        assert_http_200 = []

        def setUp(self):
            self.logger = logging.getLogger(__name__)
            self.user = User.objects.create_superuser('test', 'test@example.com', 'test')
            self.client.login(username='test', password='test')

        def tearDown(self):
            self.client.logout()
            self.user.delete()

        def test_http_200(self):
            for url in self.assert_http_200:
                response = self.client.get(url)

                if response.status_code != 200:
                    self.logger.error(f'{response.status_code} {url}')
                    raise AssertionError(f'HTTP {response.status_code} for "{url}"')
                else:
                    self.logger.info(f'{response.status_code} {url}')

.. code-block:: python

    from addressbook.tests import Test


    class ContactTest(Test):
        assert_http_200 = [
            '/admin/',
            '/admin/contact/',

            '/admin/contact/contact/',
            '/admin/contact/contact/add/',
            '/admin/contact/contact/edit/1/',

            '/admin/contact/address/',
            '/admin/contact/address/add/',
            '/admin/contact/address/edit/1/',
        ]


SonarQube
---------
.. code-block:: text

    sonar.host.url=https://sonarcloud.io
    sonar.organization=astromatt
    sonar.login=...

    sonar.language=py
    sonar.sourceEncoding=UTF-8
    sonar.verbose=true

    sonar.projectKey=habitatOS
    sonar.projectName=habitatOS
    sonar.projectDescription=Operating System for analog extraterrestrial habitats.
    sonar.links.homepage=https://github.com/astromatt/habitatOS/
    sonar.links.scm=https://github.com/astromatt/habitatOS/
    sonar.links.issue=https://github.com/astromatt/habitatOS/issues
    sonar.links.ci=https://github.com/astromatt/habitatOS/addon/pipelines/home

    sonar.projectBaseDir=habitat
    sonar.sources=.
    sonar.exclusions=**/migrations/**

    # Pylint
    sonar.python.pylint=/usr/local/bin/pylint
    sonar.python.pylint_config=.pylintrc
    sonar.python.pylint.reportPath=pylint-report.txt

    # Unit tests
    sonar.python.xunit.reportPath=test-reports/*.xml
    sonar.python.coverage.reportPath=coverage.xml

    # Integration tests
    sonar.python.coverage.itReportPath=it-coverage.xml

    # Turn off these rules
    sonar.issue.ignore.multicriteria=e1,e2
    # python:s100: "Method names should comply with a naming convention" gives many false positives when overriding
    # TestCase methods (such as setUp and tearDown) in test files.
    sonar.issue.ignore.multicriteria.e1.ruleKey=python:S100
    sonar.issue.ignore.multicriteria.e1.resourceKey=**/tests.py
    sonar.issue.ignore.multicriteria.e2.ruleKey=python:S100
    sonar.issue.ignore.multicriteria.e2.resourceKey=**/tests.py


Debug Toolbar
-------------
Append to `settings.py`:

.. code-block:: python

    DEBUG = True
    INSTALLED_APPS += ['debug_toolbar']
    MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
    INTERNAL_IPS = ['127.0.0.1']

Append to `urls.py`:

.. code-block:: python

    from django.urls import include, path
    from django.conf import settings

    if settings.DEBUG:
        urlpatterns += [
            path('__debug__/', include('debug_toolbar.urls')),
        ]
