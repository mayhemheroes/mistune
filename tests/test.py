
import os
import re
import mistune
root = os.path.dirname(__file__)

known = []


def render(folder, name):
    filepath = os.path.join(folder, name + '.text')
    with open(filepath) as f:
        content = f.read()

    html = mistune.markdown(content)

    filepath = os.path.join(folder, name + '.html')
    with open(filepath) as f:
        result = f.read()

    html = re.sub(r'\s', '', html)
    result = re.sub(r'\s', '', result)
    for i, s in enumerate(html):
        if s != result[i]:
            begin = max(i - 30, 0)
            msg = '\n\n%s\n------Not Equal------\n%s' % (
                html[begin:i+30],
                result[begin:i+30]
            )
            raise ValueError(msg)


def listdir(folder):
    folder = os.path.join(root, folder)
    files = os.listdir(folder)
    files = filter(lambda o: o.endswith('.text'), files)
    names = map(lambda o: o[:-5], files)
    return folder, names


def test_extra():
    folder, names = listdir('extra')
    for key in names:
        yield render, folder, key