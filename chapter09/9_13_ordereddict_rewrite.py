#!/usr/bin/env python3

from collections import OrderedDict

glossary = OrderedDict()

glossary = {
    'dictionary': "Basically an associative array.",
    'list': "Just another word for an array.",
    'random': "Nothing really random about it.",
}

for term, definition in glossary.items():
    print(term.title() + ":\n    " + definition)
