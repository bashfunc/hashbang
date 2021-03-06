#!/usr/bin/env python3

'''
$ completer.py --<TAB>
--arg\x0b--file

$ completer.py --arg <TAB>
app\x0bapk\x0bexe

$ completer.py --arg=<TAB>
--arg=app\x0b--arg=apk\x0b--arg=exe

$ completer.py --arg a<TAB>
app\x0bapk

$ completer.py -f /u/b/e<TAB>
/usr/bin/env 
'''

from hashbang import command, Argument
from hashbang.completion import fuzzy_path_validator


@command
def main(
        *,
        arg: Argument(
            completer=lambda **_: ('app', 'apk', 'exe')) = 'one',
        file: Argument(
            aliases=('f',),
            completer=lambda **_: ('/usr/bin/env', '/usr/bin/python'),
            completion_validator=fuzzy_path_validator) = None):
    print('arg={}'.format(repr(arg)))


if __name__ == '__main__':
    main.execute()
