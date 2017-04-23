"""A RegEx represents one of the following possible regular expressions:

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

    def __init__(self, char):
        self.char = char

    def delta(self):
        return NullSet()

    def is_empty(self):
        return False

    def derive(self, char):
        if char == self.char:
            return Epsilon()
        else:
            return NullSet()

    def normalize(self):
        return self


class Sequence:

    def __init__(self, re1, re2):
        self.re1 = re1
        self.re2 = re2

    def delta(self):
        if isinstance(self.re1, Epsilon) and isinstance(self.re2, Epsilon):
            return Epsilon()
        else:
            return NullSet()

    def is_empty(self):
        return False

    def derive(self, char):
        seq1 = Sequence(self.re1.delta(), self.re2.derive(char))
        seq2 = Sequence(self.re1.derive(char), self.re2)
        return Alternation(seq1, seq2)

    def normalize(self):
        if isinstance(self.re1, NullSet) or isinstance(self.re2, NullSet):
            return NullSet()
        elif isinstance(self.re2, Epsilon):
            return self.re1.normalize()
        elif isinstance(self.re1, Epsilon):
            return self.re2.normalize()
        else:
            return Sequence(self.re1.normalize(), self.re2.normalize())


class Alternation:

    def __init__(self, re1, re2):
        self.re1 = re1
        self.re2 = re2

    def delta(self):
        if isinstance(self.re1, Epsilon) or isinstance(self.re2, Epsilon):
            return Epsilon()
        else:
            return NullSet()

    def is_empty(self):
        return False

    def derive(self, char):
        return Alternation(self.re1.derive(char), self.re2.derive(char))

    def normalize(self):
        if isinstance(self.re1, NullSet):
            return self.re2.normalize()
        elif isinstance(self.re2, NullSet):
            return self.re1.normalize()
        else:
            return Alternation(self.re1.normalize(), self.re2.normalize())


class Closure:

    def __init__(self, re):
        self.re = re

    def delta(self):
        return Epsilon()

    def is_empty(self):
        return True

    def derive(self, char):
        return Sequence(self.re.derive(char), self.re)

    def normalize(self):
        return self.re.normalize()


def make_str(str):
    pass


def matches(regex, str):
    if len(str) == 0:
        return regex.delta().is_empty()
    else:
        derived_normalized = regex.derive(str[0]).normalize()
        if isinstance(derived_normalized, NullSet):
            return False
        else:
            return matches(derived_normalized, str[1:])

if __name__ == '__main__':
    regex = Character('x')
    regex_2 = Sequence(Character('a'), Sequence(Character('b'), Sequence(Character('c'), Epsilon())))

    str_to_match = ''
    str_to_match_2 = 'axc'

    result = matches(regex, str_to_match)
    result_2 = matches(regex_2, str_to_match_2)

    print(result)
    print(result_2)

