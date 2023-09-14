try:
    import numpy as np
except ImportError:
    pass

try:
    import pandas as pd
    pd.set_option('display.width', 200)
    pd.set_option('display.max_columns', 15)
    pd.set_option('display.max_rows', 100)
    pd.set_option('display.min_rows', 100)
    pd.set_option('display.max_seq_items', 100)
except ImportError:
    pass

try:
    import matplotlib.pyplot as plt
except ImportError:
    pass

from itertools import starmap, zip_longest, permutations, product
from uuid import uuid4
from functools import wraps, reduce
from typing import Literal, Final, ClassVar, Self, Protocol, Callable, Any, runtime_checkable, get_type_hints, NamedTuple, TypedDict
from abc import ABCMeta, ABC, abstractmethod, abstractproperty
from dataclasses import dataclass, field, asdict, astuple, KW_ONLY
from datetime import date, time, datetime, timezone, timedelta
from zoneinfo import ZoneInfo
from random import randint, seed
from pathlib import Path
from pprint import pprint
from timeit import timeit
from time import time as timestamp
import sys
import json
import csv
import pickle
import re
import logging

logging.basicConfig(
    level='INFO',
    format='{asctime}, "{levelname}", "{message}"',
    datefmt='"%Y-%m-%d", "%H:%M:%S"',
    style='{',
)



PHONE1 = '+48 123 456 789'
PHONE2 = '+48 (12) 345-6789'

TEXT = 'Email from Mark Watney <mwatney@nasa.gov> received on: Sat, Jan 1st, 2000 at 12:00 AM'

JFK = """We choose to go to the moon.
We choose to go to the moon in this decade and do the other things,
not because they are easy, but because they are hard,
because that goal will serve to organize and measure the best of our energies and skills,
because that challenge is one that we are willing to accept,
one we are unwilling to postpone,
and one which we intend to win,
and the others, too."""

APOLLO = """Apollo 11 was the American spaceflight that first landed
humans on the Moon. Commander (CDR) Neil Armstrong and lunar module
pilot (LMP) Buzz Aldrin landed the Apollo Lunar Module (LM) Eagle on
July 20th, 1969 at 20:17 UTC, and Armstrong became the first person
to step (EVA) onto the Moon's surface (EVA) 6 hours 39 minutes later,
on July 21st, 1969 at 02:56:15 UTC. Aldrin joined him 19 minutes later.
They spent 2 hours 31 minutes exploring the site they had named Tranquility
Base upon landing. Armstrong and Aldrin collected 47.5 pounds (21.5 kg)
of lunar material to bring back to Earth as pilot Michael Collins (CMP)
flew the Command Module (CM) Columbia in lunar orbit, and were on the
Moon's surface for 21 hours 36 minutes before lifting off to rejoin
Columbia."""



#def pwd():
#    return str(Path.cwd())

#def cat(file):
#    with open(file, mode='r') as f:
#        return f.read()

#def ls(path='.'):
#    result = map(str, Path(path).glob('*'))
#    pprint(list(result))


def search(pattern, text=TEXT):
    if re.search(pattern, text):
        return True
    else:
        return False


def match(pattern, string='mwatney@nasa.gov'):
    if re.match(pattern, string):
        return True
    else:
        return False


def find(pattern, text=TEXT):
    return re.findall(pattern, text)





sys.tracebacklimit = 0

ip = get_ipython()
