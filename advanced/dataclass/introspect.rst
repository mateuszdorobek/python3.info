Dataclass Introspect
====================


SetUp
-----
>>> from dataclasses import dataclass, field
>>> from datetime import date, time, datetime, timezone, timedelta
>>> from typing import Literal
>>> import dataclasses


Introspect Function
-------------------
* Source: https://stackoverflow.com/a/67232265

>>> _original_create_fn = dataclasses._create_fn
>>>
>>> def _new_create_fn(name, args, body, **kwargs):
...     args_str = ', '.join(args)
...     body_str = '\n'.join('    ' + line for line in body)
...     print(f'def {name}({args_str}):\n{body_str}\n')
...     return _original_create_fn(name, args, body, **kwargs)
>>>
>>> dataclasses._create_fn = _new_create_fn


Simple
------
>>> @dataclass
... class Mission:
...     year: int
...     name: str
...
def __init__(self, year:__dataclass_type_year__, name:__dataclass_type_name__):
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


Complex
-------
>>> @dataclass(frozen=True, slots=True, kw_only=True)
... class User:
...     firstname: str
...     lastname: str
...     birthday: date
...     job: str = 'admin'
...     agency: Literal['NASA', 'ESA'] = field(default='NASA', metadata={'choices': ['NASA', 'ESA']})
...     age: int | None = None
...     height: int | float | None = field(default=None, metadata={'unit': 'cm', 'min': 156, 'max': 210})
...     weight: int | float | None = field(default=None, metadata={'unit': 'kg', 'min': 50, 'max': 90})
...     groups: list[str] = field(default_factory=lambda: ['users', 'staff', 'admins'])
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
...             raise ValueError('Age is not valid for a user')
...
def __init__(self, *, firstname:__dataclass_type_firstname__, lastname:__dataclass_type_lastname__, birthday:__dataclass_type_birthday__, job:__dataclass_type_job__=__dataclass_dflt_job__, agency:__dataclass_type_agency__=__dataclass_dflt_agency__, age:__dataclass_type_age__=__dataclass_dflt_age__, height:__dataclass_type_height__=__dataclass_dflt_height__, weight:__dataclass_type_weight__=__dataclass_dflt_weight__, groups:__dataclass_type_groups__=__dataclass_HAS_DEFAULT_FACTORY__, friends:__dataclass_type_friends__=__dataclass_HAS_DEFAULT_FACTORY__, assignments:__dataclass_type_assignments__=__dataclass_dflt_assignments__, missions:__dataclass_type_missions__=__dataclass_HAS_DEFAULT_FACTORY__, experience:__dataclass_type_experience__=__dataclass_dflt_experience__, account_last_login:__dataclass_type_account_last_login__=__dataclass_dflt_account_last_login__, account_created:__dataclass_type_account_created__=__dataclass_dflt_account_created__):
    __dataclass_builtins_object__.__setattr__(self,'firstname',firstname)
    __dataclass_builtins_object__.__setattr__(self,'lastname',lastname)
    __dataclass_builtins_object__.__setattr__(self,'birthday',birthday)
    __dataclass_builtins_object__.__setattr__(self,'job',job)
    __dataclass_builtins_object__.__setattr__(self,'agency',agency)
    __dataclass_builtins_object__.__setattr__(self,'age',age)
    __dataclass_builtins_object__.__setattr__(self,'height',height)
    __dataclass_builtins_object__.__setattr__(self,'weight',weight)
    __dataclass_builtins_object__.__setattr__(self,'groups',__dataclass_dflt_groups__() if groups is __dataclass_HAS_DEFAULT_FACTORY__ else groups)
    __dataclass_builtins_object__.__setattr__(self,'friends',__dataclass_dflt_friends__() if friends is __dataclass_HAS_DEFAULT_FACTORY__ else friends)
    __dataclass_builtins_object__.__setattr__(self,'assignments',assignments)
    __dataclass_builtins_object__.__setattr__(self,'missions',__dataclass_dflt_missions__() if missions is __dataclass_HAS_DEFAULT_FACTORY__ else missions)
    __dataclass_builtins_object__.__setattr__(self,'experience',experience)
    __dataclass_builtins_object__.__setattr__(self,'account_last_login',account_last_login)
    __dataclass_builtins_object__.__setattr__(self,'account_created',account_created)
    __dataclass_builtins_object__.__setattr__(self,'AGE_MIN',__dataclass_dflt_AGE_MIN__)
    __dataclass_builtins_object__.__setattr__(self,'AGE_MAX',__dataclass_dflt_AGE_MAX__)
    self.__post_init__()
<BLANKLINE>
def __repr__(self):
    return self.__class__.__qualname__ + f"(firstname={self.firstname!r}, lastname={self.lastname!r}, birthday={self.birthday!r}, job={self.job!r}, agency={self.agency!r}, age={self.age!r}, height={self.height!r}, weight={self.weight!r}, groups={self.groups!r}, friends={self.friends!r}, assignments={self.assignments!r}, missions={self.missions!r}, experience={self.experience!r}, account_last_login={self.account_last_login!r}, account_created={self.account_created!r})"
<BLANKLINE>
def __eq__(self, other):
    if other.__class__ is self.__class__:
     return (self.firstname,self.lastname,self.birthday,self.job,self.agency,self.age,self.height,self.weight,self.groups,self.friends,self.assignments,self.missions,self.experience,self.account_last_login,self.account_created,self.AGE_MIN,self.AGE_MAX,)==(other.firstname,other.lastname,other.birthday,other.job,other.agency,other.age,other.height,other.weight,other.groups,other.friends,other.assignments,other.missions,other.experience,other.account_last_login,other.account_created,other.AGE_MIN,other.AGE_MAX,)
    return NotImplemented
<BLANKLINE>
def __setattr__(self, name, value):
    if type(self) is cls or name in {'firstname', 'lastname', 'birthday', 'job', 'agency', 'age', 'height', 'weight', 'groups', 'friends', 'assignments', 'missions', 'experience', 'account_last_login', 'account_created', 'AGE_MIN', 'AGE_MAX'}:
     raise FrozenInstanceError(f"cannot assign to field {name!r}")
    super(cls, self).__setattr__(name, value)
<BLANKLINE>
def __delattr__(self, name):
    if type(self) is cls or name in {'firstname', 'lastname', 'birthday', 'job', 'agency', 'age', 'height', 'weight', 'groups', 'friends', 'assignments', 'missions', 'experience', 'account_last_login', 'account_created', 'AGE_MIN', 'AGE_MAX'}:
     raise FrozenInstanceError(f"cannot delete field {name!r}")
    super(cls, self).__delattr__(name)
<BLANKLINE>
def __hash__(self):
    return hash((self.firstname,self.lastname,self.birthday,self.job,self.agency,self.age,self.height,self.weight,self.groups,self.friends,self.assignments,self.missions,self.experience,self.account_last_login,self.account_created,self.AGE_MIN,self.AGE_MAX,))
<BLANKLINE>
