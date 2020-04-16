#!/usr/bin/python3
""" A python code to generate documentation for the JSON API links """
""" Usage: Create the template python files using Node class and """
""" pass the file as argument to this code to generate """
""" correspondingly named Markdown files """
import sys

class Node:
    """ Define a node object for use in creating tree like structure """
    def __init__(self, value=None, children=None):
        if children is None:
            children = []
        self.value, self.children = value, children

def pprint_tree(node, file=None, _prefix="", _last=True):
    """ Pretty print tree to stdout or file object """
    print(_prefix, "└─ " if _last else "├─ ", node.value, sep="", file=file)
    _prefix += "   " if _last else "│  "
    child_count = len(node.children)
    for i, child in enumerate(node.children):
        _last = i == (child_count - 1)
        pprint_tree(child, file, _prefix, _last)


# Get filenames as argument (MUST END IN .py)
for filename in sys.argv[1:]:
    # Extract filename without .py extension to append .md
    name = filename[:-3]
    mdfile = open(name + '.md', 'w')

    # Read .py template file to obtain variable 'tree' that has structure data
    exec(compile(open(filename, "rb").read(), filename, 'exec'))

    # Pretty print to file with .md extension
    print('```bash', file=mdfile)
    pprint_tree(tree, file=mdfile)
    print('```', file=mdfile)
