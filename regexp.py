﻿"""A RegEx represents one of the following possible regular expressions:

1. Epsilon                - the re that matches anything (empty string)
2. NullSet                - the re that matches nothing (null)
3. Character              - the re that matches a single character c
4. Sequence(re1,re2)      - the re that matches a sequence of re1 followed by re2
5. Alternative(re1 | re2) - the re that matches an alternative: re1 OR re2
6. Closure(re*)           - the re that matches 0 or more of re
"""


class Epsilon:
    """ the empty RE """
    def delta(self):
        return self

    def is_empty(self):
        return True

    def derive(self, char):
        return NullSet()

    def normalize(self):
        return self


class NullSet:
    """ the re that matches nothing """
    def delta(self):
        return self

    def is_empty(self):
        return False

    def derive(self, char):
        return self

    def normalize(self):
        return self


class Character:
    def delta(self):
        return NullSet()

    def is_empty(self):
        return False

    def derive(self, char):
        pass

    def normalize(self):
        pass


class Sequence:
    def delta(self):
        pass

    def is_empty(self):
        return False

    def derive(self, char):
        pass

    def normalize(self):
        pass


class Alternative:
    def delta(self):
        pass

    def is_empty(self):
        return False

    def derive(self, char):
        pass

    def normalize(self):
        pass


class Closure:
    def delta(self):
        pass

    def is_empty(self):
        return True

    def derive(self, char):
        pass

    def normalize(self):
        pass


def make_str(str):
    pass


def matches(regex, str):
    pass

if __name__ == '__main__':
    regex = Character('x')
    str_to_match = 'x'
    result = matches(regex, str_to_match)
    print(result)

