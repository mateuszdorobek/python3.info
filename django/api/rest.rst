REST
====


RESTful Views
-------------
.. literalinclude:: src/django-rest-views.py
    :language: python

.. code-block:: python

    urlpatterns += [
        url(r'^api/v1/auth/', include(('rest_framework.urls', 'rest_framework'), namespace='rest_framework')),
        url(r'^api/v1/', get_schema_view(title='habitatOS API v1', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])),
        url(r'^api/$', RedirectView.as_view(permanent=False, url='/api/v1/')),
    ]


``python -m json.tool``
-----------------------

``django-rest-framework``
-------------------------
.. code-block:: console

    $ pip install django-rest-swagger

:admin.py:
    .. code-block:: python

        REST_FRAMEWORK = {
            'DEFAULT_PERMISSION_CLASSES': [
                'rest_framework.permissions.IsAuthenticated',
            ],

            'DEFAULT_AUTHENTICATION_CLASSES': [
                'rest_framework.authentication.BasicAuthentication',
                'rest_framework.authentication.SessionAuthentication',
            ],
        }

``django-rest-swagger``
-----------------------
Alternatywa:

* https://github.com/axnsan12/drf-yasg/

:admin.py:
    .. code-block:: python

        SWAGGER_SETTINGS = {
            'DOC_EXPANSION': 'list',
            'OPERATIONS_SORTER': 'alpha',
            'api_version': '1.0',
        }
