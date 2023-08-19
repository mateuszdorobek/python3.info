from pathlib import Path

dirnames = [
    '/tmp/',
    '/etc/',
    '/var/',
]

for dir in map(Path, dirnames):
    print(list(dir.glob('*')))
