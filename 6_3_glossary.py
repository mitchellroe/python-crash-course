#!/usr/bin/env python3

glossary = {
    'dictionary': "Basically an associative array.",
    'list': "Just another word for an array.",
}

word = "dictionary"
print(word.title() + ":\n    " + glossary[word])
word = "list"
print(word.title() + ":\n    " + glossary[word])
