
import re

class HTMLDocument():
    def __init__(self):
        self._document = []
    def append(self, entity):
        self._document.append(entity)
    @property
    def html(self):
        """Html document"""
        return self._document
    def __iter__(self):
        return iter(self._document)

class HTMLEntity():
    def __init__(self, tag, attrs):
        self._tag = tag
        self._attrs = dict(attrs)
        self._childrens = []
        self._css = CSSEntity()
    def append(self, child):
        self._childrens.append(child)
    def add_css(self, text):
        self._css.add_css(text)
    @property
    def tag(self):
        return self._tag
    @property
    def attrs(self):
        return self._attrs
    @property
    def css(self):
        return self._css

    def __iter__(self):
        return iter(self._childrens)
    def __str__(self):
        return self._tag


class HTMLRef():
    """Used for special characters"""
    def __init__(self, char):
        self._char = char
    @property
    def char(self):
        return self._char
    @property
    def tag(self):
        return "@htmlref"

    def __str__(self):
        return self._char
    def __repr__(self):
        return self._char



class CSSEntity():
    """Parse and store css"""
    def __init__(self):
        self._css = {}
    def add_css(self, css_text):
        if isinstance(css_text, dict):
            #we have parsed css, so we just update dict
            self._css.update(css_text)
            return

        zac = 0
        #remove comments and imports
        #TODO: parse imports
        text = re.sub(r"@.*", "", css_text, flags = re.MULTILINE)          #remove imports
        text = re.sub(r"/\*.*\*/", "", text, flags = re.DOTALL | re.MULTILINE)          #remove comments
        while True:
            az = text.find("{", zac + 1)
            ak = text.find("}", zac + 1)
            if az != -1 or ak != -1:
                #TODO: works only for one word css, border-right: 1em solid black don't work...
                attr = text[az + 1:ak]
                dict_css = {}
                for i in attr.split(";"):
                    if i and i.strip():
                        a = i.split(":")
                        a[0] = a[0].strip()
                        a[1] = a[1].strip()
                        #add/overwrite
                        dict_css[a[0]] = a[1].split()

                self._css[text[zac + 1:az].strip()] = dict_css
            else:
                break
            zac = ak + 1
    @property
    def css(self):
        """return dictionary"""
        return self._css

    def __contains__(self, item):
        return item in self._css

    def __getitem__(self, value):
        return self._css[value]

    def __str__(self):
        return str(self._css)
