Asbtract
========

>>> # doctest: +SKIP
... import logging
... from uuid import uuid4
... from django.db import models
... from django.utils.translation import gettext_lazy as _
...
...
... class Manager(models.Manager):
...     def get_queryset(self):
...         return super().get_queryset().filter(is_deleted=False)
...
...
... class BaseModel(models.Model):
...     uuid = models.UUIDField(verbose_name=_('UUID'), null=False, blank=False, editable=False, default=uuid4, help_text=_('Object Unique Identifier'))
...     created_user = models.ForeignKey(verbose_name=_('Created User'), related_name='+', to='auth.User', null=True, blank=True, on_delete=models.SET_NULL, help_text=_('User'))
...     created_date = models.DateTimeField(verbose_name=_('Created Date'), null=False, blank=False, auto_now_add=True, help_text=_('UTC Date and Time'))
...     modified_user = models.ForeignKey(verbose_name=_('Modified User'), to='auth.User', related_name='+',  null=True, blank=True, on_delete=models.SET_NULL, help_text=_('User'))
...     modified_date = models.DateTimeField(verbose_name=_('Modified Date'), null=False, blank=False, auto_now=True, help_text=_('UTC Date and Time'))
...     is_deleted = models.BooleanField(verbose_name=_('Is Deleted?'), null=False, blank=False, default=False, help_text=_('Is record deleted?'))
...     comment = models.TextField(verbose_name=_('Comment'), null=True, blank=True, default=None, help_text=_('Additional Comments'))
...
...     objects = Manager()
...
...     def log(self, message: str, level: int | str = logging.INFO):
...         log = logging.getLogger(self.__class__.__name__)
...         log.log(level, message)
...
...     class Meta:
...         abstract = True
...         ordering = ['-created_date']
...         verbose_name = _('Base Model')
...         verbose_name_plural = _('Base Models')
