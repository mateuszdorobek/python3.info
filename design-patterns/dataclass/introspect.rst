Dataclass Introspect
====================


Native
------
* Source: https://stackoverflow.com/a/67232265

>>> from dataclasses import dataclass, field, KW_ONLY
>>> from datetime import date, time, datetime, timezone, timedelta
>>> import dataclasses
>>>
>>>
>>> _original_create_fn = dataclasses._create_fn
>>>
>>> def _new_create_fn(name, args, body, **kwargs):
...     args_str = ', '.join(args)
...     body_str = '\n'.join('    ' + line for line in body)
...     print(f'def {name}({args_str}):\n{body_str}\n')
...     return _original_create_fn(name, args, body, **kwargs)
>>>
>>> dataclasses._create_fn = _new_create_fn
>>>
>>>
>>> @dataclass
... class Mission:
...     year: int
...     name: str
def __init__(self, year:_type_year, name:_type_name):
    self.year=year
    self.name=name
<BLANKLINE>
def __repr__(self):
    return self.__class__.__qualname__ + f"(year={self.year!r}, name={self.name!r})"
<BLANKLINE>
def __eq__(self, other):
    if other.__class__ is self.__class__:
     return (self.year,self.name,)==(other.year,other.name,)
    return NotImplemented
<BLANKLINE>
>>>
>>> @dataclass(frozen=True)
... class Astronaut:
...     firstname: str
...     lastname: str
...     _: KW_ONLY
...     born: date
...     job: str = 'astronaut'
...     agency: str = field(default='NASA', metadata={'choices': ['NASA', 'ESA']})
...     age: int | None = None
...     height: int | float | None = field(default=None, metadata={'unit': 'cm', 'min': 156, 'max': 210})
...     weight: int | float | None = field(default=None, metadata={'unit': 'kg', 'min': 50, 'max': 90})
...     groups: list[str] = field(default_factory=lambda: ['astronauts', 'managers'])
...     friends: dict[str,str] = field(default_factory=dict)
...     assignments: list[str] | None = field(default=None, metadata={'choices': ['Apollo18', 'Ares3', 'STS-136']})
...     missions: list[Mission] = field(default_factory=list)
...     experience: timedelta = timedelta(hours=0)
...     account_last_login: datetime | None = None
...     account_created: datetime = datetime.now(tz=timezone.utc)
...     AGE_MIN: int = field(default=30, init=False, repr=False)
...     AGE_MAX: int = field(default=50, init=False, repr=False)
...
...     def __post_init__(self):
...         HEIGHT_MIN = self.__dataclass_fields__['height'].metadata['min']
...         HEIGHT_MAX = self.__dataclass_fields__['height'].metadata['max']
...         WEIGHT_MIN = self.__dataclass_fields__['weight'].metadata['min']
...         WEIGHT_MAX = self.__dataclass_fields__['weight'].metadata['max']
...         if not HEIGHT_MIN <= self.height < HEIGHT_MAX:
...             raise ValueError(f'Height {self.height} is not in between {HEIGHT_MIN} and {HEIGHT_MAX}')
...         if not WEIGHT_MIN <= self.weight < WEIGHT_MAX:
...             raise ValueError(f'Height {self.weight} is not in between {WEIGHT_MIN} and {WEIGHT_MAX}')
...         if self.age not in range(self.AGE_MIN, self.AGE_MAX):
...             raise ValueError('Age is not valid for an astronaut')
def __init__(self, firstname:_type_firstname, lastname:_type_lastname, *, born:_type_born, job:_type_job=_dflt_job, agency:_type_agency=_dflt_agency, age:_type_age=_dflt_age, height:_type_height=_dflt_height, weight:_type_weight=_dflt_weight, groups:_type_groups=_HAS_DEFAULT_FACTORY, friends:_type_friends=_HAS_DEFAULT_FACTORY, assignments:_type_assignments=_dflt_assignments, missions:_type_missions=_HAS_DEFAULT_FACTORY, experience:_type_experience=_dflt_experience, account_last_login:_type_account_last_login=_dflt_account_last_login, account_created:_type_account_created=_dflt_account_created):
    BUILTINS.object.__setattr__(self,'firstname',firstname)
    BUILTINS.object.__setattr__(self,'lastname',lastname)
    BUILTINS.object.__setattr__(self,'born',born)
    BUILTINS.object.__setattr__(self,'job',job)
    BUILTINS.object.__setattr__(self,'agency',agency)
    BUILTINS.object.__setattr__(self,'age',age)
    BUILTINS.object.__setattr__(self,'height',height)
    BUILTINS.object.__setattr__(self,'weight',weight)
    BUILTINS.object.__setattr__(self,'groups',_dflt_groups() if groups is _HAS_DEFAULT_FACTORY else groups)
    BUILTINS.object.__setattr__(self,'friends',_dflt_friends() if friends is _HAS_DEFAULT_FACTORY else friends)
    BUILTINS.object.__setattr__(self,'assignments',assignments)
    BUILTINS.object.__setattr__(self,'missions',_dflt_missions() if missions is _HAS_DEFAULT_FACTORY else missions)
    BUILTINS.object.__setattr__(self,'experience',experience)
    BUILTINS.object.__setattr__(self,'account_last_login',account_last_login)
    BUILTINS.object.__setattr__(self,'account_created',account_created)
    self.__post_init__()
<BLANKLINE>
def __repr__(self):
    return self.__class__.__qualname__ + f"(firstname={self.firstname!r}, lastname={self.lastname!r}, born={self.born!r}, job={self.job!r}, agency={self.agency!r}, age={self.age!r}, height={self.height!r}, weight={self.weight!r}, groups={self.groups!r}, friends={self.friends!r}, assignments={self.assignments!r}, missions={self.missions!r}, experience={self.experience!r}, account_last_login={self.account_last_login!r}, account_created={self.account_created!r})"
<BLANKLINE>
def __eq__(self, other):
    if other.__class__ is self.__class__:
     return (self.firstname,self.lastname,self.born,self.job,self.agency,self.age,self.height,self.weight,self.groups,self.friends,self.assignments,self.missions,self.experience,self.account_last_login,self.account_created,self.AGE_MIN,self.AGE_MAX,)==(other.firstname,other.lastname,other.born,other.job,other.agency,other.age,other.height,other.weight,other.groups,other.friends,other.assignments,other.missions,other.experience,other.account_last_login,other.account_created,other.AGE_MIN,other.AGE_MAX,)
    return NotImplemented
<BLANKLINE>
def __setattr__(self, name, value):
    if type(self) is cls or name in ('firstname','lastname','born','job','agency','age','height','weight','groups','friends','assignments','missions','experience','account_last_login','account_created','AGE_MIN','AGE_MAX',):
     raise FrozenInstanceError(f"cannot assign to field {name!r}")
    super(cls, self).__setattr__(name, value)
<BLANKLINE>
def __delattr__(self, name):
    if type(self) is cls or name in ('firstname','lastname','born','job','agency','age','height','weight','groups','friends','assignments','missions','experience','account_last_login','account_created','AGE_MIN','AGE_MAX',):
     raise FrozenInstanceError(f"cannot delete field {name!r}")
    super(cls, self).__delattr__(name)
<BLANKLINE>
def __hash__(self):
    return hash((self.firstname,self.lastname,self.born,self.job,self.agency,self.age,self.height,self.weight,self.groups,self.friends,self.assignments,self.missions,self.experience,self.account_last_login,self.account_created,self.AGE_MIN,self.AGE_MAX,))
<BLANKLINE>
