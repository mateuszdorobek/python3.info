Case Study: Hosts
=================
1. Define `result: list[dict]`, where each dict has keys:

   * ip: str
   * hosts: list[str]

2. Iterate over lines in `DATA` skipping comments (`#`) and empty lines
3. Extract from each line: `ip` and `hosts`
4. Add `ip` and `hosts` to `result` as a dict, example:

   {'ip': '127.0.0.1', 'hosts': ['localhost', 'astromatt']}

5. Each line must be a separate dict


SetUp
-----
>>> # doctest: +SKIP
... DATA = """##
... # `/etc/hosts` structure:
... #   - IPv4 or IPv6
... #   - Hostnames
...  ##
...
... 127.0.0.1       localhost
... 127.0.0.1       astromatt
... 10.13.37.1      nasa.gov esa.int
... 255.255.255.255 broadcasthost
... ::1             localhost"""


Solution 1
----------
>>> # doctest: +SKIP
... %%timeit -r 1000 -n 1000
... result = []
... for line in DATA.splitlines():
...     line = line.strip()
...     if len(line) == 0:
...         continue
...     if line.startswith('#'):
...         continue
...     ip, *hosts = line.split()
...     result.append({'ip':ip, 'hosts':hosts})
# 4.97 µs ± 443 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)
# 5.18 µs ± 496 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)
# 5.33 µs ± 698 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)
# 5.01 µs ± 432 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)
# 5.16 µs ± 645 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)


Solution 2
----------
>>> # doctest: +SKIP
... %%timeit -r 1000 -n 1000
... result = []
... for line in DATA.splitlines():
...     if line and not (line[0] == '#' or line[1] == '#'):
...         ip, *hosts = line.split()
...         result.append({'ip':ip, 'hosts':hosts})
# 4.12 µs ± 758 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)
# 3.82 µs ± 384 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)
# 3.89 µs ± 651 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)
# 4.64 µs ± 1.81 µs per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)
# 4.32 µs ± 896 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)


Solution 3
----------
>>> # doctest: +SKIP
... %%timeit -r 1000 -n 1000
... def is_valid_line(line):
...     return line and not (line[0] == '#' or line[1] == '#')
...
... result = []
... for line in DATA.splitlines():
...     if is_valid_line(line):
...         ip, *hosts = line.split()
...         result.append({'ip':ip, 'hosts':hosts})
# 4.97 µs ± 492 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)
# 4.91 µs ± 580 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)
# 5.15 µs ± 836 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)
# 5.08 µs ± 688 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)
# 5.42 µs ± 934 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)
