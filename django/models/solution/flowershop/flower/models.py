from django.db import models
from django.utils.translation import gettext_lazy as _


class Species(models.TextChoices):
    SETOSA = 'setosa', _('Setosa')
    VERSICOLOR = 'versicolor', _('Versicolor')
    VIRGINICA = 'virginica', _('Virginica')


class Iris(models.Model):
    sepal_length = models.FloatField(verbose_name=_('Sepal Length'), null=True, blank=True, default=None)
    sepal_width = models.FloatField(verbose_name=_('Sepal Width'), null=True, blank=True, default=None)
    petal_length = models.FloatField(verbose_name=_('Petal Length'), null=True, blank=True, default=None)
    petal_width = models.FloatField(verbose_name=_('Petal Width'), null=True, blank=True, default=None)
    species = models.CharField(verbose_name=_('Species'), choices=Species.choices, max_length=20, null=True, blank=True, default=None)
    image = models.ImageField(verbose_name=_('Image'), upload_to='flower/', null=True, blank=True, default=None)

    def __str__(self):
        return f'{self.species}'

    class Meta:
        verbose_name = _('Iris')
        verbose_name_plural = _('Irises')
