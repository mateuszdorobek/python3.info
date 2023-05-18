Models Enum
===========


Use Case - 0x01
---------------
.. code-block:: python

    from django.db import models
    from django.utils.translation import gettext_lazy as _


    class species(models.TextChoices):
        SETOSA = 'setosa', _('Setosa')
        VIRGNICA = 'virgnica', _('Virginica')
        VERSICOLOR = 'versicolor', _('Versicolor')


    class Iris(models.Model):
        sepal_length = models.FloatField(verbose_name=_('sepal_length'), null=True, blank=True, default=None)
        sepal_width = models.FloatField(verbose_name=_('sepal_width'), null=True, blank=True, default=None)
        petal_length = models.FloatField(verbose_name=_('petal_length'), null=True, blank=True, default=None)
        petal_width = models.FloatField(verbose_name=_('petal_width'), null=True, blank=True, default=None)
        species = models.CharField(verbose_name=_('species'), max_length=20, choices=species.choices, null=True, blank=True, default=None, db_index=True)
        images = models.ImageField(verbose_name=_('Image'), upload_to='_media/flower', null=True, blank=True, default=None)

        def __str__(self) -> str:
            return f'{self.species}'

        class Meta:
            verbose_name = _('Iris')
            verbose_name_plural = _('Irises')


Use Case - 0x02
---------------
.. code-block:: python

    from django.core.validators import MaxValueValidator, MinValueValidator
    from django.db import models
    from django.utils.translation import gettext_lazy as _
    from django.conf import settings

    class Language(models.TextChoices):
        UNKNOWN = None, _('Unknown')
        POLISH = 'polish', _('Polish')
        ENGLISH = 'english', _('English')
        HINDI = 'hindi', _('Hindi')
        TAMIL = 'tamil', _('Tamil')


    class PhoneTypes(models.TextChoices):
        WORK = 'work', _('Work')
        HOME = 'home', _('Home')


    class PhoneCountryCodes(models.TextChoices):
        USA = '+1', _('(+1) USA')
        POLAND = '+48', _('(+48) Poland')
        GERMANY = '+49', _('(+49) Germany')
        INDIA = '+91', _('(+91) India')


    class Alive(models.IntegerChoices):
        YES = True, _('Alive')
        NO = False, _('Deceased')


    class Person(BaseModel):
        # Personal Fields
        firstname = models.CharField(verbose_name=_('First Name'), max_length=50)
        lastname = models.CharField(verbose_name=_('Last Name'), max_length=50, db_index=True)
        language = models.CharField(verbose_name=_('Language'), max_length=20, null=True, default=Language.UNKNOWN, choices=Language.choices)
        personal_identification_number = models.CharField(verbose_name=_('Personal Identification Number'), max_length=30, null=True, blank=True, default=None, help_text=_('This is country specific number such as SSN, PESEL'))

        # Relations
        groups = models.ManyToManyField(verbose_name=_('Group'), to='contact.Group', blank=True, limit_choices_to={'group__name__startswith': 'managers_'})
        friends = models.ManyToManyField(verbose_name=_('Friends'), to='contact.Person', blank=True)

        # Biometric
        is_alive = models.BooleanField(verbose_name=_('Is Alive?'), null=True, blank=True, default=None, choices=Alive.choices)
        birthday = models.DateField(verbose_name=_('Birthday'), null=True, blank=True, default=None)
        height = models.FloatField(verbose_name=_('Height'), null=True, blank=True, default=None, validators=[MinValueValidator(0), MaxValueValidator(250)], help_text=_('cm'))
        weight = models.FloatField(verbose_name=_('Weight'), null=True, blank=True, default=None, validators=[MinValueValidator(0), MaxValueValidator(250)], help_text=_('kg'))
        salary = models.DecimalField(verbose_name=_('Salary'), null=True, blank=True, default=None, max_digits=8, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(300_000)], help_text=_('USD per year'))
        image = models.ImageField(verbose_name=_('Image'), upload_to=upload_path, null=True, blank=True, default=None)

        # Contact
        current_company = models.CharField(verbose_name=_('Current Company'), max_length=50, null=True, blank=True, default=None)
        current_position = models.CharField(verbose_name=_('Current Position'), max_length=50, null=True, blank=True, default=None)
        email = models.EmailField(verbose_name=_('Email'), max_length=100, unique=True, null=True, blank=True, default=None)
        phone_type = models.CharField(verbose_name=_('Phone Type'), max_length=15, null=True, blank=True, default=None, choices=PhoneTypes.choices)
        phone_countrycode = models.CharField(verbose_name=_('Phone Country Code'), max_length=4, null=True, blank=True, default=None, choices=PhoneCountryCodes.choices)
        phone_number = models.CharField(verbose_name=_('Phone Number'), max_length=10, null=True, blank=True, default=None)
        homepage = models.URLField(verbose_name=_('Homepage'), null=True, blank=True, default=None)
        notes = models.TextField(verbose_name=_('Notes'), null=True, blank=True, default=None)
