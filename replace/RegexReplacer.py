import re

replacement_patterns = [
    (r'I\'m', 'I am'),
    (r'(\w+)\'ll', '\g<1> will'),
]


class RegexReplacer:
    def __init__(self, patterns=replacement_patterns):
        self.patterns = [(re.compile(regex), repl) for (regex, repl) in patterns]

    def replace(self, text):
        s = text

        for (pattern, repl) in self.patterns:
            s = re.sub(pattern, repl, s)

        return s
